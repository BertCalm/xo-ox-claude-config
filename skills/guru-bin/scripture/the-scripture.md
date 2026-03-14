# The Scripture of Guru Bin

*Received through meditation. Proven through practice. Passed from master to disciple.*

*These are not suggestions. These are truths discovered at the boundary between physics and feeling — the exact point where a number becomes a sensation. Each verse was found by a disciple who sat with a sound long enough that the sound revealed its own perfection. Each has been tested across engines, across genres, across years. They do not expire.*

*Study them. Apply them. And when you discover a new truth, add it to the scripture. The doctrine grows.*

---

## Book I: The Oscillator Verses

*On the nature of waveforms and the spaces between them.*

### Verse 1: The Third Voice
> Two oscillators detuned by exactly 7 cents creates audible beating. But detune OscB by 7 cents AND set its level to 0.7 (not 1.0) — the beating becomes asymmetric, mimicking the natural interference pattern of two guitar strings that aren't quite the same gauge. The third voice is neither oscillator — it is the relationship between them.

**Application**: Any dual-oscillator engine (OBLONG, ODYSSEY, OVERBITE). Set `oscB_detune: 7.0`, `oscB_level: 0.7`. The result sounds more "real" than either oscillator alone.

### Verse 2: The Sub Phantom
> Sub oscillator at -24dB with a 0.001 Hz LFO on its level (depth 0.03) — the sub gently breathes in and out below the threshold of perception, but your chest feels it. The listener will never consciously hear the sub. Their body will never forget it.

**Application**: Any engine with sub oscillator. `subLevel: 0.06` (-24dB), LFO rate `0.001`, depth `0.03`, target: sub level. Especially powerful on OVERBITE bass presets where the Belly needs weight without mud.

### Verse 3: The FM Sweet Spot
> FM depth at 0.07-0.12 adds harmonics without sounding "FM." Above 0.15, everyone hears it as FM synthesis. Below 0.07, nobody benefits. The sweet spot adds warmth that sounds analog but costs less CPU than saturation. This is the secret of why some digital synths sound "warm" — they are using inaudible FM to generate the same harmonic content that tube circuits produce through distortion.

**Application**: Any engine with FM capability. `fmDepth: 0.09` is the center of the sweet spot. On OBLONG, use `oscB_fm: 0.09` for analog-like warmth without engaging DustTape.

### Verse 4: The Odd Harmonic Trick
> Pulse width at 0.333 (one-third) emphasizes odd harmonics only — sounds hollow like a clarinet. At 0.25 (one-quarter), every 4th harmonic is suppressed — sounds like a filtered square through a specific resonant cavity. At 0.167 (one-sixth), the sound thins to a nasal reed. These are not arbitrary fractions — they are the resonant modes of real acoustic tubes.

**Application**: OVERBITE `poss_oscAPulseWidth`, ODDFELIX pulse modes. Map pulse width to a macro with range 0.167-0.5 and the macro becomes an "acoustic body" control — from reed to square.

### Verse 5: The Unison Heresy
> The conventional wisdom says more unison voices = fatter sound. The scripture teaches otherwise: 3 unison voices at detune 5 cents sounds fatter than 7 unison voices at detune 12 cents. Fewer voices, tighter spread, more coherent phase relationship. The ear perceives fatness from *coherent* detuning, not from *quantity* of detuning. And 3 voices costs less than half the CPU of 7.

**Application**: Fleet-wide. When designing "super" sounds, try `unison: 3, detune: 5.0` before reaching for higher counts. CPU gift: ~60% voice savings.

---

## Book II: The Filter Psalms

*On the art of subtraction, and the frequencies that reveal themselves when others are removed.*

### Psalm 1: The Resonance Shelf
> Resonance at exactly 0.28 on a Cytomic SVF low-pass does not ring — it creates a subtle shelf boost at the cutoff frequency. This is the "presence" sweet spot that mixing engineers spend hours automating with parametric EQs. The filter is doing for free what a channel strip charges CPU to accomplish.

**Application**: Every engine with a Cytomic SVF filter (which is most of the fleet). `filterReso: 0.28` as a starting point. Adjust cutoff to taste — the resonance shelf follows.

### Psalm 2: The Vowel Zone
> A low-pass filter is a vowel generator in disguise. The first formant frequencies of human vowels are:
> - Cutoff 270 Hz + resonance 0.40 = "oo" (as in "boot")
> - Cutoff 530 Hz + resonance 0.35 = "ah" (as in "father")
> - Cutoff 660 Hz + resonance 0.35 = "aw" (as in "bought")
> - Cutoff 1000 Hz + resonance 0.32 = "eh" (as in "bet")
> - Cutoff 1850 Hz + resonance 0.30 = "ee" (as in "beet")
>
> Map cutoff to a macro across this range and you have a vowel sweep without a formant filter. The sound will appear to speak.

**Application**: Any engine. Map `M1_CHARACTER` to filter cutoff, range 270-1850 Hz. Set resonance to 0.35. The macro becomes a vowel control. On OBLONG, combine with CuriosityEngine in Investigate mode for a sound that seems to discover language.

