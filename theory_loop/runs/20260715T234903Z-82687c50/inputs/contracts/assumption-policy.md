# Assumption Policy

Use an assumption ladder: begin with the weakest interpretable setting, attack
the target, and add only assumptions that escape a documented obstruction.
Every change must appear in the artifact's assumption change log.

## Admissible problem assumptions

Examples include i.i.d. stochastic arrivals, stationarity or an explicit mixing
condition, bounded loss and cost, a known safe expert, a finite or otherwise
learnable policy class, and a globally interpretable realizability or
feasibility condition. An active problem assumption needs a mathematical
statement, operational meaning, diagnostic or falsification method, and the
conclusion that needs it.

## Algorithm choices

Audit floors, forced exploration, clipping, proxy floors, step-size schedules,
and finite grids are design choices. Record their cost, bias, approximation, or
rate effects; do not describe them as properties of the data-generating world.

## Rejected conditions

Strict complementarity, uniqueness of an optimal dual price, optimizer-local
curvature, local nondegeneracy, and a margin defined only around an unknown
optimal policy or optimizer cannot be active theorem assumptions. Also reject
conditions introduced solely to close a proof when they lack an operational
interpretation or diagnostic.

## Assumption card

Each assumption uses this human-readable card:

- Mathematical statement
- Operational meaning
- Diagnostic or falsification
- Required by
- Optimizer-local: `yes` or `no`
- Classification: `problem`, `algorithm`, or `rejected`

