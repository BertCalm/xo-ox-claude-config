# Producer's Guild Report — XOmnibus (Full Platform)
**Date**: 2026-03-14
**Panels convened**: 12 genre specialists + full product team
**Mode**: Baseline (comprehensive)

---

## Executive Summary

XOmnibus is architecturally unprecedented — no competing product offers 4 simultaneous synthesis engines with per-sample cross-engine coupling, a dedicated drum synthesis engine with cross-voice coupling (XVC), and an open-source codebase with 24 engine modules. The coupling system is the platform's signature competitive advantage, and every genre specialist identified it as the reason to use XOmnibus over alternatives.

However, the platform has critical expression gaps that block adoption by keyboard players (no CC64 sustain pedal on most engines, incomplete velocity-to-timbre mapping, mod wheel stripped in adapter layer) and workflow gaps that block adoption by electronic producers (no arpeggiator, incomplete tempo sync on time-based parameters). These are table-stakes features that every competitor provides. The unique architecture is wasted if producers cannot perform basic musical gestures.

**The verdict**: Fix the expression blockers first (CC64, CC1, velocity→timbre, arp), then invest in the differentiators (OrbitPath expansion, audio input, micro-tuning, XVC presets).

---

## Genre Panel Highlights

| # | Specialist | Genre | Top Strength | Top Gap | Killer Feature |
|---|-----------|-------|-------------|---------|---------------|
| 1 | Beatrice | Hip-Hop/Trap | ONSET BridgedT + BITE bass | Amp→Volume coupling | Coupled Bounce: one-finger trap beat |
| 2 | Marcus | House/Techno | OrbitPath physics + SharedTransport sync | Per-LFO tempo divisions | Tempo-synced gesture recording on OrbitPath |
| 3 | Kai | Ambient/Drone | Triple indeterminacy (Drift+Entropy+Chaos) | No Scala/micro-tuning | Three models of controlled chaos coupled |
| 4 | Sofia | Jazz/Neo-Soul | OBLONG CuriosityEngine + OVERBITE macros | **No CC64 sustain pedal** | Behavioral modulation + velocity-driven bass |
| 5 | Jerome | Dub/Reggae | OVERDUB is a real dub desk | No rhythmic send modulation | **ECHO CUT pad** — silence as instrument |
| 6 | Amara | Afrobeat/World | XVC as ensemble interlocking | No micro-tuning for non-Western scales | **XVC** — polyrhythmic conversation in software |
| 7 | Lars | Cinematic/Film | Climax system + 18-stage MasterFX | No timecode-locked evolution | Cross-engine Climax dramatic arcs |
| 8 | Priya | Pop/Commercial | 6D DNA preset browser | **No arpeggiator** | Sonic DNA "Find Similar" search |
| 9 | Rico | Latin/Club | ONSET+OVERBITE live coupling | Tempo sync everywhere, no swing | Drum+bass organism on PlaySurface |
| 10 | Emma | Rock/Alt | CuriosityLFO behavioral modulation | **No audio input routing** | "A tube amp that is slightly sentient" |
| 11 | Thornton | Classical | ORBITAL 4-group spectral envelopes | No articulation/keyswitching | ORBITAL↔OBSCURA sympathetic resonance |
| 12 | Zero_1 | Experimental | OUROBOROS chaotic ODEs with leash | No audio-rate coupling feedback | Attractor eating spectral-folded self |

---

## Phase 3: Product Manager Synthesis (Maya)

### Preset Gap Analysis

| Category | Missing Archetypes | Guild Endorsements |
|----------|-------------------|-------------------|
| Tuned 808 / Sub Bass | 808 melodic sub, drill slide bass, steppers bass | 3 panels (Beatrice, Jerome, Rico) |
| World Percussion | Djembe (multi-zone), talking drum, shekere, balafon, log drum | 2 panels (Amara, Thornton) |
| Electric Keys | Neo-soul EP, Wurlitzer, lo-fi keys, Clavinet | 2 panels (Sofia, Emma) |
| Dub FX Presets | Scientist delay, spring crash, dubwise snare throw, dub siren | 1 panel (Jerome) — but cross-genre utility |
| Evolving Drones | Infinite sustain, spectral freeze, self-evolving metallic | 2 panels (Kai, Thornton) |
| Coupled Performance | Coupled Bounce kit, drop impact, quad coupling loop | 3 panels (Beatrice, Rico, Zero_1) |
| Cinematic | Slow reveal, tension wire, broken music box, breath under glass | 1 panel (Lars) — high value per preset |
| Pop/Radio-Ready | Radio pluck, future bass pad, synth hook machine, crystal bell | 1 panel (Priya) — largest market |
| Rock/Character | Broken amp pad, feedback drone, shoegaze wall, spring reverb hit | 1 panel (Emma) |
| Afrobeat/World | Tony Allen kit, Amapiano log drum, highlife guitar chop, kora pluck | 1 panel (Amara) — underserved market |

