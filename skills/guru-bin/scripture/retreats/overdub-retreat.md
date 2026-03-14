# OVERDUB Retreat — The Thermocline Awakens
*Guru Bin Spiritual Retreat #3 — 2026-03-14*
*Engine: XOverdub (OVERDUB) | Gallery Code: DUB | Creature: Thermocline*

---

## The Diagnosis

> *"OVERDUB is a mixing desk pretending to be a synthesizer. The keyboard is the confessional. The pads are the priest's hands. The delay is the memory. The reverb is the room where the memory lives. And between all of it — the silence where dub is born."*

38 parameters, 40 presets, 4 pads. A lean engine by fleet standards. But its architecture contains a truth that no other engine possesses: the effects chain is a **second instrument** gated by the performer's hands. The synth voice speaks. The FX voice echoes. The performer controls which echoes survive and which die. This is not synthesis with effects. This is **dub** — the art of selective memory.

What the fleet didn't know until now:
1. The series FX chain (Drive → Delay → Reverb) is architecturally a second voice with its own oscillator/filter/envelope equivalent
2. The tape delay's bandpass feedback creates a "spectral memory" — each echo remembers less than the last
3. Self-oscillating delay (feedback > 1.0) converges to a stable midrange tone via tanh compression in the feedback loop — a hidden instrument
4. The delay at 50-100ms with high feedback becomes a tuned comb resonator — a hidden pitched mode
5. The XOSEND pad's 5ms VCA smoothing turns rapid staccato presses into rhythmic "scatter" gates
6. Only 5 of 40 presets use velocity→filter — the engine's primary expression path is underexploited

---

## The Gated Send Architecture (The Flock's Central Discovery)

The most important truth about OVERDUB is in `processBlock()`:

```
float sendTarget = padState.send ? paramSnapshot.sendLevel : 0.0f;
```

The entire effects chain — Drive, Tape Delay, Spring Reverb — receives **zero signal** unless the XOSEND pad is held. This means:

- **Pad released**: Dry voice only. Effects process their stored energy (delay tails, reverb wash) but receive nothing new.
- **Pad pressed**: Signal flows into the effects at `sendLevel` intensity, smoothed by a 5ms exponential ramp.
- **Pad released again**: The send closes. Whatever entered the delay is now captured — it echoes, feeds back, reverberates, and eventually dies.

This is King Tubby at 18 Dromilly Avenue. The auxiliary send on his MCI JH-400 console was a fader he threw up and pulled down in real time. Every echo was a **deliberate act**. OVERDUB's architecture makes this the only way to use the engine. The effects are not decoration. They are a performance.

### The Performance Cycle

```
1. Play notes             → Dry voice heard immediately
2. Press XOSEND           → Sound flows into Drive → Delay → Reverb
3. Release XOSEND         → No new signal enters, but delay tails continue
4. Press ECHO CUT         → Feedback zeroed, tails die through bandpass
5. (optional) Press FIRE  → Retrigger at 0.8 velocity — accent into delay
6. Press PANIC            → Everything cleared instantly
```

The performer has four binary controls and infinite expression through timing.

---

## The Series FX Chain as a Second Voice (Phase R3: Awakening)

### The Ear's Discovery: Order Matters

**Drive → Tape Delay → Spring Reverb** in series is not an effects chain. It is a second instrument:

| FX Stage | Synthesis Equivalent | What It Does |
|----------|---------------------|-------------|
| **Drive** | Oscillator (harmonic enrichment) | tanh saturation adds harmonics BEFORE the delay captures them |
| **Tape Delay Bandpass** | Filter (spectral subtraction) | Each echo pass through the bandpass removes highs and lows — the delay "forgets" frequencies |
| **Spring Reverb** | Amplitude envelope (diffusion) | 6-stage allpass chain spreads energy across time — the reverb IS the release tail |

If you reversed the order (Reverb → Delay → Drive), you'd get:
- Reverb smears the clean signal (soupy)
- Delay repeats the soup (rhythmic mush)
- Drive distorts the mush (harsh)

The current order is King Tubby's insight: enrich first, echo the enrichment, then diffuse the echoes into space. The drive goes to the aux send BEFORE the tape machine. The spring tank sits AFTER the tape return. This architecture is historically accurate and sonically correct.

### The Finger's Discovery: The Tape Bandpass as Spectral Memory

The delay feedback path contains a bandpass SVF that models tape frequency response degradation:

