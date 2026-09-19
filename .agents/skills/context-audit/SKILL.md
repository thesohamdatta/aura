---
name: context-audit
description: Audit Aura's Markdown engineering and agent-context system for stale links, duplicate canonical claims, orphaned files, inconsistent paths, and broken navigation.
---

# Context Audit

## Goal

Keep Aura's agent knowledge graph navigable, bounded, and internally consistent.

## Inspect

Read `AGENTS.md`, `REPO_MAP.md`, `CONTEXT.md`, `docs/markdown-engineering.md`, `docs/agentic-sdlc.md`, and `docs/WORKFLOW.md`.

Then inventory Markdown and agent-config files.

## Rules

### Links
Every relative Markdown link must resolve to a tracked file or directory.

### Canonicality
Flag cases where multiple files claim to be the source of truth for the same fact.

### Drift
Flag references to deleted, renamed, legacy, or contradictory paths.

### Orphans
Flag durable Markdown files not reachable from `AGENTS.md`, `REPO_MAP.md`, or an appropriate domain index.

### Duplication
Flag repeated operational rules that should have one canonical owner.

### Scope
Flag large always-on files containing task-specific content that belongs in scoped knowledge.

## Output

Report finding, severity, path, evidence, and recommended canonical owner.

Audit mode is read-only. Use the full SDLC pipeline for repairs.
