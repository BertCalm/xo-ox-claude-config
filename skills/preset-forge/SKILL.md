---
name: preset-forge
description: Preset Forge — converts Guru Bin's awakening preset tables and parameter refinement logs into fully-formed .xometa preset files, ready to drop into the XOmnibus Presets/ directory. Closes the retreat→code gap. Use when the user says 'forge presets', 'convert the refinement log', 'make presets from the table', 'guru bin designed these', 'turn this into a preset file', 'preset forge', wants to turn parameter/value/why documentation into actual preset files, has just completed a Guru Bin retreat and needs the presets committed, or has a list of parameter values that should become a .xometa file. Also invoke after /guru-bin when awakening presets have been designed but not yet written to disk.
---

# Preset Forge

**The gap between retreat and ship is a table full of parameter values with nowhere to go. The Forge fixes that.**

Guru Bin designs presets in the language of truth — parameter names, exact values, and the reasoning behind each choice. The Forge translates that truth into `.xometa` JSON, correctly structured, DNA-scored, mood-categorized, and ready to live in the Presets/ directory.

---

## The .xometa Schema

Every preset file follows this structure exactly:

```json
{
  "schema_version": 1,
  "name": "Preset Name Here",
  "mood": "Foundation",
  "engines": ["EngineName"],
  "author": "XO_OX Designs",
  "version": "1.0.0",
  "description": "2-3 sentences. What this sounds like, when to use it, what makes it memorable.",
  "tags": ["tag1", "tag2", "tag3"],
  "macroLabels": ["MACRO1", "MACRO2", "MACRO3", "MACRO4"],
  "couplingIntensity": "None",
  "tempo": null,
  "dna": {
    "brightness": 0.5,
    "warmth": 0.5,
    "movement": 0.5,
    "density": 0.5,
    "space": 0.5,
    "aggression": 0.5
  },
  "parameters": {
    "EngineName": {
      "prefix_paramName": 0.0
    }
  },
  "coupling": {
    "pairs": []
  },
  "sequencer": null
}
```

### The 6 Moods

| Mood | Character | When to Use |
|------|-----------|-------------|
| `Foundation` | Grounded, clear, essential | Init patches, bread-and-butter sounds, primary voices |
| `Atmosphere` | Textural, spatial, evolving | Pads, drones, ambience, background layers |
| `Entangled` | Coupled, interactive, relational | Cross-engine presets, coupling-heavy sounds |
| `Prism` | Spectral, harmonic-rich, refractive | Bright leads, spectral pads, overtone-heavy |
| `Flux` | Dynamic, in-motion, transforming | Sequences, arpeggios, rhythmic textures, morphers |
| `Aether` | Otherworldly, unusual, extreme | Experimental, alien, boundary-pushing |

### The 6D Sonic DNA

Score each dimension 0.0–1.0 based on the sound's actual character:

| Dimension | 0.0 | 0.5 | 1.0 |
|-----------|-----|-----|-----|
| `brightness` | Dark, sub-heavy | Midrange | Air, sizzle, sparkle |
| `warmth` | Cold, digital, icy | Neutral | Analog, woody, organic |
| `movement` | Static, still | Subtle drift | Constantly evolving |
| `density` | Thin, sparse | Medium | Thick, dense, layered |
| `space` | Dry, intimate, close | Room | Vast, oceanic, infinite |
| `aggression` | Gentle, soft, delicate | Moderate | Distorted, harsh, driving |

### Engine Name vs Parameter Prefix

Engine names in `"engines"` and `"parameters"` keys use the canonical name:

