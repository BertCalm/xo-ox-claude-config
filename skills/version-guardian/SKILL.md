---
name: version-guardian
description: Version Guardian — protects preset compatibility and parameter stability across XO_OX plugin versions. Tracks parameter changes, generates migration scripts, flags breaking changes before they ship, and maintains V1→V2 compatibility records. Use when the user says 'version guardian', 'breaking change', 'preset migration', 'parameter rename', 'backward compatibility', 'version compatibility', 'will this break presets', 'migration script', 'preset compatibility check', 'version X to Y', 'parameter removed', 'schema change', is about to rename or remove parameters, is planning a major version bump, wants to check if an upcoming change will break existing presets, or is recovering from a preset compatibility break.
---

# Version Guardian

**A broken preset is a broken promise. The Guardian makes sure that doesn't happen quietly.**

Preset compatibility is the most user-visible technical contract in XO_OX. When parameters change between versions, hundreds of presets stop sounding right — and the user doesn't know why. The Version Guardian tracks these contracts, flags breaks before they ship, and generates migration tools when breaking changes are unavoidable.

---

## What Breaks Presets

Ranked by severity:

| Change Type | Severity | Impact |
|------------|---------|--------|
| Parameter removed | CRITICAL | Preset silently ignores the parameter |
| Parameter renamed | CRITICAL | Old name not found, preset loads with default |
| Parameter range changed | HIGH | Value maps to wrong place in new range |
| Parameter behavior changed | HIGH | Same value produces different sound |
| New parameter added (no default) | MEDIUM | Preset loads with undefined behavior |
| New parameter added (with sensible default) | LOW | Preset loads correctly, new param at default |
| Schema version change | VARIES | Depends on whether loading is backward-compatible |
| Engine parameter prefix change | CRITICAL | All presets for that engine break simultaneously |

---

## Pre-Change Audit

Before any parameter modification, run a pre-change audit:

### Step 1: Identify Affected Presets
```bash
# Find all presets that use a specific parameter
grep -rl "\"old_param_name\"" ~/Documents/GitHub/XO_OX-XOmnibus/Presets/
```

Count: how many presets will be affected?

### Step 2: Assess Impact
- If < 10 presets: manageable, can edit manually or with a script
- If 10–50 presets: write a migration script
- If > 50 presets: this change requires either backward compatibility handling in the plugin code, or a formal preset migration tool

### Step 3: Classify the Change
- **Safe to ship**: Adding parameters with sensible defaults
- **Requires migration script**: Renaming parameters, range changes
- **Requires plugin backward compatibility**: Removing parameters in use
- **Requires major version bump**: Any change that can't be automatically migrated

---

## Migration Script Generator

When a parameter is renamed or has a range change, generate a Python migration script:

```python
#!/usr/bin/env python3
"""
Preset Migration: [Old Name] → [New Name]
Engine: [Engine Name]
Version: v[X.X] → v[Y.Y]
Date: [Date]
"""

import json
import os
from pathlib import Path

PRESET_DIR = Path("~/Documents/GitHub/XO_OX-XOmnibus/Presets/").expanduser()
OLD_KEY = "[old_parameter_name]"
NEW_KEY = "[new_parameter_name]"
# If range changed: OLD_RANGE = (0.0, 1.0), NEW_RANGE = (0.0, 2.0)

def migrate_preset(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    changed = False
    for engine_key, engine_data in data.get("parameters", {}).items():
        if OLD_KEY in engine_data:
            old_value = engine_data.pop(OLD_KEY)
            # If range remapping needed:
            # new_value = (old_value / OLD_RANGE[1]) * NEW_RANGE[1]
            engine_data[NEW_KEY] = old_value
            changed = True

    if changed:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Migrated: {filepath.name}")

    return changed

if __name__ == "__main__":
    presets = list(PRESET_DIR.rglob("*.xometa"))
    migrated = sum(1 for p in presets if migrate_preset(p))
    print(f"\nMigrated {migrated}/{len(presets)} presets")
```

---

## Backward Compatibility in Plugin Code

When a breaking change is unavoidable and can't be fully migrated at the preset level, the plugin needs to handle the old parameter name:

```cpp
// In loadPreset() or APVTS restore:
// Handle legacy parameter name
if (state.hasProperty("old_param_name"))
{
    auto legacyValue = state.getProperty("old_param_name");
    // Map to new parameter
    apvts.getRawParameterValue("new_param_name")->store(static_cast<float>(legacyValue));
}
```

The Guardian generates the specific code block needed for each migration case.

---

## Version Compatibility Matrix

Maintain a record of breaking changes across versions:

```
VERSION COMPATIBILITY RECORD: [Engine Name]

v1.0 → v1.1: COMPATIBLE
  Added: filter_mode (default: "low_pass") — no presets affected

v1.1 → v1.2: MIGRATION REQUIRED
  Renamed: filter_freq → filter_cutoff
  Migration: run migrate_v1.1_to_v1.2.py (migrates 47 presets)
  Plugin code: backward compat handler included in v1.2

v1.2 → v2.0: BREAKING
  Removed: old_drive_algorithm parameter
  Changed: envelope_attack range (0–2s → 0–10s)
  Migration: run migrate_v1.2_to_v2.0.py
  Note: V1 presets will load but sound character may differ for high-attack presets
```

---

## Schema Version Tracking

The `.xometa` schema version must be bumped when:
- New required fields are added
- Field meaning changes
- Old fields are removed

Track schema versions in a separate record. When the schema changes, the plugin's preset loader must handle both old and new schema versions.

---

## Arguments

- (none) — status report: current version records across all engines, any known compatibility gaps
- `audit: {engine name}` — pre-change audit for a specific engine (read current parameter list, flag any planned changes)
- `check: {parameter name}` — how many presets use this parameter? Is it safe to change?
- `migrate: {old param} → {new param}` — generate a migration script for a parameter rename
- `script: {engine} v{X.X} → v{Y.Y}` — generate a migration script given version notes
- `compat-code: {engine}` — generate backward compatibility code block for plugin's loadPreset()
- `record` — show the version compatibility record for all engines
- `breaking` — list all changes in the current working diff that could break preset compatibility
