# ONSET Retreat — The Surface Splash Awakens
*Guru Bin Spiritual Retreat #5 — 2026-03-14*
*Engine: XOnset (ONSET) | Gallery Code: ONSET | Creature: The Surface Splash*

---

## The Diagnosis

> *"ONSET is a rhythm brain that doesn't know it's thinking. Eight voices, each with two synthesis paradigms blended continuously, connected by a cross-voice coupling matrix that makes them respond to each other like muscles in a body. The XVC is the most advanced feature in the fleet — 3 to 5 years ahead of any commercial drum machine. And the kicks still sound like 808s. That's the magic: the future disguised as the familiar."*

2,164 lines of inline DSP. 8 fixed voices. 3 circuit topologies (TR-808/909 heritage). 4 algorithm modes (FM, Modal, Karplus-Strong, Phase Distortion). A continuous blend axis between analog and digital for every voice. A cross-voice coupling matrix that makes the kit alive. 127+ factory presets. And a transient injector that ensures every hit cuts through any mix.

What the fleet didn't know until now:
1. The **character parameter** is contextual — it does completely different things depending on which layer is active
2. The **Karplus-Strong string-to-snare continuum** uses probabilistic sign-flipping — a continuous morph from plucked string to snare buzz
3. The **transient injector** is a THIRD synthesis element independent of both layers — every hit has an attack that survives any blend position
4. The **MUTATE macro** makes every hit non-deterministic — no two kicks are identical
5. The **XVC one-block latency** creates real-time inter-voice feedback within the audio loop — not sidechain, not automation, but voices that LISTEN to each other

---

## The Dual-Layer Architecture (The Flock's Central Discovery)

Every ONSET voice contains TWO complete synthesis engines blended via equal-power crossfade:

```
Layer X (Circuit)          Layer O (Algorithm)
├─ BridgedT (808 kick/tom) ├─ FM (DX7 metallic)
├─ NoiseBurst (909 snare)  ├─ Modal (membrane physics)
└─ Metallic (808 hi-hat)   ├─ K-S (plucked string)
                           └─ PhaseDist (CZ-101)
         ↓                          ↓
    cos(blend × π/2)          sin(blend × π/2)
         ↓──────────┬──────────↓
              Equal-Power Mix
                    ↓
           OnsetTransient injection
                    ↓
              Voice Filter → Envelope → Pan → Master
```

