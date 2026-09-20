<div align="center">

# Aura

<img src="Assets/hero/aura-ascii-gold.png" alt="AURA" width="900" />

<p>
Open-source, screenless, voice-first AI pendant.
<br />
Voice in. Memory out. No screen.
</p>

</div>

## What it is

Aura is a wearable AI pendant built around the XIAO ESP32-S3 Sense. It captures audio and images, sends them to the backend, and makes the resulting memory available through the companion app.

## Repository

| Area | Path |
|---|---|
| Firmware | [`firmware/`](firmware/) |
| Backend | [`backend/`](backend/) |
| Companion app | [`app/`](app/) |
| Hardware | [`hardware/`](hardware/) |
| Website | [`website/`](website/) |

## Start here

| Task | Read |
|---|---|
| Flash the pendant | [`firmware/readme.md`](firmware/readme.md) |
| Run the backend | [`backend/README.md`](backend/README.md) |
| Build the app | [`app/README.md`](app/README.md) |
| Build the enclosure | [`hardware/README.md`](hardware/README.md) |

## Stack

- **Hardware:** XIAO ESP32-S3 Sense, OV2640 camera, PDM microphone
- **Firmware:** ESP32 firmware in `firmware/`
- **Backend:** FastAPI with AI, memory, and retrieval components
- **App:** Flutter Android companion
- **Connectivity:** Wi-Fi and Bluetooth Low Energy

## Development

Read [`AGENTS.md`](AGENTS.md) before making repository-wide changes.

Use [`REPO_MAP.md`](REPO_MAP.md) to find the canonical owner for a part of the repository.

For agent workflow and verification, see [`docs/agentic-sdlc.md`](docs/agentic-sdlc.md).

## License

MIT. See [`LICENSE`](LICENSE).

---
<sub>Built in Pune, India.</sub>
