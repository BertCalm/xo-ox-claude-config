# B006 — Onset's Dual-Layer Blend Architecture

*Blessed: 2026-03-14 | Engine: Onset | Ghost: Ikutaro Kakehashi*

## The Blessed Feature

Each Onset voice has two synthesis layers (Layer X and Layer O) that can be blended continuously. This isn't two oscillators mixed — it's two complete synthesis algorithms (FM, Modal, Karplus-Strong, Phase Distortion) crossfaded per voice, creating timbral spaces between algorithms that no single algorithm can reach.

## Why It Is Protected

Kakehashi declared this architecture "original" — no drum machine in history has offered continuous blending between synthesis algorithms per voice. The crossfade creates timbres at the midpoints (50% FM + 50% Modal) that are genuinely new sounds, not just mixes. This is Onset's second most important innovation after XVC.

## Do Not

- Reduce to single-layer voices
- Replace continuous blend with discrete algorithm switching
- Remove any of the 4 algorithm options (FM, Modal, KS, PhaseDist) — the blend space needs all corners
