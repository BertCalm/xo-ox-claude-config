# DB003 — Init Patch Philosophy: Immediate Beauty vs. Blank Canvas

*Opened: 2026-03-14 | Status: UNRESOLVED*

## The Tension

When an engine loads for the first time, should the init patch be immediately beautiful (engaging the user emotionally) or a neutral starting point (inviting the user to build)?

## Vangelis + Kakehashi: Immediate Beauty

"The first sound someone hears defines their relationship with the instrument. The init patch should make someone say 'oh, that is interesting.' A beginner who hears silence or a raw waveform will close the plugin and never return."

Evidence:
- XOceanic's init patch praised universally — warm string ensemble, complexity hidden behind defaults
- XOverworld's NES pulse init criticized — "tells too small a story"
- Snap's init patch in no-man's-land between percussion and pluck
- XObese's init patch praised — Mojo at 0.5 produces immediate warmth

## Schulze: Blank Canvas

"Beauty should be *discovered*, not given. The init patch should be minimal, clear, unadorned. The pulse wave Init is correct: it is the seed from which the player grows their own forest."

## Engines Where This Matters

| Engine | Init Quality | Ghost Assessment |
|--------|-------------|-----------------|
| XOceanic | Beautiful strings immediately | Perfect (Kakehashi, Vangelis) |
| XObese | Warm, massive pad | Excellent (Pearlman) |
| XOverworld | Single NES pulse | "Tells too small a story" (Kakehashi) |
| Snap | Medium snap, medium decay | "No-man's-land" (Kakehashi, Pearlman) |
| XOwlfish | Warm dark bass | Good (Pearlman) |

## Current Leaning

The majority of ghosts favor immediate beauty (5 vs. 1), but Schulze's position has philosophical weight for experimental/ambient engines where discovery is part of the identity. The resolution may be engine-dependent: performance instruments need immediate beauty; experimental instruments may benefit from neutral starts.