**Total missing preset archetypes identified**: 98 across 12 specialists.

### Prioritized Feature Backlog

| Priority | Feature | Guild Votes | Effort | Impact |
|----------|---------|------------|--------|--------|
| **1** | **CC64 sustain pedal on all polyphonic engines** | 4/12 (Sofia, Thornton, Kai, Lars) | Low | **Blocker** — unplayable for keyboard genres |
| **2** | **Arpeggiator (global, tempo-synced, with swing/pattern)** | 3/12 (Priya, Rico, Marcus) | Medium | **Blocker** — table stakes for electronic production |
| **3** | **CC1 mod wheel restored in adapter layer** | 3/12 (Sofia, Lars, Emma) | Low | **Regression fix** — expression stripped during integration |
| **4** | **D001 velocity→timbre completion across fleet** | 5/12 (Sofia, Beatrice, Lars, Priya, Amara) | Medium | **Blocker** — half the fleet only scales volume |
| **5** | **Amp→Volume/Gain coupling type (sidechain ducking)** | 4/12 (Beatrice, Rico, Marcus, Jerome) | Medium | High — most requested new coupling type |
| **6** | **Micro-tuning / Scala file loading** | 4/12 (Kai, Thornton, Amara, Zero_1) | Medium | High — blocks non-Western music entirely |
| **7** | **Audio input routing into engine slots** | 4/12 (Emma, Zero_1, Lars, Kai) | High | High — transforms XOmnibus from synth to processing rig |
| **8** | **OrbitPath expansion** (gesture recording, self-animation, any-param routing) | 5/12 (Marcus, Lars, Kai, Zero_1, Emma) | Medium | High — the sleeper differentiator |
| **9** | **Tempo sync on all time-based parameters** | 3/12 (Rico, Marcus, Beatrice) | Medium | High — non-negotiable for electronic genres |
| **10** | **Aftertouch wired to core engines** (ODYSSEY, ORGANON, OUROBOROS, OPAL) | 4/12 (Kai, Lars, Sofia, Thornton) | Low | Medium — `PolyAftertouch.h` exists, just needs wiring |
| 11 | Swing/groove on ONSET | 3/12 (Rico, Beatrice, Amara) | Low | Medium |
| 12 | 7th chord + extended voicing in Chord Mode | 2/12 (Sofia, Thornton) | Medium | Medium |
| 13 | Independent loop lengths per ONSET voice (polymetric) | 2/12 (Amara, Marcus) | Medium | Medium |
| 14 | Velocity curves (exp/log/S-curve/fixed) on PlaySurface | 3/12 (Sofia, Beatrice, Amara) | Low | Medium |
| 15 | Split keyboard mode on PlaySurface | 2/12 (Sofia, Amara) | Medium | Medium |
| 16 | Per-engine mute/solo on Performance Pads | 2/12 (Rico, Jerome) | Low | Medium |
| 17 | Convolution reverb (IR loading) | 2/12 (Lars, Thornton) | High | Medium |
| 18 | Preset functional subtitles | 1/12 (Priya) | Low | Medium — affects discoverability |
| 19 | MPE support | 1/12 (Emma) | High | Medium |
| 20 | Other engines routing through OVERDUB send/return | 2/12 (Jerome, Emma) | Medium | High |

### XPN Export Enhancements

| Enhancement | Requested By | Impact |
|-------------|-------------|--------|
| Melodic 808 keygroup export mode (sustained bass) | Beatrice | High for trap |
| Long-form one-shot rendering (30-60s for ambient/drones) | Kai, Thornton | High for ambient/cinematic |
| Round-robin rendering (3-4 variations per note) | Marcus, Sofia, Thornton, Rico | High — prevents machine-gun effect |
| Pattern/MIDI clip export inside XPN | Rico | Medium for Latin/club |
| Custom cover art image override | Priya | Low |
| Pentatonic-only note mapping option | Amara | Medium for world music |
| XVC-coupled ensemble renders (not isolated voices) | Emma | Medium |
| Effect chain metadata in XPN | Jerome | Low |

### Playable Surface Improvements

