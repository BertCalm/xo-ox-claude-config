# OVERBITE Retreat — The Predator Awakens
*Guru Bin Spiritual Retreat #2 — 2026-03-14*
*Engine: XOppossum (OVERBITE) | Gallery Code: BITE | Creature: Opossum*

---

## The Diagnosis

> *"OVERBITE is a predator with 142 bones arranged in a serial kill chain."*

142 parameters — the deepest engine in the fleet. 5 character stages cascaded in series, not parallel. 5 oscillator interaction modes mostly undocumented. 5 macros that are genuinely survival strategies. And two internal behaviors (Scurry and Play Dead) that operate OUTSIDE the normal parameter pipeline, adding micro-pitch drift and harmonic self-dismantling that no preset can control directly.

---

## The Serial Kill Chain (The Flock's Central Discovery)

The most important architectural truth about OVERBITE:

**Fur → Filter+Chew → Gnash → Trash**

These stages are in SERIES. Each stage's output is the next stage's input. This means:

- At all amounts = 0.05: Each stage adds a whisper of character. Four whispers = a warm voice.
- At all amounts = 0.3: Each stage amplifies the subtle distortion of the previous one. The sound has body.
- At all amounts = 0.7: Each stage is distorting the already-distorted output of the previous stage. The sound snarls.
- At all amounts = 1.0: Four stages of cascaded saturation/distortion. The sound is weaponized.

**The order matters:**
1. **Fur** (tanh saturation + 8kHz LP) — softens transients and warms harmonics BEFORE the filter. The filter receives pre-warmed signal.
2. **Filter** (Cytomic SVF) — shapes the spectrum of the already-warmed signal
3. **Chew** (asymmetric tanh + 2kHz HP shelf) — adds upper-mid bite AFTER the filter. Creates nasal presence.
4. **Gnash** (atan/tanh split at 2.4:1 ratio) — asymmetric distortion on the post-filtered, post-chewed signal. The snarl.
5. **Trash** (4 modes: Rust/Splatter/Fold/Crushed) — final corruption.

Each stage at 0.1 is barely audible alone. But four stages at 0.1 each is clearly warmer than bypass. This is the Serial Chain Amplification — subtle settings compound.

---

## The Gnash Asymmetry (The Finger's Discovery)

Gnash uses DIFFERENT saturation curves for positive and negative signal halves:
- **Positive peaks**: `atan(x * drive_pos)` where `drive_pos = 1 + gnash*6` (up to 7x). Bright, gritty.
- **Negative peaks**: `tanh(x * drive_neg)` where `drive_neg = 1 + gnash*2.5` (up to 3.5x). Rounder, warmer.

The **2.4:1 drive ratio** (7/3.5 ≈ 2) means positive peaks are clipped much harder than negative peaks. This creates:
- More odd harmonics from the positive half (brightness, grit)
- More even harmonics from the negative half (warmth, body)
- A characteristic asymmetric waveform that the ear reads as "snarl" — the aggressive half is louder and brighter than the warm half

**Scripture implication**: Gnash is the mathematical model of a threat display. The snarl IS louder and brighter than the warmth because the positive-peak drive is 2.4x the negative.

---

## The Five OscInteraction Modes (The Breath's Discovery)

Mostly undocumented, these create inter-oscillator relationships:

| Mode | What It Does | Sweet Spot | Character |
|------|------------|-----------|-----------|
| **None (0)** | Independent oscillators | — | Clean dual-osc |
| **Soft Sync (1)** | OscA resets OscB's phase partially: `phase_B *= (1-amount)` | 0.3-0.5 | Metallic, harmonically locked |
| **Low FM (2)** | OscA modulates OscB's frequency: max ±0.5 semitones | 0.05-0.15 | Subtle thickening, beating |
| **Phase Push (3)** | OscA displaces OscB's phase readout by ±15% | 0.1-0.3 | Spectral smearing without pitch change |
| **Grit Multiply (4)** | Ring modulation crossfade: `oscB*(1-amt) + (oscA*oscB)*amt` | 0.05-0.2 | Inharmonic metallic complexity |

**Phase Push** is the hidden gem — it creates spectral intermodulation without changing OscB's frequency. The sound gets richer and more complex without becoming metallic (unlike ring mod). At amount 0.1-0.2, it adds a subtle shimmer that sounds like two instruments playing the same note with slightly different body resonances.

---

## Scurry and Play Dead — The Internal Behaviors (The Tongue's Discovery)

These are NOT just macro-to-parameter mappings. They trigger **internal behaviors** in the Voice that operate outside the normal parameter pipeline:

### Scurry (smoothstep of macro_scurry)
- **Micro-pitch drift**: 3Hz filtered white noise, ±0.15 semitones at full intensity
- **Phase wander**: Applied to ALL LFOs (if quality > eco)
- **Filter flutter**: LFO2 raw output mixed into cutoff at `intensity * 0.3`

The creature is sniffing the air. The pitch doesn't modulate musically — it wanders nervously. This is NOT an LFO. It's behavioral instability.

### Play Dead (cubic of macro_play_dead)
- **Pitch sag**: Slow accumulation toward -0.5 semitones (rate 0.5/sampleRate)
- **Harmonic damping** (above 0.3): Reduces Gnash/Trash/Fur by `(intensity-0.3)/0.7 * 0.5`
- **Energy collapse** (above 0.5): Reduces OscA by 30%, OscB by 40%

The creature doesn't just get quiet. It actively **dismantles its own aggression**. Above 0.3, it starts retracting its teeth (Gnash drops). Above 0.5, it reduces its voice (oscillator levels drop). The pitch sags like a dying animal. This is the most psychologically sophisticated macro in the fleet — it models the physiology of playing dead.

