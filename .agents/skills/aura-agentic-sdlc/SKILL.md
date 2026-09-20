---
name: aura-agentic-sdlc
description: Use when planning, scoping, implementing, reviewing, or documenting Aura work through the repo-native agentic SDLC.
---

# Aura Agentic SDLC

Use this skill for Aura work that needs context, planning, implementation, review, or durable documentation.

## Sequence

1. Read `AGENTS.md`.
2. Read `REPO_MAP.md`.
3. Run `git rev-parse --show-toplevel` before any git operation.
4. Read the nearest relevant `CONTEXT.md`.
5. Read the area source of truth.
6. Inspect actual files before proposing changes.
7. Read `MARKDOWN_ENGINEERING.md` when Markdown is the task.
8. Make the smallest coherent change.
9. Verify with the closest available check.
10. Update durable docs when knowledge will matter in future sessions.

## Decisions vs Facts

Look up facts in the repo. Ask the maintainer for decisions.

## Documentation Targets

- `CONTEXT.md`: stable terms and compact context.
- `REPO_MAP.md`: canonical paths and navigation.
- `docs/adr/`: hard-to-reverse decisions.
- `docs/agentic-sdlc.md`: workflow.
- `MARKDOWN_ENGINEERING.md`: Markdown quality and synchronization.
- Issue and PR templates: structured work intake and review checklist.

## Website Lock

The production website is `website/1.2/website/`.

Current page contract:

- `index.html`
- `manifesto.html`
- `docs.html`
- `404.html`

Do not restore `about.html` or `ai.html` unless the maintainer explicitly changes the contract.