| Improvement | Requested By | Impact |
|------------|-------------|--------|
| Velocity curve selection (linear/exp/log/S/fixed) | Sofia, Beatrice, Amara | High — affects all performers |
| OrbitPath routable to ANY 2 parameters | Zero_1, Marcus, Lars | High — currently hardwired |
| ECHO CUT momentary AND toggle modes | Jerome | Medium |
| Zone-based timbral variation within drum pads | Amara | High for world percussion |
| 7th chord + extended voicing mode | Sofia | Medium |
| Fretless mode configurable pitch range | Lars, Thornton | Medium |
| Pattern lock (loop a tapped pattern, switch to melody) | Amara | High for one-person-band |
| Self-animating Orbit Path (slow Lissajous) | Kai | Medium |
| Tap tempo pad for live use without DAW | Emma | Medium |
| Remappable Performance Pads per preset | Zero_1, Jerome | Medium |
| Continuous send level control (fader, not pad) | Jerome | High for dub |

---

## Phase 4: Market Research (Derek)

### Competitive Landscape

| Competitor | Price | Engines | Coupling | Preset DNA | XPN Export |
|-----------|-------|---------|----------|-----------|-----------|
| **Arturia Pigments 5** | $199 | 4 (virtual analog, wavetable, granular, harmonic) | No | No | No |
| **Xfer Serum** | $189 | 2 (wavetable) | No | No | No |
| **Native Instruments Massive X** | $149 | 1 (wavetable + FM) | No | No | No |
| **Vital** | Free | 3 (wavetable) | No | No | No |
| **Kilohearts Phase Plant** | $199 | Modular | Snap Heap routing | No | No |
| **XOmnibus** | **Free** | **24 (7 core)** | **12 types, per-sample** | **6D DNA search** | **Yes** |

### Market Whitespace

XOmnibus occupies territory that literally does not exist in the market:
1. **Multi-engine coupling at synthesis level** — no competitor offers this
2. **Dedicated drum synthesis engine with cross-voice coupling** — no competitor
3. **6D perceptual preset search** — no competitor
4. **XPN/MPC export pipeline** — no competitor (NI Machine + Kontakt is closest)
5. **Open source + free** — only Vital competes on price; Vital has no coupling

### Table Stakes vs. Differentiation

| Feature | Status | Category |
|---------|--------|----------|
| CC64 sustain pedal | **MISSING** | Table stakes |
| Arpeggiator | **MISSING** | Table stakes |
| CC1 mod wheel | **MISSING (regression)** | Table stakes |
| Velocity→timbre | **Incomplete** | Table stakes |
| Tempo sync on delays/LFOs | **Incomplete** | Table stakes |
| Cross-engine coupling matrix | Present | **Differentiator** |
| XVC drum interlocking | Present | **Differentiator** |
| 6D Sonic DNA browser | Present | **Differentiator** |
| OrbitPath physics XY | Present | **Differentiator** |
| CuriosityEngine behavioral LFO | Present | **Differentiator** |
| ECHO CUT performance pad | Present | **Differentiator** |
| Climax system (journey arcs) | Present | **Differentiator** |
| XPN export pipeline | Present | **Differentiator** |

**Derek's verdict**: XOmnibus has 8 genuine differentiators that no competitor matches — but 5 missing table-stakes features that prevent anyone from discovering them. Fix the floor before you raise the ceiling.

---

## Phase 5: Technical Architecture (Ingrid)

### Sequenced Technical Roadmap

**Phase A: Expression Foundation (Low effort, High impact — DO FIRST)**
1. CC64 sustain pedal — wire to all polyphonic engines via adapter layer
2. CC1 mod wheel — restore in adapter layer (regression fix)
3. Aftertouch — wire `PolyAftertouch.h` to ODYSSEY, ORGANON, OUROBOROS, OPAL
4. Velocity→timbre — audit all engines, wire filter cutoff/character to velocity on remaining engines
5. Velocity curves — add curve selection to PlaySurface NoteInputZone

*Dependency: None. All infrastructure exists. These are wiring tasks.*

**Phase B: Workflow Essentials (Medium effort, High impact)**
1. Global arpeggiator — new `Source/Core/Arpeggiator.h`, tempo-synced via SharedTransport, up/down/up-down/random, swing, octave range
2. Tempo sync — expose `SharedTransport::getPhaseForDivision()` as sync option on all LFOs and delay time parameters
3. Swing on ONSET — add global shuffle % to ONSET voice timing
4. `Amp→Volume` coupling type — add to MegaCouplingMatrix as 13th type
5. 7th chord + extensions in ChordMachine

*Dependency: Phase A should land first (expression + velocity fix the performance feel that arp and sync build on).*