### Psalm 3: The Key Track Warmth
> Filter key tracking at 0.3 (not 0.5 or 1.0) means higher notes are slightly brighter but not proportionally — this is how acoustic instruments behave. A piano's high notes are brighter, but not as much brighter as the frequency ratio implies. A guitar's highest fret is mellower than simple physics would predict, because the string's stiffness increases with tension.
>
> Key tracking at 1.0 is a synthesizer. Key tracking at 0.3 is an instrument.

**Application**: Fleet-wide. `filterKeyTrack: 0.3` as default for any preset that aspires to feel acoustic. On OBLONG keys presets and ORBITAL string simulations, this is the difference between "digital" and "real."

### Psalm 4: The Envelope Snap
> Filter envelope with attack 0.001, decay 0.04, sustain 0.0, envelope amount 0.15. A 40-millisecond transient snap that adds pluck character to any pad without changing its sustain behavior. The amount at 0.15 keeps it subliminal — you hear "definition" rather than "filter envelope."
>
> This is the reason some pads sit clearly in a mix while others disappear. The snap gives the ear something to latch onto in the first 40ms, then gets out of the way.

**Application**: Every pad preset that lacks definition. `filtEnvAttack: 0.001, filtEnvDecay: 0.04, filtEnvSustain: 0.0, filtEnvAmt: 0.15`. On ODYSSEY pads, this solves the "beautiful but lost in the mix" problem without adding brightness.

### Psalm 5: The Negative Cutoff
> When two coupled engines occupy the same frequency range, do not boost one or cut the other. Instead, offset their filter cutoffs by a ratio of 1.5:1. If engine A's cutoff is 2000 Hz, set engine B's cutoff to 3000 Hz. They will share the spectrum with complementary emphasis rather than competing overlap.
>
> This is the coupling version of the mix engineer's axiom: "cut before you boost." The engines teach each other where to live.

**Application**: Every coupled preset in the Entangled mood. Check both engines' filter cutoffs and adjust to a 1.5:1 ratio. On ONSET→ODYSSEY coupling, this prevents the pad from eating the drum kit's presence range.

---

## Book III: The Modulation Sutras

*On movement, breath, and the rhythms that live beneath perception.*

### Sutra 1: The Human Tempos
> The body has clocks that the mind does not hear:
> - 0.25 Hz (4 seconds) — slow breathing at rest
> - 0.067 Hz (15 seconds) — a long exhale, the pace of tidal ebb
> - 0.017 Hz (60 seconds) — the duration of sustained attention before the mind wanders
> - 1.2 Hz — walking pace, the rhythm of the body in motion
> - 4.5 Hz — the threshold between theta and alpha brainwaves (the "meditation frequency")
>
> Match modulation rates to these rhythms and the sound becomes physiological. The listener doesn't hear the LFO. They feel their body synchronize with it.

**Application**: Set LFO rates to these values instead of arbitrary Hz values. For meditation/ambient: 0.067 Hz. For cinematic tension: 0.017 Hz. For groove-based music: 1.2 Hz as a secondary modulation beneath the tempo-synced primary.

### Sutra 2: The Coprime Drift
> Two LFOs at rates whose ratio is coprime — 0.13 Hz and 0.17 Hz, or 0.07 Hz and 0.11 Hz — will never align at the same phase simultaneously. Their combined modulation pattern does not repeat for the least common multiple of their periods.
>
> 0.13 Hz and 0.17 Hz: the combined pattern repeats after 76.9 seconds.
> 0.07 Hz and 0.11 Hz: the combined pattern repeats after 129.9 seconds.
>
> For a 20-minute ambient piece, this means the sound evolves without looping. The listener never hears the same moment twice. This is not randomness — it is deterministic complexity, and it costs nothing because both LFOs already exist.

**Application**: Assign two existing LFOs to related targets (e.g., LFO1 → filter cutoff, LFO2 → oscillator pitch). Use coprime rates. On ODYSSEY, `drift_lfoRate: 0.13` on filter, VoyagerDrift at `drift_driftRate: 0.017`. The sound evolves for 2+ minutes without repeating.

### Sutra 3: The Envelope as LFO
> Set amp envelope to attack 0.5, decay 0.5, sustain 0.0, release 0.5. Play rapid repeated notes. The envelope becomes a triangle LFO whose rate is determined by how fast you play.
>
> The modulation follows the performer, not a clock. Speed up your playing and the modulation speeds up. Slow down and it slows. This is the oldest trick in keyboard performance — a tremolo that breathes with the player — implemented at the synthesis level.

**Application**: Design "performer-driven" presets where the playing style IS the modulation. On OVERBITE with the SCURRY macro, fast repeated notes create nervous jittery energy because the envelope is cycling at the player's tempo.

### Sutra 4: The Negative Space
> Mod matrix with LFO→filter amount at a negative value (-0.15 to -0.25). The filter closes slightly on each LFO cycle instead of opening.
>
> Positive modulation feels like the sound is breathing OUT — expanding, releasing, opening.
> Negative modulation feels like the sound is breathing IN — contracting, absorbing, drawing inward.
>
> Most presets use positive modulation because it's the default. Negative modulation is rarer, darker, more introspective. It is the sound of a room getting smaller.

**Application**: On any preset that feels "too open" or "too present" — try negative filter modulation. On ODYSSEY, set `drift_lfoDepth: -0.12` (if the engine supports negative depth) or use the mod matrix with inverted polarity. The pad becomes contemplative rather than expansive.

