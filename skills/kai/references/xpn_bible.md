# XPN/XPM Format Bible — Rex's Domain

*The authoritative technical reference for MPC program and expansion format.*
*Rex has memorized every field. He reads the spec again when unsure.*

---

## Table of Contents
1. [XPN Container Format](#1-xpn-container-format)
2. [XPM Program Types](#2-xpm-program-types)
3. [Keygroup Programs](#3-keygroup-programs)
4. [Drum Programs](#4-drum-programs)
5. [Velocity Layer Math](#5-velocity-layer-math)
6. [CycleKit / Round-Robin Patterns](#6-cyclekit--round-robin-patterns)
7. [Building From Existing Samples](#7-building-from-existing-samples)
8. [Sample Path Conventions](#8-sample-path-conventions)
9. [XML Rules and Encoding](#9-xml-rules-and-encoding)
10. [Common Errors and Diagnostics](#10-common-errors-and-diagnostics)
11. [Preview Files](#11-preview-files)
12. [Rex's Golden Rules (Cheatsheet)](#12-rexs-golden-rules-cheatsheet)

---

## 1. XPN Container Format

An XPN file is a **ZIP archive** with a specific internal structure. Get the structure wrong and nothing loads.

```
MyPack.xpn (ZIP archive)
├── Expansions/
│   └── manifest (no extension — plain text or XML)
├── Programs/
│   └── MyProgram.xpm        (keygroup or drum program XML)
├── Samples/
│   └── MyProgram/           (subfolder named after program is convention)
│       ├── Sample_C2.wav
│       └── Sample_C3.wav
└── Presets/                 (optional, for plugin programs)
```

**Critical rules:**
- Folder names are case-sensitive on MPC (Linux filesystem)
- `Programs/` contains `.xpm` files (XML, despite the name looking like a bitmap format)
- `Samples/` paths must be **relative** from the XPN root — never absolute
- The manifest file in `Expansions/` tells MPC the pack name, version, author
- Multiple programs in one XPN = multiple `.xpm` files in `Programs/`

**Manifest minimum content:**
```
Name=My Pack Name
Version=1.0
Author=Artist Name
```

---

## 2. XPM Program Types

All `.xpm` files are XML. The `type` attribute on `<Program>` sets the behavior:

| Type | `<Program type="...">` | Use Case |
|------|------------------------|----------|
| Keygroup | `"Keygroup"` | Pitched instruments, melodic content |
| Drum | `"Drum"` | Percussion, one-shots, beat kits |
| Plugin | `"Plugin"` | AIR or NI instrument |
| MIDI | `"MIDI"` | MIDI program reference |

**All program types share:**
- `<Instruments>` container
- `<Instrument>` child elements defining each zone/pad
- `<ProgramPads>` for pad-level MIDI mapping
- `<PadNoteMap>` for pad→note assignment
- `<PadGroupMap>` for mute group assignment

---

## 3. Keygroup Programs

Full keygroup XML skeleton (annotated):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPCVObject>
  <Version>2.1</Version>
  <Application>MPC-V</Application>
  <Program type="Keygroup">
    <ProgramName>My Instrument</ProgramName>

    <Instruments>
      <!-- Each Instrument = one velocity layer, one note range -->
      <Instrument>
        <!-- ZONE DEFINITION -->
        <LowNote>0</LowNote>        <!-- 0 = C-2 (MIDI note 0) -->
        <HighNote>127</HighNote>    <!-- 127 = G9 -->
        <RootNote>0</RootNote>      <!-- 0 = auto-detect (Rex's rule #2) -->
        <Tune>0</Tune>              <!-- Fine tune in cents (-100 to +100) -->
        <Transpose>0</Transpose>    <!-- Semitone offset -->

        <!-- VELOCITY SPLIT -->
        <VelStart>1</VelStart>      <!-- 1 = lowest velocity (never 0 on active layers!) -->
        <VelEnd>127</VelEnd>        <!-- 127 = hardest hit -->

        <!-- SAMPLE REFERENCE -->
        <File>Samples/MyInstrument/Sample_C3.wav</File>

        <!-- PLAYBACK BEHAVIOR -->
        <KeyTrack>True</KeyTrack>   <!-- Rex's rule #1 — ALWAYS TRUE on keygroups -->
        <OneShot>False</OneShot>    <!-- False = note-off stops playback -->
        <Loop>True</Loop>           <!-- Sustain loop -->
        <LoopStart>0</LoopStart>    <!-- Sample frame for loop start -->
        <LoopEnd>0</LoopEnd>        <!-- 0 = end of file -->
        <LoopXFade>0</LoopXFade>    <!-- Cross-fade in ms (0 = no xfade) -->

        <!-- ENVELOPE -->
        <Attack>0</Attack>
        <Decay>0</Decay>
        <Sustain>1</Sustain>
        <Release>0</Release>

        <!-- FILTER -->
        <FilterType>0</FilterType>  <!-- 0=None, 2=LowPass -->
        <Cutoff>1.0</Cutoff>        <!-- 0.0 to 1.0 -->
        <Resonance>0</Resonance>

        <!-- VOLUME/PAN -->
        <Volume>1.0</Volume>
        <Pan>0.5</Pan>

        <!-- ACTIVE STATE -->
        <Active>True</Active>
      </Instrument>

      <!-- Empty velocity layer placeholder — CRITICAL: VelStart=0 prevents ghost triggering -->
      <Instrument>
        <LowNote>0</LowNote>
        <HighNote>127</HighNote>
        <RootNote>0</RootNote>
        <VelStart>0</VelStart>      <!-- Rex's rule #3: 0 on empty layers = disabled -->
        <VelEnd>0</VelEnd>
        <File></File>
        <KeyTrack>True</KeyTrack>
        <Active>False</Active>
      </Instrument>
    </Instruments>

    <!-- PAD MAPPING -->
    <ProgramPads>
      <PadNoteMap>...</PadNoteMap>
      <PadGroupMap>...</PadGroupMap>
    </ProgramPads>
  </Program>
</MPCVObject>
```

**Multi-note keygroup (full chromatic):**
- Create one `<Instrument>` per root note with appropriate `<LowNote>` and `<HighNote>` ranges
- Standard strategy: sample every minor 3rd (C1, Eb1, F#1, A1, C2...) and assign ±1.5 semitone zones
- Each instrument gets its own `<File>` pointing to the corresponding sample
- `<RootNote>0</RootNote>` — always 0, MPC auto-detects from filename

---

## 4. Drum Programs

Full drum program XML skeleton:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<MPCVObject>
  <Version>2.1</Version>
  <Application>MPC-V</Application>
  <Program type="Drum">
    <ProgramName>My Kit</ProgramName>

    <Instruments>
      <!-- One Instrument per velocity layer per pad -->
      <!-- Pads are defined by Note range matching the pad's MIDI note -->
      <Instrument>
        <LowNote>36</LowNote>     <!-- Pad A01 = MIDI note 36 -->
        <HighNote>36</HighNote>
        <RootNote>36</RootNote>
        <VelStart>1</VelStart>    <!-- Layer 1: soft hits -->
        <VelEnd>40</VelEnd>
        <File>Samples/MyKit/Kick_soft.wav</File>
        <KeyTrack>False</KeyTrack>  <!-- DRUM programs: KeyTrack=FALSE -->
        <OneShot>True</OneShot>     <!-- DRUM programs: OneShot=TRUE -->
        <Active>True</Active>
        <!-- MuteGroup for hat choke: same number = they choke each other -->
        <MuteGroup>1</MuteGroup>
      </Instrument>

      <Instrument>
        <LowNote>36</LowNote>
        <HighNote>36</HighNote>
        <RootNote>36</RootNote>
        <VelStart>41</VelStart>   <!-- Layer 2: medium hits -->
        <VelEnd>80</VelEnd>
        <File>Samples/MyKit/Kick_med.wav</File>
        <KeyTrack>False</KeyTrack>
        <OneShot>True</OneShot>
        <Active>True</Active>
      </Instrument>

      <!-- Empty layers must exist to fill the Instrument count -->
      <Instrument>
        <LowNote>36</LowNote>
        <HighNote>36</HighNote>
        <VelStart>0</VelStart>    <!-- 0 = disabled, no ghost trigger -->
        <VelEnd>0</VelEnd>
        <File></File>
        <KeyTrack>False</KeyTrack>
        <OneShot>True</OneShot>
        <Active>False</Active>
      </Instrument>
    </Instruments>

    <ProgramPads>
      <PadNoteMap>
        <!-- Map each pad to its MIDI note -->
        <Pad number="1" note="36"/>   <!-- A01 = kick = C2 in GM layout -->
        <Pad number="2" note="38"/>   <!-- A02 = snare = D2 -->
        <Pad number="3" note="42"/>   <!-- A03 = closed hat = F#2 -->
        <Pad number="4" note="46"/>   <!-- A04 = open hat = A#2 -->
        <!-- ...pads 5-16... -->
      </PadNoteMap>
      <PadGroupMap>
        <!-- Group hat pads for choke -->
        <Pad number="3" group="1"/>  <!-- CHat in group 1 -->
        <Pad number="4" group="1"/>  <!-- OHat in group 1 — they choke each other -->
      </PadGroupMap>
    </ProgramPads>
  </Program>
</MPCVObject>
```

**GM Layout (standard pad assignments):**

| Pad | MIDI Note | GM Name |
|-----|-----------|---------|
| A01 | 36 | Kick / Bass Drum |
| A02 | 38 | Snare |
| A03 | 42 | Closed Hat |
| A04 | 46 | Open Hat |
| A05 | 45 | Low Tom |
| A06 | 47 | Mid Tom |
| A07 | 50 | High Tom |
| A08 | 49 | Crash |
| A09 | 51 | Ride |
| A10 | 39 | Clap / Hand Clap |
| A11 | 37 | Rimshot / Side Stick |
| A12 | 43 | Floor Tom |
| A13 | 54 | Tambourine |
| A14 | 56 | Cowbell |
| A15 | 75 | Clave / Claves |
| A16 | 76 | Hi Wood Block |

---

## 5. Velocity Layer Math

**Standard 4-layer split (even distribution):**
| Layer | VelStart | VelEnd | Character |
|-------|----------|--------|-----------|
| 1 | 1 | 32 | Ghost hits, barely touching |
| 2 | 33 | 64 | Light playing |
| 3 | 65 | 96 | Medium playing |
| 4 | 97 | 127 | Full force |

**Vibe-approved 4-layer split (musical curve):**
The bottom layers matter more dynamically — give them more range:
| Layer | VelStart | VelEnd | Ratio |
|-------|----------|--------|-------|
| 1 | 1 | 20 | Ghost (15%) |
| 2 | 21 | 50 | Light (23%) |
| 3 | 51 | 90 | Mid (31%) |
| 4 | 91 | 127 | Hard (29%) |

**Critical: Empty layer slots**
- MPC programs have fixed-size instrument slots (4 per pad/zone is common)
- Unused slots MUST have `<VelStart>0</VelStart><VelEnd>0</VelEnd>`
- `<Active>False</Active>` on empty slots
- DO NOT leave slots with VelStart>0 pointing to empty `<File>` — this is ghost triggering

---

## 6. CycleKit / Round-Robin Patterns

**The Masada CycleKit insight:** Real drum recordings don't repeat. A professional kit has 4-8 recordings of the same hit at the same velocity, and cycles through them on successive triggers. This eliminates the "machine gun" effect.

MPC supports this through **CycleType** or multiple layers at identical velocity ranges with different samples:

```xml
<!-- Round-robin implementation: same pad, same velocity, 3 different samples -->
<Instrument>
  <LowNote>38</LowNote>
  <HighNote>38</HighNote>
  <VelStart>65</VelStart>
  <VelEnd>96</VelEnd>
  <File>Samples/Kit/Snare_med_RR1.wav</File>
  <CycleType>RoundRobin</CycleType>  <!-- if supported by firmware -->
  <CycleGroup>1</CycleGroup>
  <KeyTrack>False</KeyTrack>
  <OneShot>True</OneShot>
  <Active>True</Active>
</Instrument>

<Instrument>
  <LowNote>38</LowNote>
  <HighNote>38</HighNote>
  <VelStart>65</VelStart>
  <VelEnd>96</VelEnd>
  <File>Samples/Kit/Snare_med_RR2.wav</File>
  <CycleType>RoundRobin</CycleType>
  <CycleGroup>1</CycleGroup>
  <KeyTrack>False</KeyTrack>
  <OneShot>True</OneShot>
  <Active>True</Active>
</Instrument>
```

**When CycleType isn't available:**
- Place RR samples in separate pads but give them the same MIDI note in the PadNoteMap
- MPC will randomly select among pads sharing a note in some configurations
- Alternative: Put RR samples as velocity layers with slightly overlapping ranges (1-40, 21-60, 41-80) — the overlap creates probabilistic selection near crossovers

**Practical RR design:**
- 2-4 RR samples per velocity layer per drum hit
- Label files: `Snare_med_RR1.wav`, `Snare_med_RR2.wav`, etc.
- Keep files at the same rough level — normalize independently

---

## 7. Building From Existing Samples

### Single Sample → Full Keygroup

The XPM exporter's primary use case: take ONE good sample and stretch it intelligently across the keyboard.

**Strategy:**
1. Identify the original pitch of the sample (root note)
2. Decide the range (e.g., C1–C6 for a piano bass sound)
3. Set `<RootNote>` to match the original pitch
4. Set `<LowNote>` and `<HighNote>` to the desired playable range
5. `<KeyTrack>True</KeyTrack>` — MPC will pitch-shift the sample based on played note vs. root note
6. For best quality: duplicate the sample into 3-4 zones and manually tune each to minimize stretch artifacts

**Pitch shift quality:**
- Single-sample across 3+ octaves will sound unnatural at extremes
- Best: sample at root + 1 octave above + 1 octave below
- "Good enough": sample every 3rd (root, +3, +6, +9 semitones)
- MPC uses internal resampling — quality depends on firmware; newer = better

**Filename convention for auto-detect:**
MPC can auto-assign root notes from filename patterns:
- `Sample_C3.wav` → MPC assigns C3 as root
- `Sample_60.wav` → MIDI note 60 = C3
- `CHORD_C2_hard.wav` → first note name found is used

### Drum Sample Folder → Coherent Kit

The other XPM exporter use case: take a folder of drum WAVs from a pack (e.g., Drum Broker) and intelligently map them to pads.

**Workflow:**
1. **Categorize** samples by keyword: kick/bass, snare/rimshot, hat/hihat, tom, clap, cymbal, perc
2. **Map to GM layout** using the pad table above
3. **Select velocity layers** — if a pack has `Kick_soft.wav`, `Kick_med.wav`, `Kick_hard.wav`, those become velocity layers on the same pad
4. **Set VelStart/VelEnd** proportionally across the layers found
5. **Handle extras** — if 16 kicks exist, overflow to Pad B01-B04 as variations

**Drum Broker packs (Filth by Beat Butcha style):**
- These packs often have: 10-30 kick variants, 10-20 snare variants, hat collections
- Don't flatten to one sample per pad — that destroys the pack's value
- Strategy: map the 4 most musical variations as velocity layers on A01
- Map bonus variations as separate pads on B row
- Make the B row feel intentional: label it "DIRTY KICKS" or "FAT SNARES" via ProgramName

**Dynamic kit design from a flat pack:**
1. Main kit (A row): 1 hero sample per instrument, velocity layered 4 deep
2. Alt kit row (B): 4 alternate kicks, 4 alternate snares, 4 alternate hats
3. Perc row (C): tambourine, cowbell, clave, additional percs
4. FX row (D): vinyl crackle, room tone, filtered hits, reversed samples

---

## 8. Sample Path Conventions

**Always relative from XPN root:**
```
<!-- CORRECT -->
<File>Samples/MyKit/Kick.wav</File>

<!-- WRONG — absolute path, will break on any MPC unit -->
<File>/Users/artist/Music/Samples/Kick.wav</File>

<!-- WRONG — traversal up the tree -->
<File>../../../Samples/Kick.wav</File>
```

**Depth limits:**
- MPC supports 2-3 levels of nesting inside Samples/
- Convention: `Samples/ProgramName/filename.wav`
- Avoid spaces in filenames when possible — use underscores
- Max filename length: 64 characters recommended, 128 technically

**Supported audio formats:**
- WAV (preferred): 16-bit or 24-bit, 44.1kHz or 48kHz
- AIFF: supported
- MP3: supported for preview files only
- Sample rate mismatch: MPC resamples internally, but 44.1kHz sounds best
- Bit depth: 24-bit offers no audible advantage in most MPC contexts (DAC is 24-bit but playback path may reduce)

---

## 9. XML Rules and Encoding

**Character escaping in XML:**
```xml
<!-- Characters that must be escaped in string values -->
& → &amp;
< → &lt;
> → &gt;
" → &quot;
' → &apos;

<!-- Example: program named "Bit & Butter" -->
<ProgramName>Bit &amp; Butter</ProgramName>
```

**Encoding declaration:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
```
- Always include this header
- Non-ASCII characters (accents, symbols) must be UTF-8 encoded
- Avoid smart quotes, em dashes — use ASCII equivalents

**Boolean values:**
- `True` / `False` (capitalized) — not `true`, not `1`/`0`
- Check existing working files for exact casing if in doubt

**Numeric formatting:**
- Float values: use decimal notation (`1.0` not `1`, `0.5` not `.5`)
- Integer values: no decimal
- Negative values work where documented (Tune, Transpose)

**Silent failures:**
- Missing required fields → MPC loads program with defaults (may not be what you want)
- Invalid float → field silently ignored
- Invalid XML structure → program may not load at all (no error shown)
- Wrong boolean casing → treated as False

---

## 10. Common Errors and Diagnostics

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Program doesn't appear in browser | Manifest missing or malformed | Check `Expansions/manifest` exists and has Name= field |
| Program loads but samples silent | Relative path wrong | Verify `Samples/` path matches actual ZIP structure |
| Pads trigger wrong sounds | PadNoteMap incorrect | Re-check pad numbers vs. note assignments |
| "Ghost" notes fire at zero velocity | VelStart=0 on non-empty layer | Set VelStart=0 AND VelEnd=0 AND Active=False on empty slots |
| Samples sound flat/wrong pitch | KeyTrack=False on keygroup | Set KeyTrack=True |
| All samples same pitch regardless of key | RootNote incorrect | Set RootNote=0 for auto-detect or set correct MIDI note |
| Kit layers don't blend smoothly | VelStart/VelEnd overlap missing | Add 1-2 unit overlaps at crossover points |
| Hat pads don't choke each other | MuteGroup not set | Assign same MuteGroup number to open/closed hat pads |
| Program corrupted on load | Non-UTF8 characters in XML | Strip special characters, check encoding |
| Import hangs / MPC freezes | Sample file too large | Keep individual samples under 100MB; total pack under 2GB |

---

## 11. Preview Files

**Rule:** Preview file must have **exactly** the same name as the `.xpm` file, just with `.mp3` or `.wav` extension.

```
Programs/
  MyKit.xpm
  MyKit.mp3    ← preview file (same name, audio extension)
```

- Recommended: 30-45 second MP3 preview, 192kbps
- Preview is what plays in the MPC expansion browser before loading
- Missing preview = no audio preview, but program loads fine
- Wrong name = no audio preview (silent failure)

---

## 12. Rex's Golden Rules (Cheatsheet)

```
1. KeyTrack = True          Always, on keygroup programs. Never False.
2. RootNote = 0             Always. MPC auto-detect convention.
3. VelStart = 0             On empty velocity layers — prevents ghost triggering.
4. Preview filename match   MyProg.xpm → MyProg.mp3 (exact same base name).
5. Relative paths only      Never absolute. Always relative to Samples/ folder.
6. XPN = ZIP                Structure: Samples/, Programs/, Expansions/manifest.
7. KeyTrack = False         On DRUM programs (not keygroups — opposite rule).
8. OneShot = True           On drum/percussion pads.
9. Active = False           On empty instrument slots.
10. VelEnd = 0              Pair with VelStart=0 on empty slots.
11. Escape XML              & → &amp; in names, < → &lt; everywhere.
12. Boolean casing          True/False (capitalized). Not true/1.
```

<!-- bible extended 2026-03 — initial build, xpn_exporter workflow documented -->
