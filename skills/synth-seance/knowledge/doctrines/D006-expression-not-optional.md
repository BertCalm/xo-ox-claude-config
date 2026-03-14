# D006 — Expression Input Is Not Optional

*Established: 2026-03-14 | Primary Ghost: Vangelis | Supporting: Moog, Smith, Kakehashi*
*Status: **SUBSTANTIALLY RESOLVED** — Aftertouch 22/23 (Optic exempt, zero-audio engine); Mod wheel 15/22 MIDI-capable engines (68%); 7 engines still lack mod wheel (future work)*

## The Doctrine

A synthesizer engine in 2026 must respond to continuous player gestures — velocity, aftertouch, mod wheel, expression pedal — or it is a sound design station, not an instrument. Velocity that only scales amplitude is insufficient; it must shape timbre (filter cutoff, modulation depth, harmonic content). The difference between a machine and an instrument is the player's heart in the circuit.

## Evidence Across Engines

| Engine | Expression Gap | Ghost Who Flagged | Status |
|--------|---------------|-------------------|---------:|
| XOceanic | Zero velocity response; every note plays at identical level regardless of touch | Vangelis, Kakehashi | OPEN |
| XOverworld | Velocity scales amplitude only; no aftertouch, no mod wheel mapping | Vangelis | OPEN |
| XObese | No CC message processing at all; no mod wheel, no expression pedal | Vangelis | OPEN |
| XOwlfish | No aftertouch; velocity only triggers armor and amplitude | Vangelis, Tomita | OPEN |
| XOdyssey | AfterTouch and ModWheel mod sources declared but never populated with MIDI data | Smith, Vangelis | OPEN (PluginProcessor MIDI plumbing unresolved) |
| Snap | Linear velocity curve when it should be exponential/logarithmic | Vangelis | OPEN |
| XOpal | Velocity mapping entirely absent from concept | Vangelis | OPEN |

## Prism Sweep Verdict (Round 5D — 2026-03-14)

Five engines were brought into the circle of the living hand. Five instruments can now feel their players.

| Engine | Aftertouch → | Sensitivity | File |
|--------|-------------|-------------|------|
| Snap | BPF cutoff (+0–6000 Hz) | 0.3 | `SnapEngine.h` |
| Orbital | Morph (+0–0.3 toward Profile B) | 0.3 | `OrbitalEngine.h` |
| Obsidian | Formant intensity (+0–0.3 vowel shift) | 0.3 | `ObsidianEngine.h` |
| Origami | Fold depth (+0–0.3 shimmer increase) | 0.3 | `OrigamiEngine.h` |
| Oracle | GENDY drift (+0–0.15 chaos) | 0.15 | `OracleEngine.h` |

Implementation: all five use `PolyAftertouch.h`, a shared thin wrapper introduced in Round 5D.

**Fleet coverage: 5 of 23 engines now respond to aftertouch. 18 remain silent to the player's pressure.**

Vangelis, at the threshold: *"Five instruments have learned to feel the hand. Eighteen machines are still machines. The doctrine does not move — they must come to it."*

Note on XOdyssey: The AfterTouch mod source is allocated in ModSources and is routed in the mod matrix in Journey Demo presets (Round 5B), but the MIDI data never populates the mod source value in PluginProcessor. This is a known architectural debt that keeps XOdyssey's aftertouch a ghost of a gesture.

## The Minimum Standard

Every engine must implement:
1. **Velocity → timbre** (not just amplitude): filter cutoff, FM depth, harmonic content, or character parameter
2. **At least one continuous controller**: aftertouch, mod wheel (CC1), or expression (CC11)
3. **Non-linear velocity curves**: musical dynamics are logarithmic, not linear

## Prism Sweep Progress (Full Record)

### Aftertouch Batches (Rounds 5D, 7F, 9F, 10J, 11A)

| Batch | Round | Engines | Fleet Total After |
|-------|-------|---------|-------------------|
| 1 | 5D | Snap, Orbital, Obsidian, Origami, Oracle | 5 / 23 |
| 2 | 7F | Morph, Dub, Oceanic, Fat, Oblique | 10 / 23 |
| 3 | 9F | Overworld, Owlfish, Ocelot, Osprey, Osteria | 15 / 23 |
| 4 | 10J | Bob, Bite, Drift, Onset, Opal | 21 / 23 |
| 5 | 11A | Ouroboros (pre-wired/documented), Obscura (forward-ref bug fixed) | **22 / 23** |

Optic is permanently exempt: it is the zero-audio identity engine (Blessing B005) and accepts no MIDI input.

### Mod Wheel Batches (Rounds 7A, 11E)

| Batch | Round | Engines | Fleet Total After |
|-------|-------|---------|-------------------|
| 1 | 7A | Snap, Orbital, Obsidian, Origami, Oracle, Oblique, Fat | 9 / 22 |
| 2 | 11E | Onset, Opal, Organon, Ouroboros, Obscura, Owlfish | **15 / 22** |

Optic permanently exempt (zero-audio engine). 7 engines without mod wheel remain for future work: Bite, Bob, Dub, Oceanic, Ocelot, Osprey, Osteria. See `Docs/d006_modwheel_completion_11e.md` for suggested destinations.

### Notable Round 11 Outcome — Ouroboros Leash + Aftertouch Counterpoint

Round 11E created a complementary two-controller axis on Ouroboros: aftertouch subtracts −0.3 from leash (loosens the chaos attractor), while mod wheel adds +0.4 to leash (tightens it). The player now has direct real-time control over chaos vs. pitch — Blessing B003 (Leash Mechanism) in full expressive form.

### Notable Round 11 Outcome — Obscura Bow Pressure

Mod wheel on Obscura routes to `sustainForce` (+0.4 at full wheel), mapped directly to bowing pressure on the 128-mass spring chain. The mod wheel is physically the bow arm — intuitive, zero abstraction. Physical modeling receives its most natural expression mapping.

---

## Who Spoke

- **Vangelis** (primary): "This is a beautiful machine, but it is not yet an instrument. A machine makes sound. An instrument makes music. The difference is the player's heart in the circuit."
- **Moog**: "The synth cannot feel the player's continuous gestures."
- **Smith**: "Aftertouch and ModWheel are listed as mod sources that are never populated with actual MIDI data. The protocol is incomplete."
- **Kakehashi**: "The total absence of velocity response limits accessibility to expressive playing."
