# SYNTHESIS SYNx2 — Windows MIDI controller

[Русский](README.ru.md) · [SYNTHESIS effect](../README.md)

The controller turns MIDI notes and Note On/Off into Zoom Note/Gate parameter
commands for the original MS-70CDR, SYNX2 ID915 or SYN10A ID914, slots 1–3.
Audio comes from the pedal, not the PC. Other pedal models are unverified.

**[Download Windows installer 0.1.2](https://github.com/Leemuzhko/Zoom-ZDL-FX/releases/latest/download/SYNTHESIS-SYNx2-0.1.2-Windows-x64-Setup.exe)**
or use the [included installer](windows/SYNTHESIS-SYNx2-0.1.2-Windows-x64-Setup.exe).
The release link becomes available after this PR is merged and a new release is
published. Existing releases do not yet contain this application.

- Python/Tk and MIDI runtime are included. Windows x64 installer is unsigned.
- Vintage panel, all eight controls, 49 piano keys, octave shifts, optional PC
  keyboard and last-note Latch; Small/Medium/Large sizes and custom icon.
- [English/Russian installation and DAW guide](windows/windows-guide.html).
- [Build receipt / SHA-256](windows/windows-build-receipt.json).

For DAW input, separately install [LoopBe1](https://nerds.de/en/download.html),
select **LoopBe Internal MIDI** as the DAW output and controller input, and
select Zoom as the controller output/reply. Physical MIDI inputs and the PC/
screen keyboard do not require LoopBe1. Avoid MIDI Thru feedback loops.

LoopBe1 is not bundled. Personal non-commercial use and bundling permission are
different terms; see [vendor licensing](https://nerds.de/en/loopbe1.html).
Permission to include the driver has not been granted.

The installer is copied byte-for-byte from validated controller version 0.1.2.
Host tests, frozen/installed application smoke, install/uninstall and explicit
desktop icon assignment passed on Windows 10 x64. This is not a full DAW-to-pedal
audio test. Windows 11, native ARM64 and macOS packages remain unverified.

The repository's MIT license covers the project material; bundled third-party
runtime components retain their own licenses under `_internal/licenses` after
installation. LoopBe1 is a separately licensed external dependency.
