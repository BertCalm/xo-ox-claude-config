---
name: preset-qa
description: Preset QA — systematic quality assurance pass over .xometa preset files. Validates schema correctness, DNA health, naming conventions, parameter ranges, mood balance, duplicate detection, and XO_OX brand compliance. Use when the user says 'preset qa', 'check the presets', 'validate presets', 'audit presets', 'are the presets correct', 'preset health check', 'scan presets for issues', wants to catch errors before shipping, just created a batch of presets with Exo Meta or Preset Forge, wants to verify preset compliance after a build cycle, or is preparing for release. Also invoke proactively after /exo-meta or /preset-forge creates new presets, and before any preset count is reported in documentation or memory.
---

# Preset QA

**Presets are the product. QA ensures what ships is what was designed.**

Twelve hundred presets across 27 engines. Each is a JSON file with 6 critical fields, a DNA signature, 4 macro labels, and a parameter block that has to exactly match what the engine code expects. One wrong field name, one out-of-range value, one duplicate name — and a producer hits an error or gets silence. Preset QA catches every category of error before they reach a user.

---

## What Preset QA Checks

### Level 1: Schema Validity (every preset)

- `schema_version` is present and = 1
- All required keys exist: `name`, `mood`, `engines`, `author`, `version`, `description`, `tags`, `macroLabels`, `couplingIntensity`, `tempo`, `dna`, `parameters`, `coupling`
- `engines` array is non-empty
- `parameters` has a key for every engine in `engines`
- `dna` has all 6 dimensions: `brightness`, `warmth`, `movement`, `density`, `space`, `aggression`
- `coupling.pairs` is an array (may be empty)
- `macroLabels` has exactly 4 entries
- JSON parses without error

**Flag level**: ERROR — any Level 1 failure makes the preset non-functional.

### Level 2: Value Range Validation

- All DNA values are 0.0–1.0 (not negative, not > 1.0)
- All normalized parameters (0.0–1.0 range) are within range
- Integer parameters (voice count, mode selection) are within documented enum range
- `mood` is one of: Foundation, Atmosphere, Entangled, Prism, Flux, Aether
- `couplingIntensity` is one of: None, Light, Medium, Heavy
- `version` follows semantic versioning (e.g., "1.0.0")

**Flag level**: ERROR for out-of-range values, WARNING for potentially unexpected extremes.

### Level 3: Parameter Prefix Validation

For each preset, verify that all parameter keys in `parameters.{EngineName}` use the correct engine prefix:

| Engine in `engines` | Expected prefix |
|---------------------|-----------------|
| OddfeliX | `snap_` |
| OddOscar | `morph_` |
| Overdub | `dub_` |
| Odyssey | `odyssey_` |
| Oblong | `bob_` |
| Obese | `fat_` |
| Overbite | `poss_` |
| Onset | `onset_` |
| Overworld | `ow_` |
| Opal | `opal_` |
| Orbital | `orbital_` |
| Organon | `organon_` |
| Ouroboros | `ouroboros_` |
| Obsidian | `obsidian_` |
| Origami | `origami_` |
| Oracle | `oracle_` |
| Obscura | `obscura_` |
| Oceanic | `oceanic_` |
| Ocelot | `ocelot_` |
| Optic | `optic_` |
| Oblique | `oblq_` |
| Ostinato | `osti_` |
| OpenSky | `sky_` |
| OceanDeep | `deep_` |
| Owlfish | `owl_` |
| Ouïe | `ouie_` |
| Ohm | `ohm_` |
| Orphica | `orph_` |
| Obbligato | `obbl_` |
| Ottoni | `otto_` |
| Olé | `ole_` |

Also flag: parameters belonging to engine A appearing in the block for engine B.

**Flag level**: ERROR for wrong prefix (preset will fail to load), WARNING for unknown parameters.

### Level 4: Naming Conventions

- Name is 2-3 words (flag if 1 word or 4+ words)
- Name is ≤ 30 characters
- No names that are just parameter descriptions ("Low Filter Pad", "Bright Lead")
- No jargon or technical feature names ("FM Synth", "Granular Pad")
- No duplicates within the same engine or scope (cross-reference all preset names)
- Name passes the "evocative test" — would a producer understand what this is from the name alone? (heuristic — flag obvious failures)

**Flag level**: ERROR for duplicates, WARNING for naming convention violations.

