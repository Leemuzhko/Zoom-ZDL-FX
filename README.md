<p align="center">
  <h1 align="center">Zoom ZDL FX</h1>
</p>

<p align="center"><strong>Ready-to-use custom effects for the original Zoom MS-series ZDL platform.</strong><br>
Amp models, cabinet effects and IR-based experiments collected in one place.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-ZDL-475569?style=flat-square" alt="Format: ZDL">
  <img src="https://img.shields.io/badge/Platform-Zoom_MS--series-2563eb?style=flat-square" alt="Platform: Zoom MS-series">
  <img src="https://img.shields.io/badge/Status-Experimental-92400e?style=flat-square" alt="Status: experimental">
  <img src="https://img.shields.io/badge/License-GPL--3.0-475569?style=flat-square" alt="License: GPL-3.0">
</p>

<p align="center"><strong>English</strong> · <a href="README.ru.md">Русский</a></p>

<p align="center"><strong>Target devices:</strong><br>
MS-50G · MS-70G · MS-60B · G1on · G1Xon · B1on<br>
<sub>Compatibility target for this repository. Individual effects may not be hardware-tested on every listed model.</sub></p>

<h3 align="center"><a href="https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest">Download all effects</a></h3>

<p align="center"><a href="#effects">Individual downloads</a> · <a href="#installation">Installation</a> · <a href="https://ko-fi.com/leemuzhko">Support on Ko-fi</a></p>

---

This repository is my collection of finished, working ZDL effects for the legacy/original Zoom MS-series ecosystem. It is intended for users who want ready-made effects without building them from source.

Development is ongoing. The target device family is **MS-50G / MS-70G / MS-60B / G1on / G1Xon / B1on**. Hardware behavior can depend on the exact pedal, firmware, effect chain and DSP load, so treat every custom ZDL as experimental and test it carefully.

## Effects

Standalone effects can be downloaded as a single `.ZDL`. Effects stored in their own directory are published as a **complete ZIP package**: keep the `.ZDL`, matching `.json`, icon/image and any other files together.

| Effect | Package | Download |
| --- | --- | --- |
| **CABSIM** | Standalone ZDL | [CABSIM.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/CABSIM.ZDL) |
| **ENGL** | Standalone ZDL | [ENGL.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL.ZDL) |
| **ENGL-2** | Standalone ZDL | [ENGL-2.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL-2.ZDL) |
| **JCM800** | Standalone ZDL | [JCM800.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/JCM800.ZDL) |
| **PLEXI** | Standalone ZDL | [PLEXI.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/PLEXI.ZDL) |
| **IRDUAL4** | Complete effect folder | [Download ZIP](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/DUAL-IR.zip) |
| **MS1960** | Complete effect folder | [Download ZIP](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/MS1960.zip) |
| **MS1960 V30 T1** | Complete effect folder | [Download ZIP](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/MS1960_V30_T1.zip) |
| **MS1960 V30 T2** | Complete effect folder | [Download ZIP](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/MS1960_V30_T2.zip) |

A tagged release also contains **Zoom-ZDL-FX-&lt;version&gt;.zip** with the complete collection.

<a id="installation"></a>

## Installation with Zoom Effect Manager

### 1. Install Zoom Effect Manager

Download the current Zoom Effect Manager here:

**[Zoom Effect Manager — Download](https://zoomeffectmanager.com/en/download/)**

### 2. Create a folder for custom effects

A convenient layout is:

```text
Zoom Effect Manager/
└─ Custom Effects/
   ├─ MS1960/
   │  ├─ MS1960.zdl
   │  ├─ MS1960.JSON
   │  └─ HYBRIDIR.png
   ├─ DUAL IR/
   │  ├─ IRDUAL4.ZDL
   │  └─ IRDUAL4.json
   └─ ...
```

For packaged effects, **extract the ZIP itself into `Custom Effects/`**. Do not move only the ZDL out of its folder; keep the JSON, image/icon and other accompanying files beside it.

Standalone ZDL files can also be placed in `Custom Effects/` or in a subfolder of your choice.

### 3. Tell Zoom Effect Manager where to look

In Zoom Effect Manager:

1. Open **Settings**.
2. Enable **Read effects from folder** for ZDL effects.
3. Add/select the parent folder you created, for example:
   `Zoom Effect Manager/Custom Effects/`
4. Restart Zoom Effect Manager after adding or changing files.

Zoom Effect Manager scans the selected directory recursively, so each effect can stay in its own subfolder.

More details: **[Reading effects from a folder](https://zoomeffectmanager.com/en/posts/reading-effects-from-folder/)**.

### 4. Write the effect to the pedal

Connect the Zoom device **before starting Zoom Effect Manager**, open the Effects section, select the effect and write it to the pedal.

See also: **[Zoom Effect Manager — Quick start](https://zoomeffectmanager.com/en/posts/quick-start/)**.

Test one custom effect at a time in an otherwise simple patch before building a larger chain. Back up your existing effects/presets before experimenting.

## IR loader note

Some IR-loader variants can exceed the available DSP budget depending on IR length and the rest of the chain. If you hear crackling or other artifacts, use a shorter configuration or a lighter routing mode where the effect provides one.

The DSP cost field used by experimental/custom effects should not be treated as a reliable CPU percentage.

## Build your own cabinet effects

If you want to prepare your own cabinet responses instead of only downloading finished effects, see **[HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR)**.

HYBRID IR can prepare conventional IRs and hybrid FIR/IIR models and package them for supported Zoom workflows.

## Releases

A repository tag matching `v*` (for example `v1.0.0`) creates:

- one ZIP for every top-level effect folder under `zdl/`;
- one complete collection ZIP: `Zoom-ZDL-FX-v1.0.0.zip`.

The workflow can also be started manually from GitHub Actions to build the same ZIPs as workflow artifacts without publishing a Release.

## Support the project

If these effects are useful to you, you can [support my work on Ko-fi](https://ko-fi.com/leemuzhko). It helps fund development, testing and documentation.

The effects remain freely available; a donation does not buy features, priority support or a release deadline.

## License

This repository is distributed under the [GNU General Public License v3.0](LICENSE).

Zoom is a trademark of Zoom Corporation. This is an independent community project and is not affiliated with or endorsed by Zoom Corporation.
