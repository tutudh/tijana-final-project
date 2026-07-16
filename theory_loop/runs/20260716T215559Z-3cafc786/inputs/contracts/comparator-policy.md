# Comparator Policy

Audit every comparator along four dimensions.

## Information parity

At round `t`, the comparator uses the same current observable context as the
learner. It does not observe the current expert label or realized cheap-source
loss before its action. If it knows the stationary data distribution, say so.

## Action parity

Use the same model-call, expert, audit, correction, and release semantics. If a
distribution-aware comparator needs no learning audits, the learner's
exploration audits remain part of regret rather than disappearing from cost.

## Complete cost accounting

Count model calls, expert deferrals, audits, and corrections for both learner
and comparator. State whether predictions are precomputed or called
adaptively. Do not equate expert-query savings with total savings when other
components are nonzero.

## Risk and probability parity

Define released-label, counterfactual cheap-source, and estimated-feedback loss
separately. Match the target's horizon and probability semantics and identify
all randomness covered by the guarantee.

