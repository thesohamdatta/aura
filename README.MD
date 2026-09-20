<div align="center">

```text
 █████╗ ██╗   ██╗██████╗  █████╗
██╔══██╗██║   ██║██╔══██╗██╔══██╗
███████║██║   ██║██████╔╝███████║
██╔══██║██║   ██║██╔══██╗██╔══██║
██║  ██║╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
```


[![License](https://img.shields.io/badge/LICENSE-MIT-171717?style=for-the-badge&labelColor=f7c600&color=171717)](LICENSE)
[![Hardware](https://img.shields.io/badge/HARDWARE-OPEN-171717?style=for-the-badge&labelColor=f7c600&color=171717)](hardware/)
[![Backend](https://img.shields.io/badge/BACKEND-FASTAPI-171717?style=for-the-badge&labelColor=f7c600&color=171717)](backend/)
[![App](https://img.shields.io/badge/APP-ANDROID-171717?style=for-the-badge&labelColor=f7c600&color=171717)](app/)

<br/>

**Aura is an open-source AI pendant you wear around your neck.**



</div>

---

## SYSTEM OVERVIEW

| Layer | Implementation |
|---|---|
| `PENDANT` | XIAO ESP32-S3 Sense |
| `SENSORS` | Digital PDM microphone + OV2640 camera |
| `BACKEND` | FastAPI + four-layer AI pipeline |
| `APP` | Android companion app |
| `HARDWARE` | Printable, open enclosure |

<div align="center">

`AUDIO` ──► `CONTEXT` ──► `MEMORY` ──► `RECALL`

</div>

## WHAT WORKS

| Component | Open |
|---|---|
| Flash the pendant | [`firmware/`](firmware/) |
| Run the backend | [`backend/`](backend/) |
| Build the Android app | [`app/`](app/) |
| Print the case | [`hardware/CASE.stl`](hardware/CASE.stl) |

## START HERE

| You want to | Read |
|---|---|
| Flash the pendant | [`firmware/readme.md`](firmware/readme.md) |
| Run the backend | [`backend/README.md`](backend/README.md) |
| Build the Android app | [`app/README.md`](app/README.md) |
| Print the enclosure | [`hardware/README.md`](hardware/README.md) |
| Understand the product | [`website/manifesto.html`](website/manifesto.html) |

## HOW THE STACK FITS

The pendant streams audio and frames over Wi-Fi. The backend converts them into searchable memory. The app lets you ask that memory questions.

## HARDWARE

Off-the-shelf parts. Printable case. No proprietary enclosure.

| Piece | Specification |
|---|---|
| MCU | XIAO ESP32-S3 Sense |
| Microphone | Digital PDM |
| Camera | OV2640 |
| Wireless | Wi-Fi 2.4 GHz + Bluetooth Low Energy 5.0 |
| Enclosure | [`hardware/CASE.stl`](hardware/CASE.stl) |

**Estimated bill of materials:** around $50 USD.

Component details and assembly notes live in [`hardware/README.md`](hardware/README.md).

## OPEN SOURCE

Aura is MIT licensed and built by a four-person undergraduate team in Pune.

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security](SECURITY.md)
- [License](LICENSE)

---

<div align="center">

[STAR ON GITHUB](https://github.com/thesohamdatta/aura) · [REPORT A VULNERABILITY](SECURITY.md) · [MIT](LICENSE)

</div>