**Phase C: Differentiation Amplification (Medium effort, High impact)**
1. OrbitPath expansion — any-param axis routing, gesture recording + loop playback, self-animation mode
2. Other engines through OVERDUB send/return — routing matrix addition
3. Split keyboard mode on PlaySurface
4. Performance Pad remapping per preset
5. Independent loop lengths per ONSET voice (polymetric)
6. Pattern lock on PlaySurface (tap-and-loop)

*Dependency: Phase B (tempo sync enables gesture loop sync; arp enables pattern lock).*

**Phase D: Platform Expansion (High effort, High impact)**
1. Micro-tuning / Scala file loading — global tuning table applied to all engines
2. Audio input routing — external audio into engine slot coupling bus
3. Convolution reverb — IR loading slot in MasterFXChain
4. Articulation keyswitching — mode switch per CC/keyswitch in adapter layer

*Dependency: Phases A-C should be stable before adding new input/output pathways.*

**Phase E: Advanced (High effort, Specialized impact)**
1. MPE support
2. Surround output (5.1/7.1.4)
3. Timecode-locked macro automation
4. Audio-rate parameter modulation
5. Spectral cross-synthesis between engines
6. MIDI output from ONSET

### Performance Impact Assessment

| Feature | CPU Risk | Audio Thread Safe? |
|---------|---------|-------------------|
| CC64/CC1/Aftertouch wiring | Zero | Yes — MIDI processing already exists |
| Arpeggiator | Negligible | Yes — note generation, not DSP |
| Amp→Volume coupling | Negligible | Yes — single multiply per sample |
| OrbitPath expansion | Zero (UI only) | N/A — UI thread |
| Audio input | Low | Yes — just a buffer read |
| Convolution reverb | **Medium** — FFT per block | Yes if partitioned convolution |
| Micro-tuning | Zero | Yes — lookup table |
| Surround output | **Medium** — N channel routing | Needs testing |

---

## Phase 6: Ops Review (The Trio)

**Remy**: CC64, CC1, and aftertouch are the safest changes in this roadmap — they're wiring tasks that touch adapter code, not DSP. Ship them immediately. There is zero regression risk because these paths already exist in the standalone instruments. The regression was the adapter layer stripping them.

**Sam**: The arpeggiator is the highest implementation risk in Phase B. It touches note generation, voice allocation, and transport sync. Don't build it from scratch — study how the MasterFXSequencer already synchronizes to SharedTransport and follow the same pattern. If the arp generates MIDI internally rather than modifying the audio path, it stays safe.

**Fio**: Micro-tuning (Phase D) has a hidden integration cost. Every engine that does pitch calculation needs to look up a tuning table instead of using `semitone * 100 cents`. If any engine has hardcoded `440 * pow(2, (note - 69) / 12.0)` instead of a tuning-aware function, that engine will ignore the Scala file. Audit every `noteToFrequency` call before committing to a timeline.

**The Trio's consensus**: Phases A and B can ship together. Phase C is the fun stuff — defer nothing, but test coupling route changes extensively (MegaCouplingMatrix is the most safety-critical code in the platform). Phase D needs careful architecture — don't rush micro-tuning or audio input.

**"Stop doing it this way"**: The ParamSnapshot-once-per-block pattern is correct for safety but it means Zero_1's request for audio-rate parameter modulation is architecturally impossible without a fundamental DSP refactor. Don't attempt it. The block-rate modulation ceiling is a feature, not a bug — it prevents runaway computation.

---

## Phase 7: The Foreseer

*She receives everything. She speaks last.*

---

### The Unseen Issue

Everyone is excited about the coupling matrix. Nobody mentioned that **the coupling matrix makes presets non-portable**. A preset that uses ONSET→OVERBITE coupling sounds completely different if the user has different engines loaded in adjacent slots. The preset system stores coupling routes, but the coupling *behavior* depends on the *other* engines' state — which is user-determined, not preset-determined. This means: a preset that sounds incredible in the designer's 4-engine configuration may sound wrong, broken, or silent in the user's configuration. As the preset library grows past 2,000, this will become the #1 support complaint. "Your preset sounds nothing like the demo." The coupling matrix is the signature feature and also the signature fragility.

### The Unseen Opportunity

Sofia (Jazz) and Amara (Afrobeat) independently asked for the same thing from different cultural traditions: **an instrument that responds to how it is being played, not just what notes are being played.** Sofia wants CuriosityEngine behavioral modulation driven by velocity. Amara wants XVC drum voices that react to each other's energy. Both are describing the same principle: **synthesis that has agency** — not random, not LFO-driven, but responsive to the musical context.