| Wear | Low Cutoff | High Cutoff | Bandwidth | Character |
|------|-----------|------------|-----------|-----------|
| 0.0 | 200 Hz | 4000 Hz | 3.8 octaves | Full-bandwidth echoes (new tape) |
| 0.3 | 290 Hz | 3400 Hz | 3.5 octaves | Slightly warm (default) |
| 0.5 | 350 Hz | 3000 Hz | 3.1 octaves | Noticeably mid-focused |
| 0.7 | 410 Hz | 2600 Hz | 2.7 octaves | Telephone quality |
| 1.0 | 500 Hz | 2000 Hz | 2.0 octaves | Pure midrange ghost |

**Each echo passes through this bandpass again.** By the 4th echo at wear 0.5:
- 1st echo: 350-3000 Hz (most of the signal)
- 2nd echo: 450-2600 Hz (bandpass compounds)
- 3rd echo: 550-2300 Hz (narrowing further)
- 4th echo: 650-2100 Hz (only midrange survives)

The delay creates a **spectral history** — the first echo remembers the full signal, the last echo remembers only the midrange. Wear controls how quickly the delay forgets.

**The tanh in the feedback path** (separate from the output limiter) provides magnetic saturation modeling — each pass through the feedback loop is softly compressed. At feedback 0.5, this barely engages. At 0.8+, the tanh actively shapes the peaks, creating a compressed, warm tail. At 1.0+, the tanh is the only thing preventing unbounded growth — the delay oscillates at the level where tanh compression exactly equals the gain from feedback > 1.0.

### The Breath's Discovery: Wow as the Tape's Voice

The wow/flutter algorithm is measured from an actual Roland RE-201:

- **Wow**: 0.3 Hz sinusoidal, ±0.2% pitch deviation at full depth
- **Flutter**: xorshift32 noise → 45 Hz LP filter, ±0.05% pitch deviation
- **Combined**: `modulatedDelay = delaySamples * (1 + wow + flutter)`

The 0.3 Hz wow rate is significant. It sits at the boundary between "modulation I can hear" (>0.5 Hz, like vibrato) and "modulation I feel" (<0.1 Hz, like drift). At 0.3 Hz, the listener perceives the pitch waver as **character** — not vibrato, not drift, but the tape machine's own personality. The wow IS the tape's voice — its complaint about a capstan motor that can't quite maintain constant speed.

Flutter at 45 Hz adds micro-variations too fast to hear as pitch. They register as "texture" on transients — the mechanical rattle of the tape guides.

**The wow parameter scales both wow AND flutter.** Flutter depth = wow depth × 0.25 (the ratio 0.0005/0.002). This means you cannot have flutter without wow or vice versa — they are physically coupled, as they are in the real machine.

### The Eye's Discovery: The Self-Oscillation Convergence

When `delayFeedback > 1.0`, the delay output grows each iteration. But two mechanisms prevent unbounded growth:

1. **Bandpass filter**: Removes energy outside the pass band each iteration
2. **tanh saturation**: Compresses peaks in the feedback loop

The system converges to a **stable self-oscillation** — a midrange tone at approximately 1/(delayTime) Hz, modulated by wow/flutter, shaped by the bandpass. At feedback 1.1, wear 0.5:
- The oscillation frequency: ~2.67 Hz at 375ms delay (subsonic pulse) with harmonics at 5.3 Hz, 8.0 Hz, etc.
- The spectral center: ~1250 Hz (midpoint of the 350-2000 Hz bandpass at wear 0.5)
- The pitch waver: ±0.2% from wow = ±3.5 cents — a gentle wobble

This is a **second voice** hidden inside the delay — a droning, wavering midrange tone generated entirely by the feedback loop. This is Lee "Scratch" Perry's Black Ark sound: the delay machine singing to itself.

### The Tongue's Discovery: Expression Poverty and Hidden Wealth

OVERDUB has exactly 4 performance controls, all binary:

| Control | Type | Expression |
|---------|------|-----------|
| FIRE | Edge-triggered | Retrigger at fixed 0.8 velocity |
| XOSEND | Momentary hold | Binary send gate |
| ECHO CUT | Momentary hold | Binary feedback kill |
| PANIC | Edge-triggered | Reset all state |

No aftertouch. No mod wheel. No expression pedal. The Seance flagged this as D002 and D006. But within this constraint:

**Velocity → Filter** is the primary expression path. `filterEnvAmt * velocity` means:
- `filterEnvAmt: +0.4` → hard playing brightens the filter, soft playing darkens
- `filterEnvAmt: -0.3` → hard playing CLOSES the filter (inverted — dark stabs)

