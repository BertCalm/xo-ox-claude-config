---
name: dsp-profiler
description: DSP Profiler — reads XOmnibus engine source and produces a CPU cost estimate, identifies inefficiencies, and recommends optimization without sacrificing sound quality. Applies Guru Bin's Doctrine of CPU Stewardship to the code level. Use when the user says 'dsp profiler', 'profile the cpu', 'why is this engine heavy', 'optimize the dsp', 'cpu cost analysis', 'how much cpu does X use', 'make it more efficient', 'check for denormals', 'polyphony vs cpu tradeoff', wants to find the expensive stages in an engine's signal chain, wants to verify the Stewardship Canons are being followed in code, wants to free up CPU headroom before adding features, or is comparing the cost of two implementation approaches.
---

# DSP Profiler

**The Bone, at the code level.**

Guru Bin's disciple The Bone can hear CPU waste. The DSP Profiler reads it — scanning engine source for patterns that are expensive, patterns that are efficient, and patterns that are dangerous (denormals, unbounded loops, blocking calls). It doesn't just identify problems; it quantifies them and recommends fixes.

---

## What the Profiler Checks

### Level 1: Architecture Scan

- **Voice count vs. use case**: 8-voice poly on a mono bass engine = 7 wasted voices. Checks: does the engine have a mono/legato mode? Should it?
- **Allocation on audio thread**: any `new`, `delete`, `malloc`, `std::vector::push_back` in `processBlock()` paths → ERROR. Memory allocation on the audio thread causes non-deterministic spikes.
- **Blocking calls on audio thread**: any file I/O, sleep, mutex lock that isn't a spinlock → ERROR
- **Static object creation in processBlock**: `juce::String`, heavy temporaries → WARNING

### Level 2: Filter Cost Estimation

Filter cost varies significantly by type. The Profiler identifies every filter instantiated in the engine and assigns a relative cost:

| Filter Type | Relative Cost | Notes |
|-------------|--------------|-------|
| One-pole (6dB/oct) | 1x | Trivial |
| Biquad (12dB/oct) | 2x | Per voice |
| SVF (12dB/oct, Cytomic) | 2.5x | Smoother modulation |
| Ladder (24dB/oct) | 4x | Classic Moog topology |
| Comb filter | 3x | Delay line included |
| Formant filter (pair of biquads) | 5x | Vowel territory |
| Spectral filter (FFT-based) | 20-40x | Heavy — per-block FFT |

