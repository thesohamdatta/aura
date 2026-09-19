---
name: aura
description: Use for any substantive work in the Aura repository. Load this skill to understand the real project structure, architecture boundaries, coding style, verification rules, and when to use specialized repo skills.
---

# Aura Repository Skill

Aura is an open-source screenless, voice-first multimodal AI pendant.

## Read First

For structural work:
1. `AGENTS.md`
2. `REPO_MAP.md`
3. nearest `CONTEXT.md`
4. area README or design contract

Treat actual code, deployment config, and tests as the source of truth when docs conflict.

## Repository Shape

- `backend/`: Python FastAPI backend and AI/data workflows
- `firmware/`: XIAO ESP32-S3 Sense firmware
- `app/`: companion Android/Flutter application
- `hardware/`: physical design and build material
- `website/`: current static website
- `.agents/skills/`: repeatable agent procedures

Do not assume a folder name implies architectural ownership.

## Architecture Rules

Prefer:
- deep modules
- shallow roles
- small public APIs
- clear ownership
- local reasoning
- explicit dependencies
- boring implementations
- minimal abstraction

Avoid:
- abstraction for abstraction's sake
- generic managers/factories
- interfaces that mirror one implementation
- service wrappers that only delegate
- speculative dependency injection
- duplicate orchestration
- framework-driven structure

The goal is fewer concepts and clearer boundaries, not more layers.

## Backend Boundaries

Use this as the default mental model:

`routers -> application behavior -> domain decisions -> infrastructure`

In the current backend:
- `routers/` handles HTTP transport/auth/serialization
- `database/` owns persistence
- provider-specific code owns external AI/service integrations
- application behavior should hide orchestration complexity

Do not create `services/`, `repositories/`, or `providers/` mechanically. Add a module only when it owns a meaningful decision.

Chat is a high-value boundary. Keep callers independent of whether the implementation uses graph routing, RAG, agents, or direct model calls.

## Firmware

Keep `firmware/src/app.cpp` primarily coordinating behavior.

Prefer small modules for:
- audio
- camera
- BLE
- power
- button/LED
- OTA

Do not introduce peripheral class hierarchies unless they solve a demonstrated problem.

Preserve hardware and protocol contracts, including BLE UUIDs, packet formats, timing, and power behavior.

## Change Discipline

Before editing:
- inspect the real execution path
- identify ownership
- define a small success criterion

During editing:
- make the smallest coherent change
- preserve behavior
- avoid unrelated cleanup
- remove only dead code made obsolete by your change

After editing:
- run the closest focused verification
- inspect the diff
- update durable documentation only when project knowledge changed

Prefer one architectural reason per commit.

## Documentation

- `AGENTS.md`: concise always-on agent rules
- `REPO_MAP.md`: canonical paths and boundaries
- `docs/agentic-sdlc.md`: workflow
- `docs/adr/`: hard-to-reverse decisions
- `.agents/skills/*/SKILL.md`: repeatable procedures

Do not duplicate long explanations across these files.

## Specialized Skills

Use when relevant:
- `.agents/skills/aura-agentic-sdlc/`: agent workflow
- `.agents/skills/karpathy-guidelines/`: careful, minimal implementation
- `.agents/skills/apple-aura-frontend/`: Aura website work
- `.agents/skills/apple-design-analysis/`: Apple-style design analysis

For architecture/refactoring, combine the Aura skill with the Karpathy guidelines. Do not assume a Matt Pocock-specific skill exists in this repository unless one is actually present.

## Verification Principle

Verify behavior, not implementation details.

If automated verification is unavailable for a touched area, document that explicitly in the PR.

## Context Budget

Keep this skill compact. Link to deeper documents instead of embedding long project history here.

The skill exists to help an agent decide:
1. where to look
2. what boundary owns the decision
3. what not to change
4. how to verify the result