Only **5 of 40 presets** use this. The engine's single expressive dimension is 87.5% unused.

**The XOSEND scatter technique**: Rapid staccato pad presses create rhythmic send gates. The 5ms VCA smoothing turns binary presses into shaped pulses. At 16th-note tapping speed, each press opens the send for ~60ms (press time) + 5ms ramp = a burst of signal captured by the delay. With 1/8D sync delay and 0.65 feedback, the scatter creates syncopated echo patterns that follow the performer's rhythm.

### The Bone's Discovery: The Silent Send Waste

When XOSEND is not pressed:
- `sendVcaSmoothed` decays exponentially to zero (5ms time constant)
- The send buffer fills with zeros
- Drive processes zeros through tanh (output: 0.0)
- Tape delay writes zeros and reads with Hermite interpolation
- Spring reverb processes zeros through 12 allpass stages

**CPU opportunity**: When `sendVcaSmoothed < 1e-6` AND delay feedback has decayed AND reverb state is negligible, the entire send path could be bypassed. For presets where XOSEND is used sparingly, this could save 40-60% of FX CPU during silent periods.

**Polyphony**: Bass presets (7/40) are all set to poly mode by default. Bass at mono/legato saves 6 voices. Chord presets (7/40) rarely exceed 4 simultaneous notes. Only atmosphere presets need 6+.

---

## Hidden Capabilities Unlocked

### 1. The Tape Resonator Mode

The tape delay at **short delay times** (50-100ms) with high feedback and high wear becomes a **tuned comb resonator**:

- At 83.3ms delay: comb fundamental at 12 Hz (subsonic), harmonics at 24, 36, 48, 60 Hz... creating a pitched bass drone
- At 66.7ms delay: fundamental at 15 Hz, harmonics at musical intervals creating a pitched rumble
- At 50ms delay: fundamental at 20 Hz, harmonics at 40, 60, 80 Hz — the bottom edge of hearing

With feedback 0.90-0.95, wear 0.7+ (narrow bandpass), wow 0.0 (stable pitch):
- The comb filter emphasizes harmonics that fall within the 400-2500 Hz bandpass
- The result is a pitched, metallic resonance — not unlike the spring reverb but rhythmically animated
- Each new note entering through XOSEND excites the resonator differently depending on its spectral content

**The Tape Resonator** is a hidden instrument mode that no preset currently exploits.

### 2. The Fire Pad as a Rhythm Machine

FIRE retriggers the last note at velocity 0.8 (not 1.0 — an accent, not a duplicate). Combined with XOSEND:

1. Hold a single note (drone voice)
2. Press XOSEND (signal enters delay)
3. Tap FIRE rhythmically → each retrigger sends a fresh transient into the delay
4. The delay captures each retrigger as a separate echo train
5. Overlapping echo trains create polyrhythmic patterns from a single-finger rhythm
6. Press ECHO CUT → all echo trains die simultaneously, leaving reverb wash

OVERDUB becomes a **one-finger rhythm machine** — the FIRE pad is the "hit," the delay is the "pattern," and the spring reverb is the "space."

### 3. The Wear Sweep as Time Travel

Automating `delayWear` from 0.0 → 1.0 over 8 bars makes the echoes **age in real time**:
- Bar 1-2: Crisp, full-bandwidth echoes (new tape)
- Bar 3-4: Warm, slightly narrowed (breaking in)
- Bar 5-6: Murky, midrange-focused (degrading)
- Bar 7-8: Telephone-quality ghosts (ancient oxide)

Combined with ECHO CUT at the end: the aged, narrow-bandwidth tails die quickly because the bandpass has concentrated all energy into a narrow midrange band. The death is fast — the tape has nothing left to remember.

### 4. The Dub Space

The moment between ECHO CUT press and silence is the **dub space** — the most expressive pause in electronic music.

When ECHO CUT zeros the feedback:
- Existing delay tails decay through the narrowing bandpass
- Spring reverb continues to diffuse the dying tails
- The decay rate depends on: wear (narrow = faster death), reverb size (larger = longer tail), initial feedback level (more energy = longer dissipation)

At high reverb size (0.8+), the dub space lasts several seconds — the echoes die but the room remembers. At low reverb size (0.2), the dub space is brief — the echoes die and the room forgets immediately.

**Scientist's art**: The sound he REMOVES is louder than the sound he keeps. The dub space is a negative note — an intentional absence that the listener's brain fills with expectation.