| Engine | Canonical Name | Parameter Prefix |
|--------|---------------|-----------------|
| OddfeliX | `OddfeliX` | `snap_` |
| OddOscar | `OddOscar` | `morph_` |
| Overdub | `Overdub` | `dub_` |
| Odyssey | `Odyssey` | `odyssey_` |
| Oblong | `Oblong` | `bob_` |
| Obese | `Obese` | `fat_` |
| Overbite | `Overbite` | `poss_` |
| Onset | `Onset` | `onset_` |
| Overworld | `Overworld` | `ow_` |
| Opal | `Opal` | `opal_` |
| Orbital | `Orbital` | `orbital_` |
| Organon | `Organon` | `organon_` |
| Ouroboros | `Ouroboros` | `ouroboros_` |
| Obsidian | `Obsidian` | `obsidian_` |
| Origami | `Origami` | `origami_` |
| Oracle | `Oracle` | `oracle_` |
| Obscura | `Obscura` | `obscura_` |
| Oceanic | `Oceanic` | `oceanic_` |
| Ocelot | `Ocelot` | `ocelot_` |
| Optic | `Optic` | `optic_` |
| Oblique | `Oblique` | `oblq_` |
| Ostinato | `Ostinato` | `osti_` |
| OpenSky | `OpenSky` | `sky_` |
| OceanDeep | `OceanDeep` | `deep_` |
| Owlfish | `Owlfish` | `owl_` |
| Ouïe | `Ouïe` | `ouie_` |
| Ohm | `Ohm` | `ohm_` |
| Orphica | `Orphica` | `orph_` |
| Obbligato | `Obbligato` | `obbl_` |
| Ottoni | `Ottoni` | `otto_` |
| Olé | `Olé` | `ole_` |

---

## Input Formats the Forge Accepts

The Forge can take any of these as input and produce `.xometa` output:

### Format A: Guru Bin Refinement Log Table

```
| Change | Parameter | Old | New | Why |
|--------|-----------|-----|-----|-----|
| The Obvious Fix | filter_cutoff | 3000 | 2600 | 3kHz peak causes listening fatigue |
| The Hidden Trick | oscB_detune | 5.0 | 7.03 | Creates 1.2 Hz beating |
```

The Forge uses the **New** column for values. Ignores **Old** and **Why** for the JSON (but includes Why reasoning in the description).

### Format B: Guru Bin Awakening Preset Table

```
## Preset: "Abyssal Memory"
Engine: Opal
Mood: Atmosphere
Parameters:
  opal_grainSize: 0.75
  opal_grainDensity: 0.6
  opal_pitch: 0.0
  ...
DNA: bright 0.2, warm 0.7, movement 0.6, dense 0.5, space 0.9, aggression 0.05
```

### Format C: Freeform Parameter List

```
opal_grainSize = 0.75
opal_grainDensity = 0.6
filter at 2600
reverb mix: 0.3
```

The Forge interprets natural language parameter descriptions and maps them to known parameter IDs. It flags any it can't resolve and asks the user to confirm before forging.

### Format D: Existing .xometa to Patch

User provides an existing preset file and a diff table. The Forge applies only the changes and writes the updated file.

---

## The Forge Protocol

### Step 1: Parse Input

Read the input — whatever format. Extract:
- Engine name (required — if ambiguous, ask)
- Parameter name:value pairs
- Any mood, DNA, description, or tag hints
- Preset name (required — if not given, propose one based on the sound character)

### Step 2: Resolve Parameters

For each parameter:
1. Check if the name includes the engine prefix — if not, prepend it
2. Check that the parameter name matches a known pattern for that engine
3. Flag any unrecognized parameters with a `⚠️` and a note to verify against the engine source
4. Convert any human-readable values to normalized floats:
   - Frequency in Hz: map to 0-1 based on typical parameter range (e.g., filter cutoff 20Hz–20kHz → logarithmic scale)
   - Percentages: divide by 100
   - Already-normalized floats (0.0–1.0): pass through
   - Integer choices: pass through as integer

### Step 3: Infer Missing Fields

