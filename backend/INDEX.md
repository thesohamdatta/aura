# Backend Module Index

## Dependency direction

```
routers -> services -> repositories/providers
                 |
                 +-> models
```

### routers/
HTTP and WebSocket adapters. No business workflow orchestration.

### services/
Application use cases. This is where a request becomes a meaningful Aura operation such as chat, transcription, memory creation, or conversation processing.

### repositories/
Persistence boundaries for Firestore, Redis, Pinecone, storage, and other data stores. Existing `database/` modules are being migrated here incrementally.

### providers/
External service clients and AI model configuration. Provider selection belongs here rather than in route handlers.

### models/
Pydantic models and lightweight domain structures shared by layers.

### utils/
Legacy compatibility area. New application logic should not be added here. Existing modules move out only when a change already touches them.

### migrations/, scripts/, testing/
Operational and maintenance code. They are not application layers.

## Deep-module rule

A module should own a complete decision, expose a small interface, and hide the details required to implement that decision. Avoid wrappers that merely rename another function or pass arguments through.
