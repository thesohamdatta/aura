# Markdown Engineering for Aura

## Purpose

Aura uses Markdown as a version-controlled control plane for coding agents: durable rules, navigation, architecture knowledge, repeatable procedures, task specifications, evidence, and decisions.

The goal is not to maximize the number of Markdown files. The goal is to make the right knowledge discoverable at the right time.

## Mental model

```text
always-on rules
      ↓
repository map
      ↓
stable context
      ↓
scoped knowledge
      ↓
skills / workflows / specs
      ↓
implementation evidence
      ↓
review
      ↓
durable learning
      ↺
```

## Source ownership

| Artifact | Canonical purpose |
|---|---|
| `AGENTS.md` | Always-on operating rules and navigation |
| `REPO_MAP.md` | Canonical repository paths and ownership |
| `CONTEXT.md` | Stable project language and durable context |
| `docs/adr/` | Hard-to-reverse, non-obvious decisions |
| `docs/agentic-sdlc.md` | Agent role model and lifecycle |
| `docs/WORKFLOW.md` | Portable delivery loop and evidence gates |
| `.agents/skills/` | Repeatable procedures |
| `.codex/agents/` | Tool-specific read-only roles that point at repository knowledge |
| `.claude/commands/` | Tool-specific command adapters |
| `docs/work/` | Task-local specifications, research notes, and evidence |

One durable fact should have one canonical home. Dependent files should link to it rather than copy it.

## Progressive disclosure

Keep always-loaded context compact.

Load deeper knowledge only when the task requires it. A useful path is:

```text
AGENTS.md
  → REPO_MAP.md
    → nearest CONTEXT.md
      → area README
        → relevant skill / ADR
          → task spec
            → source + tests
```

Do not turn `AGENTS.md` or `CONTEXT.md` into encyclopedias.

## Cross-linking rules

Every durable knowledge file should:

1. state what it owns;
2. link to its parent navigation document;
3. link to the next deeper canonical sources when relevant;
4. avoid restating rules owned elsewhere.

Prefer relative repository links.

## Compounding loop

During work, agents should capture durable discoveries such as:
- a changed architectural boundary
- a corrected canonical path
- a surprising provider constraint
- a repeated failure mode
- a useful verification command

At the end of the task, promote only durable discoveries. Put each in its canonical home and add backlinks where they improve navigation.

## Anti-patterns

Do not:
- duplicate the same rule across multiple Markdown files;
- keep old paths in active agent instructions;
- create memory files for facts that code already expresses;
- store raw session transcripts as permanent project knowledge;
- use a giant index that must list every Markdown file;
- make a tool adapter a second source of truth.

## Maintenance

Documentation/context changes are reviewed like code. Broken links, stale paths, conflicting canonical claims, and missing navigation are defects.

Use the `context-audit` skill for audits and the Aura SDLC skill for full change lifecycle work.
