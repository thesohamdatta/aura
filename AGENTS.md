# Aura Agent Guide

## Project

Aura is an open-source, screenless, voice-first AI pendant. It combines:

- `firmware/`: XIAO ESP32-S3 Sense firmware.
- `backend/`: FastAPI AI backend.
- `app/`: Android companion app.
- `hardware/`: printable case and hardware notes.

The current maintainer is solo. Optimize workflows for one strong maintainer assisted by coding agents.

## Source Of Truth

Read [REPO_MAP.md](REPO_MAP.md) before structural work.

There is no production website in this repository. Product website and visual design are maintained externally in Figma and Framer.

## Documentation System

Use [docs/agentic-sdlc.md](docs/agentic-sdlc.md) for the workflow.

Use [REPO_MAP.md](REPO_MAP.md) for navigation and canonical paths.

Use [CONTEXT.md](CONTEXT.md) for project terms and stable context.

Use [docs/adr/](docs/adr/) for hard-to-reverse decisions.

Use [.agents/skills/](.agents/skills/) for repeatable procedures.

Use [MARKDOWN_ENGINEERING.md](MARKDOWN_ENGINEERING.md) for Markdown maintenance.

Do not duplicate durable knowledge across these files. Link to the owning document.

## Git Boundaries

This workspace contains a nested git repo. Confirm the repository root before git operations:

```powershell
git rev-parse --show-toplevel
```

Never run broad staging unless the task requires parent-level repository management.

## Agentic SDLC

Use this sequence:

`context -> grill -> plan -> issue/spec -> implement -> verify -> review -> document -> ship`

Rules:

- Context first. Read the repo map, relevant README, context, and local agent guide.
- Look up repository facts. Ask the maintainer only for decisions.
- Keep `AGENTS.md` short. Put detailed workflows in docs or skills.
- Record hard-to-reverse decisions as ADRs.
- Update durable context when a stable project term or boundary changes.

## Verification

Prefer the smallest check that matches the change.

- Harness changes: run the repository's documented harness check.
- Deployment changes: verify the affected deployment configuration.
- Markdown changes: run `python scripts/docs/check_markdown.py`.

State missing automated coverage in the final report.

## Maintenance Rule

Keep agent context compact. Move detail into the owning document and link to it.

When a Markdown change affects another document's facts or links, update the affected source of truth in the same change.