### Level 5: DNA Health

- No preset has all 6 DNA values at 0.5 (lazy default — nothing was actually scored)
- No preset has all 6 DNA values identical (suggests copy-paste without updating DNA)
- The `brightness` + `warmth` pair isn't contradictory (very high brightness + very high warmth is unusual — flag for review)
- DNA profile is consistent with mood: Aether presets should have unusual DNA profiles, Foundation should be moderate

**Flag level**: WARNING — DNA errors don't break loading but hurt the search/filter experience.

### Level 6: Macro Validation

- `macroLabels` has 4 entries, all uppercase
- Macro labels are engine-appropriate (not generic "MACRO 1" unless the engine actually uses that)
- If the engine has canonical macro names (from CLAUDE.md or engine source), labels should match

**Flag level**: WARNING — mislabeled macros confuse producers.

### Level 7: Description Quality

- Description is present and non-empty
- Description is 1-3 sentences (not just a single word, not a wall of text)
- Description doesn't just repeat the preset name
- Description doesn't use forbidden terms (jargon, parameter names, feature names)

**Flag level**: WARNING.

### Level 8: Fleet-Level Analysis

When running on a full folder or fleet:

- **Mood distribution per engine**: every engine should have presets in all 6 moods (flag missing moods)
- **DNA coverage**: check that the fleet covers the full 0–1 range on each DNA axis (flag if, for example, no presets exist with brightness > 0.8 for an engine)
- **Duplicate detection across engines**: flag names that are duplicated across different engines
- **Preset count health**: flag engines with fewer than 5 presets as under-stocked

**Flag level**: WARNING (informational — not bugs, but coverage gaps).

---

## Running Modes

### Single file
```
/preset-qa path/to/preset.xometa
```
Runs all 8 levels on the specified file.

### Single engine folder
```
/preset-qa engine: Opal
```
Reads all .xometa files for the Opal engine (both in engine source folder and XOmnibus Presets/). Runs Levels 1-7 per file, Level 8 for the full set.

### Full fleet
```
/preset-qa fleet
```
Reads every .xometa file in `Presets/XOmnibus/` and `Source/Engines/*/Presets/`. Full Level 1-8 pass. Produces a fleet-wide health report.

### New presets only
```
/preset-qa new
```
Reads git status to identify newly added .xometa files and runs QA only on those.

---

## Report Format

```
══════════════════════════════════════
  PRESET QA REPORT
  Scope: {engine / fleet / file}
  {N} presets scanned
══════════════════════════════════════

ERRORS ({N}) — must fix before shipping:
  ❌ "Warm Horizon.xometa" — missing DNA field: space
  ❌ "Deep Pressure.xometa" — wrong prefix: opal_pressure should be deep_pressure
  ❌ "Tidal Sweep.xometa" — duplicate name (also exists in Prism/)

WARNINGS ({N}) — should fix:
  ⚠️  "Ambient Wash.xometa" — all DNA values at 0.5 (not scored)
  ⚠️  "Bass Motion.xometa" — name is technical description
  ⚠️  "Opal" engine — missing Flux and Aether presets

PASSED: {N} presets — no issues found

DNA COVERAGE ({engine}):
  brightness:  [████████░░] 0.0–0.8 covered, missing 0.8–1.0
  aggression:  [██████████] full range covered
  space:       [░░░░░░░░░░] only 0.3–0.7 covered — add extreme presets

FLEET SUMMARY:
  Total presets: {N}
  Zero-duplicate fleet: {yes/no}
  Engines missing moods: {list}
  Average presets per engine: {N}
══════════════════════════════════════
```

---

## Auto-Fix Mode

When errors are deterministic and safe to fix automatically (wrong engine name casing, missing schema_version, whitespace in name), the QA can apply fixes directly:

```
/preset-qa fleet --fix
```

Reports each auto-fix applied. Leaves genuine errors for human review.

---

## Integration Points

| Trigger | What QA Checks |
|---------|---------------|
| After `/exo-meta` creates presets | New presets only — schema + naming + DNA |
| After `/preset-forge` writes files | New files — full Level 1-7 |
| Before release | Full fleet — Levels 1-8 |
| After `/historical-society` runs | Cross-references preset counts in docs against actual file counts |
| Before updating MEMORY.md preset counts | Fleet scan to get accurate count |
