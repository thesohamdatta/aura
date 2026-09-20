---
name: markdown-engineering
description: Use when creating, reviewing, refactoring, or synchronizing Markdown files in the Aura repository.
---

# Markdown Engineering

## Purpose

Keep repository Markdown navigable, compact, verifiable, and synchronized.

Markdown files form a context graph. Agents should enter at any relevant document and reach the owning source of truth through links.

## Scope

### Governed

Apply these rules to Aura-authored Markdown:

- Root agent and project docs.
- Area READMEs.
- Guides.
- Architecture Decision Records (ADRs).
- Skills and agent instructions.
- Templates that define repository workflows.

### Excluded

Do not rewrite:

- Vendored dependency documentation.
- Generated files.
- Imported third-party chart docs.

Mark exclusions in the scope report when they matter.

## Laws

| ID | Rule |
|---|---|
| L1 | Document once. Link from other files. |
| L2 | Give each file one primary responsibility. |
| L3 | Define each acronym on first use. |
| L4 | Avoid filler wording and banned terms. |
| L5 | Prefer structure over prose. |
| L6 | Keep sentences at 25 words or fewer. |
| L7 | Name the subject at sentence openings. |
| L8 | Make factual claims traceable to a command, file, or link. |

## Contracts

| File type | Contract |
|---|---|
| `AGENTS.md` | Project rules, boundaries, conventions, verification, and documentation ownership |
| `README.md` | What, why, install, one usage path, and links |
| `CONTEXT.md` | Stable terms and compact project context |
| `REPO_MAP.md` | Canonical paths and navigation |
| `principle.md` | Rule, why, fails-when |
| `sold.md` | Principle plus proof |
| Guide | Intro, prerequisites, verb-first steps, conclusion |
| Skill | Frontmatter, trigger, procedure, verification |

Use a more specific contract when the repository or third-party format requires one.

## Read Before Writing

1. List all Markdown files in scope.
2. Read the target file.
3. Read its top three cross-references.
4. Search for the main phrase before adding new content.
5. Read the applicable contract.
6. Verify every new link against the repository tree.

Do not invent a missing file to satisfy a link. Fix or remove the link.

## Workflow

1. **Scope**: list files and affected laws.
2. **Audit**: run the quality gate and list failures.
3. **Plan**: order fixes by cross-file blast radius.
4. **Edit**: make the smallest coherent diff.
5. **Verify**: rerun the gate and link checks.
6. **Log**: append durable lessons to [LEARNINGS.md](LEARNINGS.md).
7. **Commit**: use `docs(<file>): <imperative>`.

## Quality Gate

Run:

```bash
python scripts/docs/check_markdown.py
```

The checker covers heading depth, sentence length, banned terms, sentence openers, frontmatter, and internal links.

Manual review still covers:

- One primary responsibility per file.
- No duplicated durable knowledge.
- Correct source-of-truth ownership.
- Acronym definitions.
- Example consistency.
- Appropriate callout density.

A Markdown change passes only when the checker passes and manual ownership review finds no blocking issue.

## Context Budget

- Read only the scope required for the task.
- Load one owning source before loading derived docs.
- Follow links by relevance, not by volume.
- Stop reading when the source of truth answers the question.
- Never request every Markdown file when one canonical source is enough.

## Change Policy

Do not rewrite a file unless more than 40% of the content violates this contract.

Prefer block-level edits. Preserve correct structure and working links.

Do not duplicate knowledge to make context feel complete.

## Cross-File Synchronization

When one document changes:

1. Identify claims that other docs repeat.
2. Keep the changed claim in its owner.
3. Replace repeated text with a link.
4. Update navigation when paths change.
5. Record drift or a new rule in LEARNINGS.md.

## Sub-Agents

Use one sub-agent per independently owned file.

Brief each sub-agent with:

`{path, contract, laws, quality gate, allowed scope}`

Sub-agents edit only their assigned file. Merge changes sequentially.

Resolve conflicts by preserving L1 and the documented source of truth.

## Refuse Conditions

Stop rather than edit when:

- The requested file has no single responsibility.
- The request requires duplicated durable knowledge.
- A cross-file link cannot be verified.

## Output

Report:

1. Scope
2. Audit
3. Diff
4. Gate
5. Log
6. Commit
7. Next
