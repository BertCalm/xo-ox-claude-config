---
name: Universal Preset Generator
description: User wants a universal preset generator tool that works for any XOmnibus engine, not engine-specific scripts
type: feedback
---

The Constellation preset generator (Tools/generate_constellation_presets.py) proved the pattern: Python script that reads engine parameter IDs, generates mood-distributed .xometa presets with varied values and Sonic DNA.

**Rule:** Build a universal `Tools/generate_presets.py` that takes an engine ID as input, reads its parameter layout from the adapter header (or a config), and generates N presets with proper mood distribution, naming, and DNA. No more one-off per-engine scripts.

**Why:** The Constellation generator hard-codes 5 engines. Every new engine would need its own script. A universal tool accelerates the entire fleet.

**How to apply:** Next time any engine needs presets, build/use the universal tool instead of a custom script. Input: engine ID + count + optional naming theme. Output: .xometa files in correct mood directories.