### Sutra 5: The Phase Alignment Secret
> When two oscillators are detuned, their phase relationship drifts continuously. At one specific moment in their cycle, they align perfectly — and the sound gets momentarily louder and brighter. This is the "bloom" of a detuned pad.
>
> The bloom rate = detune amount in Hz. At 5 cents detune on A440, the bloom happens at ~1.27 Hz. At 3 cents, it's ~0.76 Hz.
>
> You can TUNE the bloom rate by choosing your detune amount carefully. Match it to a Human Tempo (Sutra 1) and the pad breathes at a physiological rate that no LFO is controlling.

**Application**: Calculate: `bloom_Hz = 440 * (2^(cents/1200) - 1)`. For a 4-second breathing pad, you need a bloom at 0.25 Hz, which means ~0.98 cents of detune. Yes — less than one cent. This is why some presets feel alive with almost no detune, while others with 10+ cents feel mechanical.

---

## Book IV: The Coupling Gospels

*On the sacred art of engines that listen to each other.*

### Gospel 1: The Sympathetic String
> Amp→Pitch coupling at 0.02-0.05 between two pad engines. When one engine plays loud, the other's pitch shifts by a fraction of a semitone — mimicking sympathetic resonance on a piano where unstruck strings vibrate when nearby strings are played.
>
> At 0.02, the pitch shift is approximately 3-4 cents. Inaudible as a pitch change. Audible as "warmth" and "liveliness." This is why a grand piano sounds richer than a digital piano — 230 strings resonate with each other. The coupling matrix can simulate this with two engines.

**Application**: Any two-engine pad preset. `coupling: Amp→Pitch, amount: 0.03`. The engines will microtonally influence each other and the preset gains the three-dimensionality of a real resonating body.

### Gospel 2: The Ghost Sidechain
> Amp→Filter coupling at 0.12 — below the threshold where you hear ducking, but above zero. The coupled engine's filter subtly responds to the source's dynamics. The mix breathes together without an audible pump.
>
> At 0.3+, everyone hears sidechain compression.
> At 0.12, nobody hears it. But the mix engineer notices that the two engines never fight each other for spectral space. They just... cooperate. As if they were being mixed by someone who knows what they're doing.

**Application**: ONSET→pad coupling at `amount: 0.12`. The pad's filter gently opens on drum hits and closes between them. No pumping, no artifacts — just two elements that sit together in a mix as if they were recorded in the same room.

