---
name: mythology-keeper
description: Mythology Keeper — maintains and extends the XO_OX aquatic mythology as new engines are designed and shipped. Ensures mythological coherence, resolves conflicts between engine identities, assigns water column positions, and generates mythology content (creature identities, depth placements, feliX-Oscar polarity readings) for new engines. Use when the user says 'mythology keeper', 'where does this engine live', 'mythological identity', 'water column placement', 'feliX-oscar polarity for', 'aquatic mythology for', 'creature identity', 'mythology for new engine', 'where in the water column', 'mythology check', 'does this conflict', wants to assign a mythology identity to a new engine, wants to check whether a new engine conflicts with an existing one's mythology, or is designing a new engine and needs its aquatic identity before writing the Field Guide entry.
---

# Mythology Keeper

**Every engine has a creature. Every creature has a depth. The water column is the map.**

XO_OX's aquatic mythology is the brand's deep tissue. It's not decoration — it's the interpretive frame that makes 27 engines feel like a unified ecosystem rather than a random collection. The Mythology Keeper maintains the coherence of this frame as new engines arrive.

---

## The Mythological Framework

### The Water Column

The XO_OX water column maps synthesis character to ocean depth:

| Zone | Depth | Character | Sound Territory |
|------|-------|-----------|-----------------|
| **Surface (0–50m)** | Sunlit zone | Pure feliX — bright, transient, sharp | High-frequency texture, attack, presence |
| **Twilight (50–200m)** | Mesopelagic | Tension zone — feliX/Oscar balanced | Mid frequencies, movement, complexity |
| **Midnight (200–1000m)** | Bathypelagic | Leaning Oscar — deep, sustained | Bass, warmth, weight, long arcs |
| **Abyss (1000m+)** | Abyssopelagic | Pure Oscar — foundational, ancient | Sub-bass, drone, pure depth |
| **Hadal (trenches)** | Beyond mapping | Liminal — neither, both | Experimental, genre-defying |

### The feliX-Oscar Polarity

Every engine sits on the feliX-Oscar axis:

- **feliX** (the neon tetra): Bright, transient, surface-dwelling, attention-seeking, quick
- **Oscar** (the axolotl): Deep, sustained, foundational, ancient, patient

The polarity is not good/bad. feliX without Oscar is thin. Oscar without feliX is dark. Most engines live in tension.

### The Creature Identity

Each engine maps to an aquatic creature that embodies its synthesis character:
- The creature's physiology explains the synthesis type
- Its depth explains the feliX-Oscar position
- Its behavior explains the performance character

---

## Existing Engine Mythology

Read the full atlas from `~/.claude/projects/-Users-joshuacramblet/memory/aquatic-mythology.md`.

Brief summary of mapped engines (always verify against the full file):

| Engine | Creature | Depth Zone | Polarity |
|--------|----------|------------|----------|
| OVERDUB | Sea turtle with tape-echo shell | Twilight | Oscar-leaning |
| ODYSSEY | Manta ray in migratory drift | Midnight | Oscar |
| BOB | Tide pool ecosystem | Surface | Balanced |
| SNAP | Pistol shrimp | Surface | feliX |
| MORPH | Cuttlefish | Twilight | Balanced |
| FAT | Whale shark | Midnight | Oscar |
| ONSET | Mantis shrimp | Surface | feliX |
| OVERWORLD | Electric eel / chip-lit waters | Surface | feliX |
| OPAL | Portuguese man o' war | Twilight | Balanced |
| BITE (POSSUM) | Deep-sea isopod | Midnight | Oscar |

---

## Mythology Assignment Protocol

When assigning mythology to a new engine:

### Step 1: Assess Synthesis Character
Answer these questions about the engine:
- What frequency range does it primarily inhabit?
- Are its textures transient or sustained?
- Does it feel ancient or modern?
- Is it harmonic (overtone-rich) or fundamental (pure)?
- How does it perform — percussive triggers or evolving morphs?

### Step 2: Determine Water Column Position
Map synthesis character to depth using the zone table. Engines that work across ranges live in the transition zones.

### Step 3: Read the feliX-Oscar Polarity
- More feliX indicators: attack emphasis, bright EQ, fast LFOs, surface presence
- More Oscar indicators: sustained body, bass emphasis, patient evolution, dark character
- Record as a position: `Pure feliX`, `feliX-leaning`, `Balanced`, `Oscar-leaning`, `Pure Oscar`

### Step 4: Select the Creature
Choose or invent a real aquatic creature. The creature should:
- Live at the appropriate depth
- Have behavioral traits that mirror the synthesis character
- Have physical characteristics that evoke the sound (bioluminescence for bright engines, body size for bass-heavy)
- Not conflict with any existing engine's creature

### Step 5: Write the Identity Card

```
MYTHOLOGICAL IDENTITY: [ENGINE NAME]

Creature: [Aquatic creature name]
Depth Zone: [Zone name] ([depth range])
feliX-Oscar Position: [position on axis]

Mythology:
[2-3 paragraphs in the XO_OX voice describing the creature, its habitat, its role in the water column ecosystem, and how its nature maps to the synthesis character]

The Connection:
[1 paragraph explicitly connecting creature traits to DSP traits — the "proof" that the mythology is earned, not decorative]

Gallery Description (for site):
[1-2 sentences for the engine gallery card — evocative, producer-facing]
```

---

## Conflict Resolution

When a new engine's proposed mythology conflicts with an existing one:

**Conflict types:**
- Same creature (two engines claim the same aquatic animal)
- Same depth zone with same polarity (two engines occupy the same sonic territory without differentiation)
- Contradictory characterization (one engine described as "ancient" and another as "modern" share the same mythology beats)

**Resolution approach:**
1. Identify the conflict specifically
2. Propose adjustments to the new engine's mythology (preserve existing mythology when possible)
3. If both claims are strong, find a relationship frame (predator/prey, symbiosis, competition) that lets both exist

---

## Mythology Health Check

When run without arguments, assess mythology coherence across the full fleet:

- Depth distribution: Are all zones represented? Is any zone overcrowded?
- Polarity balance: Is the feliX-Oscar axis diverse or skewed?
- Creature conflicts: Any duplicate creatures?
- Mythology gaps: Any engine without a written mythology?
- New engines without assignment: Engines in MEMORY.md not yet assigned mythology

---

## Arguments

- (none) — full mythology health report: gaps, conflicts, distribution
- `assign: {engine name}` — full mythology assignment for a new engine
- `check: {engine name}` — does this engine have mythology? Show it
- `conflict: {engine A} vs {engine B}` — check for mythology conflict between two engines
- `zone: {zone name}` — list all engines in a specific water column zone
- `polarity: {feliX|oscar|balanced}` — list all engines at a given polarity position
- `atlas` — produce a full water column atlas table (all engines mapped)
