# Instability Synth - Build Learnings

## MPC Plugin Hosting Quirks
- **User-level plugin dirs take priority**: `~/Library/Audio/Plug-Ins/` loads BEFORE `/Library/Audio/Plug-Ins/`. If old copies exist in user dir, MPC loads those. Always check both locations.
- **MPC settings file**: `~/Library/Application Support/Akai/MPC 3/application-settings.xml` — check `useAudioUnits` and `pluginFolderEnabled` flags
- **No dedicated plugin cache**: MPC doesn't have a separate cache dir for plugins (unlike Logic/AU Lab)
- **Rescan**: User must manually rescan in MPC after installing new plugin builds

## JUCE Build System
- **CMakeLists.txt must have `LANGUAGES C CXX`** — JUCE includes some C files
- **Manufacturer code change requires clean rebuild**: `rm -rf build` then reconfigure. Plugin won't be recognized as same plugin otherwise
- **COPY_PLUGIN_AFTER_BUILD FALSE**: VST3 system dir is owned by root. Use manual `sudo cp` instead
- **LTO bitcode objects**: After a corrupted build, `ar` shows "no symbols" because they're LLVM bitcode. Clean rebuild fixes it
- **JUCE shallow clone corruption**: If disk I/O times out during clone, the git repo corrupts ("current branch 'master' does not have any commits"). Fix: `rm -rf JUCE && git clone --depth 1 https://github.com/juce-framework/JUCE.git JUCE`

## Audio DSP Lessons
- **getTailLengthSeconds()**: Must return >0 for synths, otherwise DAW stops processing when MIDI stops. We use 10.0s
- **ScopedNoDenormals**: Essential in renderNextBlock to prevent CPU spikes from tiny floats in filters/envelopes
- **NaN guard**: Check `std::isfinite(output)` — reset filter and zero sample, but DON'T kill voice (let envelope fade naturally). Killing voice = silent preset bug
- **SVF filter normalization**: Cytomic TPT SVF requires `a1 = 1/(1+g*(g+k))` normalization. Without it, `g = tan(π*fc/sr)` blows up at high cutoff → NaN. This was the root cause of many silent preset issues
- **Triangle integrator DC drift**: Leaky integrator (`triState *= 0.999`) prevents DC accumulation on sustained triangle notes
- **Envelope minimum time**: Never allow 0.0 attack/release — causes clicks. Use 0.001 (1ms) minimum in timeRange()
- **Integer overflow in sample counters**: Cap at ~1 billion to prevent overflow after ~6 hours at 44.1kHz
- **Stereo Width requires L≠R content**: Mid/side processing with mono input = zero side channel = Width knob does nothing. Fix: per-voice stereo panning (spread voices ±0.3 across stereo field)
- **Saturation audibility**: Drive multiplier must be high enough (~12x) to push typical signals (~0.25 amplitude) into nonlinear region. Use partial gain compensation (`/sqrt(gain)` not `/gain`) to preserve audible effect
- **Instability events**: At very low rates (2/sec), micro-pitch events of ±3 cents are inaudible. Need ±15-25 cents range and 8/sec rate to be noticeable

## Silent Preset Bug (Root Cause & Fix)
- **Problem**: Some presets produced no sound (Init, Classic Saw Lead, Sync Lead, Pluck, Brass)
- **Root cause 1 (design)**: `loadFactoryPreset()` resets all params via `setValueNotifyingHost(getDefaultValue())` before applying preset values. Presets that rely on defaults for critical params get wrong values
- **Root cause 2 (deeper)**: SVF filter was missing normalization factor → filter blows up at high cutoff → NaN → NaN guard kills voice instantly → silence
- **Fix 1**: Every preset explicitly sets ALL sound-critical parameters
- **Fix 2**: Added SVF normalization `a1 = 1/(1+g*(g+k))`
- **Fix 3**: NaN guard now resets filter + zeros sample instead of killing voice

## UI Layout Lessons
- **Min window size**: 960x700 (was 860x650, caused overlapping at min size)
- **Row overlap math**: Always verify that section widths at minimum window size don't exceed available space
- **KnobComponents**: `setNumDecimalPlacesToDisplay(2)` prevents excessive decimal display

