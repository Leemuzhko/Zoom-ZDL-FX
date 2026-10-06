# MIDI routing options — checked 2026-10-06

[Русский](MIDI_ROUTING.ru.md)

Daniel Schmitt of nerds.de gave written permission on 2026-10-06 for the requested
free non-commercial distribution with the original, unmodified, signed LoopBe1
installer, retaining vendor licensing and attribution. General commercial-use
terms still apply. The separate branded-build pricing question was not answered.
The current controller 0.1.2 does not bundle the driver; installer integration is
not implemented by this documentation update.

Windows MIDI Services provides native loopback with existing WinMM application
compatibility. A MIDI 2.0 loopback has cross-wired A/B endpoints; a Basic Loopback
has one name like LoopBe1. Microsoft's current documentation schedules consumer
Basic Loopback availability for late November 2026, with developer availability
now. Detect capabilities on each PC rather than assuming every Windows 11 has it.
Choose user loopbacks, not the diagnostic endpoints. Names can be customized.

The controller uses the RtMidi WinMM backend, so consuming a created native port
is expected to be compatible. Endpoint creation needs MIDI Services tools/SDK;
the current DAW shortcut still searches for LoopBe1. Win11 runtime/audio routing
was not tested: the checked build host is Win10 22H2/build19045. No driver/service
was installed. Proposed future behavior is native routing when available, with
LoopBe1 fallback. This is a plan, not a released controller feature.

Official sources:

- [Windows MIDI Services overview](https://microsoft.github.io/MIDI/)
- [A/B loopbacks](https://microsoft.github.io/MIDI/kb/virtual-loopback/)
- [Basic Loopback and rollout dates](https://microsoft.github.io/MIDI/tools/midiloopbacksetup/)
- [WinMM compatibility](https://microsoft.github.io/MIDI/sdk-reference/Transports/BasicLoopback/)
- [Diagnostic endpoint restrictions](https://microsoft.github.io/MIDI/kb/diagnostic-endpoints/)
