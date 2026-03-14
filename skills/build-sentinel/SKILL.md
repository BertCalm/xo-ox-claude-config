---
name: build-sentinel
description: Build Sentinel — monitors the XOmnibus build, validates that all engines compile, auval passes, and new code integrates without breaking the fleet. Use when the user says 'build sentinel', 'run the build', 'check if it builds', 'does this break the build', 'run auval', 'validate the build', 'test the integration', 'build check before committing', 'does the new engine compile', wants to verify a code change doesn't break the fleet before committing, just added a new engine and wants to validate the integration, suspects a build regression, or wants a clean build + auval PASS confirmation before shipping.
---

# Build Sentinel

**The last line of defense before a broken build reaches git.**

The Sentinel runs the XOmnibus build, validates that every engine compiles clean, and runs `auval` to confirm the AU component passes Apple's validation. It doesn't just report pass/fail — it diagnoses failures and points to the exact file and line where things broke.

---

## Build Commands

The XOmnibus build uses CMake + Ninja:

```bash
# Standard release build
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build

# Run auval after build
auval -au aumu XO_O XO_O
```

The working directory must be `~/Documents/GitHub/XO_OX-XOmnibus/`.

---

## What the Sentinel Checks

### Phase 1: Pre-Build Validation

Before building, the Sentinel checks for known integration issues:

**REGISTER_ENGINE macro check:**
Any engine using `REGISTER_ENGINE(namespace::EngineClass)` will fail — the token-paste `registered_##EngineClass` cannot concatenate a namespace-qualified name. The Sentinel scans for:
```
grep -r "REGISTER_ENGINE" Source/
```
If any registration includes `::`, flag as ERROR before building (the build will fail at this exact point).

**CMake configuration check:**
- CMakeLists.txt lists the engine in `target_sources`
- Engine .h file exists at the expected path
- No circular dependencies between engine headers

**Parameter prefix collision check:**
- No two engines use the same parameter prefix (would cause preset loading conflicts)
- Verify against CLAUDE.md prefix table

### Phase 2: Build

Run the build and capture output:

```bash
cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release 2>&1
cmake --build build 2>&1
```

Parse the output for:
- `error:` — build errors (file + line)
- `warning:` — significant warnings (flag, don't fail)
- Build success: look for Ninja completion without errors

### Phase 3: auval

```bash
auval -au aumu XO_O XO_O
```

auval PASS indicators: `PASS` in output, no `FAIL` lines
auval failure indicators: Any `FAIL:` prefixed line

Common auval failure patterns and their causes:

| auval Error | Cause | Fix |
|-------------|-------|-----|
| `FAIL: MIDI input does not transmit` | Missing MIDI handler | Check `processMidi()` is implemented |
| `FAIL: silence after note off` | Note-off not clearing voices | Check `stopNote()` implementation |
| `FAIL: output not silent` | Denormal values leaking | Add denormal protection to output stage |
| `FAIL: parameter count changed` | Param added without version bump | Bump plugin version or ensure backward compat |
| Component not found | Wrong PLUGIN_CODE in CMake | Check 4-char code matches in Info.plist and CMake |

### Phase 4: Regression Check

After a successful build, the Sentinel verifies nothing that was previously working has regressed:

1. All engine `.h` files present (none deleted or renamed)
2. Preset count stable — no .xometa files accidentally deleted (compare count vs. MEMORY.md)
3. Parameter count in APVTS matches last known count (from CLAUDE.md)

---

## Report Format

### PASS

```
══════════════════════════════════════
  BUILD SENTINEL REPORT
  Time: {timestamp}
══════════════════════════════════════

Pre-build validation: ✅ PASS
  - No REGISTER_ENGINE namespace issues
  - All engine headers present
  - No parameter prefix collisions

Build: ✅ PASS
  - 0 errors, 0 warnings
  - Build time: {N}s

auval: ✅ PASS
  - AU component validated
  - MIDI handling confirmed
  - Silence behavior confirmed

Regression check: ✅ PASS
  - All {N} engines present
  - Preset count stable: {N}

READY TO COMMIT / SHIP
══════════════════════════════════════
```

### FAIL

```
══════════════════════════════════════
  BUILD SENTINEL REPORT
  Time: {timestamp}
══════════════════════════════════════

Pre-build validation: ❌ FAIL
  ERROR: REGISTER_ENGINE(xomnibus::OhmEngine) at Source/Engines/Ohm/OhmEngine.h:1
  FIX: Move to centralized registration in XOmnibusProcessor.cpp

Build: ⏭️ SKIPPED (pre-build failed)

──────────────────────────────────────
DIAGNOSIS:
The REGISTER_ENGINE macro uses token-paste (##) which cannot handle
namespace-qualified names. The 5 Constellation engines (Ohm, Orphica,
Obbligato, Ottoni, Ole) are broken by this pattern.

Fix: In XOmnibusProcessor.cpp, add centralized registration:
  #include "Source/Engines/Ohm/OhmEngine.h"
  // In the registration block:
  engines.add(std::make_unique<xomnibus::OhmEngine>(...));
Remove the REGISTER_ENGINE macro call from each engine header.
══════════════════════════════════════
```

---

## Integration Validation Mode

When adding a new engine (after `/new-xo-engine`), the Sentinel runs a focused integration check:

1. Engine adapter `.h` exists and implements `SynthEngine` interface
2. Engine is registered in `XOmnibusProcessor.cpp` (not via broken macro pattern)
3. Engine is listed in `EngineRegistry.h`
4. At least one `.xometa` preset exists for this engine
5. Build + auval PASS

Reports: INTEGRATED (all checks pass), PARTIAL (some items missing), NOT INTEGRATED (engine not wired in).

---

## Arguments

- (none) — full build + auval + regression check
- `--pre-only` — pre-build validation only (no build, fastest)
- `--build-only` — skip auval (for iterating on DSP code)
- `--auval-only` — skip build (assumes already built, just run auval)
- `--engine {name}` — integration check for a specific new engine
- `--fast` — pre-build + build only, skip regression check

---

## XO_OX Build Gotchas

Known issues that have caused build failures before:

| Gotcha | Description | How to avoid |
|--------|-------------|-------------|
| REGISTER_ENGINE namespace | `REGISTER_ENGINE(xomnibus::Engine)` fails token-paste | Use centralized registration in XOmnibusProcessor.cpp |
| JUCE 8 atomic load | `jmax` needs `.load()` for atomic values | `jmax(limit.load(), value)` not `jmax(limit, value)` |
| keyPressed signature | JUCE 8 uses 1-param `keyPressed(const KeyPress&)` not 2-param | |
| apvts.processor | Use `apvts.processor` not deprecated `apvts.getProcessor()` | |
| OSX_ARCHITECTURES placement | Must come before `project()` in CMakeLists.txt | |
| Include path collision | `Source/DSP/` vs `src/dsp/` on case-insensitive macOS | Use full qualified include paths |
| atPressure scope | Aftertouch variable `atPressure` must be declared in correct scope | Declare in processBlock header, not per-sample |
