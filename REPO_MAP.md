# Aura Repository Map

## Repositories

| Path                           | Git root    | Purpose                                                                         |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------- |
| `D:\PROJECTS\AURA`             | parent repo | Aura hardware, firmware, backend, Android app, deployment, top-level agent docs |
| `D:\PROJECTS\AURA\website\1.2` | nested repo | Current Aura website and agent harness experiments                              |

Always confirm the git root before committing:

```powershell
git rev-parse --show-toplevel
```

## Product Areas

| Area                   | Path                                                                             | Current role                                        |
| ---------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| Website                | `website/`                                                           | Production static website served by GitHub Pages    |
| Website design sources | `website/BRAND_BRIEF.md`, `website/DESIGN.md`, `website/PRODUCT.md`  | Design and product contract for website agents      |
| Website harness        | `website/` agent files, when present | Website-specific workflows |
| Firmware               | `firmware/`                                                                      | Pendant firmware                                    |
| Backend                | `backend/`                                                                       | AI backend                                          |
| Android app            | `app/`                                                                           | Companion app                                       |
| Hardware               | `hardware/`                                                                      | Case and physical build notes                       |
| Agent docs             | `AGENTS.md`, `docs/agentic-sdlc.md`, `docs/adr/`                                 | How agents should navigate and change the repo      |

## Website Truth

The canonical production website source is `website/`. The former nested website repo is no longer part of the canonical parent-repository layout.

GitHub Pages deploys this directory from:

```text
.github/workflows/deploy-website.yml
```

Current page contract:

- `index.html`
- `manifesto.html`
- `docs.html`
- `404.html`

Do not treat `website/1.1/` or deleted files under parent `docs/` as active website source.

## Documentation Truth

- Top-level project context: `CONTEXT.md`
- Website context: `website/CONTEXT.md`
- Agentic workflow: `docs/agentic-sdlc.md`
- Architecture decisions: `docs/adr/`

Keep `CONTEXT.md` glossary-like. Put workflows in docs. Put hard-to-reverse decisions in ADRs.
