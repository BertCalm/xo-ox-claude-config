# B007 — Ouroboros's Velocity Coupling Outputs

*Blessed: 2026-03-14 | Engine: Ouroboros | Ghost: Dave Smith*

## The Blessed Feature

Ouroboros routes velocity to its coupling outputs — meaning how hard you play doesn't just affect Ouroboros's own sound, but modulates the parameters of every other engine it's coupled to. Velocity becomes a cross-engine expressive tool.

## Why It Is Protected

This is "unique in the gallery" — no other engine routes velocity to coupling. It turns Ouroboros into an expressive controller for the entire XOmnibus ecosystem. A hard keystrike on Ouroboros can brighten XOblongBob's filter, widen XOceanic's chorus, intensify XOdyssey's Climax. The chaos engine becomes a conduit for human expression across the gallery.

## Prism Sweep Implementation (Round 11)

**"Aizawa Mobile" preset** (`Ouro_Aizawa_Mobile.xometa`) is the canonical B007 demonstration: the Aizawa attractor with velocity coupling outputs feeding into a second engine. Playing hard on the keyboard drives the coupling signal high, reshaping the target engine's character in proportion to keystrike force. The velocity-as-coupling-signal pattern is fully audible and immediately playable.

See `Docs/ouroboros_guide.md` for the full topology of velocity coupling output routing.

## Do Not

- Remove velocity from coupling outputs
- Make coupling outputs static (velocity-independent)
- Limit coupling to audio-only (the velocity modulation IS the unique feature)
