import uuid
import re
import base64
import threading
from datetime import datetime, timezone
from typing import List, Optional
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from multipart.multipart import shutil

import database.chat as chat_db
import database.conversations as conversations_db
from database.apps import record_app_usage
from models.app import App, UsageHistoryType
from models.chat import (
    ChatSession,
    Message,
    SendMessageRequest,
    MessageSender,
    ResponseMessage,
    MessageConversation,
    FileChat,
)
from models.conversation import Conversation
from routers.sync import retrieve_file_paths, decode_files_to_wav
from services.chat import stream_chat
from utils.apps import get_available_app_by_id
from utils.chat import (
    process_voice_message_segment,
    process_voice_message_segment_stream,
    resolve_voice_message_language,
    transcribe_voice_message_segment,
)
from utils.llm.persona import initial_persona_chat_message
from utils.llm.chat import initial_chat_message
from utils.llm.goals import extract_and_update_goal_progress
from utils.other import endpoints as auth, storage
from utils.other.chat_file import FileChatTool
from utils.llm.usage_tracker import set_usage_context, reset_usage_context, Features

router = APIRouter()


def filter_messages(messages, app_id):
    print('filter_messages', len(messages), app_id)
    collected = []
    for message in messages:
        if message.sender == MessageSender.ai and message.plugin_id != app_id:
            break
        collected.append(message)
    print('filter_messages output:', len(collected))
    return collected


def acquire_chat_session(uid: str, app_id: Optional[str] = None):
    chat_session = chat_db.get_chat_session(uid, app_id=app_id)
    if chat_session is None:
        cs = ChatSession(id=str(uuid.uuid4()), created_at=datetime.now(timezone.utc), plugin_id=app_id)
        chat_session = chat_db.add_chat_session(uid, cs.dict())
    return chat_session


@router.post('/v2/messages', tags=['chat'], response_model=ResponseMessage)
def send_message(
    data: SendMessageRequest,
    plugin_id: Optional[str] = None,
    app_id: Optional[str] = None,
    uid: str = Depends(auth.get_current_user_uid),
):
    compat_app_id = app_id or plugin_id
    print('send_message', data.text, compat_app_id, uid)

    if compat_app_id in ['null', '']:
        compat_app_id = None

    # get chat session
    chat_session = chat_db.get_chat_session(uid, app_id=compat_app_id)
    chat_session = ChatSession(**chat_session) if chat_session else None

    message = Message(
        id=str(uuid.uuid4()),
        text=data.text,
        created_at=datetime.now(timezone.utc),
        sender='human',
        type='text',
        app_id=compat_app_id,
    )
    if data.file_ids is not None and chat_session:
        new_file_ids = chat_session.retrieve_new_file(data.file_ids)
        chat_session.add_file_ids(data.file_ids)
        chat_db.add_files_to_chat_session(uid, chat_session.id, data.file_ids)

        if len(new_file_ids) > 0:
            message.files_id = new_file_ids
            files = chat_db.get_chat_files(uid, new_file_ids)
            files = [FileChat(**f) if f else None for f in files]
            message.files = files

    if chat_session:
        message.chat_session_id = chat_session.id
        chat_db.add_message_to_chat_session(uid, chat_session.id, message.id)

    chat_db.add_message(uid, message.dict())

    # Check for goal progress (background)
    threading.Thread(target=extract_and_update_goal_progress, args=(uid, data.text)).start()

    app = get_available_app_by_id(compat_app_id, uid)
    app = App(**app) if app else None

    app_id_from_app = app.id if app else None

    messages = list(reversed([Message(**msg) for msg in chat_db.get_messages(uid, limit=10, app_id=compat_app_id)]))

    def process_message(response: str, callback_data: dict):
        memories = callback_data.get('memories_found', [])
        ask_for_nps = callback_data.get('ask_for_nps', False)
        langsmith_run_id = callback_data.get('langsmith_run_id')
        prompt_name = callback_data.get('prompt_name')
        prompt_commit = callback_data.get('prompt_commit')
        chart_data = callback_data.get('chart_data')

        # cited extraction
        cited_conversation_idxs = {int(i) for i in re.findall(r'\[(\d+)\]', response)}
        if len(cited_conversation_idxs) > 0:
            response = re.sub(r'\[\d+\]', '', response)
        memories = [memories[i - 1] for i in cited_conversation_idxs if 0 < i and i <= len(memories)]

        memories_id = []
        # check if the items in the conversations list are dict
        if memories:
            converted_memories = []
            for m in memories[:5]:
                if isinstance(m, dict):
                    converted_memories.append(Conversation(**m))
                else:
                    converted_memories.append(m)
            memories_id = [m.id for m in converted_memories]

        ai_message = Message(
            id=str(uuid.uuid4()),
            text=response,
            created_at=datetime.now(timezone.utc),
            sender='ai',
            app_id=app_id_from_app,
            type='text',
            memories_id=memories_id,
            chart_data=chart_data,
            langsmith_run_id=langsmith_run_id,  # Store run_id for feedback tracking
            prompt_name=prompt_name,  # LangSmith prompt name for versioning
            prompt_commit=prompt_commit,  # LangSmith prompt commit for traceability
        )