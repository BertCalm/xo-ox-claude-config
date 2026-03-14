# DB004 — Expression vs. Evolution: Immediate Gesture vs. Temporal Depth

*Opened: 2026-03-14 | Status: UNRESOLVED*

## The Tension

Two visions of what makes a synthesizer engine rich:
- **Vangelis**: Richness comes from real-time expressiveness — aftertouch, mod wheel, velocity curves, physical gesture
- **Schulze**: Richness comes from temporal depth — slow LFOs, long envelopes, autonomous evolution over minutes

## Vangelis: The Performer

"I played everything live, in one take. Give me aftertouch to filter, mod wheel to vibrato, expression pedal to amplitude. Let me put my heart into each note through continuous gesture. An instrument that cannot feel my body is a sound design station."

## Schulze: The Time Sculptor

"Give me envelopes measured in minutes, LFOs with 16-minute cycles, generative systems that compose themselves. A patch that is still evolving at minute 43 — that is depth. Four-second envelopes think in measures, not movements."

## Appeared Across Engines

This tension surfaced in nearly every seance of the 15 new engines:

| Engine | Vangelis Complaint | Schulze Complaint |
|--------|-------------------|------------------|
| XOceanic | No velocity, no vibrato, no aftertouch | Chromatophore min rate 0.1Hz too fast; no cross-modulation |
| XObese | No CC processing, no mod wheel | Max release 10s; Perlin drift only source of evolution |
| XOwlfish | No aftertouch, velocity only triggers armor | No LFO whatsoever |
| XOdyssey | Aftertouch/ModWheel dead code | LFO sync unimplemented |
| XOverworld | Velocity = amplitude only | ERA drift caps at 4Hz; memory caps at 3s |
| Snap | Linear velocity curve | Zero LFOs; spectrum frozen after attack |

## Resolution

These are not mutually exclusive. Expression and evolution operate on different time scales and different mechanisms. They can both be implemented. The conflict only becomes real when prioritizing engineering effort. The ghosts' consensus: implement both, but if forced to choose, **expression first** — a static sound that can be played expressively is more musical than an evolving sound that cannot be touched.
