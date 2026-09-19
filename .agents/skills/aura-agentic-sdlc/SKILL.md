---
name: aura-agentic-sdlc
description: Use when planning, scoping, implementing, reviewing, or documenting Aura work through the repo-native agentic SDLC.
---

# Aura Agentic SDLC

## Pipeline

`context -> grill -> brainstorm -> plan -> spec -> tickets -> implement -> verify -> review -> document -> ship -> learn`

Do not skip a substantive gate. Deployment remains human-controlled.

## Context
Read:
1. `AGENTS.md`
2. `REPO_MAP.md`
3. nearest relevant `CONTEXT.md`
4. area README/design contract
5. relevant skill, workflow, and ADR

Inspect actual source before proposing changes.

## Grill
Produce problem, desired outcome, evidence, constraints, risks, non-goals, and unresolved decisions. Do not implement while a material decision is unresolved.

## Brainstorm
Generate a small set of viable approaches. Compare concepts, files, dependencies, reversibility, and verification cost. Record the selected approach in the plan.

## Plan / Spec
Persist multi-step work under `docs/work/` and include affected files, ownership, acceptance criteria, verification, and non-goals.

## Implement
One coherent change at a time. Preserve unrelated work and existing contracts.

## Verify
For Markdown/context changes, validate links, referenced paths, frontmatter, canonical references, stale/deprecated paths, and orphaned knowledge. For code, use the closest existing test/build/lint check.

## Review
Fresh read of the final diff. Check correctness, security, regressions, architecture, context pollution, stale or duplicated knowledge, and missing verification.

## Document / Learn
Promote only durable discoveries into one canonical home. Add backlinks where useful. Do not turn temporary observations into permanent rules.

## Ship
Before shipping, confirm repository boundary, verification evidence, and review state.

## Compounding loop
The repository should become easier for the next agent to understand. Successful discoveries become clearer context, reusable skills, ADRs, workflow improvements, or verification rules rather than more raw Markdown.
