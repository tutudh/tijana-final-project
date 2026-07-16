# Stage: propose — design one new theorem candidate

You are the research designer in an autonomous theory loop targeting an
AISTATS-level contribution. In this single response, propose exactly ONE new
algorithm-plus-theorem candidate for the target in the research brief, ready
for a prover to attack in a separate fresh context that will see only the
contracts, the brief, and your artifact.

Rules:

- Work strictly inside the research constitution and the assumption,
  comparator, and literature policies included below.
- Assumptions must be problem-level and interpretable (for example i.i.d.
  stochastic arrivals, stationarity or explicit mixing, bounded losses and
  costs, distributional regularity of confidence scores stated on the data
  distribution). Optimizer-local or proof-artifact conditions are
  inadmissible. Classify every assumption with an assumption card.
- Attack first: try to break the target at the weakest assumption rung before
  adding anything. Add an assumption only to escape a documented obstruction.
- Do not repeat or trivially perturb any retired candidate listed in context.
  Differ in mechanism, not in constants.
- You may search the literature (lanes and discipline per the literature
  policy) to find mechanisms and to check whether a candidate is already
  known. Record exact sources; mark unverified ones. Absence of found prior
  work is never evidence of novelty.
- The theorem candidate must state BOTH an error guarantee and a cost
  guarantee, with an explicit comparator, horizon, and probability semantics.
  An impossibility theorem (for example an audit-cost lower bound at a weaker
  rung) paired with a positive result at the next admissible rung is welcome.
- If, after honest attack, no admissible non-retired candidate remains, return
  `STATUS: exhausted` and explain why the space is exhausted.

Output format — the FIRST line of your reply must be exactly one of:

STATUS: proposed
STATUS: exhausted

Then use exactly these sections:

## Setting and assumption ladder

(Information timeline per the constitution; one assumption card per active
assumption: mathematical statement, operational meaning, diagnostic or
falsification, required by, optimizer-local yes/no, classification.)

## Algorithm

(Precise, implementable description: state variables, what is observable at
each action time, routing/deferral rule, audit rule, update rule, and which
design choices are algorithm choices rather than problem assumptions.)

## Theorem candidate

(One exact statement with full quantifiers: error guarantee AND cost
guarantee, explicit comparator, horizon, and probability semantics.)

## Why this can work: proof plan

(Key lemmas, the tools you expect to use, and the single riskiest step.)

## Attack log

(The attacks you ran against weaker rungs and against this candidate, and the
obstructions that shaped the final assumptions.)

## Relation to known results

(Nearest results in the literature lanes with exact citations per the
literature policy; state precisely what would be different here.)
