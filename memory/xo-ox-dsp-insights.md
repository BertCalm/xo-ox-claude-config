# XO_OX DSP Engineering Insights

Accumulated from building XOverdub, XOdyssey, XOblongBob, and Instability Synth.

## Stereo DSP
- **Never share read/write positions between L/R channels** in parallel allpass/delay chains. This produces mono output and survives auval — only caught by code review or ear. Use separate state arrays and optionally offset delay lengths by +5-15 samples for decorrelation.

## Filter Modulation
- **LFO → filter must modulate actual cutoff frequency, not output amplitude.** Scaling output is a common shortcut that sounds nothing like real cutoff movement. Use multiplicative modulation: `cutoff *= pow(2, mod * octaves)` for musical scaling. Always clamp to [20, 20000] Hz.

## LFO Resolution
- **Per-sample LFO is non-negotiable.** Per-block LFO causes audible staircase artifacts at 512+ buffer sizes. Advance the LFO inside the sample render loop from day one, even during prototyping.

## Output Safety
- **Any synth with feedback > 0.5 needs a soft limiter.** Self-oscillating delay feedback (>100%) can produce unbounded output. `tanh()` on master output is cheap and effective.

## Portamento
- **Exponential frequency slew sounds more natural than linear.** Formula: `coeff = 1 - exp(-1 / (sr * timeSec))`. Only activate when target voice is already sounding (skip glide on first note).

## Preset Systems
- **Always reset ALL parameters to defaults before applying a preset.** Partial-application presets inherit values from the previous patch, causing unpredictable state bleed. Also clear FX state (delay buffer, reverb) on preset change for clean transitions.

## Velocity Expressiveness
- **Scale filter envelope amount by velocity** for natural dynamics — harder hits = brighter, softer = darker. This matches acoustic instrument behavior and requires zero new parameters.

## Legato vs Mono
- **Never copy-paste mono as legato.** Mono retriggers envelope; legato skips retrigger when voice is already active. Add a `legatoRetrigger` flag to noteOn.

## Denormal Protection
- Every recursive DSP (filter, envelope decay/release, delay feedback, reverb damping) needs denormal flush. Check `std::abs(x) < 1e-20`. The `ScopedNoDenormals` in processBlock helps but doesn't cover all state variables.

## JUCE Patterns
- `keyPressed`/`keyStateChanged` from `juce::KeyListener` (2-arg) will produce `-Woverloaded-virtual` warnings against `juce::Component` (1-arg). This is expected and benign when using `addKeyListener`.
- Finder copy operations create "filename 2.h" duplicates that cause signing warnings. Search for " 2." before first commit.

## Parameter Discipline
- **Every declared parameter must have a code path.** Unwired params show up in AU automation lists but do nothing — confusing for users and a sign of incomplete implementation. Audit all params after scaffold, before first build.
