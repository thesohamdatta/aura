---
name: improve-codebase-architecture
description: Use when reviewing or refactoring Aura architecture. Apply deep-module/shallow-role principles, simplify dependency direction, and preserve behavior.
---

# Improve Aura Codebase Architecture

## Objective

Make Aura simpler to understand and change.

Do not add layers or abstractions unless they hide meaningful complexity.

## Inspect First

Read:
- `AGENTS.md`
- `REPO_MAP.md`
- nearest `CONTEXT.md`
- relevant tests
- relevant area README

Then inspect actual imports and execution paths.

## Deep Module / Shallow Role Test

A deep module:
- owns a complete decision
- hides implementation complexity
- exposes a small API

A shallow role:
- adapts input
- coordinates
- delegates
- serializes output

Find and correct:
- routers with business logic
- database modules with business decisions
- utilities that own unrelated workflows
- orchestrators calling other orchestrators
- wrappers that only delegate

## Backend Target

Prefer:

`transport -> application behavior -> domain decisions -> infrastructure`

A practical form may be:

`routers -> services -> repositories/providers -> external systems`

Do not create those folders mechanically.

## Chat

Treat chat as a primary application boundary.

Prefer one clear entry point such as:
- `execute_chat(...)`
- `stream_chat(...)`

Callers should not know whether chat uses graph routing, RAG, agents, or direct LLM calls.

Streaming is a delivery mechanism, not a second business implementation.

Never use nested `asyncio.run()` inside an already-async workflow.

## Database

Persistence modules persist and retrieve data.

They should not decide:
- model selection
- chat routing
- memory policy
- response strategy

Avoid generic repository hierarchies unless they solve a demonstrated problem.

## Providers

Keep provider-specific configuration behind meaningful boundaries.

Do not build a universal provider interface merely because several providers exist.

## Firmware

Keep `firmware/src/app.cpp` coordinating behavior.

Prefer small, understandable modules for:
- audio
- camera
- BLE
- power
- button/LED
- OTA

Preserve hardware and protocol behavior.

## Refactoring Rules

For each change:
1. identify current responsibility
2. identify correct owner
3. move responsibility
4. simplify callers
5. remove obsolete indirection
6. run focused verification
7. inspect the diff

Avoid unrelated cleanup.

Prefer one architectural reason per commit.

## Decision Rule

When two designs work, prefer the one with:
- fewer concepts
- fewer dependencies
- smaller interfaces
- stronger ownership
- easier local reasoning
- fewer files touched per behavior change

Ask:

> What complexity does this abstraction hide?

If the answer is unclear, do not add it.
