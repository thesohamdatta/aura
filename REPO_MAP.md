# Aura Repository Map

## Canonical paths

| Area | Path | Ownership |
|---|---|---|
| Backend | `backend/` | FastAPI application, AI/data workflows |
| Firmware | `firmware/` | Pendant firmware |
| Android app | `app/` | Companion Android application |
| Hardware | `hardware/` | Physical design and build material |
| Website | `website/` | Production static website |
| Agent guidance | `AGENTS.md`, `.agents/skills/`, `.codex/`, `.claude/`, `.opencode/` | Agent behavior and repeatable procedures |
| Durable knowledge | `docs/` | Workflow, ADRs, knowledge indexes, task artifacts |

Confirm the repository root before any Git operation:

```bash
git rev-parse --show-toplevel
```

## Website truth

The production website source is `website/`.

GitHub Pages deploys:

```text
./website
```

from `.github/workflows/deploy-website.yml`.

Current page contract:

- `index.html`
- `manifesto.html`
- `docs.html`
- `404.html`

Do not treat `website/1.1/` or the former nested `website/1.2/` layout as active source unless a maintainer changes this contract.

## Documentation graph

- [Agent Guide](AGENTS.md)
- [Project Context](CONTEXT.md)
- [Markdown Engineering](docs/markdown-engineering.md)
- [Knowledge Index](docs/knowledge/INDEX.md)
- [Agentic SDLC](docs/agentic-sdlc.md)
- [Portable Workflow](docs/WORKFLOW.md)
- [Architecture Decisions](docs/adr/)
- [Task Work](docs/work/)
- [Repository Skills](.agents/skills/)

Use these as navigation roots. Do not make a second index that restates the same map.