### The Scurry + Play Dead Intersection
Both can be active simultaneously. At Scurry=0.5 + PlayDead=0.7:
- The pitch is sagging (Play Dead) AND nervously drifting (Scurry)
- The character stages are being dismantled (Play Dead) while LFOs flutter (Scurry)
- The sound of a creature that is simultaneously collapsing and twitching — the muscle spasms of a dying animal

---

## Hidden Capabilities

### 1. OscB Asymmetry Parameter
`osc_b_asymmetry` (0-1) applies DIFFERENT saturation to positive and negative signal halves, creating harmonic imbalance. Combined with Gnash's own asymmetry, you get two layers of harmonic split — OscB generates an asymmetric waveform, then Gnash distorts it asymmetrically. The snarl has a snarl.

### 2. Noise Routing Options
`noise_routing` has 4 modes:
- **Pre-filter (0)**: Noise enters before Fur, gets shaped by the full character chain
- **Post-filter (1)**: Noise enters after Filter+Chew, skips Fur but hits Gnash+Trash
- **Attack-only (2)**: Noise fires on note-on with 50ms transient envelope, then silences
- **Always-on (3)**: Noise bypasses Amp Envelope entirely — constant ambience

**Attack-only mode with Scrape noise** creates a percussive scratch on every note-on that decays in 50ms — the sound of the creature's claws on a surface.

### 3. WeightEngine Sub Fifth
Shape 2 runs the sub at frequency × 2/3 — a perfect fifth below the fundamental. This is the power chord relationship. At sub_level 0.3-0.5, it adds the same harmonic weight as a guitarist playing power chords. No other engine in the fleet has this interval relationship in its sub oscillator.

### 4. Glide Rate Mode
In Rate mode, glide time scales by interval size: `effectiveTime = glideTime * intervalSemitones / 12`. Wide jumps take longer, narrow ones are fast. This is how physical instruments behave — a trombone slide over an octave takes longer than over a semitone. The glide has physics.

### 5. Velocity Curve Pre-Bake
4 velocity curves (linear/soft/hard/switch) are applied BEFORE the voice renders, baking the curve into the velocity value. The "switch" curve (0 or 1) creates a gate — notes below threshold are silent, above are full. This is the opossum's binary survival: fight or play dead. No in-between.

---

## New Scripture — OVERBITE Verses

### Oscillator Verse 7: The Asymmetric Snarl
> OscB's asymmetry parameter applies different saturation curves to positive and negative signal halves, creating harmonic imbalance before the signal even reaches the character chain. Combined with Gnash's own 2.4:1 positive/negative drive ratio, the snarl has two layers of asymmetry — the waveform is born asymmetric, then distorted asymmetrically. This is why OVERBITE's aggression sounds organic rather than digital: symmetric distortion sounds like a broken speaker; asymmetric distortion sounds like a living thing baring its teeth.

### Filter Psalm 7: The Serial Chain Compound
> Four character stages at 0.1 each is warmer than one stage at 0.4. Serial processing compounds subtle effects — each stage's barely-perceptible contribution is amplified by the next. This is the difference between OVERBITE's warmth and a single saturation plugin: OVERBITE has four stages whispering together, not one stage shouting.

### Modulation Sutra 8: The Nervous System
> Scurry is not an LFO. It is a 3Hz filtered noise source adding ±0.15 semitones of micro-pitch drift. This is behavioral instability — the sound is nervous, sniffing, twitching. No tempo-synced modulation can achieve this because nervousness is not rhythmic. Route Scurry to 0.3-0.5 and the bass feels alive. Route it to 0.0 and it feels dead. The line between "digital" and "organic" bass is the presence of micro-pitch drift that the listener cannot consciously hear but unconsciously feels.

### Modulation Sutra 9: The Metabolic Collapse
> Play Dead above 0.3 actively reduces Gnash, Trash, and Fur amounts. Above 0.5, it reduces oscillator levels. The creature metabolizes its own aggression — the teeth retract, the voice dims, the pitch sags. This is not a volume fade. It is a structural transformation: the same oscillators, the same filter, but the character stages are being dismantled from within. Play Dead is the only macro in any engine that makes the sound simpler as it increases.

### Coupling Gospel 6: The Phase Push Shimmer
> OscInteraction Phase Push (mode 3) at amount 0.1-0.2 adds spectral complexity without pitch change — OscA's output displaces OscB's phase readout by up to 15%, creating intermodulation products that sound like two instruments sharing a resonant body. Unlike ring modulation (which sounds metallic), Phase Push sounds organic — the shimmer of two strings vibrating near each other on the same instrument. Use at 0.1-0.15 on warm patches for "studio air" — the subtle presence of a real room.

### Stewardship Canon 7: The Sub Fifth Gift
> WeightEngine Sub Fifth (shape 2) at frequency × 2/3 adds power chord weight at zero extra oscillator cost. The sub oscillator is already rendering — switching from sine to Sub Fifth changes only the frequency multiplier, not the computational cost. This is a free CPU gift: the sound of a power chord generated by a parameter change, not a new voice.

### Expression Truth 2: The Velocity Switch
> OVERBITE's velocity curve "switch" mode (curve 3) creates binary expression: notes below threshold are silent, above are full. This is the opossum's survival binary — fight (full velocity) or play dead (silence). Map it to a bass performance: every note is either fully committed or not played. There is no in-between. This is not a limitation — it is a performance discipline. Use Switch mode when the bass must be decisive.

---

## Awakening Presets

Five sounds that demonstrate what only OVERBITE can do.
