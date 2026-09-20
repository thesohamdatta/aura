# Aura Repository Map

## Repositories

| Path | Git root | Purpose |
|---|---|---|
| parent repository | parent root | Hardware, firmware, backend, Android app, deployment, top-level docs |
| `website/1.2` | nested git root | Current website and website agent harness |

Confirm the root before commits:

```powershell
git rev-parse --show-toplevel
```

## Product Areas

| Area | Path | Current role |
|---|---|---|
| Website | `website/1.2/website/` | Production static website |
| Website design sources | `website/1.2/BRAND_BRIEF.md`, `website/1.2/DESIGN.md`, `website/1.2/PRODUCT.md` | Website design and product contract |
| Website harness | `website/1.2/agent_harness.py`, `website/1.2/workflows/`, `website/1.2/prompts/` | Website agent workflow |
| Firmware | `firmware/` | Pendant firmware |
| Backend | `backend/` | AI backend |
| Android app | `app/` | Companion app |
| Hardware | `hardware/` | Physical build assets |
| Agent docs | `AGENTS.md`, `docs/agentic-sdlc.md`, `docs/adr/`, `MARKDOWN_ENGINEERING.md` | Agent navigation and operating rules |

## Website Truth

The live website source is `website/1.2/website/`.

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