## Preset Design Tips
- **Category naming**: "CATEGORY - Name" format (e.g., "BASS - Sub", "LEAD - Classic Saw") for easy browsing
- **Pluck presets**: ampSustain=0 is by design (decay-only envelope) — not a bug
- **80s sounds**: Pulse waves + chorus-like detune (6-10 cents) + moderate filter = Juno/Jupiter character
- **Pad presets**: Long attack (1-3s), high sustain, long release (2-5s), detune for width

## Parameter System Architecture
- **APVTS**: AudioProcessorValueTreeState manages all parameters
- **getRawParameterValue()**: Returns std::atomic<float>* with denormalized (actual) values
- **ParamSnapshot**: Frozen per-block snapshot of all params — DSP code never touches APVTS directly
- **ChoiceParam in presets**: Use float index (0.0f=first, 1.0f=second, etc.), `convertTo0to1()` maps correctly
- **BoolParam in presets**: Use 1.0f for true, 0.0f for false
- **IntParam in presets**: Use float of integer value (e.g., -1.0f for octave -1)
- **Skewed ranges**: `timeRange(5.0f)` uses skew 0.35 for envelope times; `freqRange()` uses skew 0.25 for frequency

## Per-Sample Loop Optimization
- **Block-constant values**: Waveform selection, pan gains (std::sqrt), key tracking, velocity offsets — move outside per-sample loop. With 16 voices × 44.1kHz, every constant moved saves ~700K ops/sec
- **Filter coefficient updates**: `setCutoff()` + `setResonance()` separately = double `std::tan()` per sample. Use combined `setParams()` instead
- **Xorshift RNG zero-state**: If state reaches 0, `x ^= x << n` stays 0 forever. Guard: `if (rngState == 0) rngState = 1;`
- **DC blocker NaN poisoning**: `y = x - x1 + R * y1` with NaN y1 propagates forever. Guard: check `std::isfinite(y)`, reset on failure
- **Hash function zero input**: `hashNote(0) = 0 * constant = 0` → all offsets zero. Fix: `(note + 1) * constant`
- **Preset value clamping**: Values below parameter range minimum (e.g., 0.0f for 0.001f min) get clamped silently — fix at source

## JUCE 8 Migration Gotchas (from XOblongBob, March 2026)
- **`jmax` / `jmin` with atomics**: `*apvts.getRawParameterValue(id)` yields `std::atomic<float>`, not `float`. Template functions like `juce::jmax` can't deduce the type across the implicit conversion. Fix: use `.load()` explicitly — `apvts.getRawParameterValue(id)->load()`
- **`keyPressed` signature change**: `Component::keyPressed` is now 1-param (`const KeyPress&`). The 2-param version (`const KeyPress&, Component*`) belongs to `KeyListener` only. Override the wrong one and you get "hides virtual member function" error
- **`APVTS::getProcessor()` removed**: Use the public member `apvts.processor` directly instead
- **`Font::getStringWidth` deprecated**: Use `GlyphArrangement` or `TextLayout` for text measurement. Still compiles as a warning but will eventually be removed
- **CMake cache + project moves**: `CMakeCache.txt` stores absolute paths. Moving a project directory requires `rm -rf build` and full reconfigure — no shortcut
- **AU install for auval**: `auval` scans `~/Library/Audio/Plug-Ins/Components/`, not the build artifacts folder. Must `cp -R` the `.component` bundle before validation

## DSP Audit Checklist (Verified Pattern from XOblongBob)
1. `ScopedNoDenormals` in PluginProcessor::processBlock AND VoiceEngine::processBlock
2. No `new`/`malloc`/`push_back`/`resize` in any audio-thread file
3. No `mutex`/`lock_guard` on audio thread — use `std::atomic` with relaxed ordering
4. Two-stage algebraic soft clip: `x / (1 + |x|)` in voice mix AND final output
5. Filter: clamp resonance < 1.0, clamp cutoff to [20, sr*0.45], add `std::isfinite` recovery
6. Envelopes: guard `rateForTime()` against zero, flush denormals when level < 0.0001
7. Per-voice random state (never shared mutable RNG on audio thread)
8. `prepareToPlay` propagates sample rate to ALL DSP modules
9. Voice pool = `std::array<Voice, N>` (stack-allocated, no heap on noteOn)
10. Cross-thread int params → `std::atomic<int>` with relaxed ordering

## xattr Warning
- **Never wildcard xattr on plugin dirs**: `xattr -cr /Library/Audio/Plug-Ins/VST3/*.vst3` will modify ALL plugins (Arturia, etc.). Always quote the specific plugin path
