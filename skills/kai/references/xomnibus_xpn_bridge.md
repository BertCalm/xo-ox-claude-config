# XOmnibus ↔ XPN Bridge — Atlas's Domain

*The architecture connecting XOmnibus presets to MPC expansion packs.*
*Atlas lives between the two worlds. She knows exactly where they fit and where they fight.*

---

## Table of Contents
1. [The Bridge Philosophy](#1-the-bridge-philosophy)
2. [XPN Tool Suite Overview](#2-xpn-tool-suite-overview)
3. [xpn_drum_export.py — XOnset Drum Programs](#3-xpn_drum_exportpy--xonset-drum-programs)
4. [xpn_bundle_builder.py — Multi-Engine Bundler](#4-xpn_bundle_builderpy--multi-engine-bundler)
5. [xpn_cover_art.py — Procedural Art Generator](#5-xpn_cover_artpy--procedural-art-generator)
6. [xpn_exporter.py — Keygroup Exporter](#6-xpn_exporterpy--keygroup-exporter)
7. [Sample-Based Kit Builder Workflows](#7-sample-based-kit-builder-workflows)
8. [Sonic DNA → MPC Pad Feel Mapping](#8-sonic-dna--mpc-pad-feel-mapping)
9. [XOmnibus Macro → MPC Knob Mapping](#9-xomnibus-macro--mpc-knob-mapping)
10. [Engine-Specific XPN Strategies](#10-engine-specific-xpn-strategies)
11. [Atlas's Ongoing Advisory Cadence](#11-atlass-ongoing-advisory-cadence)
12. [Known Gaps and Future Work](#12-known-gaps-and-future-work)

---

## 1. The Bridge Philosophy

XOmnibus is a software synthesizer ecosystem. XPN is a hardware expansion format. They are not the same thing — and pretending they are is the fastest path to bad results.

**What can translate well:**
- Drum programs from XOnset (synthesis → rendered WAV → XPN kit)
- Keygroup programs from XOdyssey/Drift (rendered multi-samples → XPN keygroup)
- Pad feel design informed by Sonic DNA (dynamics → velocity curves)
- Macro philosophy translated to MPC 4-knob assignments

**What doesn't translate:**
- Real-time synthesis (MPC expects samples, not synthesis algorithms)
- Complex 6-macro setups (MPC has 4 assignable knobs per program)
- Cross-engine coupling (XOmnibus routing doesn't exist in standalone MPC)
- Granular/spectral engines that require long render times per note

**Atlas's principle:** The XPN pack should feel like the XOmnibus engine's *soul* rendered into hardware form. The goal is the feeling, not the signal path.

---

## 2. XPN Tool Suite Overview

All tools live in `~/Documents/GitHub/XO_OX-XOmnibus/Tools/`:

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `xpn_drum_export.py` | XOnset drum program builder | Rendered WAV stems | `.xpm` drum program + XPN zip |
| `xpn_bundle_builder.py` | Multi-engine bundler | `.xometa` preset files | `.xpn` bundle with all programs |
| `xpn_cover_art.py` | Procedural cover art | Engine name | `2000×2000` + `1000×1000` PNG |
| `xpn_exporter.py` | XOdyssey keygroup exporter | Multi-sample WAV folder | `.xpm` keygroup program |

**Running tools:**
```bash
cd ~/Documents/GitHub/XO_OX-XOmnibus
python Tools/xpn_drum_export.py --help
python Tools/xpn_bundle_builder.py --help
python Tools/xpn_cover_art.py --help
```

**Dependencies:**
- `Pillow` (xpn_cover_art.py)
- `numpy` (xpn_cover_art.py)
- Standard library only for drum export and bundle builder

---

## 3. xpn_drum_export.py — XOnset Drum Programs

**Purpose:** Build MPC drum programs from XOnset rendered WAVs.

**XOnset → XPN workflow:**
1. Configure an XOnset preset in XOmnibus
2. Record/render individual drum hits as WAV stems:
   - 4 velocity layers per voice: soft, medium, hard, very hard
   - Voice layout follows GM mapping:
     - V1=Kick (A01, MIDI 36)
     - V2=Snare (A02, MIDI 38)
     - V3=Closed Hat (A03, MIDI 42)
     - V4=Open Hat (A04, MIDI 46)
     - V5=Clap (A05, MIDI 39)
     - V6=Tom (A06, MIDI 45)
     - V7=Perc (A07, MIDI 37)
     - V8=FX (A08, MIDI 49)
3. Run `xpn_drum_export.py` to generate the `.xpm` XML
4. Run `xpn_bundle_builder.py` to package into `.xpn`

**Expected file naming for the exporter:**
```
Kit_Name/
  Kick_v1.wav    (velocity layer 1: ghost/soft)
  Kick_v2.wav    (velocity layer 2: light)
  Kick_v3.wav    (velocity layer 3: medium)
  Kick_v4.wav    (velocity layer 4: hard/full)
  Snare_v1.wav
  Snare_v2.wav
  ...
```

**Checklist mode:**
```bash
python Tools/xpn_drum_export.py --checklist Kit_Name/
```
Reports which velocity layers are present, which are missing, what velocity splits will be used.

**Hat choke groups:**
- Closed hat (V3) and Open hat (V4) are automatically placed in MuteGroup=1
- All hat chokes are handled — no manual XML editing needed

**XOnset XVC coupling presets:**
These don't translate to XPN (XVC is a cross-voice synthesis coupling, not a sample-playback feature). Render the *result* of the coupling as a complex sample — the XPN pack captures the output, not the routing.

---

## 4. xpn_bundle_builder.py — Multi-Engine Bundler

**Purpose:** Create XPN bundles containing presets from multiple XOmnibus engines.

**3 modes:**

**Mode 1: Custom** — specify exactly which presets to include
```bash
python Tools/xpn_bundle_builder.py \
  --mode custom \
  --presets "Bob/Dark Pulse.xometa" "Drift/Alien Breath.xometa" \
  --output MyCustomBundle.xpn
```

**Mode 2: Category** — include all presets of a given mood/category tag
```bash
python Tools/xpn_bundle_builder.py \
  --mode category \
  --category "Cosmic" \
  --output CosmicBundle.xpn
```

**Mode 3: Predefined** — 8 curated bundle profiles
```bash
python Tools/xpn_bundle_builder.py \
  --mode predefined \
  --profile "Founder_Pack_01" \
  --output FounderPack01.xpn
```

The 8 predefined profiles:
1. `Founder_Pack_01` — Best-of across all engines
2. `Dark_Atmospheres` — Dark, tension, cinematic
3. `Cosmic_Textures` — Space, drift, ambient
4. `Urban_Beats` — Onset kits + Bob/Dub pads
5. `Live_Performance` — Dynamic, expressive, stage-ready
6. `Film_Score` — Cinematic beds and tensions
7. `Neo_Soul` — Warm, soulful, musical
8. `Experimental` — Aggressive, weird, challenging

**Engine name normalization:**
The bundler handles XOmnibus display names vs. folder names:
- XOblongBob → Bob
- XOdyssey → Drift
- XOpossum → Bite (in Presets/Bite/)
- XOverworld → Overworld
- XOdyssey standalone → Drift (adapter name)
- All others: use engine display name

**Preset indexing:**
The bundler scans both flat preset directories AND subdirectories:
```
Presets/Bob/Dark_Pulse.xometa          ← indexed
Presets/Bob/Aggressive/Saw_Storm.xometa ← also indexed
```

---

## 5. xpn_cover_art.py — Procedural Art Generator

**Purpose:** Generate visual identity art for XPN bundles.

**Output:**
- `2000×2000` px PNG: Expansion browser thumbnail
- `1000×1000` px PNG: Lower resolution version

**Per-engine visual identities:**

| Engine | Visual Style |
|--------|-------------|
| ONSET | Radial spike waveform (drum transient visual) |
| OVERWORLD | Pixel grid + scanline overlay (CRT chip aesthetic) |
| DRIFT | Lissajous figure (XOdyssey trajectory curves) |
| MORPH | Overlapping sine waves (harmonic blend) |
| BOB | Oscilloscope trace (warm analog glow) |
| DUB | Feedback spiral (dub delay feedback) |
| SNAP | Sharp waveform angles (percussive attack) |
| FAT | Low-frequency wave (heavy bass weight) |

**Usage:**
```bash
python Tools/xpn_cover_art.py --engine ONSET --name "My Kit Name" --output cover.png
```

**Customization:**
- Accent color follows engine's canonical hex code
- Text overlay: engine name + pack name + XO_OX branding
- Background: dark with subtle noise texture

---

## 6. xpn_exporter.py — Keygroup Exporter

**Primary location:** `~/Documents/GitHub/XOdyssey/tools/xpn_exporter/xpn_export.py`
*(Originally built for XOdyssey, reusable for any multi-sampled engine)*

**Purpose:** Take a folder of multi-sampled WAV files and generate a complete keygroup XPN.

**Sample strategy:**
- Multi-sample every minor 3rd: C1, Eb1, F#1, A1, C2, Eb2, F#2, A2, C3, Eb3, F#3, A3, C4, Eb4, F#4, A4, C5, Eb5, F#5, A5, C6
- 21 sample points across 5 octaves
- Each sample covers ±1.5 semitone range

**Naming convention:**
```
PRESET_NAME__C2__v1.WAV    (double underscore separators)
PRESET_NAME__C2__v2.WAV
PRESET_NAME__D#2__v1.WAV   (use # for sharps, not b for flats)
```
The exporter parses note name and velocity layer from filename automatically.

**Validated against:**
- Repository Bass format (working reference)
- DX-TX format (working reference)

**Key format settings applied automatically:**
- `Application=MPC-V` (not MPC2 or older variants)
- Full ProgramPads/PadNoteMap/PadGroupMap structure
- `FilterType=2` with `Cutoff=1.0`
- `Active=True` on live layers, `VelEnd=0` for empty placeholder layers
- All envelope and LFO blocks included
- `KeyTrack=True`, `RootNote=0` — Rex's golden rules enforced

---

## 7. Sample-Based Kit Builder Workflows

The XPN toolchain is not only for XOmnibus-rendered content. It's a general sample-to-XPN pipeline for transforming existing sample libraries into intelligent MPC content.

### Single Sample → Full Keygroup

**Use case:** You have one great sample (a bass hit, a synth stab, a recorded instrument note) and want it playable across the keyboard.

**Steps:**
1. Identify the root pitch of the sample
2. Optionally: record/render 2-3 additional pitches for better quality (every octave minimum)
3. Run `xpn_exporter.py` with the sample(s) — it handles the zone math
4. Result: fully playable keygroup XPN where MPC pitch-shifts the sample to fill the keyboard

**Quality tip:** Record at the root note + octave above + octave below. The exporter assigns zones automatically.

### Sample Pack → Dynamic Drum Kit

**Use case:** You have a Drum Broker pack (e.g., "Filth by Beat Butcha") — 50+ samples — and want to make an intelligent, dynamic MPC kit from it.

**Anatomy of a professional sample pack:**
- Folder structure typically: `Kicks/`, `Snares/`, `Hats/`, `Percs/`, `Claps/`
- Within each folder: named variations (Dark, Bright, Compressed, Filtered, etc.)
- No velocity layers built-in — need to map variations as layers

**Atlas's sample pack → XPN mapping strategy:**

```
Pack Folder           → MPC Kit
─────────────────────────────────
Kicks/ (30 samples)   → A01: 4 best kicks, velocity layered
                        B01-B04: 4 next-best kicks as bonus variations
Snares/ (25 samples)  → A02: 4 best snares, velocity layered
                        B05-B08: 4 alternates
Hats/ (20 samples)    → A03 (Closed Hat): 4 velocity layers
                        A04 (Open Hat): 4 velocity layers
                        MuteGroup=1 applied to all hat pads
Percs/ (15 samples)   → A05-A08: mapped to perc pads
Claps/ (10 samples)   → A10: 4 velocity layers
                        B13-B16: bonus clap variations
```

**Making it "CycleKit"-dynamic:**
The best sample packs have 6-10 different recordings of the same hit. Real CycleKit dynamism means:
1. Layer 4 round-robin variations PER velocity layer
2. Use `CycleType=RoundRobin` (if firmware supports) or overlapping velocity ranges
3. Result: 4 velocity layers × 4 RR variations = 16 samples per instrument — never repeats

**Naming samples for the exporter:**
```
Kick_soft_RR1.wav
Kick_soft_RR2.wav
Kick_med_RR1.wav
Kick_med_RR2.wav
```
A kit naming scheme should communicate: instrument, velocity level, round-robin index.

### Curated Collection → Thematic Bundle

**Use case:** You have dozens of sample packs and want to curate a thematic XPN pack.

**Atlas's curation philosophy:**
A good XPN pack tells a story. The pads should feel connected. "Dark Grit" shouldn't have one warm fluffy pad alongside brutal industrial hits.

1. Define the vibe/theme first (Boom Bap, Lo-Fi, Industrial, Tropical...)
2. Select the hero samples that define the theme's core
3. Add supporting elements that complement, not compete
4. Test the kit as a whole — do the sounds work together?
5. Name the pack and individual pads with the theme in mind

---

## 8. Sonic DNA → MPC Pad Feel Mapping

XOmnibus Sonic DNA has 6 dimensions. Each translates to specific MPC design choices:

| Sonic DNA Dimension | MPC Translation |
|--------------------|----------------|
| **Brightness** (high) | Samples rendered with resonant high-end intact; velocity → filter brightness |
| **Brightness** (low) | Dark samples, low-pass filtered renders, velocity barely changes brightness |
| **Warmth** (high) | Velocity crossovers are soft and gradual; attacks are gentle; round wave shapes |
| **Warmth** (low) | Immediate transients, thin tails, velocity = sharp vs. very sharp |
| **Movement** (high) | LFO-modulated renders captured; multiple velocity layers capture peak movement |
| **Movement** (low) | Static, stable samples; consistency across velocity layers |
| **Density** (high) | Layered renders with multiple elements; complex stereo field |
| **Density** (low) | Clean, single-element sounds; mono or narrow stereo |
| **Space** (high) | Longer reverb tails captured in renders; but trim for MPC standalone CPU |
| **Space** (low) | Dry, close sounds; no reverb baked in |
| **Aggression** (high) | Hot velocity curves: soft hit = 60% volume, hard = 110% (clip-style) |
| **Aggression** (low) | Gentle velocity response; soft hits are genuinely soft |

**Practical velocity curve design from DNA:**
```
High aggression (0.8+):
  VelStart 1→20: volume 40%, bright
  VelStart 21→50: volume 70%, hot
  VelStart 51→90: volume 95%, peak
  VelStart 91→127: volume 110% (overdrive)

Low aggression (0.2-):
  VelStart 1→40: volume 25%, warm
  VelStart 41→80: volume 55%, rounded
  VelStart 81→127: volume 85%, still gentle
```

**Space dimension and MPC CPU:**
High-space XOmnibus presets have long reverb tails. Rendering them into samples with 8-second tails is valid but expensive in RAM. Recommendation:
- Render with 2-3 second natural tail (not the full reverb)
- Let the MPC user add reverb via MPC's built-in FX
- State in the preset description: "add MPC reverb to taste"

---

## 9. XOmnibus Macro → MPC Knob Mapping

XOmnibus engines have 4 canonical macros: CHARACTER (M1), MOVEMENT (M2), COUPLING (M3), SPACE (M4).

In XPN packs, these 4 concepts translate to 4 assignable knobs (Q-Links) in the MPC program:

| XOmnibus Macro | MPC Q-Link | Parameter Target | Range |
|---------------|-----------|-----------------|-------|
| M1: CHARACTER | Q1 | Filter Cutoff (or Tone/Brightness) | 0.3 → 0.9 |
| M2: MOVEMENT | Q2 | LFO Rate (or Vibrato depth if using plugin) | 0.1 → 0.8 |
| M3: COUPLING | Q3 | (instrument-specific) e.g., Drive, Texture, Grain | varies |
| M4: SPACE | Q4 | Reverb Send Level | 0.0 → 0.7 |

**Important:** In XPN/sample-based programs, macros work differently than in live synthesis:
- You can't assign a Q-Link to a synthesis parameter (there is no synthesis in a sample program)
- Q-Links in drum/keygroup programs can target: volume, pan, filter cutoff/resonance, pitch, sample start point
- Design the Q-Link assignments based on what movement the sample supports, not what the XOmnibus macro did

**Per-engine macro translation examples:**
```
BOB (XOblongBob):
  M1 CHARACTER → Filter Cutoff (warmth dial)
  M2 MOVEMENT → Sample Start (texture scrubbing)
  M3 COUPLING → Resonance (fatness)
  M4 SPACE → Reverb Send

DRIFT (XOdyssey):
  M1 CHARACTER → Filter Cutoff (familiar/alien axis)
  M2 MOVEMENT → Pitch LFO Rate (drift speed)
  M3 COUPLING → N/A in sample → Drive level
  M4 SPACE → Reverb Send + Delay Send
```

---

## 10. Engine-Specific XPN Strategies

| Engine | Strategy | Program Type | Notes |
|--------|---------|-------------|-------|
| **ONSET** | Render drum voices as multi-layer WAVs | Drum | Primary target. 4 vel layers, GM layout, hat choke. |
| **ODYSSEY/DRIFT** | Multi-sample keygroup via xpn_exporter | Keygroup | Render at every minor 3rd, capture Tidal Pulse in layers |
| **BOB/OBLONG** | Keygroup multi-sample | Keygroup | Warm analog character needs close-mic rendering |
| **FAT/OBESE** | Keygroup (bass register focus) | Keygroup | Prioritize C1-C3 range; C4+ optional |
| **MORPH** | Snapshot multiple morph states as separate programs | Keygroup × N | Morph A, Morph Mid, Morph B = 3 separate keygroups |
| **DUB** | Keygroup + delay baked into renders | Keygroup | Capture delay character; annotate dry vs wet variants |
| **SNAP** | Keygroup (transient-heavy) | Keygroup | Ensure transients survive rendering — no normalization |
| **OVERWORLD** | Keygroup (chip register) | Keygroup | Low octaves only; NES/Genesis character |
| **OPAL** | WAV stems (texture beds, not pitched programs) | — | Granular textures → time-based samples, not keygroups |
| **ONSET XVC** | Render complex coupled hits as single samples | Drum | Capture XVC output; don't try to replicate routing |

---

## 11. Atlas's Ongoing Advisory Cadence

When working in the XOmnibus repo, Atlas checks in on:

1. **New preset additions** — Are they XPN-exportable? Do dynamics translate?
   - Check: velocity response (D001 compliant)
   - Check: macro assignments reach appropriate MPC targets
   - Check: the preset sounds good as a flat render (not just in live synthesis)

2. **New engine additions** — Does it have a clear MPC export strategy?
   - Assign: program type (Drum/Keygroup/WAV stem)
   - Assign: render strategy (note range, velocity layers)
   - Assign: macro → Q-Link mapping

3. **XPN tool updates** — Does the toolchain need to grow?
   - Watch for: engines without dedicated export scripts
   - Watch for: render quality gaps (new sample rates, new formats)

4. **Non-destructive preset audits** — Which parameters shift for better pad feel?
   - Deliver as recommendations with before/after parameter values
   - Never modify presets directly without user approval

---

## 12. Known Gaps and Future Work

**SNAP filter envelope → XPN:**
SNAP has a unique amp-to-filter detection chain (B002) that creates its signature transient click. This doesn't render cleanly into static samples — the characteristic is the real-time synthesis. Workaround: render multiple attack transient lengths and give the player velocity layers that capture different transient shapes.

**OPAL granular → MPC:**
XOpal's granular synthesis is fundamentally incompatible with sample-based XPN programs. The correct strategy is exporting texture WAV stems (30-60 seconds of granular output) that can be loaded as loop samples in MPC. Not a drum kit, not a keygroup — a texture library.

**AudioToBuffer coupling renders:**
When AudioToBuffer Phase 3 is complete, OPAL will accept audio-rate coupling input. This creates new render possibilities: capture Overworld→Opal or Drift→Opal coupled outputs as multi-samples. Atlas will document this when the coupling architecture is finalized.

**Round-robin in XPN (firmware limitation):**
`CycleType=RoundRobin` support varies by MPC firmware version and is not documented in the public format spec. Always test round-robin behavior on actual hardware before shipping a pack that relies on it.

<!-- bible extended 2026-03 — initial build, sample-based kit builder workflow documented -->
