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

<h3 align="center"><a href="https://github.com/Leemuzhko/Zoom-ZDL-FX/releases">Download all effects</a></h3>

<p align="center"><a href="#effects">Individual downloads</a> · <a href="#installation">Installation</a> · <a href="https://ko-fi.com/leemuzhko">Support on Ko-fi</a></p>

---

This repository is my collection of finished, working ZDL effects for the legacy/original Zoom MS-series ecosystem. It is intended for users who want ready-made effects without building them from source.

Development is ongoing. Hardware behavior can depend on the exact pedal, firmware, effect chain and DSP load, so treat every custom ZDL as experimental and test it carefully.

## Effects

The links below download the current files directly from the `main` branch.

| Effect | Package | Download |
| --- | --- | --- |
| **CABSIM** | Standalone ZDL | [CABSIM.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/CABSIM.ZDL) |
| **ENGL** | Standalone ZDL | [ENGL.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL.ZDL) |
| **ENGL-2** | Standalone ZDL | [ENGL-2.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/ENGL-2.ZDL) |
| **JCM800** | Standalone ZDL | [JCM800.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/JCM800.ZDL) |
| **PLEXI** | Standalone ZDL | [PLEXI.ZDL](https://raw.githubusercontent.com/Leemuzhko/Zoom-ZDL-FX/main/zdl/PLEXI.ZDL) |
| **IRDUAL4** | ZDL + metadata | [Open folder](zdl/DUAL%20IR/) |
| **MS1960** | ZDL + metadata | [Open folder](zdl/MS1960/) |
| **MS1960 V30 T1** | ZDL + metadata | [Open folder](zdl/MS1960_V30_T1/) |
| **MS1960 V30 T2** | ZDL + metadata | [Open folder](zdl/MS1960_V30_T2/) |

For new tagged releases, GitHub Actions packages the full `zdl/` directory into a single ZIP and attaches it to the GitHub Release.

<a id="installation"></a>

## Installation

1. Download the effect you want, or download the complete ZIP from [Releases](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases).
2. Transfer the ZDL to your pedal with [Zoom Effect Manager](https://zoomeffectmanager.com/en/download/).
3. Test one custom effect at a time in an otherwise simple patch before building a larger chain.
4. If you hear crackling, glitches or the pedal becomes unstable, reduce the DSP load and remove the last effect you added.

Back up your existing effects/presets before experimenting with custom ZDL files.

## IR loader note

Some IR-loader variants can exceed the available DSP budget depending on IR length and the rest of the chain. If you hear crackling or other artifacts, use a shorter configuration or a lighter routing mode where the effect provides one.

The DSP cost field used by experimental/custom effects should not be treated as a reliable CPU percentage.

## Build your own cabinet effects

If you want to prepare your own cabinet responses instead of only downloading finished effects, see **[HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR)**.

HYBRID IR can prepare conventional IRs and hybrid FIR/IIR models and package them for supported Zoom workflows.

## Releases and the download ZIP

A repository tag matching `v*` (for example `v1.0.0`) triggers the release workflow. It creates:

```text
Zoom-ZDL-FX-v1.0.0.zip
```

containing the distributable `zdl/` collection plus the README and license.

The workflow can also be started manually from GitHub Actions to build a test ZIP without publishing a release.

## Support the project

If these effects are useful to you, you can [support my work on Ko-fi](https://ko-fi.com/leemuzhko). It helps fund development, testing and documentation.

The effects remain freely available; a donation does not buy features, priority support or a release deadline.

## License

This repository is distributed under the [GNU General Public License v3.0](LICENSE).

Zoom is a trademark of Zoom Corporation. This is an independent community project and is not affiliated with or endorsed by Zoom Corporation.