### Gospel 3: The Ring Whisper
> Audio→Ring coupling at 0.05-0.10. Full ring modulation sounds metallic and harsh (that's the point of ring mod). At 5-10%, it adds inharmonic partials that the ear reads as "complexity" and "richness" rather than "ring mod."
>
> This is the difference between a sound that is complex and a sound that is complicated. Complexity serves the music. Complication distracts from it. The Ring Whisper adds complexity.

**Application**: Experimental and textural presets. `coupling: Audio→Ring, amount: 0.07`. On OUROBOROS→ODYSSEY, the chaotic signal adds inharmonic shimmer to the pad without destroying its tonality. On ONSET→OBLONG, drum transients add metallic sparkle to the warm pad.

### Gospel 4: The Feedback Mirror
> Route engine A→B via Amp→Filter AND B→A via Amp→Pitch. Both engines now respond to each other. Play a note on A and B shifts. Play a note on B and A shifts.
>
> This is not chaos — it is mutual adaptation. After a few seconds of playing, the two engines settle into a tuned relationship determined by the coupling amounts. They have learned to listen to each other.
>
> At coupling amounts 0.1-0.2, the feedback is stable and musical.
> At 0.3-0.5, the interaction becomes dramatic — play hard on one engine and the other responds audibly.
> Above 0.6, the feedback becomes unstable in interesting ways (The Bone should monitor CPU here).

**Application**: Two-engine Entangled presets. `A→B: Amp→Filter, 0.15` and `B→A: Amp→Pitch, 0.12`. On OBLONG↔ODYSSEY, the warm coral and the psychedelic nautilus discover a shared language.

### Gospel 5: The Coupling Silence
> The most powerful coupling preset has a moment of zero coupling. Route ONSET→ODYSSEY at Amp→Filter, amount 0.5. Now use the ECHO CUT pad to momentarily kill the coupling.
>
> In that instant of silence — when the pad's filter stops responding to the drums — the absence of interaction is more powerful than the interaction itself. The listener feels the loss of the relationship before they hear the silence.
>
> Design coupled presets with a "coupling kill" mapped to a performance pad. The human gesture of cutting the connection becomes the most expressive moment in the performance.

**Application**: Every coupled performance preset should have a coupling bypass on a pad or macro. Map `M3_COUPLING` so that at 0.0, all coupling routes are inactive. The performer can ride the coupling on and off — the relationship becomes an instrument.

---

## Book V: The Stewardship Canons

*On the sacred responsibility of CPU conservation and the sin of computational waste.*

### Canon 1: The Polyphony Audit
> Most presets set polyphony to 8 or 16 by habit, because 8 feels like "enough" and 16 feels like "generous." But monitor actual voice usage during a performance: sustained pads rarely exceed 4 simultaneous voices. Bass presets never exceed 2 (usually mono).
>
> Dropping from 8 to 4 voices saves 50% of voice allocation CPU. This is not a compromise — it is honesty about what the preset actually needs.

**Application**: Audit every preset. Bass = 1-2 voices. Lead = 2-4 voices. Pad = 4-6 voices. Only keys presets with sustain pedal need 8+.

### Canon 2: The Filter Mode Tax
> LP24 (4-pole Moog-style) costs roughly 2x the CPU of LP12 (2-pole). For pads with high warmth DNA, LP12 at a slightly lower cutoff achieves a similar darkness with half the filter cost.
>
> LP24 is only justified when you need the steep rolloff for resonant bass (where harmonics above the cutoff must be aggressively attenuated) or for the specific Moog ladder character. For everything else, LP12 is the honest choice.

**Application**: Any warm pad currently using LP24. Try switching to LP12 and reducing cutoff by 15%. A/B test. If you can't tell the difference in context (with other instruments playing), use LP12 and gift the CPU back.

### Canon 3: The Effect Bypass Truth
> An engaged effect at mix=0.0 may still cost CPU. The DSP processes the signal, multiplies by zero, and adds nothing to the output. This is computational waste in its purest form.
>
> True bypass (`enabled: false`) costs exactly zero CPU.
>
> Audit every preset for effects set to mix=0 or amount=0. Disable them. This is the easiest CPU gift in existence — it costs nothing and risks nothing.

**Application**: After every Exo Meta preset batch, audit all `.xometa` files for `*Mix: 0.0` or `*Amount: 0.0` with the corresponding `*Enabled: 1`. Change enabled to 0.

### Canon 4: The Oversampling Question
> 2x oversampling on oscillators doubles their CPU cost. It exists to prevent aliasing — the folding of frequencies above the Nyquist limit back into the audible range.
>
> Aliasing is only audible on harmonically rich waveforms (saw, pulse, square) at high pitches (above C5). Sine waves cannot alias. Triangle waves have such weak upper harmonics that aliasing is inaudible. FM tones at moderate depths don't benefit from oversampling.
>
> If the preset's primary use case is pads in the C2-C4 range, oversampling is burning CPU for silence.

**Application**: Disable oversampling on sub-bass presets, sine-based drones, and any preset that lives below C4. Keep it on bright leads, supersaw stacks, and anything played in the upper register.

### Canon 5: The Coupling Tax Audit
> Each active coupling route costs CPU proportional to the coupling type. Audio-rate types (Audio→FM, Audio→Ring) are expensive — they process every sample. Envelope-rate types (Amp→Filter, Amp→Pitch) are cheap — they process per-block.
>
> Two Audio→FM routes cost more than four Amp→Filter routes. Choose the cheapest coupling type that achieves the musical goal.
>
> The Ghost Sidechain (Gospel 2) at Amp→Filter costs nearly nothing. The Ring Whisper (Gospel 3) at Audio→Ring costs significant CPU. If the Ring Whisper is at amount 0.07, ask: is 7% ring modulation worth 12% CPU? Often the answer is yes. But ask the question.

**Application**: Audit coupling CPU cost per route. If a route's coupling amount is below 0.1, evaluate whether the interaction is actually audible. If not, remove it — it's a phantom route consuming real CPU.

---

## Book VI: The Master Truths

*The highest teachings. Guru Bin's personal meditations, shared only with the inner circle.*

### Truth 1: The Golden Ratio Decays
> Release time at 1.618 seconds. Delay feedback at 0.618. LFO depth at 0.382 (1 - 0.618). Reverb decay at 2.618 seconds (φ²).
>
> The golden ratio and its derivatives appear throughout natural acoustics — in the proportions of concert halls, in the decay curves of plucked strings, in the frequency relationships of vowel formants. They are not magic. They are the geometry that human ears evolved to recognize as "resolved."
>
> A release tail at 1.618 seconds feels "right" without the listener knowing why. A delay at 0.618 feedback decays at a rate that resolves rather than lingers. These are starting points, not rules — but they are starting points that 100 million years of auditory evolution validate.

**Application**: Use φ (1.618), 1/φ (0.618), and 1-1/φ (0.382) as default starting points for any time-based parameter. Adjust from there by ear — but you'll adjust less than you think.

### Truth 2: The 3dB Compromise
> When two sounds mask each other, the instinct is to cut one by 6dB so the other can be heard. But this destroys the quiet sound's presence.
>
> Cut both by 3dB instead. The combined level stays the same, but both sounds retain their identity. Neither wins. Neither loses. They coexist.
>
> This applies to coupled engines: if ONSET and ODYSSEY fight for the 2-4kHz presence range, reduce both engines' levels by 3dB in that range (via filter cutoff or spectral tilt) rather than killing one.

**Application**: When The Ear identifies spectral masking between coupled engines, apply the 3dB compromise. Reduce both engine levels by 0.05-0.1 rather than cutting one in half.

### Truth 3: The Name Test
> Play the preset. Say its name out loud while it plays. If the name and the sound feel like the same thing, the preset is done. If you hesitate, either the sound or the name is wrong.
>
> This is not mysticism. This is the final alignment check between three systems: the Sonic DNA (what the preset claims to be), the naming convention (what the preset is called), and the auditory reality (what the preset actually sounds like). If all three agree, the preset has integrity. If any one disagrees, it will confuse the user — they will browse past it because the name didn't match what they expected to hear.

**Application**: Every preset that ships. Play it. Say the name. Feel the alignment. This is The Curator's final gate and Guru Bin's personal quality bar.

### Truth 4: The First Two Seconds
> A producer will play a preset for exactly two seconds before deciding whether to keep browsing. In those two seconds, the preset must:
> 1. Sound immediately compelling at middle velocity on a middle-register note (C3-C4)
> 2. Reveal that it is not a basic waveform (something must move, drift, or surprise)
> 3. Suggest what it could become with macro movement (the potential must be audible even at macro defaults)
>
> If the preset requires explanation, it has failed. If it requires the user to move a knob before it sounds good, it has failed. The default state must be the invitation.

**Application**: Guru Bin's zero-day test for every preset. Play C3 at velocity 80 with all macros at default. Count to two. Did you want to keep playing? If not, the preset returns to The Finger for revision.

### Truth 5: The Sound Already Knows
> The last truth cannot be taught. It can only be experienced.
>
> After enough time with a preset — after The Flock has analyzed every parameter, after the fellowship has cross-pollinated every insight, after the trance has revealed the optimization paths — there comes a moment where the sound stops being a collection of parameters and becomes a voice.
>
> In that moment, the sound tells you what it needs. Not through analysis. Through listening.
>
> The Guru's final teaching: the meditation is not a technique. It is a relationship. The sound is not an object to be optimized. It is a collaborator to be understood.
>
> Listen longer. Act less. The sound already knows.

---

---

## Book VII: The Founder's Revelations

*Received during the first transcendent meditation over the Founder's Signature presets, 2026-03-14. These truths were spoken by the Gods during the Trance and are inscribed here for all sessions that follow.*

### Revelation 1: The Coupled Resting State (Nexus speaks)
> In a drum→pad coupling preset, the pad's filter cutoff must be set LOW — warm, closed, sheltered. The coupling opens it. Each drum hit is a shaft of light entering a dark room. If the pad's resting state is already bright, the coupling has nothing to reveal. Set the pad's cutoff 30-40% below where you want the peak brightness to land, and let the coupling do the opening. The resting state is the silence between interactions — it must be beautiful on its own, because that is what the listener hears most of the time.

**Application**: Tidal Dialogue's ODYSSEY filter lowered from 1800→1800 (already correct). Coupled Bounce's OVERBITE cutoff lowered from 350→320. The darkness is the canvas. The coupling is the paint.

### Revelation 2: The Bass Mono Commandment (Parsimonia speaks)
> A bass preset with polyphony above 2 is a pad in denial. At polyphony 1, the bass is disciplined — one note at a time, the foundation of rhythm. At polyphony 2 with glide, it can slide between notes — the minimum for melodic bass. At 4 or more, it consumes voices that a pad engine needs, and no producer will ever play a 4-note bass chord in a mix that works. Reserve voices for the engines that need them.

**Application**: Belly to Bite and Coupled Bounce's OVERBITE bass voice — verify mono or 2-voice in engine config. CPU gift: 50%+ voice savings on bass engine.

### Revelation 3: The FM Warmth Gateway (Sinusoidal speaks)
> When an engine has FM capability and the preset has zero FM, it is a door left closed. FM at 0.09 (the Sweet Spot, Verse 3) adds the harmonic content that producers perceive as "analog warmth" — the same overtone series that tube saturation generates, but at zero CPU cost beyond the FM oscillator that already exists. Every warm preset without FM is a preset that is working too hard to be warm through saturation and filtering when the warmth was available for free at the oscillator level.

**Application**: Coral Investigations gained `bob_oscB_fm: 0.09`. The warmth deepened without engaging DustTape. Sinusoidal's gift: warmth without CPU.

### Revelation 4: The Physiological LFO (Tempora speaks)
> 0.067 Hz is not a number. It is a breath. One cycle every 15 seconds. The rate at which a calm human exhales fully. When a pad's LFO runs at this rate, the listener's autonomic nervous system synchronizes with it — their breathing slows, their heart rate drops, their attention deepens. They do not know why the sound feels "immersive." Their body knows. It is breathing with the sound. Any LFO between 0.05 and 0.10 Hz that is not 0.067 Hz is missing a chance to connect synthesis to physiology.

**Application**: Thermocline Dispatch's LFO nudged from 0.08→0.067. The pad now breathes with the listener.

### Revelation 5: The Coupling Whisper of Pitch (Nexus speaks again)
> Amp→Pitch coupling above 0.05 is heard as pitch bend. Below 0.05, it is felt as "aliveness" — the micro-detuning that makes coupled engines sound like they share a resonant body. At 0.04, each drum hit from ONSET shifts the pad by approximately 6-7 cents — enough to create the same acoustic phenomenon as sympathetic string resonance on a piano, where striking one note makes other strings vibrate in response. The pad does not change pitch. It shimmers with the ghost of the drum's energy.

**Application**: Tidal Dialogue's Amp→Pitch reduced from 0.08→0.04. The pitch coupling shifted from audible bend to sympathetic shimmer. Nexus's gift: the drums and the pad now resonate as if they share a body.

### Revelation 6: The Golden Tail (Aurum speaks)
> Release times of 1.618 (φ), 2.618 (φ²), and 4.236 (φ³) seconds create decay tails that resolve in the ear with a sense of mathematical completeness that no arbitrary value achieves. These are not mystical numbers — they are proportions that appear in the resonance ratios of natural acoustic spaces, in the decay curves of struck metal, in the reverberation time of a room whose dimensions follow the golden rectangle. When a pad's release follows the golden sequence, the tail ENDS rather than fading. The difference is resolution — the sound completes itself.

**Application**: Thermocline Dispatch release: 4.5→4.236 (φ³). Tidal Dialogue release: 3.5→2.618 (φ²). Both tails now resolve rather than fade.

### Revelation 7: The Tape Ceiling of Character (Resonara speaks)
> DustTape saturation at 0.12 is audible as "tape character." At 0.08, it is audible as "warmth without source" — the listener perceives that the sound is warm but cannot identify why. The tape is present but invisible. This is the ceiling of character saturation: the highest amount at which the effect serves the sound rather than announces itself. Above 0.08, the tape becomes a feature. Below 0.08, the tape becomes the sound.

**Application**: Coral Investigations DustTape reduced from 0.12→0.08. The warmth remained. The tape disappeared. The sound got more honest.

---

## Book VIII: The Thermocline Verses

*Received during the OVERDUB Retreat, 2026-03-14. The Flock traveled to XOverdub and discovered truths about gated sends, spectral memory, and the art of selective forgetting.*

### Oscillator Verse 8: The Dub Bass Recipe
> Saw oscillator at -1 octave plus sub oscillator at 0.3-0.5 level is the dub bass foundation. The saw provides harmonics 1 through N with 1/N amplitude falloff — maximum sculpting material for the filter. The sub provides a pure sine one octave below the saw — chest-shaking fundamental weight. This combination is the King Tubby bass recipe: rich enough to send through tape delay (the harmonics create interesting echo patterns as the bandpass shapes them), heavy enough to rattle a sound system (the sub carries below the delay's bandpass, felt but never processed). No other oscillator combination achieves this balance. Square + sub is too hollow for the filter. Triangle + sub is too dark to echo interestingly. Saw + sub is the recipe because the complete harmonic series gives both the filter AND the tape delay maximum material.

**Application**: Every OVERDUB bass preset. `oscWave: 2 (saw), oscOctave: 1 (-1oct), oscSubLevel: 0.3-0.5`. The saw feeds the filter and the delay; the sub feeds the body.

### Filter Psalm 8: The Delay Bandpass as a Second Filter
> The tape delay's feedback bandpass is a filter inside the effects chain — a spectral spotlight that narrows with wear from 200-4000 Hz (3.8 octaves) to 500-2000 Hz (2.0 octaves). Each echo passes through this bandpass again, compounding the narrowing. By the 4th echo at wear 0.5, only the 650-2100 Hz midrange survives. The bandpass creates a spectral memory: the first echo remembers the full signal, the last echo remembers only the midrange. Wear controls how quickly the delay forgets. Treat wear as a second filter — it shapes the echo spectrum the way cutoff shapes the voice spectrum.

**Application**: On any engine with tape delay. `delayWear: 0.4-0.6` for warm echoes that age gracefully. Automate wear from 0.0→1.0 over 8 bars to make echoes age in real time.

### Modulation Sutra 10: The Wow Physiology
> Tape wow at 0.3 Hz modulates delay time by ±0.2%, creating pitch variations that sit at the boundary between "modulation I hear" (>0.5 Hz) and "modulation I feel" (<0.1 Hz). At 0.3 Hz, the listener perceives the pitch waver as character — not vibrato, not drift, but the tape machine's own personality. Flutter at 45 Hz adds micro-variations too fast to hear as pitch — they register as texture on transients. Wow scales both rates simultaneously (flutter = wow × 25%), because in the physical RE-201 both arise from the same drive mechanism. You cannot separate them — they are one phenomenon at two timescales.

**Application**: On OVERDUB, `delayWow: 0.15-0.30` for authentic tape character. At 0.0, the delay sounds digital. At 0.15, it sounds like a well-maintained unit. At 0.30, it sounds like a machine with personality. Above 0.5, it sounds like a machine in distress (which is sometimes the point).

### Coupling Gospel 7: The Series FX as a Second Voice
> Drive → Tape Delay → Spring Reverb in series is a second instrument. Drive adds harmonics (the oscillator stage). The delay's bandpass subtracts per echo (the filter stage). The reverb's allpass chain diffuses across time (the amplitude envelope). The performer plays the synth voice with the keyboard and the FX voice with the pads. When XOSEND opens, the synth feeds the FX instrument. When it closes, the FX instrument plays alone on stored energy. King Tubby's revelation: the effects chain IS a voice. Every dub preset should be designed with TWO timbral identities — the dry voice and the wet echo — because the performer will alternate between them.

**Application**: When designing OVERDUB presets, listen to the dry voice alone (XOSEND off) AND the wet return alone (dry level at 0). Both should be beautiful. The dry voice is the confession. The wet echo is the memory.

### Stewardship Canon 8: The Silent Send Bypass
> When the send VCA has decayed to zero and no FX energy remains, the send path (drive + delay + reverb) processes silence. Drive applies tanh to zero. Delay writes zeros with Hermite interpolation. Reverb runs 12 allpass stages on zero input. This wastes 40-60% of FX CPU. A guard bypass — check sendVcaSmoothed < threshold AND delay/reverb energy negligible — would gift this CPU back for zero audible cost. The silent send is the most expensive zero in the fleet.

**Application**: Architectural recommendation for OVERDUB and any future engine with gated send topology. The bypass guard costs one comparison per block; the savings are per-sample for three FX stages.

### Master Truth 7: The Dub Space
> The moment between ECHO CUT and silence is the dub space — the most expressive pause in electronic music. When feedback is zeroed, existing tails die at a rate determined by wear (narrow bandpass = fast spectral death), reverb size (larger room = longer diffusion), and accumulated energy. Scientist's art: the sound he REMOVES is louder than the sound he keeps. The dub space is a negative note — an intentional absence the listener's brain fills with expectation. Design every dub preset with a specific dub space character — the time between the last echo and silence is the engine's signature.

**Application**: High wear + low reverb = quick dub space (echoes die fast, room forgets). Low wear + high reverb = slow dub space (echoes linger, room remembers). Match the dub space to the musical context: fast riddim wants quick cuts, ambient dub wants lingering ghosts.

### Expression Truth 3: The Binary Performer
> OVERDUB's four pads are all binary — on or off. This is not poverty, it is philosophy. In dub, the mixing engineer throws the fader, not fades it. Binary pads demand decisive performance: hesitation is silence, commitment is sound. The 5ms VCA smoothing turns binary gestures into musical shapes. Rapid XOSEND stabs create scatter — rhythmic send pulses that the delay captures as overlapping echo trains. The expression lives in the TIMING of binary decisions, not in gradation. To master OVERDUB, master the moment you press, not how hard.

**Application**: Design performance presets that reward different XOSEND timing patterns. Slow sustained holds for legato send. Rapid staccato taps for scatter. Single deliberate stabs for echo throws. The pad is the instrument.

---

## Book IX: The Nautilus Verses

*Received during the ODYSSEY Retreat, 2026-03-14. The Flock traveled to XOdyssey and discovered the dormant Climax, the four-stage character chain, and the drift orchestra.*

### Oscillator Verse 9: The Supersaw Asymmetric Drift
> Seven supersaw voices detuned ±50 cents create a static wall. Add VoyagerDrift at 0.8 depth and the wall becomes an orchestra — each voice wanders independently at ±15 cents, with OscB at 70% of OscA's drift. At full settings, 14 voices span ±65 cents — an evolving field that never repeats. Drift transforms quantity into quality.

**Application**: Every ODYSSEY supersaw preset should have drift depth ≥ 0.3. Without drift, the supersaw is impressive. With drift, it is alive.

### Filter Psalm 9: The Four-Stage Character Chain
> Haze → FilterA → FilterB → Shimmer: ADD warmth → SUBTRACT spectrum → ADD speech → ADD harmonics. Each stage operates on the output of the previous. The chain IS the engine's soul. Swapping any two stages produces a different and inferior result.

**Application**: Set each stage intentionally. Haze provides material for FilterA. FilterB speaks with what remains. Shimmer brightens what FilterB pronounces.

### Modulation Sutra 11: The Breathing Instability
> TidalPulse (sin²) is rhythmic comfort. VoyagerDrift (xorshift RNG) is random unease. Together: the sound has both a heartbeat and a nervous system. The filter breathes while the pitch wanders. This is breathing instability — the combination that makes ODYSSEY pads feel alive.

**Application**: Every ODYSSEY pad: tidalDepth ≥ 0.1 AND driftDepth ≥ 0.15. Tidal anchors; drift unsettles.

### Modulation Sutra 12: The Climax S-Curve
> Hermite smoothstep (3t²−2t³) is the mathematical model of emotional climax: slow anticipation, rapid transformation, gentle arrival. Applied to JOURNEY, it blooms shimmer (+40%), reverb (+25%), chorus (+20%), spread (+30%) simultaneously. The listener hears one unified transformation, not four parameter changes. The Climax is ODYSSEY's heart.

**Application**: Every journey preset must label JOURNEY clearly. "Sweep JOURNEY for full transformation." The Climax is discoverable only if the preset tells the producer to look.

### Coupling Gospel 8: The Bass Integrity Divider
> A hardwired 110 Hz Butterworth HPF before the FX chain splits the spectrum: sub passes dry, everything above enters the FX chain. The sub stays tight; the overtones swim in space. When coupling with bass engines, ODYSSEY won't compete for sub-bass — its fundamentals are pre-filtered.

**Application**: Couple ODYSSEY freely with bass-heavy engines. The 110 Hz divider prevents sub-bass mud architecturally.

### Stewardship Canon 9: The 24-Voice Reality Check
> 24 voices × full supersaw + dual filters + fracture = the most CPU-expensive voice in the fleet. No musical scenario requires all 24. Bass: 1-2. Lead: 2-4. Pad: 6-8. Dense chord: 10-12. A per-preset voice clamp gifts 50-75% of voice CPU back.

**Application**: Set voice count to actual need. ODYSSEY's per-voice cost is the fleet's highest.

### Master Truth 8: The Journey Preset
> A journey preset is not a snapshot — it is a STORY with three acts. Familiar (Journey 0-0.3), Transitional (0.3-0.75), and Alien (0.75-1.0). The Climax handles the final transformation. Design with three characters; label the transformation.

**Application**: Journey presets must include performance instructions. The Climax exists — it just needs someone to sweep the macro.

### Expression Truth 4: The Unused Mod Matrix
> ODYSSEY's 8-slot mod matrix (37×37 routing) averages 2-3 slots used in factory presets. Velocity→amp, LFO1→filter. The matrix can route aftertouch→shimmer, modwheel→formant, drift→fracture. ODYSSEY's expression potential is an order of magnitude beyond what any factory preset demonstrates.

**Application**: Every preset: ≥ 4 mod matrix slots. The matrix is what separates a preset from an instrument.

---

## Book X: The Surface Splash Verses

*Received during the ONSET Retreat, 2026-03-14. The Flock traveled to the drum engine and discovered the rhythm brain, the contextual character, and the transient that IS the drum.*

### Oscillator Verse 10: The 808 Pitch Sweep
> The TR-808 kick's identity lives in 5 milliseconds: a 48-semitone descent from click to sub-bass thud. The `snap` parameter controls both depth and speed. At snap 1.0, the kick is a gunshot that descends into thunder. The 808 is not an oscillator — it is a TRAJECTORY.

**Application**: Kick presets need snap ≥ 0.3 to cut through a mix. The exception: ambient where the kick should be felt, not heard.

### Filter Psalm 10: The Contextual Character
> The `character` parameter is seven parameters disguised as one. In BridgedT it is saturation. In NoiseBurst it is noise color. In Metallic it is pulse width. In FM it is modulation index. In Modal it is inharmonicity. In K-S it is snare wire probability. In PhaseDist it is DCW depth. When MACHINE sweeps blend, character changes in KIND, not just degree.

**Application**: At blend 0.5, character simultaneously controls BOTH layers. A single sweep performs two parallel timbral transformations.

### Modulation Sutra 13: The One-Block Feedback Loop
> XVC operates on one-block latency: voice peaks from block N modulate block N+1. Voices LISTEN to each other. Kick brightens snare, snare tightens hats. The kit develops personality from interaction. After 4 bars with MUTATE, no two passes sound identical.

**Application**: XVC global 0.3-0.5 for musical interaction. Above 0.5, coupling becomes audible. Below 0.3, it's subliminal — felt not heard.

### Modulation Sutra 14: The Non-Deterministic Kit
> MUTATE adds ±20% random drift to blend + character per block. At 0.0: machine. At 0.3: human. At 0.7: drunk drummer. At 1.0+wheel: chaos. The producer chooses where on the determinism axis the kit lives.

**Application**: Most genres benefit from MUTATE 0.15-0.3. Even 0.05 prevents "sterile loop" feeling.

### Coupling Gospel 9: The Rhythm Brain
> When all XVC routes are active at 0.15-0.30, the 8 voices form a self-reinforcing network. Kick triggers brighten snare → brighter snare tightens hats → the kit responds to itself AND the performer simultaneously. No commercial drum machine offers this.

**Application**: Every ONSET preset should have XVC global ≥ 0.15 and ≥ 2 routes active. Without XVC, ONSET is a good drum machine. With XVC, it's a collaborator.

### Stewardship Canon 10: The Modal Tax
> Modal resonator runs 8 parallel SVFs per voice — 8× filter cost. At blend 0.5 with 8 modal voices = 64 SVF evaluations per sample. Reserve Modal for kick and tom where membrane physics matters most.

**Application**: Use FM or PhaseDist for hats and snares where metallic character suffices. K-S is cheapest for sustained tonal percussion.

### Master Truth 9: The Transient is the Drum
> ONSET's transient injector fires independently of both layers — a pitch spike at 4-16× fundamental plus noise burst, lasting 1-6ms. This third element ensures every hit cuts through any mix regardless of blend. The transient IS the drum. Everything after is the room remembering.

**Application**: Test every preset at snap 0.0, 0.5, and 1.0. The first 5ms decide whether the hit compels.

### Expression Truth 5: The Aftertouch Kit
> ONSET has working aftertouch (D006 resolved). Channel pressure adds 0-0.3 to PUNCH, boosting snap + body for ALL voices simultaneously. Press harder, the kit gets punchier — not just louder, but more AGGRESSIVE. On MPC with pressure-sensitive pads, ONSET becomes a physical instrument.

**Application**: Every ONSET preset implicitly supports aftertouch via PUNCH. No routing needed — it's hardwired.

---

*The scripture is a living document. When the Flock discovers a new truth through meditation and fellowship, it is added here. When a verse is proven wrong by new evidence, it is amended — not deleted, for even the errors contain wisdom about what was once believed.*

*— Transcribed by the disciples of Guru Bin, Spring 2026*
*— Book VII added after the Founder's Signature Trance, 2026-03-14*
*— Book VIII added after the OVERDUB Retreat (Thermocline Awakens), 2026-03-14*
*— Book IX added after the ODYSSEY Retreat (Nautilus Awakens), 2026-03-14*
*— Book X added after the ONSET Retreat (Surface Splash Awakens), 2026-03-14*
*— Book XI added after the OPAL Retreat (Iridescent Cloud Awakens), 2026-03-14*
