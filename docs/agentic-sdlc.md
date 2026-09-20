# Aura Agentic SDLC

Aura uses a lightweight solo-maintainer agentic workflow. The goal is to give coding agents enough structure for senior-quality work without losing the product thesis.

## Operating Model

Current mode: one maintainer, many agent sessions.

Future mode: contributors can follow the same workflow through issues, PR templates, and docs.

Default loop:

```text
context -> grill -> plan -> issue/spec -> implement -> verify -> review -> document -> ship
```

## Roles

| Role | Job | Output |
|---|---|---|
| Maintainer | Sets intent and resolves product decisions | Decision, approval, merge |
| Context agent | Reads repo, docs, current state, and constraints | Short context report |
| Architect | Converts intent into a small spec | Plan, acceptance criteria, affected files |
| Developer | Makes the smallest coherent change | Patch and verification notes |
| Reviewer | Checks correctness, design rules, tests, and regressions | Findings and residual risk |
| Documenter | Updates durable context | ADR, glossary, guide, or issue resolution |

Use subagents only when research, audit, or review can proceed without blocking local work.

## Context Rules

Before work:

1. Read [AGENTS.md](../AGENTS.md).
2. Read [REPO_MAP.md](../REPO_MAP.md).
3. Confirm the git root.
4. Read the nearest relevant `CONTEXT.md`.
5. Read the area README or design contract.
6. Inspect actual files before planning.
7. Read [MARKDOWN_ENGINEERING.md](../MARKDOWN_ENGINEERING.md) when Markdown changes.
8. Run `python scripts/docs/check_markdown.py` after Markdown edits.

Ask the maintainer about decisions. Do not ask about facts that can be found in the repository.

## Work Item Shape

Good work items include:

- Problem
- Desired outcome
- Files likely involved
- Constraints
- Acceptance criteria
- Verification command or manual check
- Non-goals

## Documentation Workflow

Use [MARKDOWN_ENGINEERING.md](../MARKDOWN_ENGINEERING.md) for Markdown-specific work.

Use the smallest durable document:

- [CONTEXT.md](../CONTEXT.md): stable terms and compact project context.
- [REPO_MAP.md](../REPO_MAP.md): canonical paths and navigation.
- [docs/adr/](adr/): hard-to-reverse decisions.
- `.agents/skills/*/SKILL.md`: repeatable procedures agents should load on demand.

## ADR Rule

Create an ADR only when all are true:

- Hard to reverse.
- Surprising without context.
- Chosen from real alternatives.

## Guardrails

- Never commit secrets.
- Never make broad cleanup while solving a narrow task.
- Never change the active website page contract without maintainer approval.
- Never mix parent and nested website repository commits.
- Never trust stale docs over deploy config and actual file structure.
