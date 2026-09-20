# Aura

**An open-source, screenless AI wearable for ambient memory and voice-first interaction.**

Aura is a wearable pendant that captures audio and visual context, sends it through an AI pipeline, and makes the resulting memories searchable through a companion app. The project combines open hardware, embedded firmware, an AI backend, and a mobile interface in one repository.

[Website](https://thesohamdatta.github.io/aura/) · [Documentation](https://thesohamdatta.github.io/aura/docs.html) · [Manifesto](https://thesohamdatta.github.io/aura/manifesto.html) · [Contributing](CONTRIBUTING.md) · [License](LICENSE)

> Aura is an engineering project in active development. Interfaces, hardware revisions, and AI providers may change. For current behavior, use the code and linked documentation as the source of truth.

## Why Aura

Most computing makes you look at a screen. Aura explores a different interaction model: a small wearable that can stay with you, capture context, and let software turn that context into useful memory.

The project is intentionally open from the physical device to the software stack:

- **Screenless:** the pendant is designed around voice and ambient interaction rather than a display.
- **Multimodal:** audio is the primary stream, with visual context available through the camera.
- **Memory-first:** captured context can become searchable, conversational memory instead of a collection of isolated recordings.
- **Open hardware:** the enclosure and core hardware approach are intended to be reproducible rather than locked to a proprietary shell.
- **Open software:** firmware, backend, app, documentation, and developer tooling live in the repository.

Read the product thesis in the [Manifesto](website/manifesto.html).

## What is in this repository

| Area | Purpose | Start here |
|---|---|---|
| [`firmware/`](firmware/) | Embedded firmware for the wearable | [`firmware/readme.md`](firmware/readme.md) |
| [`backend/`](backend/) | FastAPI backend and AI/data workflows | [`backend/README.md`](backend/README.md) |
| [`app/`](app/) | Companion Android application | [`app/README.md`](app/README.md) |
| [`hardware/`](hardware/) | Physical design files and enclosure | [`hardware/`](hardware/) |
| [`website/`](website/) | Public website and build manual | [`website/docs.html`](website/docs.html) |
| [`docs/`](docs/) | Developer documentation, workflow, architecture, and durable project knowledge | [`docs/knowledge/INDEX.md`](docs/knowledge/INDEX.md) |
| [`.agents/skills/`](.agents/skills/) | Repeatable agent and engineering procedures | [Aura skill](.agents/skills/aura/SKILL.md) |

For the canonical repository boundaries, see [`REPO_MAP.md`](REPO_MAP.md).

## How the system fits

At a high level:

```text
+------------------+
|   Aura Pendant   |
|------------------|
| microphone       |
| camera           |
| XIAO ESP32-S3    |
+--------+---------+
         |
         | audio / visual context
         v
+------------------+
| Transport layer  |
| Wi-Fi / BLE      |
+--------+---------+
         |
         v
+------------------+
| Aura Backend     |
|------------------|
| transcription    |
| vision           |
| reasoning        |
| retrieval/memory |
+--------+---------+
         |
         v
+------------------+
| Companion App    |
|------------------|
| history          |
| search           |
| AI interaction   |
+------------------+
```

The exact provider and orchestration path can evolve. The important architectural boundary is that the wearable captures context, the backend turns context into useful data and intelligence, and the companion app provides the primary user-facing interface.

For the deeper system view, start with the [Build Manual](website/docs.html) and [developer documentation](docs/developer/).

## Core technical pieces

### Hardware

The current prototype is built around the **Seeed XIAO ESP32-S3 Sense**, which provides the main MCU platform together with onboard camera and microphone hardware.

The repository includes the printable enclosure at [`hardware/CASE.stl`](hardware/CASE.stl).

For the detailed build path, see the [Aura Build Manual](website/docs.html).

### Firmware

The firmware is responsible for device-side concerns such as capture and device connectivity.

Start with:

```text
firmware/
├── readme.md
├── src/
└── releases/
```

See [`firmware/readme.md`](firmware/readme.md) for the current flashing and architecture notes.

### Backend

The backend is a Python/FastAPI system that handles the heavier AI and data workflows.

Conceptually:

```text
device input
    |
    v
capture / ingestion
    |
    v
transcription + vision
    |
    v
reasoning / orchestration
    |
    v
memory + retrieval
    |
    v
API consumed by the companion app
```

Start with [`backend/README.md`](backend/README.md).

### Companion app

The app provides the human-facing layer for interacting with captured memories and AI features.

Start with [`app/README.md`](app/README.md).

## Getting started

There are four useful starting points, depending on what you are trying to do.

### I want to understand Aura

Read the [Manifesto](website/manifesto.html), then the [Build Manual](website/docs.html).

### I want to build the hardware

Start with the [hardware files](hardware/) and the [Build Manual](website/docs.html), then continue to [`firmware/readme.md`](firmware/readme.md).

### I want to work on the backend

Start with [`backend/README.md`](backend/README.md), then inspect the relevant developer documentation under [`docs/developer/backend/`](docs/developer/backend/).

### I want to work on the app

Start with [`app/README.md`](app/README.md), then continue to [`docs/developer/`](docs/developer/).

## Developer documentation

Aura's documentation is intentionally split by purpose so the root README stays useful to both humans and contributors.

### Start with these

- [Developer documentation](docs/developer/)
- [Knowledge index](docs/knowledge/INDEX.md)
- [Project context](CONTEXT.md)
- [Repository map](REPO_MAP.md)
- [Agentic SDLC](docs/agentic-sdlc.md)
- [Markdown engineering](docs/markdown-engineering.md)

The documentation system also contains architecture decisions in [`docs/adr/`](docs/adr/) and task-level engineering artifacts in [`docs/work/`](docs/work/).

## Building and developing

Aura spans multiple toolchains. Avoid assuming that one setup command builds the entire repository.

### Backend

See [`backend/README.md`](backend/README.md) for backend-specific environment and development instructions.

### Firmware

See [`firmware/readme.md`](firmware/readme.md) for flashing and device development.

### App

See [`app/README.md`](app/README.md) for Android development.

### Website

The website is a static site under [`website/`](website/). The deployment workflow publishes that directory through GitHub Pages.

## Current project shape

Aura is not presented here as a finished consumer platform. It is an open-source engineering project where hardware, firmware, application code, AI workflows, and documentation are developed together.

| Contributor | Useful areas |
|---|---|
| Embedded / hardware engineer | `firmware/`, `hardware/` |
| Backend / AI engineer | `backend/`, `docs/developer/backend/` |
| Mobile engineer | `app/`, `docs/developer/` |
| AI / agent engineer | `backend/`, `.agents/skills/`, `docs/` |
| Researcher | `docs/`, architecture notes, experiments, and implementation |
| Open-source contributor | Issues, `CONTRIBUTING.md`, and the relevant subsystem docs |

## Open-source scope

The repository brings together:

- wearable hardware and enclosure work
- embedded firmware
- mobile application code
- backend and AI workflows
- developer documentation
- agent engineering and repository context

The goal is not simply to publish source code. It is to keep the design, implementation, and reasoning visible enough that another developer can reproduce the system, understand its trade-offs, and improve it.

## Contributing

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

For a substantive engineering change, read the repository context first:

```text
AGENTS.md
   ↓
REPO_MAP.md
   ↓
CONTEXT.md
   ↓
relevant subsystem README
   ↓
relevant skill / architecture decision
   ↓
source + tests
```

Use small, reviewable changes. Preserve existing hardware, API, and protocol contracts unless the change explicitly intends to modify them.

## Security and responsible use

Aura is a wearable sensing system. Contributions that affect recording, capture, storage, authentication, device communication, or user data deserve particular care.

See [`SECURITY.md`](SECURITY.md) for vulnerability reporting.

## Project links

[Website](https://thesohamdatta.github.io/aura/) · [Documentation](https://thesohamdatta.github.io/aura/docs.html) · [Issues](https://github.com/thesohamdatta/aura/issues) · [Pull Requests](https://github.com/thesohamdatta/aura/pulls) · [Contributing](CONTRIBUTING.md)

## License

Aura is released under the [MIT License](LICENSE).