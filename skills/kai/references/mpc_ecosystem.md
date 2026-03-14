# MPC Ecosystem — Sage's Domain

*Hardware specs, firmware history, AIR/NI plugins, CPU optimization.*
*Sage never promises what the hardware can't deliver.*

---

## Table of Contents
1. [MPC Hardware Matrix 2025](#1-mpc-hardware-matrix-2025)
2. [MPC Live III Deep Dive](#2-mpc-live-iii-deep-dive)
3. [MPC Key Series](#3-mpc-key-series)
4. [Legacy Hardware Still in Use](#4-legacy-hardware-still-in-use)
5. [MPC Force: Distinct Paradigm](#5-mpc-force-distinct-paradigm)
6. [OS Version History](#6-os-version-history)
7. [AIR Instrument Collection](#7-air-instrument-collection)
8. [Native Instruments on MPC](#8-native-instruments-on-mpc)
9. [CPU Optimization Strategies](#9-cpu-optimization-strategies)
10. [Storage and File System](#10-storage-and-file-system)
11. [MIDI Implementation](#11-midi-implementation)
12. [Sage's Warnings (Common Mistakes)](#12-sages-warnings-common-mistakes)

---

## 1. MPC Hardware Matrix 2025

| Model | CPU | RAM | Storage | Pads | I/O | Key Feature | Best For |
|-------|-----|-----|---------|------|-----|------------|----------|
| **Live III** | 8-core ARM | 8GB | 128GB | 16 (MPCe 3D) | Full | Flagship, Oct 2025 | Everything |
| **Key 61** | 4-core ARM | 4GB | 16GB | 16 | Stereo I/O | 61 keys + aftertouch, NI native | Keyboard players |
| **Key 37** | 4-core ARM | 4GB | 16GB | 16 | Stereo I/O | 37 keys, compact | Desktop performance |
| **Live II** | 4-core ARM | 2GB | 16GB | 16 | Full | Previous flagship | Budget flagship |
| **One Plus** | 4-core ARM | 4GB | 32GB | 16 | Multi-out | Desktop-focused | Studio production |
| **Force** | 4-core ARM | 4GB | 32GB | 64 (8×8) | Full | Clip-launching | Ableton-style live |

**I/O "Full" = :** Stereo in/out, 8 individual outs, 2 inputs (combo XLR/TRS), MIDI DIN in/out, USB host+device, CV/Gate (Live series)

---

## 2. MPC Live III Deep Dive

Released October 2025. The most capable standalone sampler ever shipped.

**CPU: 8-core ARM (exact chip not publicly disclosed)**
- Measured plugin headroom: ~32 simultaneous plugin tracks (vs 8 on Live II)
- Polyphony increase: 128+ voices for built-in engines
- Parallel plugin processing finally usable for dense arrangements

**MPCe 3D Pads**
- Pressure-sensitive in 3 dimensions: velocity (Z), X-position, Y-position
- Each dimension is MIDI-mappable
- Enables performance gestures not possible on flat velocity pads
- Software support: MPC OS 3.7+ (included with Live III)
- X/Y can control filter, pitch, any assignable parameter
- Think of it as 3D aftertouch built into every pad

**8GB RAM Impact**
- Full library can be pre-loaded into RAM — no disk streaming stutter
- Allows all 32 plugin tracks to load simultaneously without swapping
- Complex sample libraries (multi-GB orchestral) finally viable standalone

**128GB Internal Storage**
- First MPC where you can store a real sample library internally
- SD card still supported (exFAT recommended)
- USB drives still fastest for bulk transfer

**Comparison to Live II:**
- Live II maxes out at ~8 plugin tracks before audio drop-outs
- Live III handles complex multi-engine scenes Live II couldn't run
- MPCe pads are hardware incompatibility — can't add to Live II retrofit

---

## 3. MPC Key Series

### Key 61
**The keyboard player's MPC**

- 61-key semi-weighted keyboard with **aftertouch** (channel pressure)
- 4GB RAM, good for 12-16 simultaneous plugins comfortably
- **NI Komplete native integration** — key differentiator vs other MPC models
  - Kontakt, Massive X, Battery 4, etc. run natively in standalone
  - NI plugin scanning built into OS — no extra steps
  - This is Key 61 ONLY — no other MPC supports NI natively in standalone
- **Ableton Live Control Mode NOT available** (the only MPC model without it)
- CV/Gate outputs for modular integration
- No MPCe pads (standard velocity-only pads on Key series)

### Key 37
- Compact 37-key version of Key 61 architecture
- Same CPU/RAM as Key 61
- Good travel companion for Key 61 users
- NI integration: Yes (same as Key 61)
- Ableton Live Control Mode: NOT available (same exception as Key 61)

---

## 4. Legacy Hardware Still in Use

**MPC Live II** (2021, still widely used)
- 4-core ARM, 2GB RAM, 16GB storage
- Plugin limit: ~8 tracks safely before CPU strain
- Buffer size matters more here — 256 or 512 recommended
- Maximum 4 AIR instruments simultaneously in complex scenes

**MPC One / One Plus** (2020/2022)
- Desktop-only (no battery), but often cleaner performance at desk
- One Plus: 4GB RAM, better polyphony headroom
- Popular for "set it up at desk and leave it" producers

**MPC X** (2017, still in service)
- First touchscreen MPC — some producers swear by the big screen
- CPU is oldest in current fleet — hardest to run complex scenes
- 4GB RAM but older architecture means fewer simultaneous plugins

---

## 5. MPC Force: Distinct Paradigm

The Force shares MPC OS code but is **conceptually different**:

**What the Force is:**
- 8×8 pad grid (64 pads vs 16)
- Clip-launching workflow (like Ableton Live's Session View)
- Scenes and Clips are the primary organizational units
- Designed for live looping and arrangement

**What's different from MPC:**
- Pad mapping is scene-based, not program-based
- MIDI track behavior differs from MPC's sequence paradigm
- "Song mode" equivalent works differently
- Some MPC preset types load but don't behave identically

**Cross-content compatibility:**
- XPN packs import fine
- Drum programs load and work (pads just assigned to grid)
- Keygroup programs work
- MIDI patterns from MPC: compatible with caveats
- Don't assume workflow parity — Force users think in clips, not sequences

**Sage's Force rule:** When designing content for Force users, think 8×8 pad grid, not 4×4. A drum kit designed for 4×4 feels cramped on Force.

---

## 6. OS Version History

| Version | Key Changes | Hardware |
|---------|------------|----------|
| **3.7** (2025) | MPCe 3D pad support, 8-core optimization, improved plugin scanning | Live III required for MPCe; all hardware for core features |
| **3.6** (2024) | MIDI over Bluetooth, improved Ableton Live Control Mode, CV/Gate improvements | All current hardware |
| **3.5** (2023) | NI integration (Key 61/37 only), new AIR instruments, stem separation | Stems: Live II+ (RAM-dependent) |
| **3.x** (2021–23) | Plugin tracks, improved audio interface mode, MPC One Plus | Progressive improvements |
| **2.x** (2018–21) | Touch screen workflow established, AIR Instrument Collection introduced | MPC X, Live I, One |
| **1.x** (2016–18) | Original software-only instruments, basic program types | MPC Touch, early MPC Live |

**Important 2.x → 3.x behavioral changes:**
- Plugin programs replaced custom sampler programs for many instruments
- Sequence/Track paradigm refined
- File browser improved significantly
- Program type "Plugin" became first-class citizen

**Firmware gotcha:** Features listed in release notes may only be available on hardware released at the same time. Always check hardware compatibility matrix in the release notes.

---

## 7. AIR Instrument Collection

AIR Music Technology makes all built-in MPC instruments. These run natively on every MPC — no latency, CPU-optimized for ARM.

### Fabric XL (Flagship Synth)
- **Type:** Hybrid synthesis (sample + synthesis)
- **Core:** 8-layer instrument with 4 oscillators per layer
- **Synthesis modes:** Sample playback, VA, wavetable, granular
- **Modulation:** 2 filters, 3 envelopes, 4 LFOs, 8-slot mod matrix
- **Presets:** 600+ factory presets
- **Best for:** Complex pads, leads, anything that needs depth
- **CPU cost:** High — limit to 4-6 simultaneously on Live II

### OPx-4 FM Synth
- **Type:** FM synthesis (4-operator)
- **Core:** Classic 4-op FM with 8 algorithms
- **Character:** Clean digital, plucks, bells, electric pianos, classic FM basses
- **Presets:** 200+ presets
- **CPU cost:** Low — very efficient FM implementation
- **Connection to history:** Inspired by Yamaha DX21/DX7 architecture

### Stage Electric Piano
- **Type:** Sample-based electric piano
- **Engines:** Rhodes Suitcase (3 weight variants), Wurlitzer, CP80
- **Key-switching:** Velocity crossfade between amp settings
- **Best for:** Lush keys, jazz, neo-soul, lofi
- **CPU cost:** Medium

### Stage Piano (Acoustic)
- **Type:** Sample-based acoustic piano
- **Engines:** Upright, Grand (Yamaha-inspired), prepared piano
- **Best for:** Acoustic compositions, intros, ballads
- **CPU cost:** Medium-high (large samples)

### Organ
- **Type:** Tonewheel simulation
- **Engines:** Hammond-style (with drawbars), Farfisa, Vox Continental
- **Drawbars:** All 9 drawbars assignable to pad controls
- **Best for:** Church/gospel chords, rock organ, classic soul
- **CPU cost:** Low

### Studio Strings
- **Type:** Multi-sampled orchestral strings
- **Sections:** Violins, Violas, Celli, Basses (individual + ensemble)
- **Articulations:** Legato, staccato, pizzicato, tremolo
- **Best for:** Film scoring, background pads, cinematic arrangements
- **CPU cost:** High — largest RAM footprint of AIR instruments

### Additional AIR instruments (MPC OS 3.5+)
- **Hybrid 3:** Classic hybrid synth (sample + subtractive)
- **Linn Drum (MPC):** Samples from original LinnDrum hardware (licensed)
- **The Riser:** Performance FX instrument (drop/rise creator)

**CPU costs summary:**
| Instrument | CPU Weight | Max simultaneous (Live II) |
|-----------|-----------|---------------------------|
| Fabric XL | High | 4-6 |
| OPx-4 | Low | 15+ |
| Stage EP | Medium | 8-10 |
| Stage Piano | Medium-High | 5-6 |
| Organ | Low | 12+ |
| Studio Strings | High | 3-4 |

---

## 8. Native Instruments on MPC

**Exclusive to MPC Key 61 and Key 37 — standalone mode only**

Supported NI instruments (Key 61/37 standalone):
- Kontakt 7 (full, including custom NKI libraries)
- Battery 4 (drum sampling)
- Massive X (wavetable synth)
- Form (sample-based synth)
- Monark (Mini Moog model)
- Rounds (sample sequencer)
- Session Strings / Session Horns (ROMpler series)

**Important caveats:**
- NI plugins work in standalone on Key 61/37 only
- On other MPC hardware (Live II, One, etc.) NI plugins only available in DAW/controller mode
- NI library scanning can be slow on first load — allow 5-10 minutes
- Custom Kontakt libraries: must be installed on internal or external drive, MPC-formatted
- Not all NI instruments are available — AIR handles the official supported list

**NI + MPC workflow:**
- NI instruments behave as Plugin programs in MPC
- Pad/key mapping works through NI's internal mapping, not MPC's PadNoteMap
- Save states as MPC projects, not NI snapshots — more portable

---

## 9. CPU Optimization Strategies

**Buffer size:** The most important single setting for CPU headroom.
- 64 samples: Lowest latency, highest CPU load — live performance only if needed
- 128 samples: Good for live play with moderate plugin count
- 256 samples: Best balance for complex scenes
- 512 samples: Maximum headroom, some latency — fine for sequenced tracks

**Disk Streaming:**
- Quality = High: sounds best, uses more RAM (pre-loads more)
- Quality = Low: saves RAM, disk reads more aggressively
- On Live III (8GB RAM): always set High
- On Live II (2GB RAM): set to Medium or Low for large sample libraries

**Plugin count per model:**
| Hardware | Safe plugin limit | Push limit (with buffer 512) |
|---------|-------------------|------------------------------|
| Live III | 32 | 40+ |
| Live II | 8 | 12 |
| One Plus | 10-12 | 16 |
| Key 61 | 12 | 18 |
| One | 6-8 | 10 |

**Polyphony management:**
- Set per-track voice limits: unnecessary for monophonic bass/leads
- 4 voices for solo leads, 8 for chords, 16 for pads
- Large sample instruments: limit polyphony first (Studio Strings: 8 max)

**Sample rate:**
- 44.1kHz: Standard, best compatibility, lowest CPU
- 48kHz: Only if exporting to video sync projects
- 96kHz: Not recommended on MPC — doubles CPU load, no perceptible benefit

---

## 10. Storage and File System

**USB drives MUST be formatted:**
- **exFAT**: Recommended — supports files >4GB, MPC-compatible
- **FAT32**: Works, but 4GB file size limit
- **APFS** (macOS default): NOT COMPATIBLE — MPC won't see the drive
- **NTFS** (Windows default): NOT COMPATIBLE without special firmware/drivers
- **HFS+** (older macOS): NOT COMPATIBLE

**SD Cards:**
- Class 10 minimum, U3/V30 recommended for streaming
- Same format rules as USB (exFAT recommended)
- Cheap SD cards cause stutters on complex projects

**Internal storage management:**
- Factory content is pre-installed and cannot be deleted via MPC UI
- User content lives in `/Volumes/MPC/Expansions/` equivalent path
- Expansion packs installed via USB transfer or MPC Software

**File transfer workflow:**
1. Format USB as exFAT on computer
2. Create folder structure: `Expansions/[PackName]/`
3. Copy XPN file into `Expansions/` folder
4. Eject safely, insert into MPC USB port
5. MPC scans on boot or via Media menu > Rescan

---

## 11. MIDI Implementation

**MIDI over USB Device** (MPC as controller):
- Standard class-compliant USB MIDI
- Works on any computer without drivers
- MPC sends on channels 1-16 per track

**MIDI DIN (5-pin):**
- In and Out on all current models
- Thru via software passthrough (not hardware thru)
- 31.25kbps standard rate

**MIDI over USB Host** (connect MIDI device to MPC):
- USB A port acts as host for USB MIDI controllers
- Class-compliant controllers only (no driver installation possible)
- Supports: keyboards, pad controllers, knob boxes, MIDI interfaces

**MIDI over Bluetooth** (MPC OS 3.6+):
- Bluetooth MIDI to/from iOS devices, Bluetooth MIDI controllers
- Latency: typically 5-15ms — acceptable for most uses, not for tight sync
- Pair via MPC Settings > MIDI > Bluetooth

**Ableton Live Control Mode:**
- Available on: MPC X, Live I, Live II, Live III, One, One Plus, Force
- NOT available on: Key 61, Key 37 (hardware architecture limitation)
- Enables MPC pads to control Ableton clips, scenes, parameters

---

## 12. Sage's Warnings (Common Mistakes)

```
1. Older MPC hardware (Live II, One) hits plugin limits fast — plan for 8 plugins max
2. Buffer size affects latency AND CPU headroom — don't set it and forget it
3. USB drives must be formatted exFAT or FAT32 — APFS and NTFS are silent failures
4. Disk streaming quality setting affects playback quality vs. RAM tradeoff
5. Force and MPC share OS code but have UX differences — never assume parity
6. NI plugins standalone = Key 61/37 ONLY — no other MPC hardware in standalone
7. Ableton Live Control Mode = NOT available on Key 61/37 — the only exception
8. Sample rate: stay at 44.1kHz — 96kHz doubles CPU for zero perceptible gain
9. Don't format SD cards or USB on macOS without changing format — APFS is default
10. MPCe 3D pads are Live III exclusive hardware — no firmware upgrade possible
```

---

*Side project: `references/mpc_mobile.md` — Sage's study of iMPC Pro 2, MPC Beats iOS, and cross-platform workflows.*

<!-- bible extended 2026-03 — initial build, hardware matrix through Live III launch -->
