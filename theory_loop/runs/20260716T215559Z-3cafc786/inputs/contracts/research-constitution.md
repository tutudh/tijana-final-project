# Research Constitution

This constitution is the invariant boundary for every discovery, search,
proof, and review stage. It is independent of any particular algorithm, rate,
optimizer, or theorem candidate.

1. Define the action-time information timeline. State what is observable before
   each model call, routing action, expert deferral, audit decision, correction,
   release, and update. Online actions and audit probabilities must be
   predictable with respect to the stated filtration.
2. Keep three losses distinct: final released-label loss after any correction,
   counterfactual cheap-source loss used to assess the uncorrected action, and
   estimated or importance-weighted feedback used by the learner.
3. Total cost includes every paid model call, expert deferral, audit, and
   correction. State when each component is incurred and use the same
   accounting in learner and comparator objectives.
4. The learner and comparator use the same action-time observable information
   and action space. Neither sees the current expert label or realized
   cheap-source loss before acting. A distribution-aware stochastic comparator
   may know the data distribution only when this is stated explicitly.
5. State the policy class, horizon, probability space, sources of randomness,
   and whether each guarantee is fixed-horizon, anytime, in expectation, or
   high probability.
6. Separate problem assumptions from algorithm choices and rejected
   proof-only conditions. Every active problem assumption must have a deployment
   interpretation and a diagnostic or falsification route.
7. A model output is always a theorem or proof candidate. `COMPLETE_CANDIDATE`
   and a reviewer `PASS` are workflow statuses, not claims that a theorem has
   been established.
8. Novelty assessment and promotion into the paper or research-state documents
   require human review. Absence of located prior work is never evidence of
   novelty.

