---
name: hardware-expander
description: Hardware Expander — extends XO_OX plugin integration beyond MPC to Push, Maschine, Novation, Arturia, and other hardware controllers. Maps XOmnibus parameters to controller layouts, designs control surface mappings, generates MIDI CC maps, and validates hardware compatibility. Use when the user says 'hardware expander', 'Push integration', 'Maschine mapping', 'controller mapping', 'MIDI map for', 'hardware compatibility', 'Novation mapping', 'Arturia integration', 'map to controller', 'CC mapping', 'hardware template', 'controller preset', 'can I use this with Push', wants to bring XO_OX to a new hardware platform, wants a controller mapping file for a specific hardware, or wants to know which XO_OX parameters to surface on a controller.
---

# Hardware Expander

**XO_OX belongs in producers' hands, not just their screens.**

The Hardware Expander designs and validates control surface mappings for XO_OX plugins across major hardware platforms. Every hardware platform has different ergonomics — the Expander finds the right parameter-to-control mapping that makes XO_OX playable on each one.

---

## Supported Platforms

| Platform | Connection | Format | Priority |
|----------|-----------|--------|----------|
| **Akai MPC** | Native plugin + XPN | .xpn bundle | PRIMARY (handled by /kai) |
| **Ableton Push 2/3** | MIDI / User Mapping | Push preset | HIGH |
| **Native Instruments Maschine** | Controller Editor | NI mapping | HIGH |
| **Novation Launchpad / Circuit** | MIDI CC | CC map | MEDIUM |
| **Arturia Keylab / Minilab** | MIDI Control Center | Arturia preset | MEDIUM |
| **Akai APC40/APC Key25** | MIDI CC | CC map | LOW |
| **Generic MIDI Controller** | MIDI CC | CC table | ALWAYS |

---

## Parameter Priority Tiers

Not all parameters deserve hardware real estate. The Expander classifies by performance value:

### Tier 1 — Always on Hardware
The controls that matter during performance:
- Master volume / output level
- Filter cutoff (primary filter)
- Filter resonance
- Primary envelope (attack, release — or macro that combines them)
- Reverb/delay send
- Macro controls (if the engine has them: MACHINE, PUNCH, BOND, etc.)
- Mod wheel destination

### Tier 2 — Useful on Hardware
Sound-shaping controls worth having accessible:
- LFO rate and depth
- Filter mode or character control
- Oscillator mix / layer balance
- Drive / saturation amount
- Chorus depth
- Arp/sequence rate (if applicable)

### Tier 3 — Deep Edit Only
Parameters that are set once per preset and rarely adjusted in performance:
- Individual envelope stages (ADSR individually)
- Oscillator fine tune / detune
- Individual effect parameters
- Voice count / polyphony mode
- Internal routing switches

---

## Mapping Design Process

### Step 1: Read the Engine Parameter List
Identify all parameters with their MIDI CC assignments or names. Source from:
- Engine `.h` file (APVTS parameter definitions)
- Preset files (parameter keys)
- CLAUDE.md parameter table

### Step 2: Assign Hardware Slots
For each target hardware, map Tier 1 and Tier 2 parameters to physical controls:

**Push 2/3 Layout Example:**
```
8 knobs (top row): Volume, Cutoff, Resonance, Env Attack, Env Release, Reverb, Delay, Drive
8 buttons (row 2): Preset +/-, Arp on/off, Filter mode, LFO sync, Coupling on/off, [engine macros]
Pad matrix: [velocity-mapped notes / trigger pads for drum engines]
```

**Maschine Layout Example:**
```
8 smart strips: Primary macros (MACHINE, PUNCH, SPACE, MUTATE for ONSET)
4 pages of 8 knobs:
  Page 1: Performance (volume, cutoff, resonance, reverb, delay, drive, macro1, macro2)
  Page 2: Envelope (attack, decay, sustain, release, mod depth, mod rate, LFO shape, LFO rate)
  Page 3: Character (oscillator mix, detune, saturation, chorus, filter mode, voice, ...)
  Page 4: Engine-specific (unique parameters for this engine)
Pads: Velocity-sensitive notes
```

### Step 3: Generate CC Map
For generic MIDI controllers, produce a MIDI CC map:

```
MIDI CC MAP: [ENGINE NAME]
[Version: X.X]

CC01 (Mod Wheel): Filter Cutoff depth
CC07 (Volume): Master Volume
CC11 (Expression): Macro 1
CC14: Filter Cutoff
CC15: Filter Resonance
CC16: Env Attack
CC17: Env Release
CC18: Reverb Send
CC19: Delay Send
CC20: Drive Amount
...
```

### Step 4: Validate Range Mapping
Every parameter has a range (0.0–1.0 or engine-specific). CC values are 0–127. The mapping document must specify:
- Whether the parameter is linear or log-scaled
- Whether the CC range covers the full parameter range or a useful subset
- Whether the parameter is bipolar (centered at 64 in CC terms)

---

## Hardware Integration Templates

### Ableton Push Template
Output format: Markdown document describing the User Mapping + MIDI CC assignments for Push. (Push User Mapping is configured in Ableton Live's MIDI Map mode — the Expander produces the instructions, not an automated file.)

### Maschine Controller Editor Template
Output format: JSON or XML for NI Controller Editor (if engine-specific mapping file needed), or step-by-step instructions for manual mapping.

### Generic MIDI Controller Template
Output format: CC map table + recommended physical layout for a typical 8-knob, 8-pad controller.

---

## XOmnibus Coupling Parameters on Hardware

For XOmnibus specifically, coupling parameters are high-value performance controls:

```
Coupling CC Map (suggested):
CC80: Coupling amount (Engine A → Engine B)
CC81: Coupling amount (Engine B → Engine A)
CC82: Coupling type (if switchable via MIDI)
CC83: Coupling bypass toggle
```

---

## Arguments

- (none) — assess current hardware coverage: which platforms have mappings, which are missing
- `{engine name}` — design a full hardware mapping for a specific engine across Push, Maschine, and generic MIDI
- `push: {engine name}` — Push 2/3-specific mapping
- `maschine: {engine name}` — Maschine-specific mapping
- `cc-map: {engine name}` — generic MIDI CC map for any controller
- `xomnibus` — XOmnibus-level hardware design (coupling + engine switching + multi-engine performance)
- `validate: {engine name}` — check an existing mapping against the engine's actual parameter list
