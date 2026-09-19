# Aura Backend

FastAPI backend for Aura's capture, memory, retrieval, and AI workflows.

## Architecture

The backend follows a deliberately small dependency direction:

```
HTTP / WebSocket
      ↓
routers/
      ↓
services/
      ↓
repositories/ + providers/
```

- `routers/` owns HTTP concerns only: validation, authentication, status codes, and response serialization.
- `services/` owns application behavior and orchestration.
- `repositories/` owns persistence and external data stores.
- `providers/` owns replaceable external AI/infrastructure clients.
- `models/` contains request, response, and domain data structures.

Do not add a new abstraction layer unless it removes a real dependency or makes a concrete boundary easier to test.

## Core request path

Chat should have one application entry point:

```
routers/chat.py
    -> services/chat.py
        -> retrieval/chat.py
            -> repositories + providers
```

Streaming and non-streaming are two delivery modes of the same service operation. They should not create parallel business logic.

## Rules

1. Prefer one deep module over many shallow helpers.
2. Keep routers thin. A route should normally read as: authenticate -> call service -> serialize result.
3. Keep provider details out of services when practical.
4. Keep Firestore, Redis, Pinecone, and provider SDK imports out of domain modules.
5. Prefer plain functions and small data objects over speculative classes.
6. Delete dead paths instead of preserving duplicate implementations.
7. Preserve public API behavior while refactoring internals.

## Verification

Run the smallest relevant test set after changes. For chat changes, run the chat/retrieval unit tests and a Python import check before considering the refactor complete.
