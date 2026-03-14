# Other Brands — Bridge's Side Project

*Cross-brand compatibility matrix, conversion workflows, and competitive intelligence.*
*Bridge doesn't pick sides — she finds the connection.*

---

## Table of Contents
1. [The Cross-Brand Philosophy](#1-the-cross-brand-philosophy)
2. [Roland MV-1 Verselab](#2-roland-mv-1-verselab)
3. [Roland SP-404 Mk II](#3-roland-sp-404-mk-ii)
4. [Native Instruments Maschine (+ MK3)](#4-native-instruments-maschine--mk3)
5. [Elektron Digitakt](#5-elektron-digitakt)
6. [Pioneer Toraiz SP-16](#6-pioneer-toraiz-sp-16)
7. [Compatibility Matrix](#7-compatibility-matrix)
8. [Conversion Workflows](#8-conversion-workflows)
9. [What Competitors Do Better (Steal These Ideas)](#9-what-competitors-do-better-steal-these-ideas)
10. [Bridge's Maxims](#10-bridges-maxims)

---

## 1. The Cross-Brand Philosophy

Bridge studies competitors not to dismiss them but to steal their best ideas and build compatibility bridges. Every sampler ecosystem has solved different problems. Understanding all of them makes the MPC stronger.

**Three questions Bridge asks about any competitor:**
1. What workflow problem does this device solve that MPC doesn't solve as well?
2. Can users import MPC content here? Can they import this content into MPC?
3. What does the community do across both ecosystems?

**The oval pegs principle:** When adapting ideas from other platforms, find the natural fit. Don't force round-peg square-hole compatibility. Sometimes the best answer is "that workflow exists natively in MPC as X — use that instead."

---

## 2. Roland MV-1 Verselab

**Category:** All-in-one groove production workstation with vocal recording

**Target user:** Singer-songwriters, hip-hop producers who work vocally first

**What makes it different from MPC:**
- Built-in microphone + vocal processing (pitch correction, harmonizer)
- "Zenbeats" integration — cloud project sync
- Scene-based composition workflow (less linear than MPC's sequence model)
- Chord memory and melody assist for non-traditional musicians
- Battery-powered, very portable (smaller than MPC One)

**Sample format:**
- WAV files, 44.1kHz or 48kHz
- Standard stereo file support
- No proprietary sample container format (unlike MPC's XPN)

**MPC → MV-1 compatibility:**
- Export MPC samples as individual WAV files
- MV-1 will load them directly — no conversion needed
- MPC sequence data: no direct import (different file formats)
- Workaround: export MPC loops as audio, import audio into MV-1

**MV-1 → MPC compatibility:**
- MV-1 audio exports as WAV — directly importable to MPC
- Vocal recordings, loops, one-shots: full compatibility
- MV-1 project files: no direct import

**What MPC should steal from MV-1:**
- Integrated vocal chain (pitch correction as a first-class feature)
- Guided chord/melody assist for non-musicians

---

## 3. Roland SP-404 Mk II

**Category:** Performance-focused sampler with legendary lo-fi character

**Target user:** Crate diggers, beat-tape producers, live performers, boom bap

**What makes it different from MPC:**
- SP-404 sound character: specific compression, saturation, vinyl feel
- "Looper" mode — realtime performance recording
- BPM sync triggers — pads can be set to stutter and gate rhythmically
- Very fast "sample and chop" workflow
- No screen keyboard entry — pad-centric workflow only
- The community around it is almost a subculture

**Sample format:**
- WAV files (the SP stores samples as standard WAV)
- 12 pattern banks, 12 pads each = 144 sample slots
- Sample assignment is per-pad, no velocity layers (single sample per pad)

**MPC → SP-404 compatibility:**
- Individual WAV samples: direct compatibility
- Copy MPC's Samples folder to SD card in SP-404 format structure
- Multi-velocity layers from MPC: SP-404 can only use ONE layer — export the "medium velocity" layer
- XPN packs: not compatible (SP-404 has no expansion concept)

**SP-404 → MPC compatibility:**
- SP-404 samples are plain WAVs — directly loadable in MPC
- The community has many free sample packs distributed as SP-404-style WAV folders
- Load into MPC: organize by instrument (kick/snare/hat), build drum kit manually
- SP-404's "scene" organization doesn't translate — rebuild drum layout using GM mapping

**SP-404 MK II pattern files:**
- `.spf` format — proprietary, not directly openable in MPC
- Community tool: **SP-404 Toolkit** (unofficial) can export patterns as MIDI
- MIDI export → import into MPC as MIDI track → works for rhythmic patterns

**What MPC should steal from SP-404:**
- BPM-synced stutter/gate effects as a first-class performance FX
- The fast "chop this loop immediately" workflow (SP-404's speed here is unmatched)
- The vinyl sim character in its effect chain

---

## 4. Native Instruments Maschine (+ MK3)

**Category:** The closest true competitor to MPC — sample/synthesis production system

**Target user:** Electronic music producers, sound designers, DAW-integrated beatmakers

**What makes it different from MPC:**
- Deep Komplete integration (Maschine is part of the NI ecosystem)
- **Maschine + is purely software** — the hardware is just a controller
- Pattern/Scene/Song arrangement workflow is strong
- VST plugin hosting on the computer side is unlimited
- Stem separation built-in (newer versions)

**Sample format:**
- **Maschine Groups (.nmsv/.nkg)**: Proprietary format, not openable in MPC
- Raw samples: standard WAV — the underlying audio is always accessible
- Maschine library: `.ncw` compressed format for NI content (needs NI to decompress)

**MPC → Maschine compatibility:**
- WAV samples: direct load into Maschine groups
- XPN packs: no direct compatibility — extract WAVs, rebuild manually in Maschine
- MIDI patterns: export as Standard MIDI File from MPC → import into Maschine

**Maschine → MPC compatibility:**
- Identify raw WAV samples (in `Maschine/Samples/` folder)
- Copy WAVs to MPC storage
- Rebuild drum kits manually using MPC's drum program
- Groups/patterns: no direct import
- Community tool: **MPC-Transfer** (unofficial, fragile) — attempts group conversion

**Maschine Expansion Packs:**
Maschine has a well-developed expansion pack ecosystem. Structure:
```
Expansion/
  Groups/    (Maschine group files)
  Samples/   (raw WAVs)
  Patches/   (synth patches)
```
The `Samples/` folder is always accessible and compatible with MPC. Ignore Groups and Patches.

**Maschine MK3 as MPC controller (bridge mode):**
- Maschine MK3 sends HID/MIDI data
- Not natively recognized by MPC as a controller surface
- Workaround: use MIDI over USB host, map buttons manually to MPC MIDI CCs
- Functional but not elegant — no visual feedback integration

**What MPC should steal from Maschine:**
- Maschine's **auto-chop** algorithm is faster and smarter than MPC's
- Pattern variation system (lock scenes, switch variations mid-performance)
- The quality of NI's sound library — the depth and playability of Komplete content

---

## 5. Elektron Digitakt

**Category:** Digital drum machine + sampler with Elektron sequencer paradigm

**Target user:** Electronic producers who love generative/probability sequencing

**What makes it different from MPC:**
- Elektron's **probability system**: every step can have % chance of firing
- **Parameter locks**: every step can have different parameter values (pitch, volume, filter)
- Trig conditions: complex pattern logic (only play if last step fired, etc.)
- 8 audio tracks + 8 MIDI tracks
- Decidedly non-MPC workflow — step sequencer first, sample player second

**Sample format:**
- WAV files, 16-bit/48kHz specifically (important!)
- Stored on Compact Flash or internal flash memory
- No concept of "expansion packs" — just raw sample libraries

**MPC → Digitakt compatibility:**
- Convert MPC samples to 16-bit/48kHz WAV
- Transfer via Elektron Transfer app (macOS/Windows utility)
- MPC drum kit → Digitakt: 8 tracks max (Digitakt is 8 voices)
- Multi-velocity layers: Digitakt doesn't support them — pick one layer

**Digitakt → MPC compatibility:**
- Digitakt samples (WAVs): direct compatibility
- MIDI patterns: Digitakt can send MIDI out — record MPC MIDI input from Digitakt in real-time
- No project file compatibility

**What Elektron does exceptionally:**
- Step-locked parameters (every single step has its own parameter state) — MPC's automation is per-bar, not per-step
- Probability sequencing (firing chance per step) — MPC has nothing equivalent
- Trig conditions (only fire if 3 steps have fired, etc.) — very powerful for variation

**What MPC should steal from Digitakt:**
- Per-step parameter locks in MPC's sequencer
- Probability gates on MPC step sequences (would revolutionize drum programming)

---

## 6. Pioneer Toraiz SP-16

**Category:** Performance-focused sampler with Pioneer DJ ecosystem integration

**Target user:** DJs who produce, DJ/producer crossover, electronic live sets

**What makes it different from MPC:**
- Pioneer DJ ecosystem integration (DJPU Rekordbox sync, Pioneer CDJ bridge)
- 16 pads (vs MPC's 16 with different layout philosophy)
- Strong beatmatch/sync to DJ gear
- Dave Smith (Prophet-6) filter built into analog signal path
- More "DJ tool" than "production tool"

**Sample format:**
- Standard WAV/AIFF files
- Rekordbox track library integration
- No proprietary expansion format

**MPC → Toraiz SP-16:**
- WAV samples: compatible
- No direct project translation
- Good for: moving finished samples/loops into DJ-facing workflow

**Toraiz → MPC:**
- WAV exports: compatible
- The Rekordbox library: no direct integration with MPC
- Community use case: export Rekordbox-analyzed samples (BPM-tagged) → import into MPC

**What MPC should steal from Toraiz:**
- Tighter CDJ/DJ gear sync protocol
- The analog filter in the signal path (not a plugin, not digital — hardware diff-amp)

---

## 7. Compatibility Matrix

| Content Type | SP-404 | Maschine | Digitakt | Toraiz SP-16 | MV-1 |
|-------------|--------|---------|---------|-------------|------|
| WAV samples | ✅ Full | ✅ Full | ✅ (16-bit/48kHz) | ✅ Full | ✅ Full |
| MIDI patterns | ❌ None | ✅ SMF export/import | ✅ MIDI out (realtime) | ❌ None | ❌ None |
| Drum kits (project) | ❌ None | ❌ Format mismatch | ❌ Format mismatch | ❌ None | ❌ None |
| Expansion packs | ❌ None | ❌ Maschine-specific | ❌ N/A | ❌ N/A | ❌ N/A |
| Audio loops | ✅ Full | ✅ Full | ✅ (convert) | ✅ Full | ✅ Full |

**Always works:** Raw WAV audio files. Every sampler ecosystem reads standard WAV.

**Never works directly:** Project files, expansion packs, patch data. Always extract the raw audio.

---

## 8. Conversion Workflows

### Maschine → MPC (Complete Kit)

1. Open Maschine on computer, locate Group
2. Find Group's sample folder: `~/Documents/Native Instruments/Maschine/Samples/`
3. Copy all WAV files to MPC-formatted USB drive: `Samples/GroupName/`
4. On MPC: File Browser → navigate to samples → auto-build drum program
5. Manually recreate velocity layers if the Maschine group had them
6. Build the XPN if you want to redistribute

### SP-404 → MPC

1. Remove SP-404's SD card, mount on computer
2. Navigate to SD card structure → find `.WAV` files
3. Organize by folder (SP-404 stores in numbered banks — A001, A002...)
4. Rename files meaningfully (SP-404 uses numerical naming)
5. Copy to MPC storage
6. Build drum program in MPC using the samples

### General WAV Pack → MPC Expansion

1. Organize: create `Kicks/`, `Snares/`, `Hats/`, `Percs/` subfolder structure
2. Identify velocity layers by keyword (soft, med, hard) or auditioning
3. Run `xpn_drum_export.py` to generate XPM
4. Run `xpn_bundle_builder.py` to create `.xpn` file
5. Test on hardware

### Digitakt → MPC

1. Use Elektron Transfer app to export samples from Digitakt
2. Note: Digitakt stores 48kHz/16-bit — optionally resample to 44.1kHz for consistency
3. Import into MPC via standard file browser
4. Rekindling Digitakt patterns: use MIDI — Digitakt MIDI out → MPC MIDI in → record live

---

## 9. What Competitors Do Better (Steal These Ideas)

| Competitor | What They Do Better | Why It Matters |
|-----------|---------------------|----------------|
| **Maschine** | Auto-chop speed and quality | Faster sample preparation saves hours |
| **Digitakt** | Per-step parameter locks | Variation without automation lanes |
| **Digitakt** | Probability sequencing | Human feel without human imperfection |
| **SP-404** | BPM-sync stutter/gate as performance FX | Live energy unavailable in MPC |
| **Toraiz SP-16** | Analog filter in hardware signal path | Sound character that software can't replicate |
| **MV-1** | Integrated vocal processing workflow | Barrier removal for singing producers |
| **Maschine** | Komplete plugin depth and quality | Best synths in the world in one box |

---

## 10. Bridge's Maxims

```
1. The handshake must work both ways — a connection is only as good as its weakest end
2. Always test sync drift over 4+ minutes, not just the first bar
3. Document MIDI channel assignments — they're the first thing to forget
4. NI on Key 61 is real — but it's Key 61 only in standalone, not other hardware
5. Ableton Live Control Mode is NOT available on MPC Key 61 (the only exception)
6. Raw WAVs always cross the border — proprietary project files never do
7. Don't force Maschine workflow onto MPC — find the MPC equivalent instead
8. Study competitors to steal, not to dismiss — every device solved something
```

<!-- bible extended 2026-03 — initial build, cross-brand matrix through 2025 hardware -->
