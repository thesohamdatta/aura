# Aura Repository Map

## Repositories

| Path | Git root | Purpose |
|---|---|---|
| parent repository | parent root | Hardware, firmware, backend, Android app, deployment, top-level docs |

Confirm the root before commits:

```powershell
git rev-parse --show-toplevel
```

## Product Areas

| Area | Path | Current role |
|---|---|---|
| Firmware | `firmware/` | Pendant firmware |
| Backend | `backend/` | AI backend |
| Android app | `app/` | Companion app |
| Hardware | `hardware/` | Physical build assets |
| Agent docs | `AGENTS.md`, `docs/agentic-sdlc.md`, `docs/adr/`, `MARKDOWN_ENGINEERING.md` | Agent navigation and operating rules |

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
