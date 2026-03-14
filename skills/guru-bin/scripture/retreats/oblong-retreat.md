# OBLONG Retreat — The Coral Awakening
*Guru Bin Spiritual Retreat #1 — 2026-03-14*
*Engine: XOblongBob (OBLONG) | Gallery Code: BOB | Creature: Coral Polyp*

---

## The Diagnosis

> *"OBLONG is a coral reef that doesn't know it has five nervous systems."*

The CuriosityEngine is the soul — five behavioral modulation algorithms in one parameter slot. But the engine's full expressive range has never been explored because:
1. The vel_filter parameter (velocity→filter) exists but was never promoted in presets
2. CuriosityEngine is autonomous — it doesn't respond to the player's touch (the "locked behind glass" problem)
3. SnoutFilter's character knob secretly does four different things depending on filter mode
4. BobMode's S-curve creates a hidden 50% threshold where texture appears from silence
5. LFO1→FX Depth routing (target mode 3) is undocumented and unused in any preset

---

## The Five Nervous Systems (CuriosityEngine Deep Dive)

What the Scripture didn't know until now: the 5 Curiosity modes are not speed variations. They are five fundamentally different modulation algorithms.

### Mode 0: Sniff — Random Drift with 22ms Ramp
- Random target every 0.5-1.5 seconds
- Exponential approach at 22ms time constant
- The modulation is gentle, occasional, unpredictable
- **Best for**: Subtle filter exploration. The pad seems to notice something in the harmonic spectrum and drift toward it, then lose interest.

### Mode 1: Wander — Direct LFO2 Passthrough
- Uses LFO2 (always Smooth Random, 0.001-2 Hz) directly
- No additional randomness — the modulation IS the LFO2
- At LFO2 rate 0.05 Hz, one cycle takes 20 seconds
- **Best for**: Glacial evolution. The pad changes so slowly you don't notice until it's somewhere else.

### Mode 2: Investigate — 60/40 Cross-Modulation Blend
- 60% LFO1 (user-controlled rate, shape, depth) + 40% LFO2 (always Smooth Random)
- Creates cross-modulation patterns that no single LFO can produce
- The LFO1 provides intentional movement; the LFO2 adds unpredictable undertones
- **This is the most important mode** — it's the only one that blends controlled and uncontrolled modulation
- **Best for**: Evolving pads where you want direction but not predictability. The pad has a purpose but gets distracted.

### Mode 3: Twitch — Nervous Random Jumps with 20ms Snap
- Random target every 0.3-2.3 seconds
- Rapid 20ms approach (faster than Sniff by 2ms)
- The modulation is jittery, reactive, startled
- **Best for**: Glitchy textures, nervous energy, the ADD synth. The pad is anxious.

### Mode 4: Nap — Ultra-Slow Drift at 0.3x Magnitude
- Random target every 2-6 seconds
- 5.6-SECOND approach time (250x slower than Twitch)
- Target scaled by 0.3 — the modulation barely moves
- **Best for**: Near-static pads where you want the faintest suggestion of life. "Did it move or did I imagine that?"

### The Per-Voice Phase Truth
Each of 16 voices gets offset `voiceIndex / 16.0` on both LFOs. A 4-note chord = voices at 0°, 22.5°, 45°, 67.5° phase offset. This is deterministic decorrelation — the voices don't drift randomly, they start at evenly-spaced phases and then diverge according to the CuriosityEngine's behavior. The result is a chord where each note has its own "personality" from the first millisecond.

---

## The Character Chameleon (SnoutFilter Character Parameter)

The most versatile single parameter in the engine — and the most misunderstood:

| Filter Mode | What Character Does | At 0.0 | At 0.5 | At 1.0 |
|------------|-------------------|--------|--------|--------|
| **Snout LP** | Blends clean vs. saturated resonance tail | Pure clean LP | Balanced warmth | Heavy saturated resonance |
| **Snout BP** | Soft saturation intensity on BP output | Clean bandpass | Mild crunch | Distorted bandpass |
| **Snout Form** | Morph between two formant bands (1x and 2x cutoff) | Lower formant only | Equal blend | Upper formant only |
| **Snout Soft** | Nothing (1-pole has no character) | — | — | — |

### The Retreat Revelation: Character + Mode Combinations

The real power is combining Character with filter Mode changes:
- **LP at Character 0.28**: The Resonance Shelf (Psalm 1) — presence without ringing
- **Form at Character 0.5**: Two formant bands in equal balance — the "two mouths" of the coral feeding
- **Form with Character on a macro**: Sweeping between formants IS vowel morphing — no formant filter needed
- **BP at Character 0.6-0.8**: The nasal singing quality that sits in a mix like a human voice

---

## BobMode — The Tidal S-Curve

BobMode is not a linear macro. It's an S-curve with thresholds:

```
bob_mode  →  oscDrift    filterChar  texLevel    modDepth    fxDepth
0.0          0.0         0.0         0.0         0.0         0.0
0.25         0.015       0.12        0.0         0.12        0.02
0.50         0.125       0.39        0.0 (!)     0.39        0.27
0.60         0.216       0.50        0.03        0.50        0.41
0.75         0.393       0.67        0.13        0.67        0.60
1.00         0.80        0.90        0.25        0.90        0.85
```

**The 50% threshold**: Texture level is zero below 50% BobMode. This means the bottom half of BobMode is purely about warmth and character — oscillator drift and filter saturation. The top half is where the tape cassette personality enters. This is by design: the coral is warm underwater, and only when the tide rises fully does the tape patina appear.

