---
name: documentation-update
description: Run the Aura documentation workflow using canonical Markdown engineering rules.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /documentation-update

Start with [AGENTS.md](../../../../AGENTS.md), [REPO_MAP.md](../../../../REPO_MAP.md), and [docs/markdown-engineering.md](../../../../docs/markdown-engineering.md).

Follow the [Aura SDLC](../../../../docs/agentic-sdlc.md).

When documentation changes durable project knowledge:
1. update the single canonical owner;
2. repair dependent links;
3. run the context audit;
4. record verification evidence.

This command is an adapter, not a second source of truth.