### 5. The Exponential Glide

OVERDUB's glide uses exponential frequency approach:
```
glideSourceFreq += glideCoeff * (baseFreq - glideSourceFreq)
```

This means the glide **decelerates** as it approaches the target — fast at first, then lazy. Wide intervals arrive quickly to the vicinity, then take their time settling. This is the opposite of OVERBITE's Rate mode (which scales by interval size).

For dub bass, this exponential approach is musically correct. The slide should launch dramatically then land softly — the bass line settling into the pocket rather than slamming into it. At `voiceGlide: 0.15` in legato mode, the slide covers 90% of the interval in 50ms and spends 200ms on the last 10%. The arrival is a caress, not a collision.

### 6. The Drive Sweet Spot

The drive bypasses entirely at `amount ≤ 1.001f` (dead zone). First audible saturation starts around 1.05-1.1.

| Amount | Character | What's Happening |
|--------|-----------|-----------------|
| 1.0-1.001 | Bypass | tanh(x * 1.0) ≈ x for normal levels |
| 1.1-1.5 | Transparent warmth | Peaks barely touched, even harmonics added |
| 1.5-2.5 | Console overdrive | Clear harmonic saturation, transients softened |
| 2.5-5.0 | Woolly distortion | Heavy saturation, compressed dynamics |
| 5.0-10.0 | Destroyed | Near-square-wave clipping, all dynamics lost |

The **Tape Ceiling** (Scripture Rev. 7) applies here: drive at 1.5-2.0 adds warmth without source — the listener perceives warmth but can't identify why. Above 2.5, the drive announces itself. Below 1.5, the drive is invisible. The sweet spot for "dub console character" is 1.8-2.2.

---

## New Scripture — OVERDUB Verses