---

## Hidden Capabilities Unlocked

### 1. vel_filter — The D001 Fix That Already Exists
`vel_filter` parameter [0-1] maps velocity to filter cutoff bipolar: soft playing darkens, hard playing brightens. **This is exactly what the Seance demanded under Doctrine D001** and it's been built into the engine the entire time. Default is 0.3 — subtle but present. At 0.6-0.8, the timbral arc from pianissimo to fortissimo is dramatic.

**Retreat proclamation**: Every OBLONG preset should have `vel_filter` at minimum 0.3. Presets designed for keyboard expression should set it to 0.5-0.7.

### 2. LFO1 → FX Depth (Target Mode 3)
When `lfo1_target = 3`, LFO1 modulates all FX simultaneously — SmearChorus, DustTape, SpaceReverb. The FX breathe in and out together. At LFO1 rate 0.067 Hz (the Physiological LFO, Sutra 1), the entire effects chain inhales and exhales every 15 seconds.

**Retreat proclamation**: This is the "Breathing Reef" — the coral's FX stage pulsing with the tide. Use `lfo1_target=3, lfo1_rate=0.067, lfo1_depth=0.15` for presets where the space itself breathes.

### 3. Texture Breath Mode Tracks Pitch
Texture mode 3 (Breath) is band-pass filtered noise that tracks the voice's frequency. This means the noise texture is harmonically related to the note being played — not random white noise but formant-tracking breath.

**Retreat proclamation**: For "vocal" pad presets, use `tex_mode=3 (Breath), tex_level=0.08, tex_tone=0.6`. The pad will sound like it's exhaling through the notes.

### 4. Form Mode's Fixed Octave Relationship
SnoutFilter Form mode always places the second band at 2x the cutoff frequency. This means sweeping cutoff from 500→2000 Hz simultaneously sweeps band 1 from 500→2000 and band 2 from 1000→4000. The interval between them is always an octave. This creates a fixed harmonic structure that sounds like a resonant body — not unlike the inside of a piano or a vocal tract.

---

## New Scripture — OBLONG Verses

### Oscillator Verse 6: The Oblong Harmonic
> The Oblong Sine is not a sine. It is a sine plus its 2nd harmonic at 10% — an even-harmonic warm foundation that already contains the tape-like character before any saturation is applied. This is why OBLONG sounds warm at the oscillator level while other engines need DustTape or saturation to achieve warmth. The warmth is in the waveform, not the processing.

### Filter Psalm 6: The Character Chameleon
> The SnoutFilter `character` parameter is four controls in one body. In LP mode it saturates the resonance tail. In BP mode it distorts the output. In Form mode it morphs between formants. In Soft mode it does nothing. Design presets that exploit this: map Character to a macro, then switch filter modes to transform what the macro controls. One knob, four behaviors, selected by the mode switch.

### Modulation Sutra 6: The Investigate Blend
> CuriosityEngine Investigate mode blends LFO1 at 60% and LFO2 at 40%. LFO1 is the conscious intention — the rate, shape, and depth you choose. LFO2 is the unconscious undertone — always Smooth Random, always slightly unpredictable. This 60/40 blend creates modulation patterns that are directional but never repetitive. It is the only mode where the designer's will and the engine's instinct collaborate. No other modulation system in any engine offers this blend of control and chaos.

### Modulation Sutra 7: The Breathing Reef
> Route LFO1 to FX Depth (target mode 3) at rate 0.067 Hz and depth 0.15. The entire effects chain — chorus, tape, reverb — inhales and exhales together every 15 seconds, synchronized with the listener's breathing. The reef doesn't just make sound. It breathes. The FX aren't decoration — they're the organism's respiration.

### Stewardship Canon 6: The SmearChorus Width Tax
> SmearChorus width at 0.5 is identity — stereo image passes through unchanged. Many presets set width=0.5, meaning the chorus stage is active but the stereo processing does nothing. Check `smear_width` on every preset: if it's 0.5 and `smear_mix` is 0, the entire chorus can be bypassed. Free CPU for the reef to grow.

### Master Truth 6: The BobMode Tide Table
> BobMode is not linear. Texture appears only above 50%. FX depth blooms after 20%. Oscillator drift follows a quadratic curve. The sweet spot for warm pads is 0.3-0.5 BobMode — the zone where warmth increases without tape artifacts. The sweet spot for lo-fi character is 0.7-0.9 — where texture and FX are both active but not maxed. BobMode at 1.0 is a storm surge — everything at maximum, deliberately overwhelming. Each zone is a different instrument.

### Expression Truth 1: The Glass Door Opens
> OBLONG has `vel_filter` — velocity→filter cutoff mapping that the Seance ghosts demanded but didn't know existed. At 0.3, the timbral change is subtle. At 0.6, pianissimo and fortissimo are different instruments. This is not just D001 compliance — this is the difference between a synth preset and a playable instrument. Every OBLONG preset should expose this. The glass door between the player's hands and the CuriosityEngine's soul is `vel_filter`.

---

## Awakening Presets (5 sounds that demonstrate OBLONG at peak)

These presets showcase capabilities that only OBLONG possesses.

**Design principles for the Awakening set:**
- Every preset uses `vel_filter ≥ 0.3` (the Glass Door is always open)
- Every preset uses CuriosityEngine in the mode that best serves the sound
- Every preset respects CPU stewardship (polyphony ≤ 6, FX bypassed when unused)
- Every preset passes the First Two Seconds test and the Name Test