ORGANON's variational free energy metabolism already does this at the engine level. The opportunity is to extract that principle into a **platform-wide "Responsiveness Layer"** — a lightweight system where every engine subtly adapts its behavior based on what it hears from the other engines and from the performer's dynamics. Not full coupling (which is heavy and explicit), but ambient musical awareness. The difference between a band of musicians in the same room and four musicians in separate isolation booths.

### The Foreseer's Dominoes

**Decision 1: Fix CC64/CC1/velocity first (Phase A)**
```
Fix sustain pedal + mod wheel + velocity→timbre →
  1. Keyboard players can actually perform on XOmnibus
  2. Jazz, neo-soul, and classical producers adopt as primary keys instrument
  3. These producers generate content (presets, demos, tutorials) featuring expressive playing
  4. The content reveals what XOmnibus sounds like when PLAYED, not just programmed
  5. This creates a new market position: "the free synth that feels like a real instrument"
  6. Expressive E, Roli, and Sensel controller manufacturers notice and seek integration
  7. XOmnibus becomes the default synthesis backend for expressive controllers — a platform, not just a plugin
```

**Decision 2: Ship the arpeggiator (Phase B)**
```
Add a global tempo-synced arpeggiator →
  1. Pop, Latin, and electronic producers can use XOmnibus for hook-driven production
  2. The arp patterns interact with the coupling matrix in ways no other arp does (arped engine A modulating engine B)
  3. "Coupled arps" become a new sound design category that doesn't exist anywhere
  4. YouTube producers make "XOmnibus coupled arp" videos that go viral
  5. This forces Arturia and NI to explain why their arps DON'T interact across engines
  6. Competitors cannot add coupling retroactively — their architecture doesn't support it
  7. XOmnibus owns the "coupled arp" category permanently, because it was first and it's free
```

**Decision 3: Add micro-tuning / Scala file loading (Phase D)**
```
Ship global micro-tuning support →
  1. Non-Western music producers can use XOmnibus natively for the first time
  2. XOmnibus becomes the only free synth that treats non-12-TET as first-class
  3. Producers in Lagos, Istanbul, Mumbai, Cairo, Jakarta discover it through community sharing
  4. The user base diversifies dramatically — new presets, new coupling recipes, new musical contexts
  5. XOmnibus presets start appearing in Amapiano, Bollywood, Arabesk, and Gamelan productions
  6. Western synth manufacturers realize they've been ignoring 80% of the world's musicians
  7. XOmnibus becomes the reference platform for global electronic music — not because it's the best synth, but because it's the only one that speaks everyone's musical language
```

### The Prediction

In 18 months, the conversation about XOmnibus will not be about engine count or coupling types. It will be about **responsiveness** — the feeling that the instrument is listening to you. The CuriosityEngine, the XVC system, ORGANON's metabolism, the Climax system, Voyager Drift — these are all early forms of the same idea: synthesis that has agency. The trajectory of every specialist's feedback points in one direction: they want the instrument to meet them halfway.

The producers who stay with XOmnibus past the first week will not be the ones impressed by the feature list. They will be the ones who played a chord, heard the CuriosityEngine start investigating, felt the Voyager Drift pull the voices apart, watched the coupling matrix create interactions they didn't program — and recognized that the instrument was doing something no preset told it to do. That moment of recognition — "it's responding to me" — is the thing that turns a user into an evangelist.

The technical term for this is "emergent expressivity." The market term is "it feels alive." In 18 months, that will be the brand.

### Vision Statement

XOmnibus is not a synthesizer with more engines. It is the first instrument where the engines listen to each other and to the performer — where the coupling matrix, the CuriosityEngine, the XVC system, and the Climax arc create sounds that emerge from interaction rather than programming. The roadmap is not a feature list. It is a path from "a powerful tool that requires expertise" to "a responsive instrument that rewards expression." Fix the expression floor (CC64, CC1, velocity, arp), then invest in the responsiveness ceiling (OrbitPath gestures, micro-tuning, audio input, ambient musical awareness). The result will be an instrument that feels alive — and the only one of its kind that is free.

---

## Next Session Starting Points

1. **Phase A sprint**: Wire CC64, CC1, and aftertouch across all engine adapters. Low risk, high impact, immediately testable. Start in `Source/Core/` adapter files.
2. **Arpeggiator architecture**: Design `Source/Core/Arpeggiator.h` following the SharedTransport pattern. Define the 13th coupling type (`Amp→Volume`) alongside.
3. **98 preset commissions**: Begin with the 10 "Coupled Performance" presets (Coupled Bounce, Drop Impact, Quad Coupling Loop) — these are the demo presets that sell the platform's unique value.