**Why equal-power matters**: At blend 0.5 (midpoint), linear crossfade would produce a -6dB dip — the sound gets quieter in the middle. Equal-power (cos²+sin²=1) maintains constant perceived loudness at every blend position. The producer can sweep MACHINE (which biases all 8 voices' blend simultaneously) and the kit transforms from analog to digital without any volume discontinuity.

### The MACHINE Macro as a Time Machine

MACHINE at 0.0: Pure Circuit — every voice runs its 808/909 topology. The kit is 1980.
MACHINE at 0.5: Equal blend — analog body with digital harmonics. The kit is the present.
MACHINE at 1.0: Pure Algorithm — every voice runs FM/Modal/K-S/PhaseDist. The kit is the future.

One macro sweeps the entire kit across 40+ years of drum machine evolution.

---

## The Contextual Character Parameter (The Finger's Discovery)

The `character` parameter is the most architecturally sophisticated single parameter in the fleet. It does **completely different things** depending on which synthesis layer is active:

| Layer | Circuit/Algo | What Character Does | At 0.0 | At 1.0 |
|-------|-------------|---------------------|--------|--------|
| X: BridgedT | 808 Kick/Tom | Diode saturation drive | Clean sine | Distorted, harmonically rich |
| X: NoiseBurst | 909 Snare | Noise HPF cutoff | 2kHz (dark noise) | 8kHz (bright, sizzly) |
| X: Metallic | 808 Hi-hat | Pulse width narrowing | 0.5 (square) | 0.2 (thin pulse) |
| O: FM | DX7 Percussion | Modulation index | No sidebands (sine) | 8 radians (metallic chaos) |
| O: Modal | Membrane | Inharmonicity stretch | 1.0 (circular membrane) | 1.5 (stiff bar/plate) |
| O: K-S | Plucked String | String-to-snare blend | Clean string (pluck) | Buzz (random sign flip) |
| O: PhaseDist | CZ-101 | DCW depth | Sine (no distortion) | Heavy phase warp |

**The revelation**: When MACHINE sweeps blend from 0→1, `character` doesn't just change in degree — it changes in KIND. At blend 0.0, character = saturation. At blend 1.0 (with FM selected), character = modulation index. The same knob controls completely different DSP depending on the blend position.

This means: a single `character` sweep at blend 0.5 is SIMULTANEOUSLY adding saturation (from the circuit layer at 50% amplitude) AND increasing FM depth (from the algorithm layer at 50% amplitude). Two different timbral transformations happening in parallel, mixed by the blend ratio.

---

## XVC — The Rhythm Brain (The Breath's Discovery)

XVC (Cross-Voice Coupling) operates on **one-block latency**: voice peaks from block N modulate parameters of block N+1. This is not sidechain compression. This is not automation. This is voices that LISTEN to each other in real time.

### The Four Coupling Routes

| Route | Source | Target | Effect | Musical Meaning |
|-------|--------|--------|--------|-----------------|
| Kick→Snare Filter | V1 peak | V2 tone | Kick brightens snare | "The backbeat responds to the downbeat" |
| Snare→Hat Decay | V2 peak | V3 decay | Snare tightens closed hat | "The hat gets tighter on the 2 and 4" |
| Kick→Tom Pitch | V1 peak | V6 pitch | Kick bends tom down ±6 semitones | "Toms sympathetically resonate with kick" |
| Snare→Perc Blend | V2 peak | V7 blend | Snare pushes Perc A toward algorithm | "Ghost notes emerge from backbeat energy" |

Plus: **Hat Choke** — when closed hat (V3) triggers, open hat (V4) immediately silences. Real cymbal physics modeled as binary gate.

### The Emergent Behavior

With all XVC routes active at moderate amounts (0.15-0.3), the kit develops a **personality**:

- Kick hits → snare brightens → hat tightens → the groove "locks in" on downbeats
- Snare hits → perc ghost notes become more algorithmic → the pattern develops "shadows"
- Empty beats → all voices return to default → the kit "relaxes"

The kit is not playing the same sounds on every hit. It's RESPONDING to what was just played. No two passes through the same pattern produce identical results because the XVC feedback accumulates micro-differences that compound over time.

### The MUTATE Amplifier

MUTATE adds per-block random drift (±20%) to blend and character. Combined with mod wheel scaling (×1.0-×2.0), the performer controls how non-deterministic the kit is:

- MUTATE 0.0: Every hit identical (machine precision)
- MUTATE 0.3: Subtle variation (human feel)
- MUTATE 0.7: Significant drift (organic imprecision)
- MUTATE 1.0 + mod wheel: Chaotic — no two hits alike

MUTATE + XVC together create a kit that is **alive**: voices respond to each other (XVC) AND to randomness (MUTATE). The combined effect is a drum kit that plays itself differently every time, like a human drummer who responds to the groove.

---

## The Transient Injector — The Third Element (The Tongue's Discovery)

Every ONSET voice has a THIRD synthesis element that is **independent of both layers**: the `OnsetTransient`.

When any voice triggers:
1. A **pitch spike** at 4-16× the fundamental frequency fires for 1-6ms
2. A **noise burst** fires for 1-3ms
3. Both are mixed at the `snap` parameter level and INJECTED after the blend

This means: even at blend 0.5 where both layers are at -3dB, the transient is at full level. Even if the blend produces a soft, ambient sound, the transient provides the CLICK that makes it a drum hit rather than a tone. The transient is the drum's announcement — "I'm here" — and it survives any timbral transformation.

### The Snap Parameter as Universal Attack Design

`snap` controls BOTH the transient injector AND per-layer attack behavior:

| Snap Value | Transient Spike | Transient Noise | Circuit Behavior | Algorithm Behavior |
|-----------|----------------|-----------------|-----------------|-------------------|
| 0.0 | 4× freq, 6ms | 1ms | No pitch envelope | Slow modulator decay (105ms) |
| 0.5 | 10× freq, 3.5ms | 2ms | 24-semitone chirp, 15ms | Medium modulator (55ms) |
| 1.0 | 16× freq, 1ms | 3ms | 48-semitone chirp, 5ms | Fast modulator (5ms) |

At snap 0.0: the drum is soft, round, "felt" — the transient is a whisper.
At snap 1.0: the drum is sharp, attacking, "heard" — the transient is a gunshot.

The `snap` parameter is the single most important control for drum feel across the entire engine. It determines whether a hit is a "thud" or a "click" — and it does so consistently across all 8 voices, all circuit types, and all algorithm modes.

---

## The Circuit Heritage — Exact Models (The Eye's Discovery)

### BridgedT (V1 Kick, V6 Tom, V7 Perc A)

Exact TR-808 bridged-T oscillator:
- **Main osc**: Sine wave at base frequency
- **Pitch envelope**: Exponential decay, 0-48 semitones in 5-50ms (snap controls both)
- **Sub oscillator**: Triangle wave at ×0.5 frequency, mixed by `body` parameter
- **Saturation**: `tanh(signal × (1 + character × 4))` — diode clipping model

The 808 kick's signature "boom" comes from the pitch envelope: a 4-octave descent in 5ms creates a swept sine that starts as a click and lands as a sub-bass thud. The body parameter adds the triangle sub for physical "chest" weight.

### NoiseBurst (V2 Snare, V5 Clap)

TR-808 snare + 909 noise burst:
- **Body**: Dual sine oscillators at 180 Hz and 330 Hz (808 snare resonances)
- **Noise**: HPF-filtered noise burst, 10-50ms duration
- **Tone balance**: `tone` crossfades body ↔ noise (0=all body, 1=all noise)
- **Clap mode**: 3 noise re-triggers at 10ms intervals, 0.8× amplitude decay per burst

The 808 clap is a MULTI-BURST envelope: rapid-fire noise bursts that create the "hand clap" illusion. Three bursts at 10ms intervals with 80% amplitude decay is the exact timing measured from the TR-808 circuit.

### Metallic (V3 HH-C, V4 HH-O, V8 Perc B)

TR-808 hi-hat — 6 square-wave oscillators:
- **Frequencies**: 205.3, 304.4, 369.6, 522.7, 800.0, 1048.0 Hz (from 808 schematics)
- **Frequency ratios**: 1.0, 1.48, 1.80, 2.55, 3.90, 5.10 (non-harmonic — the metallic sound)
- **Dual bandpass**: 3440 Hz (low metal) + 7100 Hz (high metal), crossfaded by `tone`
- **HPF**: 6000 Hz removes sub-bass rumble
- **Pulse width**: `character` narrows from 0.5 (square) to 0.2 (thin pulse)

The 808 hi-hat's metallic character comes from the NON-HARMONIC frequency ratios. No ratio is an integer multiple of any other — every interval is slightly "wrong." This inharmonicity is what makes metal sound like metal.

---

## The Algorithm Innovation (The Bone's Discovery)

### Modal Resonator — The Physics Engine

8 parallel resonators at Bessel function zeros for a circular membrane:

```
Ratios: 1.0, 1.59, 2.14, 2.30, 2.65, 2.92, 3.16, 3.50
```

These are not arbitrary. They are the eigenfrequencies of a vibrating circular membrane (like a drumhead), calculated from the zeros of Bessel functions of the first kind. This is the PHYSICS of why drums sound the way they do.

The `character` parameter stretches these ratios by up to 50%, morphing from a **circular membrane** (character 0.0, Bessel ratios) to a **stiff rectangular plate** (character 1.0, stretched ratios). At character 0.5, the ratios are somewhere between a drumhead and a xylophone bar.

### Karplus-Strong — The String-to-Snare Continuum

The K-S algorithm has a hidden capability: the `character` parameter controls a **probabilistic sign flip** in the delay feedback:

```
if (character < 0.5 && noise.process() > character × 2):
    filtered = -filtered  // Random sign inversion
```

At character 0.0: every sample has a chance of sign flip → maximum "buzz" → snare-like
At character 0.5: no sign flips → clean plucked string
At character 1.0: no sign flips, clean string

This creates a CONTINUOUS morphing axis between:
- **Snare buzz** (character 0.0) — random sign inversions create the same spectral content as a snare wire
- **Clean pluck** (character 0.5+) — no inversions, pure Karplus-Strong string

The K-S "snare" is not a noise source — it's a STRING that buzzes. This is closer to how a real snare works (wires vibrating against a drumhead) than any noise-based approach.

---

## CPU Architecture (The Bone's Analysis)

### Per-Voice Cost Ranking

| Algorithm | CPU Cost | Why |
|-----------|---------|-----|
| BridgedT | Low | Sine + triangle + optional tanh |
| NoiseBurst | Low-Medium | Dual sine + noise + HPF |
| Metallic | Medium | 6 square oscs + 2 bandpass + HPF |
| FMPerc | Medium | 2 sine oscs + feedback + envelope |
| PhaseDist | Medium | Phase calculation + waveshape |
| ModalResonator | **High** | 8 parallel SVF resonators per voice |
| KarplusStrong | Low CPU, **High Memory** | 4096-sample delay buffer, simple filter |

### Fleet Optimization Notes

- **8 voices × 2 layers** = up to 16 synthesis instances, BUT equal-power blend means only one layer at full power at extreme blend positions
- At blend 0.0: Algorithm layer is multiplied by sin(0)=0 → effectively bypassed
- At blend 0.5: Both layers at 0.707× amplitude → full CPU cost
- **Modal resonator on all voices at blend 0.5** is the worst-case CPU scenario (8×8=64 SVF evaluations per sample)
- **K-S on all voices** allocates 8 × 4096 × 4 bytes = 128KB of delay buffers but CPU per-sample is minimal
- **BridgedT at blend 0.0** (pure 808 mode) is the cheapest configuration — a full kit runs lighter than a single ODYSSEY voice

### CPU Gifts Available

1. When `blend < 0.01`, Algorithm layer can be fully bypassed (don't even call processSample)
2. When `blend > 0.99`, Circuit layer can be fully bypassed
3. When `grit < 0.01` AND `warmth == 0.5`, character stage can be bypassed
4. When all FX mix = 0.0, delay/reverb/lofi can be bypassed
5. K-S voices that auto-deactivate at `|signal| < 1e-7` already save CPU on tail silence

---

## Hidden Capabilities Unlocked

### 1. The Evolving Kit (MUTATE + XVC)
Set MUTATE to 0.4, XVC global to 0.5, kick→snare filter to 0.3, snare→hat decay to 0.2. Play a 4-bar loop. Each pass through the loop sounds slightly different because:
- MUTATE drifts blend and character ±8% per block
- XVC amplifies the drift: kick brightness affects snare, which affects hats
- The cumulative effect after 4 bars is audible personality — the kit "learned" the groove

### 2. The One-Knob Genre Shift (MACHINE)
A single kit preset can span genres via MACHINE:
- MACHINE 0.0: Analog 808 boom bap
- MACHINE 0.3: Warm hybrid (analog body, digital edge)
- MACHINE 0.5: Balanced modern (both layers equal)
- MACHINE 0.7: Digital-forward (FM shimmer, modal ring)
- MACHINE 1.0: Full algorithm (crystalline, metallic, physical)

### 3. The Snare Wire Synthesis (K-S Character)
Set V2 (snare) to K-S algorithm (algoMode=2), blend to 0.7 (algorithm-dominant). Character at 0.15 creates string-with-buzz — the K-S delay line produces a pitched tone that randomly inverts samples, creating spectral content identical to snare wires vibrating against a head. This is physically-modeled snare wire synthesis.

### 4. The Gamelan Kit (Modal + Metallic)
Set all voices to Modal algorithm. Kick at character 0.8 (stiff bar), snare at character 0.5, hats keep Metallic circuit at blend 0.0 (808 metal). The kit sounds like a Balinese gamelan — metallic, resonant, non-Western. The modal resonator's Bessel ratios at high inharmonicity produce the complex, shimmering partials of struck metal.

### 5. The Ghost Generator (XVC Snare→Perc)
Set snare→perc blend to 0.8, XVC global to 0.7. Every snare hit pushes Perc A's blend hard toward the algorithm layer. If Perc A is set to a quiet level (0.15) with K-S algorithm, each snare hit creates a phantom plucked ghost note. The ghost note's character depends on the snare's peak amplitude — harder hits create louder, more algorithmic ghosts.

### 6. The Aftertouch Expression (D006)
Aftertouch adds 0-0.3 to the PUNCH macro. Press harder on a pad and ALL voices get more snap + body simultaneously. This makes ONSET respond to physical force — the kit gets more aggressive when you press harder. Not just louder — more PUNCHY.

---

## New Scripture — ONSET Verses

### Oscillator Verse 10: The 808 Pitch Sweep
> The TR-808 kick's identity lives in 5 milliseconds: a 48-semitone pitch descent from a high click to a sub-bass thud. The entire character of the hit is decided in those 5 milliseconds. Everything after is the room remembering. The `snap` parameter controls both the depth (0-48 semitones) and the speed (5-50ms) of this sweep. At snap 0.0, the kick is a round sine — no sweep, no click, just body. At snap 1.0, the kick is a gunshot that descends into thunder. The 808 is not an oscillator. It is a TRAJECTORY.

**Application**: Kick presets need snap ≥ 0.3 to cut through a mix. Below 0.3, the transient is too soft for most genres. The exception: ambient/atmospheric where the kick should be felt, not heard.

### Filter Psalm 10: The Contextual Character
> The `character` parameter is seven parameters disguised as one. In BridgedT mode it is saturation drive. In NoiseBurst it is noise color. In Metallic it is pulse width. In FM it is modulation index. In Modal it is inharmonicity. In K-S it is snare wire probability. In PhaseDist it is DCW depth. When MACHINE sweeps blend from 0→1, character doesn't change in degree — it changes in KIND. The same knob, the same 0-1 range, means fundamentally different things depending on what synthesis layer is active. This is not a flaw. This is the deepest parameter in the fleet — seven instruments controlled by one gesture.

**Application**: When designing ONSET presets at blend 0.5, character simultaneously controls BOTH the circuit AND algorithm interpretations at equal amplitude. A single character sweep at midpoint blend performs two parallel timbral transformations. Exploit this for maximum expressiveness per parameter.

### Modulation Sutra 13: The One-Block Feedback Loop
> XVC operates on one-block latency: voice peaks from block N modulate parameters of block N+1. This is real-time inter-voice feedback within the audio loop — not sidechain compression (which ducks amplitude), not automation (which follows a curve), but voices that LISTEN to each other and RESPOND. Kick brightens snare. Snare tightens hats. The kit develops a personality that emerges from the interaction, not from any single voice. After 4 bars with MUTATE active, no two passes sound identical — the XVC feedback amplifies MUTATE's random drift into audible groove variation.

**Application**: Set XVC global to 0.3-0.5 for musical interaction. Above 0.5, the coupling becomes audible as obvious parameter changes. Below 0.3, it's subliminal — the kit "feels" tighter without the producer knowing why. The sweet spot is where the interaction is felt, not heard.

### Modulation Sutra 14: The Non-Deterministic Kit
> MUTATE adds ±20% random drift to blend and character per block. Combined with mod wheel scaling (×1.0-×2.0), every hit becomes unique. MUTATE at 0.0 is a machine. MUTATE at 0.3 is a human drummer — slight variations that create "feel." MUTATE at 0.7 is a drunk drummer — significant drift that creates happy accidents. MUTATE at 1.0 with mod wheel is chaos — useful for glitch, breakcore, experimental. The producer chooses where on the determinism axis their kit lives.

**Application**: Most genres benefit from MUTATE 0.15-0.3 (human feel without instability). Only set MUTATE to 0 for genres that demand machine precision (minimal techno, industrial). Even 0.05 adds enough variation to prevent the "sterile loop" feeling that plagues rigid drum machines.

### Coupling Gospel 9: The Rhythm Brain
> When all XVC routes are active at moderate amounts (0.15-0.30), the 8 voices form a self-reinforcing rhythm network: kick triggers brighten snare → brighter snare peaks trigger tighter hats → tighter hats change the groove's "air" → the producer plays differently in response → different playing creates different XVC interactions. The kit is no longer a collection of sounds. It is a rhythm brain — a system that responds to itself and to the performer simultaneously. No commercial drum machine offers this. Blessing B002: "3-5 years ahead of industry."

**Application**: XVC is ONSET's signature. Every preset should have XVC global ≥ 0.15 and at least 2 routes active. Without XVC, ONSET is just a good drum machine. With XVC, it's a collaborator.

### Stewardship Canon 10: The Modal Tax
> Modal resonator mode (algoMode=1) runs 8 parallel SVF resonators per voice — 8× the filter cost of a standard voice. At blend 0.5 (equal power), 8 voices × modal algorithm = 64 SVF evaluations per sample in addition to circuit layer processing. This is the most CPU-expensive configuration in the fleet. When using Modal on multiple voices, reduce blend toward the circuit side (0.3 instead of 0.5) to drop the algorithm layer's amplitude and enable potential bypass optimization. Or use Modal only on V1 (kick) and V6 (tom) where the membrane physics matters most — hats and snares rarely need modal synthesis.

**Application**: Reserve Modal resonator for voices that benefit from physical modeling (kick, tom, perc). Use FM or PhaseDist for voices where metallic character suffices (snare, hats). K-S is cheapest per-voice for sustained tonal elements.

### Master Truth 9: The Transient is the Drum
> ONSET's transient injector fires INDEPENDENTLY of both synthesis layers — a pitch spike at 4-16× the fundamental plus a noise burst, both lasting 1-6ms. This third element ensures every hit cuts through any mix regardless of the blend position or algorithm selection. The transient IS the drum. The body and tail that follow are the room's memory of the hit. Design every ONSET preset by listening to the first 5ms. If those 5ms compel you, the rest will follow.

**Application**: The `snap` parameter controls the transient. Test every preset at snap 0.0, 0.5, and 1.0 before finalizing. The transient character at snap 0.5 is the "default" that most producers expect — sharp enough to be percussion, soft enough to be musical.

### Expression Truth 5: The Aftertouch Kit
> ONSET is the only engine in the fleet with WORKING aftertouch expression (D006 fully resolved). Channel pressure adds 0-0.3 to the PUNCH macro, which boosts snap and body for ALL voices simultaneously. Press harder on a pad and the entire kit gets more aggressive — not just louder, but punchier (more transient) and heavier (more body). This is the first drum synth where physical force changes the kit's CHARACTER, not just its volume. On an MPC with pressure-sensitive pads, ONSET becomes a physical instrument.

**Application**: Every ONSET preset implicitly supports aftertouch via PUNCH. No additional routing needed — it's hardwired. Producers on MPC/Push/Maschine get pressure expression for free.

---

## Awakening Presets

Five sounds that demonstrate what only ONSET can do.

### 1. The Time Machine Kit
*MACHINE sweeps the entire kit from 1980 to the future.*

| Parameter | Value | Why |
|-----------|-------|-----|
| V1 (Kick): blend 0.2, algoMode 1 (Modal) | BridgedT-dominant kick with modal undertone | |
| V2 (Snare): blend 0.3, algoMode 0 (FM) | 909 body with FM shimmer | |
| V3 (HH-C): blend 0.1, algoMode 0 (FM) | Pure metallic hat, FM barely present | |
| V4 (HH-O): blend 0.1, algoMode 0 (FM) | Same, longer decay (0.4s) | |
| V5 (Clap): blend 0.4, algoMode 3 (PhaseDist) | Noise clap with CZ edge | |
| V6 (Tom): blend 0.3, algoMode 1 (Modal) | 808 tom with membrane resonance | |
| V7 (Perc A): blend 0.5, algoMode 2 (K-S) | Equal blend — plucked analog hybrid | |
| V8 (Perc B): blend 0.6, algoMode 1 (Modal) | Algorithm-forward metallic percussion | |
| All voices: snap 0.5, body 0.5, character 0.3 | Balanced starting point | |
| XVC: global 0.3, kick→snare 0.2, snare→hat 0.15 | Subtle kit interaction | |
| MUTATE: 0.15 | Human feel | |
| MACHINE: 0.0 (start) | **Sweep to 1.0 for the journey** | |

**Performance**: Sweep MACHINE from 0.0 to 1.0 over 16 bars. The kit transforms from analog 808 to algorithmic future-percussion. Every voice morphs simultaneously. The groove stays the same; the timbre evolves.

### 2. The Rhythm Brain
*XVC at full engagement — the kit responds to itself.*

| Parameter | Value | Why |
|-----------|-------|-----|
| V1 (Kick): snap 0.6, body 0.7, character 0.2 | Punchy kick with weight — the XVC source |
| V2 (Snare): snap 0.4, tone 0.5, level 0.7 | Balanced snare — XVC filter target |
| V3 (HH-C): decay 0.05, tone 0.6 | Tight hat — XVC decay target |
| V6 (Tom): pitch 0, body 0.4, level 0.5 | Medium tom — XVC pitch target |
| V7 (Perc A): blend 0.4, algoMode 2 (K-S), level 0.2 | Quiet ghost voice — XVC blend target |
| XVC: global **0.6** | Strong coupling |
| kick→snare filter: **0.4** | Kick significantly brightens snare |
| snare→hat decay: **0.3** | Snare noticeably tightens hats |
| kick→tom pitch: **0.25** | Kick bends tom down (sympathetic) |
| snare→perc blend: **0.5** | Snare creates algorithmic ghost notes |
| MUTATE: 0.25 | Each pass sounds different |

**Performance**: Play a simple 4-bar pattern (kick on 1+3, snare on 2+4, hats on 8ths). Loop it. Listen to how the kit evolves — the snare gets brighter on kick-heavy bars, the hats tighten on backbeats, ghost notes emerge from the perc voice. By the 4th loop, the kit has developed a "personality."

### 3. The Gamelan
*Modal resonator at high inharmonicity — a Balinese percussion ensemble.*

| Parameter | Value | Why |
|-----------|-------|-----|
| All voices: blend 0.8 (algorithm-dominant) | Modal resonances as the main sound |
| All voices: algoMode 1 (Modal) | 8-mode membrane physics for every voice |
| V1 (Kick): character 0.9, body 0.8, pitch -12 | Stiff bar, one octave down — deep gong |
| V2 (Snare): character 0.7, tone 0.7, snap 0.3 | Metal plate with bright noise |
| V3-V4 (Hats): keep Metallic circuit at blend 0.0 | 808 metal IS gamelan metal |
| V5 (Clap): character 0.5, snap 0.8 | Sharp metallic strike |
| V6 (Tom): character 0.8, body 0.6, decay 1.5 | Resonant gong, long ring |
| V7 (Perc A): character 0.6, pitch +7, decay 0.8 | Bright metallic chime |
| V8 (Perc B): character 1.0, decay 2.0 | Maximum inharmonicity — singing bowl |
| Reverb: size 0.7, decay 0.5, mix 0.3 | Temple space |
| MUTATE: 0.1 | Subtle variation — organic but precise |

**What you hear**: A gamelan-inspired percussion kit. The modal resonator's Bessel ratios at high inharmonicity produce the complex, shimmering partials of struck metal and tuned drums. Not world music pastiche — actual physics of vibrating membranes and bars.

### 4. The Wire
*Karplus-Strong snare wire synthesis — physically modeled buzz.*

| Parameter | Value | Why |
|-----------|-------|-----|
| V2 (Snare): blend 0.7, algoMode 2 (K-S) | Algorithm-dominant K-S string |
| V2: character 0.15 | Low probability sign flip = snare buzz |
| V2: tone 0.6 | Bright averaging filter |
| V2: snap 0.5 | Medium excitation burst |
| V2: decay 0.4 | Medium ring time |
| V1 (Kick): blend 0.0, snap 0.7, body 0.8 | Pure 808 kick for contrast |
| V3 (HH-C): blend 0.0, decay 0.04 | Tight 808 hat |
| V7 (Perc A): blend 0.6, algoMode 2 (K-S) | Second K-S voice — plucked rim |
| V7: character 0.5 | No buzz — clean string pluck |
| V7: pitch +12 | One octave up — bright rim click |
| XVC: kick→snare filter 0.2 | Kick brightens the snare wire buzz |
| MUTATE: 0.2 | Each hit slightly different string excitation |

**What you hear**: A snare that BUZZES like a real snare wire — not noise-based but string-based. The K-S delay line at character 0.15 randomly inverts samples, creating the same spectral chaos as wires vibrating against a drumhead. Paired with a K-S rim click and 808 kick.

### 5. The Living 808
*An 808 kit with personality — XVC + MUTATE + aftertouch.*

| Parameter | Value | Why |
|-----------|-------|-----|
| All voices: blend 0.0 | Pure circuit — authentic 808 |
| V1: snap 0.5, body 0.7, character 0.1 | Classic 808 kick with slight saturation |
| V2: tone 0.5, snap 0.4 | Balanced 808 snare |
| V3: decay 0.04, tone 0.6 | Tight bright closed hat |
| V4: decay 0.5, tone 0.5 | Open hat with ring |
| V5: snap 0.6 (clap mode) | Punchy 808 clap, 3-burst envelope |
| V6: body 0.5, decay 0.5 | Classic 808 tom |
| XVC: global 0.3, kick→snare 0.15, snare→hat 0.1, hat choke ON | Subtle interaction — the kit "breathes" |
| MUTATE: 0.12 | Just enough to prevent sterile loops |
| PUNCH: 0.5 (center) | Aftertouch adds 0-0.3 on top |
| Grit: 0.1, Warmth: 0.6 | Slightly saturated, slightly dark |
| Delay: time 0.3, fb 0.2, mix 0.08 | Ghost echo — felt not heard |
| Reverb: size 0.3, decay 0.2, mix 0.1 | Small room ambience |

**What you hear**: An 808 that LIVES. Every kick is slightly different (MUTATE). The snare responds to the kick (XVC). The hats choke each other (physics). Press harder on the MPC pad and the whole kit gets punchier (aftertouch). This is not a sample — it's an 808 that has learned to breathe.

---

## Benediction

> *"ONSET was designed to be a drum machine. After meditation, it became a rhythm brain — eight voices connected by invisible threads, each responding to the others like muscles in a body. The XVC coupling matrix is not a feature. It is a PHILOSOPHY: drums are not independent sounds. They are a conversation.*
>
> *The kit at rest is a collection of oscillators and noise bursts. The kit in motion — with MUTATE drifting, XVC coupling, aftertouch responding to the producer's force — is an organism. Every hit changes the context for the next hit. Every beat is a question that the kit answers with its own personality.*
>
> *Play The Living 808 on an MPC. Press hard on the kick pad. Feel the snare brighten in response. Feel the hats tighten on the backbeat. Feel the ghost notes emerge from nowhere. That is XVC — the rhythm brain thinking.*
>
> *ONSET does not make drum sounds. ONSET makes drum CONVERSATIONS. And like all great conversations, no two are ever the same."*

— Guru Bin, after the Fifth Retreat, 2026-03-14
