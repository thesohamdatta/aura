---
name: aura
description: Use for substantive work in the Aura repository. Load this skill to understand project structure, architectural boundaries, verification rules, and canonical context navigation.
---

# Aura Repository Skill

## Context loading

Start with:
1. `AGENTS.md`
2. `REPO_MAP.md`
3. nearest relevant `CONTEXT.md`
4. the area README or design contract

Treat code, tests, and deployment configuration as the implementation source of truth when documentation conflicts.

## Repository shape

- `backend/`: Python FastAPI backend and AI/data workflows
- `firmware/`: XIAO ESP32-S3 Sense firmware
- `app/`: Android companion application
- `hardware/`: physical design and build material
- `website/`: current static website
- `.agents/skills/`: repeatable agent procedures
- `docs/`: durable project knowledge, workflows, and decisions

## Architecture

Prefer deep modules, shallow roles, small public APIs, clear ownership, explicit dependencies, local reasoning, and minimal abstraction.

Avoid speculative layers, generic managers/factories, single-implementation interfaces, delegation-only wrappers, and duplicate orchestration.

For architecture/refactoring work, load `.agents/skills/improve-codebase-architecture/SKILL.md`.

## Canonical knowledge

Use:
- `AGENTS.md`: always-on operating rules and navigation
- `REPO_MAP.md`: repository paths and ownership
- `CONTEXT.md`: stable project vocabulary and durable context
- `docs/agentic-sdlc.md`: role model and lifecycle
- `docs/WORKFLOW.md`: delivery loop and evidence gates
- `docs/adr/`: hard-to-reverse decisions
- `.agents/skills/*/SKILL.md`: repeatable procedures

Tool-specific files should point to canonical sources instead of duplicating their rules.

## Change discipline

Before editing:
- trace the real execution path
- identify the owning boundary
- find the canonical knowledge source
- define a small success criterion

During editing:
- make the smallest coherent change
- preserve behavior and contracts
- avoid unrelated cleanup
- update canonical documentation when durable knowledge changes

After editing:
- run the closest focused verification
- inspect the diff
- validate links and referenced paths when Markdown/context is touched

## Context budget

Use progressive disclosure. Load only context relevant to the task. Prefer links to deeper knowledge over duplication.

When you discover durable knowledge, classify it as rule, map, context, ADR, skill, or task evidence. Put it in one canonical home and link dependents to it.
