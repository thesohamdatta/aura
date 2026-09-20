# Aura Agent Guide

## Project

Aura is an open-source, screenless, voice-first AI pendant. It combines:

- `firmware/`: XIAO ESP32-S3 Sense firmware.
- `backend/`: FastAPI AI backend.
- `app/`: Android companion app.
- `hardware/`: printable case and hardware notes.
- `website/1.2/website/`: production website.

The current maintainer is solo. Optimize workflows for one strong maintainer assisted by coding agents.

## Source Of Truth

Read [REPO_MAP.md](REPO_MAP.md) before structural work.

The production website is `website/1.2/website/`. Its active page contract is:

- `index.html`
- `manifesto.html`
- `docs.html`
- `404.html`

Legacy website files do not define current behavior. Verify deploy config and actual files before relying on older docs.

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

Website work belongs in `website/1.2`. Parent work belongs in the parent repository.

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

## Website Design Contract

For website edits, read the local website guidance before editing.

Website principles:

- Apple-like product page discipline.
- Photography first.
- One accent color: Action Blue.
- No hype or fake claims.
- CSS literals belong in design tokens.
- Keep pages static unless the maintainer changes the contract.

## Verification

Prefer the smallest check that matches the change.

- Website changes: inspect affected HTML, CSS, and assets. Use browser checks when visual behavior changes.
- Harness changes: run the repository's documented harness check.
- Deployment changes: verify `.github/workflows/deploy-website.yml`.

State missing automated coverage in the final report.

## Maintenance Rule

Keep agent context compact. Move detail into the owning document and link to it.

When a Markdown change affects another document's facts or links, update the affected source of truth in the same change.
