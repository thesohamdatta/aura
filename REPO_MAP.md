# Aura Repository Map

## Repositories

| Path | Git root | Purpose |
|---|---|---|
| parent repository | parent root | Hardware, firmware, backend, Android app, deployment, top-level docs |
| `website/` | parent repository | Production static website |

Confirm the root before commits:

```powershell
git rev-parse --show-toplevel
```

## Product Areas

| Area | Path | Current role |
|---|---|---|
| Website | `website/` | Production static website |
| Website design sources | `website/` source files and assets | Website design and product contract |
| Website harness | `.agents/`, `.codex/`, `.claude/`, `.opencode/` | Repository-wide agent workflow |
| Firmware | `firmware/` | Pendant firmware |
| Backend | `backend/` | AI backend |
| Android app | `app/` | Companion app |
| Hardware | `hardware/` | Physical build assets |
| Agent docs | `AGENTS.md`, `docs/agentic-sdlc.md`, `docs/adr/`, `MARKDOWN_ENGINEERING.md` | Agent navigation and operating rules |

## Website Truth

The live website source is `website/`.

GitHub Pages deploys that directory through `.github/workflows/deploy-website.yml`.

Current page contract:

- `index.html`
- `manifesto.html`
- `docs.html`
- `404.html`

Verify deploy config and actual files before using older website references.

## Documentation Truth

| Need | Source |
|---|---|
| Agent rules | [AGENTS.md](AGENTS.md) |
| Repository paths | [REPO_MAP.md](REPO_MAP.md) |
| Project terms | [CONTEXT.md](CONTEXT.md) |
| Agent workflow | [docs/agentic-sdlc.md](docs/agentic-sdlc.md) |
| Hard-to-reverse decisions | [docs/adr/](docs/adr/) |
| Markdown maintenance | [MARKDOWN_ENGINEERING.md](MARKDOWN_ENGINEERING.md) |

One fact has one owner. Other documents link to that owner.