Reports: total filter cost score for the engine. Flags if filter mode can be dynamically selected (LP24 → LP12 switch saves 2x filter cost when quality isn't needed).

### Level 3: Oscillator Cost

| Oscillator Type | Relative Cost |
|----------------|--------------|
| Sine (lookup table) | 1x |
| Sawtooth (BLEP) | 2x |
| Pulse (BLEP) | 2x |
| Wavetable (linear interp) | 3x |
| Wavetable (4-point interp) | 5x |
| FM (2 ops) | 4x |
| Physical model (KS/waveguide) | 8-15x |
| Granular (8 grains) | 12x |
| Granular (32 grains) | 48x |
| Additive (16 partials) | 16x |
| GENDY stochastic | 10x |

Multiplied by voice count to get total oscillator cost.

### Level 4: Modulation Cost

| LFO Type | Cost |
|----------|------|
| Sine LFO (lookup) | near zero |
| Smoothed parameter | ~0.5x |
| Envelope (per-voice) | 2x |
| Envelope follower | 3x |
| Per-voice LFO | ~1x × voice count |
| Mod matrix routing | linear with route count |

### Level 5: Denormal Detection

Denormal numbers (very small floating point values near zero) can cause 100-1000x slowdowns in x86 processors without denormal protection. The Profiler checks:

- Are feedback paths (delay lines, comb filters, reverb) protected with a DC-blocking filter or denormal clamp?
- Does the engine set DAZ/FZ flags (JUCE sets these in processBlock header — check it's not bypassed)?
- Any obvious feedback loops without `+1e-25f` or equivalent denormal killer?

Denormal bugs are silent — the preset sounds fine but CPU usage spikes on sustained notes. Flag: WARNING if unprotected feedback path exists.

### Level 6: The Stewardship Audit

Applying Book V: The Stewardship Canons directly to the code:

- **Canon 1: Polyphony Audit** — count actual voices. For pads and drones, recommend reducing from default. Calculate: estimated CPU at N voices vs N-2 voices.
- **Canon 2: Filter Mode Tax** — identify if LP24 is always-on vs. LP12. If always LP24, estimate savings of switching to dynamic mode selection.
- **Canon 3: Effect Bypass** — are bypass flags checked before processing? Reverb at bypass=true should cost near zero.
- **Canon 4: ParamSnapshot Pattern** — are parameter values cached once per block (recommended) or called via `getParameter()` per sample (expensive)?

---

## Cost Report Format

```
══════════════════════════════════════════════════════
  DSP PROFILER: {EngineName}
  Source: {file path, line count}
══════════════════════════════════════════════════════

## ARCHITECTURE SUMMARY
- Synthesis type: {what it is}
- Voices: {N} (estimated poly need: {N})
- Signal chain: {Oscillator} → {Filter} → {FX} → {Output}

## COST BREAKDOWN (per voice, normalized units)

| Stage | Type | Cost | Notes |
|-------|------|------|-------|
| Oscillator A | Wavetable (4-pt) | 5u | Heavy interpolation |
| Oscillator B | Sawtooth BLEP | 2u | Efficient |
| Filter | SVF LP + HP | 5u | Two SVFs |
| Reverb | Algorithmic | 8u | Shared (not per-voice) |
| LFO x3 | Sine lookup | <1u | Trivial |

Total per voice: ~12u
At 8 voices: ~96u
Shared FX: ~10u
**Estimated total: ~106u**

(Fleet average for medium-complexity engine: ~80u)

## CRITICAL ISSUES

❌ No issues found at Level 1 (audio thread safety)

## WARNINGS

⚠️  {Stage}: Denormal risk — feedback path at {location:line} has no denormal protection
⚠️  {Param}: Called `getParameter()` inside per-sample loop at {location:line} — cache in processBlock()
⚠️  Voice count: 8 voices at 12u each = 96u. A pad engine rarely needs more than 4 simultaneous voices. Reducing to 4 saves ~48u.

## OPTIMIZATION OPPORTUNITIES

Gift (zero-quality-cost savings):
1. Cache parameter pointer in processBlock() header — saves per-sample parameter lookup: ~5u savings
2. Reduce voice count from 8 to 4 for pad use case: ~48u savings

Borrow (quality tradeoff):
1. LP12 mode instead of LP24 when RESONANCE < 0.3: saves 2u per voice × 8 voices = ~16u, inaudible at low resonance
2. Reduce reverb quality setting from "high" to "medium" — saves ~4u, subtle difference

## THE BONE'S VERDICT

Estimated engine cost: **~106u** (medium-heavy for the fleet)
After zero-cost optimizations: **~53u** (fleet average or below)
Primary driver: {N}-voice granular oscillator stack

"The voice count is the debt. The reverb is the rent. Cut the voices, the rest is gratuity."

══════════════════════════════════════════════════════
```

---

## Implementation Guide Mode

When a specific optimization is chosen, the Profiler produces concrete code changes:

```cpp
// BEFORE: parameter read per sample (expensive)
for (int i = 0; i < numSamples; ++i)
{
    float cutoff = *apvts.getRawParameterValue("filter_cutoff");
    // ...
}

// AFTER: cached in processBlock header (gift optimization)
void processBlock(...)
{
    const float cutoff = *apvts.getRawParameterValue("filter_cutoff");
    // cached once — now free inside the loop
    for (int i = 0; i < numSamples; ++i)
    {
        // use cached 'cutoff'
    }
}
```

---

## Arguments

- `{engine name}` — profile a specific engine
- `{engine name} --fix` — profile and apply safe zero-cost optimizations
- `compare {Engine A} {Engine B}` — side-by-side cost comparison
- `fleet` — fleet-wide cost ranking (shows which engines are most expensive)
- `--focus denormals` — denormal check only
- `--focus polyphony` — voice count audit only
