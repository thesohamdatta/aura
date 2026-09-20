---
name: domain-modeling
description: Build and sharpen Aura's domain model. Use when discussing codebase terminology, writing or editing CONTEXT.md, or recording or editing an ADR.
---

# Domain Modeling

This repository uses one root domain context: `CONTEXT.md`.

## Before changing the model

Read:
- `CONTEXT.md` for canonical vocabulary
- relevant `docs/adr/` decisions
- the code paths that use the term being discussed

Do not use this skill merely to consume context. Use it when the domain language itself is changing.

## Challenge terminology

When a new term conflicts with `CONTEXT.md`, stop and surface the conflict instead of silently choosing a synonym.

When a term is vague or overloaded, propose a precise canonical term and list rejected synonyms under `_Avoid_`.

## Stress-test the model

Use concrete scenarios to test boundaries between concepts, especially:
- one input belonging to multiple concepts
- empty or missing state
- lifecycle transitions
- cross-area interactions
- legacy names that still exist in code

When code and the stated model disagree, identify the contradiction and resolve the terminology before rewriting documentation.

## Update `CONTEXT.md` inline

When a domain term is resolved, update `CONTEXT.md` immediately.

Rules:
- definitions are one or two sentences
- define what the concept is, not implementation details
- include only Aura-specific domain language
- use `_Avoid_` for competing names
- keep implementation paths, workflows, and architecture out of `CONTEXT.md`

## ADR rule

Create an ADR only when all three are true:
1. the decision is meaningfully hard to reverse;
2. a future maintainer would find the choice surprising without context;
3. there were real alternatives with a meaningful trade-off.

Otherwise keep the decision in the appropriate workflow/specification file.

Use the repository's `docs/adr/` numbering and format.

## Context-engineering integration

Domain language is canonical knowledge. Agent skills, workflow docs, specs, and area documentation should link to `CONTEXT.md` rather than redefining its terms.

Do not add implementation details merely to make an agent feel informed. Progressive disclosure is preferred.