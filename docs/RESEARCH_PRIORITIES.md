# Cost-Aware PAC Labeling: Research Priorities

Snapshot date: 2026-07-13.

This is the ordered roadmap from the current project to a research-paper draft.
Current results and limitations live in
[`RESEARCH_STATE.md`](RESEARCH_STATE.md).

## Current Assessment

The project is a strong course report and an early research prototype, not yet
a submission-ready paper. The candidate contribution is online audited PAC
labeling that controls finite-horizon released-label error under partial
feedback while approaching the cost of a defined feasible comparator.

This is a target, not an established novelty claim. The offline LP view should
support the derivation rather than serve as the headline contribution.

## P1: Prove an Honest Cost Guarantee

Define total cost to include every paid model call, expert deferral, audit, and
correction. Choose one primary comparator and target both
`error <= epsilon T + o(T)` and
`cost <= comparator cost + o(T)`.

If cost regret is impossible in the fully adversarial setting, an impossibility
or audit-cost lower bound followed by a positive result under a minimal
assumption is an acceptable—and potentially stronger—contribution.

## P2: Run a Real Multi-Source Online Benchmark

Use at least two independently trained real models or real non-expert
annotators. Routing features must precede the expert label, and all incurred
model, audit, and correction costs must be counted. Include an i.i.d. stream and
at least one distribution- or source-reliability-shift stream.

Report final and counterfactual loss, violations of `epsilon` and
`epsilon + B_T`, total cost and its components, audit rate, routing frequency,
and cost gap to the oracle. Keep the parity construction only as a sanity check.
