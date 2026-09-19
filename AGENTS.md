# Aura Agent Guide

## Project

Aura is an open-source, screenless, voice-first multimodal AI pendant.

- `backend/`: Python FastAPI backend and AI/data workflows.
- `firmware/`: XIAO ESP32-S3 Sense firmware.
- `app/`: companion Android/Flutter application.
- `hardware/`: physical design and build material.
- `website/`: current static website.

## Source Of Truth

Read `REPO_MAP.md` before structural work.

When documentation conflicts with code, deployment configuration, or tests, inspect the actual implementation and record the discrepancy before changing architecture.

## Agentic SDLC

For substantive work:

`context -> plan -> implement -> verify -> review -> document -> ship`

Keep `AGENTS.md` short. Use `.agents/skills/*/SKILL.md` for repeatable procedures and `docs/adr/` for hard-to-reverse decisions.

## Architecture

Prefer:
- deep modules
- shallow roles
- small public APIs
- clear ownership
- explicit dependencies
- local reasoning
- minimal abstraction

Avoid:
- speculative layers
- generic managers/factories
- single-implementation interfaces
- service wrappers that only delegate
- duplicate orchestration

Use `.agents/skills/improve-codebase-architecture/SKILL.md` for architecture/refactoring work.

## Safety

Never commit secrets.

For firmware work, preserve hardware/protocol contracts unless explicitly changing them. Be especially careful with BLE UUIDs, packet formats, timing, power behavior, camera/audio behavior, and battery-related code.

For website work, keep the current static page contract in `REPO_MAP.md` authoritative.

## Verification

Use the smallest useful check for the change:
- backend: focused tests/import/type/lint checks where available
- firmware: compile/build where available
- app: focused tests/analyzer where available
- website: static inspection and browser verification when visual behavior changes

If no automated check exists for a touched area, state that explicitly in the PR.

## Context Budget

Do not duplicate long project history in agent instructions.

Before editing, load only the context relevant to the task.