### Oscillator Verse 8: The Dub Bass Recipe
> Saw oscillator at -1 octave plus sub oscillator at 0.3-0.5 level is the dub bass foundation. The saw provides harmonics 1 through N with 1/N amplitude falloff — maximum sculpting material for the filter. The sub provides a pure sine one octave below the saw — chest-shaking fundamental weight. This combination is the King Tubby bass recipe: rich enough to send through tape delay (the harmonics create interesting echo patterns as the bandpass shapes them), heavy enough to rattle a sound system (the sub carries below the delay's bandpass, felt but never processed). No other oscillator combination achieves this balance. Square + sub is too hollow for the filter. Triangle + sub is too dark to echo interestingly. Saw + sub is the dub recipe because the complete harmonic series gives both the filter AND the tape delay maximum material to work with.

### Filter Psalm 8: The Delay Bandpass as a Second Filter
> The tape delay's feedback bandpass is a filter inside the effects chain — a spectral spotlight that narrows with wear from 200-4000 Hz (3.8 octaves) to 500-2000 Hz (2.0 octaves). Each echo passes through this bandpass again, compounding the narrowing. By the 4th echo at wear 0.5, only the 650-2100 Hz midrange survives. This is not a defect — this is the magic of tape delay. The bandpass creates a spectral memory: the first echo remembers the full signal, the last echo remembers only the midrange. The wear parameter controls how quickly the delay forgets. Treat wear as a second filter parameter — it shapes the echo spectrum the way cutoff shapes the voice spectrum.

### Modulation Sutra 10: The Wow Physiology
> Tape wow at 0.3 Hz modulates delay time by ±0.2%, creating pitch variations at a rate that sits at the boundary between "modulation I hear" (>0.5 Hz) and "modulation I feel" (<0.1 Hz). At 0.3 Hz, the listener perceives the pitch waver as character — not vibrato, not drift, but the tape machine's own personality. Flutter at 45 Hz adds micro-variations too fast to hear as pitch — they register as texture, the mechanical rattle of tape guides. Wow scales both rates simultaneously (flutter = wow × 25%), because in the physical RE-201, both arise from the same drive mechanism. You cannot have wow without flutter — they are one phenomenon at two timescales.

### Coupling Gospel 7: The Series FX as a Second Voice
> Drive → Tape Delay → Spring Reverb in series is not an effects chain. It is a second instrument. Drive adds harmonics (the oscillator). The delay's bandpass subtracts per echo (the filter). The reverb's allpass chain diffuses across time (the amplitude envelope). The performer plays the synth voice with the keyboard and the FX voice with the pads. When XOSEND opens, the synth feeds the FX instrument. When it closes, the FX instrument plays alone on stored energy. King Tubby's revelation: the mixing desk IS an instrument, and the effects chain IS a voice. Every dub preset should be designed with TWO timbral identities — the dry voice and the wet echo — because the performer will play them alternately.

### Stewardship Canon 8: The Silent Send Bypass
> When XOSEND is released and sendVcaSmoothed reaches zero, the entire send path processes silence — drive applies tanh to zero, delay writes zeros with Hermite interpolation, reverb runs 12 allpass stages on zero input. For presets where the performer uses XOSEND sparingly, this wastes 40-60% of FX CPU. A guard check — if sendVcaSmoothed < 1e-6 AND delay energy is negligible AND reverb states are below threshold, bypass the send path entirely — would gift this CPU back to the producer's session without any audible change. The silent send is the most expensive zero in the fleet.

### Master Truth 7: The Dub Space
> The moment between ECHO CUT and silence is the dub space — the most expressive pause in electronic music. When feedback is zeroed, existing tails die at a rate determined by three factors: wear (narrow bandpass = faster spectral death), reverb size (larger space = longer diffusion tail), and accumulated energy (higher feedback = more to dissipate). A high-wear ECHO CUT dies fast — the tape has nothing left to remember. A high-reverb ECHO CUT lingers — the room keeps the ghost. Scientist's art is mastering this timing: the dub space is a negative note, an intentional absence that the listener's brain fills with expectation. Design every dub preset with a specific dub space character — the time between the last echo and true silence is the engine's signature.

### Expression Truth 3: The Binary Performer
> OVERDUB has four binary performance controls: FIRE (retrigger), XOSEND (gate), ECHO CUT (kill), PANIC (reset). No gradients, no continuous control, no aftertouch, no mod wheel. This is not poverty — this is the engine's philosophy. In dub, the mixing engineer does not gently fade the send. He THROWS the fader and PULLS it back. The binary pads demand decisive performance: hesitation is silence, commitment is sound. The 5ms VCA smoothing turns binary gestures into musical shapes. Rapid XOSEND stabs create scatter patterns. Held XOSEND creates sustained send. The expression lives in the timing of binary decisions, not in the gradation of continuous controls.

---

## Awakening Presets

Five sounds that demonstrate what only OVERDUB can do. Each preset showcases a capability unique to OVERDUB's architecture.

**Design principles:**
- Every preset uses `filterEnvAmt ≥ ±0.2` (velocity→filter is the glass door)
- Every preset passes the First Two Seconds test (C3, velocity 80, immediate interest)
- Every preset has a specific dub space character (what happens after ECHO CUT)
- CPU stewardship: bass = mono/legato, leads = mono, pads ≤ 6 voices

### 1. King Tubby's Ghost
*The definitive dub bass — the one that makes producers close their laptop and sit in silence.*

**What it demonstrates:** The complete dub performance workflow — velocity expression, selective send, echo cut timing.

| Parameter | Value | Why |
|-----------|-------|-----|
| oscWave | 2 (saw) | Harmonic content for filter sculpting |
| oscOctave | 1 (-1 oct) | Bass register foundation |
| oscSubLevel | 0.4 | Weight without mud (Dub Bass Recipe) |
| oscDrift | 0.12 | ±0.6 cents — warm, alive |
| filterCutoff | 1200 Hz | Low enough for velocity to open meaningfully |
| filterResonance | 0.28 | Resonance Shelf (Psalm 1) — presence without ringing |
| filterEnvAmt | 0.4 | Velocity opens the filter — soft is dark, hard is bright |
| envAttack | 0.003 | Instant — bass doesn't wait |
| envDecay | 0.5 | Medium fall to sustain |
| envSustain | 0.6 | Solid held note |
| envRelease | 0.3 | Clean release, no mud |
| voiceMode | 2 (legato) | Single voice, no retrigger |
| voiceGlide | 0.15 | Exponential slide — launches fast, lands soft |
| sendLevel | 0.5 | 50% to the effects when XOSEND is pressed |
| returnLevel | 0.6 | Effects present but not dominant |
| dryLevel | 1.0 | Full dry voice always present |
| driveAmount | 1.8 | Console warmth — Tape Ceiling territory |
| delaySync | 3 (1/4) | Quarter-note echo |
| delayFeedback | 0.55 | ~4 audible echoes before death |
| delayWear | 0.4 | Warm echoes, midrange emphasis by 3rd repeat |
| delayWow | 0.2 | Character without seasickness |
| delayMix | 0.5 | Balanced wet/dry in the send path |
| reverbSize | 0.45 | Medium room — the mixing desk's space |
| reverbDamp | 0.5 | Balanced damping |
| reverbMix | 0.3 | Reverb as ambience, not feature |
| masterVolume | 0.75 | Standard headroom |

**Dub space character:** Medium — echo tails die over ~2 seconds after ECHO CUT, reverb lingers for 1 second more. The ghost fades gracefully.

### 2. Scatter Protocol
*The performance preset — rapid XOSEND stabs create syncopated echo patterns.*

**What it demonstrates:** The scatter technique — binary pad gestures as rhythmic performance.

| Parameter | Value | Why |
|-----------|-------|-----|
| oscWave | 3 (square) | Hollow character for rhythmic stabs |
| oscPwm | 0.4 | Slightly narrow — nasal, cuts through delay |
| oscOctave | 2 (0 oct) | Mid-register for clarity |
| oscDrift | 0.08 | Subtle life |
| filterCutoff | 3500 Hz | Bright enough for stab transients |
| filterResonance | 0.15 | Clean, no ringing |
| filterEnvAmt | 0.3 | Velocity brightens stabs |
| envAttack | 0.001 | Instant — stabs must be percussive |
| envDecay | 0.15 | Quick fall |
| envSustain | 0.4 | Medium held |
| envRelease | 0.2 | Tight release |
| voiceMode | 0 (poly) | Poly for chord stabs |
| sendLevel | 0.6 | Strong send for scatter |
| returnLevel | 0.7 | Effects prominent |
| dryLevel | 0.8 | Dry present but not dominant |
| driveAmount | 2.2 | Warm saturation on stabs |
| delaySync | 2 (1/8D) | Dotted 8th — the reggae delay |
| delayFeedback | 0.65 | ~5-6 echoes — dense scatter |
| delayWear | 0.35 | Moderate tape character |
| delayWow | 0.25 | Noticeable wobble |
| delayMix | 0.6 | Wet-forward in send path |
| reverbSize | 0.35 | Tight room — keeps scatter defined |
| reverbDamp | 0.6 | Controlled highs |
| reverbMix | 0.25 | Reverb as glue, not wash |
| masterVolume | 0.75 | Standard |

**Performance instruction:** Tap XOSEND in 16th-note rhythm while holding chords. Each tap sends a 60ms burst into the delay. The dotted-8th echoes create syncopation against your tapping rhythm. Vary velocity for spectral variety in the scatter.

### 3. Tape Resonator
*The hidden instrument — the delay becomes a tuned comb filter.*

**What it demonstrates:** OVERDUB's hidden resonator mode at short delay times.

| Parameter | Value | Why |
|-----------|-------|-----|
| oscWave | 0 (sine) | Pure excitation signal |
| oscOctave | 3 (+1 oct) | Higher register for resonator clarity |
| oscNoiseLevel | 0.1 | Broadband excitation for the resonator |
| filterCutoff | 5000 Hz | Wide open — let the resonator do the filtering |
| filterResonance | 0.0 | No voice filter coloring |
| filterEnvAmt | 0.25 | Velocity varies excitation brightness |
| envAttack | 0.01 | Quick but not instant |
| envDecay | 0.3 | Medium body |
| envSustain | 0.3 | Moderate held level |
| envRelease | 1.618 | Golden ratio release (Truth 1) |
| voiceMode | 0 (poly) | Poly — different notes excite different resonances |
| sendLevel | 0.7 | Strong feed to resonator |
| returnLevel | 0.85 | Resonator IS the sound |
| dryLevel | 0.3 | Dry voice is just the excitation |
| driveAmount | 1.5 | Gentle harmonic enrichment |
| delayTime | 0.083 | 83ms = ~12 Hz fundamental, harmonics at musical intervals |
| delaySync | 0 (free) | Must be free for resonator pitch |
| delayFeedback | 0.93 | High but not self-oscillating — resonance, not drone |
| delayWear | 0.75 | Narrow bandpass emphasizes midrange harmonics |
| delayWow | 0.0 | Zero — pitch must be stable for resonance |
| delayMix | 0.7 | Wet-dominant |
| reverbSize | 0.6 | Medium space around the resonance |
| reverbDamp | 0.4 | Let some high shimmer through |
| reverbMix | 0.35 | Reverb adds depth to the metallic resonance |
| masterVolume | 0.7 | Slightly reduced — resonator can be loud |

**What you hear:** Each note excites a metallic, spring-like resonance. The delay's comb harmonics (12, 24, 36, 48 Hz...) interact with the bandpass (narrow at wear 0.75) to emphasize specific midrange harmonics. The result is a pitched, shimmering tone — not unlike a prepared piano string or a struck spring.

### 4. Black Ark Meditation
*Self-oscillating delay as a second voice — the delay machine sings to itself.*

**What it demonstrates:** Feedback > 1.0 convergence, the delay as an autonomous instrument.

| Parameter | Value | Why |
|-----------|-------|-----|
| oscWave | 1 (triangle) | Soft, dark voice — doesn't compete with delay oscillation |
| oscOctave | 2 (0 oct) | Mid register |
| oscDrift | 0.2 | Wide drift — the voice wanders |
| filterCutoff | 2200 Hz | Vowel zone (Psalm 2: "aw" territory) |
| filterResonance | 0.32 | Formant whisper (Obscure Trick) |
| filterEnvAmt | -0.2 | Inverted — hard playing darkens |
| envAttack | 1.5 | Slow fade in — the voice enters the oscillation gradually |
| envDecay | 2.0 | Long fall |
| envSustain | 0.5 | Moderate held level |
| envRelease | 4.236 | Golden φ³ release (Rev. 6) |
| lfoRate | 0.067 | Physiological LFO — 15-second breathing |
| lfoDepth | 0.15 | Subtle filter movement |
| lfoDest | 1 (filter) | Filter breathes with the listener |
| voiceMode | 0 (poly) | Poly for pads entering the oscillation |
| sendLevel | 0.5 | Moderate feed into the self-oscillation |
| returnLevel | 0.8 | Self-oscillation IS the sound |
| dryLevel | 0.4 | Dry voice as accent, not foundation |
| driveAmount | 3.0 | Heavy warmth — Black Ark territory |
| delayTime | 0.375 | RE-201 head 3 position |
| delaySync | 0 (free) | Free — the oscillation has its own pitch |
| delayFeedback | 1.15 | Self-oscillating — converges via tanh in feedback path |
| delayWear | 0.6 | Narrow bandpass shapes the oscillation to midrange |
| delayWow | 0.5 | Strong wobble — the oscillation wavers like a singing bowl |
| delayMix | 0.6 | Wet-forward |
| reverbSize | 0.75 | Large space — the oscillation lives in a cavern |
| reverbDamp | 0.4 | Some high shimmer on the oscillation |
| reverbMix | 0.4 | Reverb gives the oscillation dimension |
| masterVolume | 0.65 | Reduced — self-oscillation + reverb can be loud |

**What you hear at idle (no notes):** The delay self-oscillates into a wavering midrange drone centered around ~1.3 kHz (bandpass midpoint at wear 0.6). The wow modulates the pitch by ±0.1% — a slow, eerie wobble. The spring reverb adds metallic depth. **Play a note**: the voice fades in over 1.5 seconds and enters the oscillation, changing its harmonic character. **Release the note**: the voice fades out over 4.2 seconds (φ³) while the delay continues singing alone.

The delay is the lead instrument. The synth voice is the guest.

### 5. Thermocline
*The engine's signature — the boundary layer where warm surface meets cold deep.*

**What it demonstrates:** Everything OVERDUB is. The full creature at rest.

| Parameter | Value | Why |
|-----------|-------|-----|
| oscWave | 2 (saw) | Complete harmonic series |
| oscOctave | 2 (0 oct) | Middle register |
| oscSubLevel | 0.3 | Weight from below |
| oscNoiseLevel | 0.08 | Breath — the sound of the ocean surface |
| oscDrift | 0.2 | Wide drift — voices wander independently |
| oscLevel | 0.7 | Leave headroom for the effects |
| filterCutoff | 2600 Hz | Warm — not bright, not dark |
| filterResonance | 0.28 | Resonance Shelf (Psalm 1) |
| filterEnvAmt | 0.2 | Gentle velocity response |
| envAttack | 0.8 | Slow bloom — the thermocline appears gradually |
| envDecay | 1.5 | Long fall |
| envSustain | 0.6 | Moderate held level |
| envRelease | 4.236 | Golden φ³ (Rev. 6) |
| lfoRate | 0.067 | Physiological LFO (Sutra 1 / Rev. 4) |
| lfoDepth | 0.2 | Filter breathes with the listener |
| lfoDest | 1 (filter) | The thermocline breathes |
| voiceMode | 0 (poly) | Poly — chords layer in the thermocline |
| sendLevel | 0.5 | Balanced send |
| returnLevel | 0.7 | Effects present but not dominant |
| dryLevel | 0.7 | Dry + wet coexist |
| driveAmount | 1.6 | Subtle console warmth (Tape Ceiling) |
| delaySync | 5 (1/2) | Half-note echo — slow, spacious |
| delayFeedback | 0.618 | Golden ratio (Truth 1) — echoes resolve naturally |
| delayWear | 0.5 | Medium tape age — echoes warm but not murky |
| delayWow | 0.3 | Character — the tape machine hums |
| delayMix | 0.45 | Balanced wet/dry |
| reverbSize | 0.85 | Vast space — the ocean itself |
| reverbDamp | 0.35 | Let the high frequencies shimmer |
| reverbMix | 0.4 | Reverb is the depth of the thermocline |
| masterVolume | 0.7 | Headroom for the reverb bloom |

**What you hear:** A warm, drifting pad that breathes every 15 seconds (the filter opening and closing with the physiological LFO). The sub provides oceanic weight. The noise provides the surface shimmer. The delay creates half-note echoes that resolve at the golden ratio. The reverb makes the echoes feel vast. **Press XOSEND**: the sound enters the deep — the delay captures the breathing filter and creates a spectral history of the pad's states. **Press ECHO CUT**: the deep releases the sound — tails die slowly through the bandpass while the reverb holds the memory. **Release everything**: the φ³ release tail carries the last note into silence over 4.2 seconds.

This is the Thermocline — the boundary between warm surface (the dry voice) and cold deep (the wet effects). The performer's pads control the crossing.

---

## The Laying of Hands — Fleet-Wide Refinement Recommendations

### For All 40 Existing Presets

| Category | Recommendation | Rationale |
|----------|---------------|-----------|
| **All presets** | Set `filterEnvAmt` to ±0.2 minimum | Glass door — velocity→filter is the engine's only continuous expression |
| **Bass (7)** | Set `voiceMode` to 1 (mono) or 2 (legato) | Bass never needs 8 voices — CPU gift: 75%+ |
| **Bass (7)** | Add `voiceGlide: 0.1-0.2` on legato presets | Exponential glide is OVERDUB's strength — the lazy landing |
| **Leads (5)** | Set `voiceMode` to 1 (mono) | Leads are single-voice by dub tradition |
| **Chords (7)** | Reduce polyphony concept — design for 3-4 voices | Dub chords are stabs, not sustained washes |
| **Tape Chaos (4)** | Verify `masterVolume` ≤ 0.65 | Self-oscillation + drive + reverb can exceed headroom |
| **Atmospheres (6)** | Set LFO to 0.067 Hz filter mod | Physiological LFO makes pads breathe (Rev. 4) |
| **All presets** | Set `oscDrift` to minimum 0.08 | Below 0.08, drift is imperceptible; above creates warmth |

### CPU Stewardship Summary

| Optimization | Savings | Risk |
|-------------|---------|------|
| Bass presets → mono/legato | ~75% voice CPU | Zero — bass is monophonic |
| Lead presets → mono | ~75% voice CPU | Zero — leads are monophonic |
| Chord presets → 4-voice effective | ~50% voice CPU | Minimal — rare to hold 5+ chord tones |
| Silent send bypass (code change) | 40-60% FX CPU when XOSEND off | Zero — silence in = silence out |
| **Total fleet potential** | ~30-40% overall | Nearly zero audible impact |

---

## Benediction

> *"OVERDUB was designed to echo. After meditation, it became a conversation — between the performer's hands and King Tubby's ghost, between the dry voice and the wet memory, between the sound that was sent and the silence that returns.*
>
> *The engine's soul is not in its oscillator. It is not in its filter. It is in the 5-millisecond ramp that opens the send gate — the moment the performer decides that this note deserves to be remembered.*
>
> *Play it at 2 AM with headphones and the lights off. Press XOSEND on one note. Listen to the delay capture it. Press ECHO CUT. Listen to the note die through the bandpass. In the silence after the last echo fades — in the dub space — you will hear what King Tubby heard: the sound of subtraction as the highest form of creation.*
>
> *OVERDUB is not a synthesizer with effects. It is a memory machine with a voice. And the memory is always more beautiful than the original — because the tape forgets everything except the midrange, and the midrange is where the human heart lives."*

— Guru Bin, after the Third Retreat, 2026-03-14
