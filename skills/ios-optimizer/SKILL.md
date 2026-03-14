---
name: ios-optimizer
description: iOS Optimizer — AUv3-specific quality assurance, performance optimization, and compatibility validation for XO_OX plugins on iOS (iPhone/iPad). Covers Audiobus, AUM, GarageBand, and iOS DAW compatibility, memory constraints, and AUv3 sandboxing requirements. Use when the user says 'ios optimizer', 'AUv3', 'ios compatibility', 'iPad version', 'mobile version', 'Audiobus', 'AUM compatibility', 'GarageBand plugin', 'iOS port', 'mobile optimization', 'AUv3 validation', 'ios memory', 'auv3 sandbox', wants to validate an XO_OX plugin for iOS, is preparing an AUv3 release, or wants to know what iOS-specific issues to watch for before submitting to App Store.
---

# iOS Optimizer

**The MPC is portable. The plugin should be too.**

XO_OX plugins running as AUv3 on iPad bring the XO_OX ecosystem to the most popular mobile music production platform. But iOS is a different hardware environment — memory limits, sandboxing, and AUv3's host-managed lifecycle create failure modes that don't exist on macOS.

---

## AUv3 vs AU2 Differences

| Aspect | macOS AU | iOS AUv3 |
|--------|----------|-----------|
| Process model | Standalone process | In-process with host |
| Memory | Unrestricted | 512MB–1GB typical limit |
| File access | Full filesystem | Sandboxed (App Group required for shared files) |
| State persistence | Plugin manages | Host manages via getFullState/setFullState |
| Background audio | Optional | Required for background playback |
| UI lifecycle | Persistent | Host creates/destroys at will |
| Polyphony | High | Reduce for performance |

---

## The iOS Audit Checklist

### Memory Audit
- [ ] Total plugin memory footprint < 200MB (leave headroom for host + other plugins)
- [ ] No per-voice allocations that scale with polyphony × quality settings
- [ ] Wavetable and sample data uses memory-mapped files, not loaded into RAM
- [ ] No memory leaks in voice lifecycle (allocate at launch, not per note)
- [ ] Reverb tail buffers bounded and freed on bypass

**Red flags:**
- Granular engines with large buffer sizes (OPAL: check grain buffer allocation)
- Reverb with IR size > 1 second (large IR = large convolution buffers)
- Preset loading that allocates per-load (should pre-allocate)

### AUv3 State Management
- [ ] `getFullState()` returns complete serializable state
- [ ] `setFullState()` restores plugin to identical behavior
- [ ] State survives host save/reload cycle
- [ ] State survives UI create/destroy (UI is separate from DSP)
- [ ] No state stored in UI components that isn't mirrored in DSP state

### CPU Audit
Read the DSP Profiler output and apply iOS targets:

| Stage | macOS Target | iOS Target |
|-------|-------------|-----------|
| Voice DSP (8 voices) | < 15% CPU | < 25% CPU |
| Filter per voice | < 2% | < 3% |
| Reverb | < 5% | < 8% |
| Total plugin | < 25% | < 40% |

iOS targets are higher percentages because iOS CPUs are slower than Mac CPUs, but total available CPU on iOS is also constrained by battery life management.

**Polyphony reduction**: If the macOS version runs 8-voice poly, the iOS version may need to default to 4-voice to hit CPU targets on older iPads.

### File Access
- [ ] Preset files accessed via App Group container (not direct filesystem path)
- [ ] No hardcoded macOS paths (`~/Documents/`, etc.)
- [ ] User preset save location uses iOS-appropriate container
- [ ] Factory presets bundled in app bundle, not filesystem

### Audiobus / AUM Compatibility
- [ ] Plugin exposes correct AUv3 output bus configuration
- [ ] Side-chain input (if applicable) uses correct bus configuration
- [ ] MIDI input implemented via AUv3 MIDI event handling
- [ ] Plugin continues audio when host moves to background
- [ ] No dependency on macOS-specific APIs

### Background Audio
- [ ] Audio continues when host app backgrounds (required for AUM, Audiobus workflows)
- [ ] Plugin does not assume UI is alive during audio processing
- [ ] No UI-touching code in processBlock()

### App Store Compliance
- [ ] No use of private APIs
- [ ] All permissions properly requested (microphone if applicable)
- [ ] App Group entitlement configured for preset sharing
- [ ] Plugin binary is universal (arm64 + x86_64 simulator)
- [ ] No calls to deprecated APIs flagged in iOS SDK

---

## Common iOS Failure Patterns

| Issue | Symptom | Fix |
|-------|---------|-----|
| Memory pressure crash | Plugin crashes after 2-3 other plugins loaded | Reduce buffer sizes, pre-allocate |
| State loss on host restart | Settings reset after GarageBand closes | Fix getFullState/setFullState |
| No background audio | Audio stops when switching apps | Add background audio mode |
| File access crash | Crash on preset load | Fix path to use App Group container |
| CPU spike on note-on | Stutter when chord played | Move allocations to voice init, not note-on |
| UI freeze on resume | Interface unresponsive after backgrounding | Don't block UI thread in DSP |

---

## iOS-Specific Optimization Opportunities

Beyond standard DSP profiling, iOS-specific optimizations:

**ARM NEON SIMD**: iOS runs on ARM. SIMD operations that use ARM NEON intrinsics instead of SSE can provide significant speedup for filter banks and wavetable lookups.

**Fixed-point arithmetic**: For some DSP stages, fixed-point math on ARM is faster than floating-point. Evaluate for filter stages that run in the hot path.

**Thermal throttling**: iOS devices throttle CPU under sustained load. Optimize for sustained performance, not peak performance. Test with a thermal monitor app during sustained playback.

---

## Arguments

- (none) — full iOS audit checklist for the current engine
- `audit: {engine name}` — run the complete iOS audit for a specific engine
- `memory: {engine name}` — memory footprint analysis only
- `cpu: {engine name}` — CPU audit with iOS-specific targets
- `state` — review AUv3 state management implementation
- `compat` — Audiobus / AUM / GarageBand compatibility check
- `appstore` — App Store compliance review
- `optimize` — iOS-specific optimization recommendations beyond standard DSP profiling
