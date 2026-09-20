# Aura: Project Context

## What this is

Aura is an open-source, screenless, voice-first AI pendant. Worn around the neck. Built by a 4-person undergraduate team in Pune, India. MIT licensed.

## Domain Glossary

| Term | Definition |
|---|---|
| **Pendant** | The physical Aura hardware, a roughly 42mm sphere worn on a lanyard. |
| **AI Pipeline** | Cloud processing for transcription, reasoning, vision, and searchable memory. See [backend/README.md](backend/README.md) for implementation details. |
| **BOM** | Bill of Materials, the list of hardware components and their costs. |
| **MCU** | Microcontroller Unit, the XIAO ESP32-S3 Sense that runs the firmware. |
| **Manifesto** | The essay page, "The Third Device Hypothesis". |

## Stable principles

1. Screenless is the product direction.
2. Open source is part of the product identity.
3. Project knowledge should have one canonical home and explicit links between layers.
4. Agent context should be progressively disclosed rather than loaded as one large document.

## Knowledge navigation

See [REPO_MAP.md](REPO_MAP.md) for canonical paths and [docs/markdown-engineering.md](docs/markdown-engineering.md) for the context architecture.

Stable architecture decisions belong in [docs/adr/](docs/adr/), not here.

## Domain Language Rules

Domain terms are canonical vocabulary, not implementation labels. Before introducing a new project-specific term, check existing definitions and the code that uses the concept. When terminology is resolved, update this glossary immediately; implementation details belong in skills, workflow docs, specs, or ADRs.