If the user didn't specify, infer sensibly:
- **Mood**: from the sound character description and parameter values (high reverb → Atmosphere, heavy distortion → Flux or Aether)
- **DNA**: from the parameter values (high filter_cutoff → brightness 0.7+, reverb mix → space scales with reverb amount, distortion → aggression)
- **Tags**: 3-5 tags from the sound character (genre clues, texture words, instrument analogues)
- **Description**: 2-3 evocative sentences from the parameter set and any Guru Bin diagnosis text provided
- **macroLabels**: use the engine's canonical macro names (look these up from CLAUDE.md or ask)

### Step 4: Name the Preset

Preset names follow XO_OX conventions:
- 2-3 words, max 30 characters
- Evocative, not technical (not "Low Filter Pad" — yes "Tide Before Rain")
- No jargon, no feature names
- No duplicates — read existing preset names from the destination mood folder before confirming

If the user provided a name, check it against these rules and flag any issues.

### Step 5: Write the File

Output the `.xometa` file to:
```
~/Documents/GitHub/XO_OX-XOmnibus/Presets/XOmnibus/{Mood}/{PresetName}.xometa
```

Or if it's an engine-specific preset (not XOmnibus-level):
```
~/Documents/GitHub/XO_OX-XOmnibus/Source/Engines/{EngineName}/Presets/{Mood}/{PresetName}.xometa
```

Always ask the user to confirm the destination path before writing.

### Step 6: Validate

After writing, run a quick validation:
- JSON parses without error
- `schema_version` is present
- `engines` array is non-empty and uses canonical names
- `parameters` keys match engine names in `engines` array
- DNA values are all 0.0–1.0
- No parameter values obviously out of range (negative when they shouldn't be, > 1.0 when normalized)
- Preset name is unique in the destination folder

Report the validation result. Flag any issues.

---

## Batch Mode

When Guru Bin produces a full Awakening Preset set (5-10 presets from a Retreat), the Forge processes all of them in sequence:

1. Read all preset descriptions from the retreat document
2. Parse each one
3. Infer all missing fields
4. Propose all names as a batch for user review
5. User confirms or revises
6. Write all files
7. Report: files written, paths, any flags

---

## Coupling Presets

When a preset involves two engines (coupling preset in `Presets/XOmnibus/Entangled/`):

- `"engines"` array contains both engines: `["Opal", "Overdub"]`
- `"parameters"` has keys for both engines
- `"coupling"` section describes the pairs:

```json
"coupling": {
  "pairs": [
    {
      "source": "Opal",
      "target": "Overdub",
      "type": "FilterFrequencyModulation",
      "amount": 0.25
    }
  ]
}
```

Available coupling types (from MegaCouplingMatrix.h):
`FilterFrequencyModulation`, `AmplitudeModulation`, `PitchModulation`, `WaveshapeModulation`, `TemporalModulation`, `SpectralShaping`, `EnvelopeFollowing`, `GrainTrigger`, `ResonanceControl`, `PhaseModulation`, `AudioToBuffer`, `RingModulation`

---

## Alternative Output: C++ setParam() Code

If the user needs C++ code instead of (or in addition to) a .xometa file — for example, to hardcode a factory preset in an engine's PluginProcessor — the Forge can generate:

```cpp
// Preset: "Abyssal Memory" — Opal — Atmosphere
void loadPreset_AbyssalMemory(juce::AudioProcessorValueTreeState& apvts)
{
    auto setParam = [&](const juce::String& id, float value) {
        if (auto* p = apvts.getParameter(id))
            p->setValueNotifyingHost(value);
    };

    setParam("opal_grainSize",    0.75f);
    setParam("opal_grainDensity", 0.60f);
    setParam("opal_pitch",        0.00f);
    // ...
}
```

Invoke this with: "Forge as C++" or `mode: cpp`.

---

## Arguments

- (none) — the Forge reads the current conversation for parameter input
- `mode: json` (default) — output .xometa file(s)
- `mode: cpp` — output C++ setParam() function(s)
- `mode: both` — output both formats
- `batch` — process multiple presets from a retreat document
- `patch` — modify an existing .xometa file rather than creating new
