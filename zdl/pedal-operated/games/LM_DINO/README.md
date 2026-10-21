# LM_DINO — DINO RUN 1.00

[Русский](README.ru.md) · [Zoom ZDL FX library](https://github.com/Leemuzhko/Zoom-ZDL-FX)

A dinosaur runner inspired by the Chrome dinosaur game, running on your Zoom
pedal. Jump over cacti, survive the increasing speed and beat your preset's
high score — with one footswitch.

<img src="LM_DINO-screen.png" alt="DINO RUN title screen" width="384" height="256">

## Compatibility

| Pedal | Installed firmware | Status |
| --- | --- | --- |
| **Original MS-70CDR** | MS-70CDR | **Tested and working.** |
| **MS-50G / MS-60B** | **MS-70CDR firmware** | **Works.** |
| **MS-50G / MS-60B** | Native MS-50G / MS-60B firmware | **Does not work.** |
| **G1on / B1on family** | Native firmware | **Does not work.** The author reports no harm to the pedal. |

This version requires **MS-70CDR firmware**. Compatibility information reflects
the author's hardware report, updated **2026-10-21**. The build uses
the original MS-70CDR **SYSTEM 2.10** profile.

## Installation

1. Extract **LM_DINO.zip** into the custom-effects folder used by Zoom Effect Manager.
2. Keep `LM_DINO.ZDL`, `LM_DINO.json`, `LM_DINO.png` and the accompanying files together
   in the **LM_DINO** folder.
3. Enable **Read effects from folder** in Zoom Effect Manager, select the parent
   custom-effects folder and restart the Manager after changing its files.
4. Install **DINO RUN** from the **PedalOperated (11 / 0x0B)** category.
5. Add the game to a preset and open its main screen.

[Library installation guide](https://github.com/Leemuzhko/Zoom-ZDL-FX#installation)

## How to play

| Control | Action |
| --- | --- |
| Short footswitch press on the title screen | Start a round |
| Short footswitch press while running | Jump |
| Short footswitch press after a collision | Start another round |
| Sound in EDIT | Switch game sounds Off/On; On by default |
| Leave the game screen | Pause; return to resume |

Holding the footswitch retains the pedal's normal tuner/tap-tempo function.
The game uses short presses. Gameplay presses do not change the preset's saved
effect On/Off state or request a preset save for each jump.

The run speeds up as the score increases. Three cactus shapes vary the jump
timing. The score and high score display up to **99999**.

Stereo input passes through the effect; optional game sounds are mixed into it.
Game sounds stop while the game screen is hidden.

## Sound and high score

**Sound is saved with the preset.** The high score belongs to the current preset
and effect slot. Only an improved record is updated at the end of a round;
it is saved through the pedal's normal **Auto Save or manual Save** operation.
With Auto Save disabled, save the preset manually to retain a new record or
a changed Sound setting.

Leaving the game screen pauses the current round. Reloading the preset starts
a fresh round and restores the saved Sound setting and high score.

## Screen and package identity

The title **DINO RUN** uses the bold system font. The sound icon remains visible
during play. Graphics account for the LCD's non-square pixels: **3:4 width to
height**. The preview above preserves that physical pixel ratio.

| Field | Value |
| --- | --- |
| File | `LM_DINO.ZDL` |
| Display name | `DINO RUN` |
| Version | `1.00` |
| Effect ID | `0x33FF` (13311) |
| ZDL / ZEM category | `PedalOperated`, GID `0x0B` (11) |

SHA-256 of `LM_DINO.ZDL`:

```text
efefa3ae18b0bbb1ca9958d3bc1beaa990c2db9127f88051e7c44efebc5cc7b9
```

Inspired by the Chrome dinosaur game. This independent project is not affiliated
with Google or Zoom Corporation.
