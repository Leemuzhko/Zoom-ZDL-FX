<p align="center">
  <h1 align="center">Zoom ZDL FX</h1>
</p>

<p align="center"><strong>Ready-to-use custom effects for the original Zoom MS-series ZDL platform.</strong><br>
Amp models, cabinet effects and IR-based experiments collected in one place.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Format-ZDL-475569?style=flat-square" alt="Format: ZDL">
  <img src="https://img.shields.io/badge/Platform-Zoom_MS--series-2563eb?style=flat-square" alt="Platform: Zoom MS-series">
  <img src="https://img.shields.io/badge/Status-Experimental-92400e?style=flat-square" alt="Status: experimental">
  <img src="https://img.shields.io/badge/License-MIT-475569?style=flat-square" alt="License: MIT">
</p>

<p align="center"><strong>English</strong> · <a href="README.ru.md">Русский</a></p>

<p align="center"><strong>Target devices:</strong><br>
MS-50G · MS-70CDR · MS-60B · G1on · G1Xon · B1on<br>
<sub>Compatibility target for this repository. Individual effects may not be hardware-tested on every listed model.</sub></p>

<h3 align="center"><a href="https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest">Download all effects</a></h3>

<p align="center"><a href="#effects">Individual downloads</a> · <a href="#installation">Installation</a> · <a href="https://ko-fi.com/leemuzhko">Support on Ko-fi</a> · <a href="https://www.patreon.com/Leemuzhko">Support on Patreon</a></p>

---

This repository is my collection of finished, working ZDL effects for the legacy/original Zoom MS-series ecosystem. It is intended for users who want ready-made effects without building them from source.

Development is ongoing. The target device family is **MS-50G / MS-70G / MS-60B / G1on / G1Xon / B1on**. Hardware behavior can depend on the exact pedal, firmware, effect chain and DSP load, so treat every custom ZDL as experimental and test it carefully.

## Effects

Every effect is distributed as a **complete folder package**. Keep the `.ZDL`, matching `.json`, PNG icon/image and any accompanying files together.

Cards in the project catalogues are separate opaque-white preview copies. The original Manager
icons inside `zdl/` and the downloadable effect packages are unchanged.

<!-- BEGIN GENERATED EFFECT CATALOG -->

| Type / Group | Project | Effects | Catalog / Description |
| --- | --- | ---: | --- |
| Filter (2) | HYBRID IR | 5 | [Catalog](zdl/filter/hybrid-ir/README.md) |
| Filter (2) | DUAL IR loaders | 4 | [Catalog](zdl/filter/DUAL-IR/README.md) |
| Drive (3) | Experimental NAM captures | 2 | [Catalog](zdl/drive/nam/README.md) |
| GuitarAmp (4) | Modified Guitar Amps | 6 | [Catalog](zdl/guitar-amp/modified-amps/README.md) |
| SFX (7) | SYNTHESIS SYNx2 | 1 | [Catalog](zdl/sfx/synthesis/README.md) |

<!-- END GENERATED EFFECT CATALOG -->

A tagged release also contains **All-ZDL-FX-<version>.zip** with the complete collection.

Browse a project above for its effect cards and downloads. IR and amp projects also have
a `<project>-project.zip` release package. [Catalogue maintenance](CATALOG.md).

### SYNTHESIS SYNx2 + MIDI controller

[Effect, Windows installer and DAW instructions](zdl/sfx/synthesis/README.md).

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
   │  ├─ MS1960.ZDL
   │  ├─ MS1960.json
   │  └─ HYBRIDIR.png
   ├─ GJ_IR/
   │  ├─ GJ_IR.ZDL
   │  ├─ GJ_IR.json
   │  └─ GJ_IR.png
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

## Build your own cabinet effects

If you want to prepare your own cabinet responses instead of only downloading finished effects, see **[HYBRID IR](https://github.com/Leemuzhko/HYBRID-IR)**.

HYBRID IR can prepare conventional IRs and hybrid FIR/IIR models and package them for supported Zoom workflows.

## Releases

A repository tag matching `v*` (for example `v1.0.0`) creates:

- one ZIP for every effect package listed in `catalog.json`, keeping the existing asset names;
- project ZIPs for the IR and amp projects; SYNTHESIS has separate effect and installer downloads;
- the standalone SYNTHESIS Windows installer and DAW guide;
- one complete collection ZIP: `All-ZDL-FX-<version>.zip`.

The workflow can also be started manually from GitHub Actions to build the same ZIPs as workflow artifacts without publishing a Release.

## Support the project

If these effects are useful to you, you can support my work on [Ko-fi](https://ko-fi.com/leemuzhko) or [Patreon](https://www.patreon.com/Leemuzhko). It helps fund development, testing and documentation.

The effects remain freely available; a donation does not buy features, priority support or a release deadline.

## License

This repository is distributed under the [MIT License](LICENSE).

Zoom is a trademark of Zoom Corporation. This is an independent community project and is not affiliated with or endorsed by Zoom Corporation.
