# Aura Agent Guide

## Project

Aura is an open-source, screenless, voice-first multimodal AI pendant.

- `backend/`: Python FastAPI backend and AI/data workflows.
- `firmware/`: XIAO ESP32-S3 Sense firmware.
- `app/`: Android companion application.
- `hardware/`: physical design and build material.
- `website/`: current static website.

## Source Of Truth

Start with [REPO_MAP.md](REPO_MAP.md), then load only the nearest relevant context.

Canonical knowledge boundaries are documented in [docs/markdown-engineering.md](docs/markdown-engineering.md).

## Agentic SDLC

For substantive work follow [docs/agentic-sdlc.md](docs/agentic-sdlc.md) and [docs/WORKFLOW.md](docs/WORKFLOW.md):

`context -> grill -> brainstorm -> plan -> spec -> tickets -> implement -> verify -> review -> document -> ship -> learn`

## Knowledge rules

- Keep this file short and always-on.
- Put repository navigation in [REPO_MAP.md](REPO_MAP.md).
- Put stable domain context in [CONTEXT.md](CONTEXT.md).
- Put durable decisions in [docs/adr/](docs/adr/).
- Put repeatable procedures in [.agents/skills/](.agents/skills/).
- Put task-local plans/specs/evidence in [docs/work/](docs/work/).
- Use [docs/knowledge/INDEX.md](docs/knowledge/INDEX.md) for durable entry points.
- One durable fact should have one canonical home. Link to it instead of copying it.
- Promote durable discoveries at the end of substantive work so the repository compounds over time.

## Safety and scope

Never commit secrets.

For firmware, preserve hardware and protocol contracts unless explicitly changed. Be especially careful with BLE UUIDs, packet formats, timing, power, camera, and audio behavior.

For website work, [REPO_MAP.md](REPO_MAP.md) is authoritative for the active page contract.

## Verification

Use the smallest useful check for the touched area and record the evidence. For Markdown/context work, run the context audit when relevant.

## Context budget

Do not load unrelated project history. Use progressive disclosure and follow links to deeper knowledge only when the task requires it.
