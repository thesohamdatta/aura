# Aura: Project Context

## What this is

Aura is an open-source, screenless, voice-first AI pendant. Worn around the neck. Built by a 4-person undergraduate team in Pune, India. Total bill of materials: about $50 USD. MIT licensed.

## Domain Glossary

| Term | Definition |
|---|---|
| **Pendant** | The physical Aura hardware, a roughly 42mm sphere worn on a lanyard. |
| **AI Pipeline** | The 4-layer cloud processing: Deepgram for Speech-to-Text, Groq Llama-3 for language, GPT-4o for vision, Pinecone for Retrieval Augmented Generation (RAG) memory. |
| **BOM** | Bill of Materials, the list of hardware components and their costs. |
| **MCU** | Microcontroller Unit, the XIAO ESP32-S3 Sense that runs the firmware. |

## Design Principles

1. Certainty, not excitement. Use measured language and honest limits.
2. No exclamation marks. Prefer facts and verified claims.
3. Screenless is the product. Keep the pendant as the visual hero.
4. Open source is part of the product identity.

## Durable Decisions

Architecture decisions live in [docs/adr/](docs/adr/). Do not copy decision text here.

## Documentation Ownership

- [AGENTS.md](AGENTS.md): always-on agent rules.
- [REPO_MAP.md](REPO_MAP.md): repository navigation.
- [docs/agentic-sdlc.md](docs/agentic-sdlc.md): agent workflow.
- [MARKDOWN_ENGINEERING.md](MARKDOWN_ENGINEERING.md): Markdown quality and synchronization rules.
