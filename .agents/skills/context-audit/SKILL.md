---
name: context-audit
description: Audit Aura's Markdown engineering and agent-context system for stale links, duplicate canonical claims, orphaned files, inconsistent paths, and broken navigation.
---

# Context Audit

## Goal

Keep Aura's agent knowledge graph navigable, bounded, and internally consistent.

## Inspect

Read:
- `AGENTS.md`
- `REPO_MAP.md`
- `CONTEXT.md`
- `docs/markdown-engineering.md`
- `docs/agentic-sdlc.md`
- `docs/WORKFLOW.md`

Then inventory Markdown and agent-config files.

## Audit rules

### Links
- Every relative Markdown link must resolve to a tracked file or directory.
- Paths named in code blocks and prose should be checked when they are presented as canonical or executable.

### Canonicality
Flag cases where multiple files claim to be the source of truth for the same fact.

### Drift
Flag references to deleted, renamed, legacy, or contradictory paths.

### Orphans
Flag durable Markdown files that are not reachable from `AGENTS.md`, `REPO_MAP.md`, or an appropriate domain index.

### Duplication
Flag repeated operational rules that should live in one canonical source.

### Scope
Flag large always-on files that contain task-specific material better moved to scoped knowledge.

## Output

Report:
- finding
- severity
- file/path
- evidence
- recommended canonical owner

Do not edit during an audit unless explicitly asked to run the repair phase.
