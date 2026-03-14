---
name: engine-comparator
description: Engine Comparator — side-by-side analysis of two or more XOmnibus engines to clarify when to use which, where they overlap, and how they couple. Answers the "which engine for this task?" question that producers face when choosing between engines with similar territory (e.g., Organon vs Ouroboros, Opal vs Origami). Use when the user says 'engine comparator', 'compare X and Y', 'which engine for X', 'X vs Y', 'how are X and Y different', 'should I use X or Y for this sound', 'what's the difference between', wants to understand engine differentiation for a specific use case, wants to know which engines can couple effectively, or is designing a new engine and wants to check for redundancy with existing ones.
---

# Engine Comparator

**"What's the difference between Opal and Origami for ambient textures?"**

That's a question with a real answer — one that lives in the engines' DSP architectures, their preset libraries, their aquatic mythology positions, and their coupling behaviors. The Comparator reads both engines and gives you the answer a Seance session would take an hour to produce.

---

## What Gets Compared

For each engine in the comparison set, the Comparator reads:

1. **Synthesis architecture** — what DSP technique is at the core? (granular, physical model, additive, FM, etc.)
2. **Parameter space** — how many parameters, which categories dominate?
3. **Preset territory** — which moods are strongest? What sonic DNA does the preset library emphasize?
4. **feliX-Oscar polarity** — surface/transient/bright vs. deep/sustained/warm
5. **Water column depth** — aquatic mythology placement (open sky ↔ ocean floor)
6. **Coupling compatibility** — which CouplingType enums does each engine accept/output?
7. **Seance verdict** — what the ghosts said, any blessings, any concerns

---

## Report Format

```
══════════════════════════════════════════════════════
  ENGINE COMPARATOR: {Engine A} vs {Engine B}
  For use case: "{what the user described}"
══════════════════════════════════════════════════════

## At a Glance

| Dimension | {Engine A} | {Engine B} |
|-----------|------------|------------|
| Core synthesis | Granular | Physical string |
| Water column | Mid-column (250m) | Surface (20m) |
| feliX-Oscar | 0.4 (slightly Oscar) | 0.8 (strongly feliX) |
| Best mood | Atmosphere | Prism |
| Preset count | 150 | 67 |
| CPU cost | Medium | Low |
| Coupling outputs | FilterFreq, Amplitude | Pitch, Spectral |

## When to Use {Engine A}

{Engine A} excels at:
- {specific sound character 1}
- {specific use case 2}
- {genre/context 3}

Choose {Engine A} when you want: {2-3 sentences describing the irreplaceable territory}

## When to Use {Engine B}

{Engine B} excels at:
- {specific sound character 1}
- {specific use case 2}

Choose {Engine B} when you want: {2-3 sentences}

## The Overlap Zone

Both engines can produce: {what they share}
In the overlap, the tiebreaker is: {the key difference — e.g., "{Engine A} will be warmer and slower to evolve; {Engine B} will be brighter and more responsive to playing dynamics"}

## Coupling Potential

{Engine A} → {Engine B}: {what this coupling does, recommended amount}
{Engine B} → {Engine A}: {what this coupling does, recommended amount}
Best coupling type: {CouplingType}
This coupling exists in the preset library: {yes/no, preset name if yes}

## The Verdict for "{use case}"

Recommendation: {Engine A / Engine B / both / depends}
Reasoning: {2-3 sentences}

If using both: {how to layer or couple them for the stated use case}

══════════════════════════════════════════════════════
```

---

## Multi-Engine Comparison

When comparing 3+ engines (e.g., "which engine for ambient pads — Opal, Odyssey, or Oracle?"):

- Produces the same table but multi-column
- Ranks the engines from most-to-least suited for the stated use case
- Identifies the "combination play" — which 2 of the 3 to couple together

---

## Redundancy Check (for new engine design)

When invoked with a new engine concept (from `/theorem` or `/new-xo-engine`), the Comparator checks whether the proposed engine:

- Duplicates the synthesis technique of an existing engine
- Occupies the same feliX-Oscar polarity position as an existing engine
- Targets the same genre/use case as existing engines
- Could achieve the same sound by coupling two existing engines

Reports: UNIQUE (fills a genuine gap), ADJACENT (similar territory but differentiated), REDUNDANT (this territory is already well-covered — reconsider or find a differentiating angle).

---

## Arguments

- `{Engine A} vs {Engine B}` — direct comparison
- `{Engine A} vs {Engine B} for {use case}` — use-case-focused comparison
- `{Engine A} vs {Engine B} vs {Engine C}` — three-way
- `new: {concept description}` — redundancy check for a new engine idea
- `coupling: {Engine A} {Engine B}` — focused on coupling compatibility only
