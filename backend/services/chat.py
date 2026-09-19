"""Application-level chat service.

Keeps HTTP concerns out of chat orchestration while the existing retrieval
engine is migrated incrementally.
"""

from typing import AsyncGenerator, List, Optional, Tuple

from models.app import App
from models.chat import ChatSession, Message, PageContext
from models.conversation import Conversation
from utils.retrieval.graph import execute_graph_chat, execute_graph_chat_stream


def execute_chat(
    uid: str,
    messages: List[Message],
    app: Optional[App] = None,
    cited: bool = False,
) -> Tuple[str, bool, List[Conversation]]:
    """Execute the chat use case through Aura's current engine."""
    return execute_graph_chat(uid, messages, app=app, cited=cited)


async def stream_chat(
    uid: str,
    messages: List[Message],
    app: Optional[App] = None,
    cited: bool = False,
    callback_data: Optional[dict] = None,
    chat_session: Optional[ChatSession] = None,
    context: Optional[PageContext] = None,
) -> AsyncGenerator[str, None]:
    """Stream the same chat use case without duplicating business logic."""
    async for chunk in execute_graph_chat_stream(
        uid,
        messages,
        app=app,
        cited=cited,
        callback_data=callback_data if callback_data is not None else {},
        chat_session=chat_session,
        context=context,
    ):
        yield chunk
