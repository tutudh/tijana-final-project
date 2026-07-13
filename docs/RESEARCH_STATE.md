# Cost-Aware PAC Labeling: Research State

Snapshot date: 2026-07-13.

This document records the current research question, technical approach,
experimental evidence, limitations, and concise priority summary. The detailed
research roadmap lives in
[`RESEARCH_PRIORITIES.md`](RESEARCH_PRIORITIES.md). Setup and reproduction
commands live in [`README.md`](../README.md); durable agent rules live in
[`AGENTS.md`](../AGENTS.md).

## Research Problem

For a fixed pool of items, choose among an expert and one or more cheap labeling
sources. Minimize average labeling cost subject to an average-loss constraint
of at most `epsilon` with high probability.

The current paper assumes normalized loss in `[0, 1]`. Most main results use:

- expert action: zero loss and unit cost;
- cheap model actions: unknown realized loss and zero deployment cost; and
- proxy losses, such as `1 - confidence`, to route or defer without observing
  the current expert label.

## Current Technical Approach

1. **LP formulation and dual price.** The oracle labeling problem is a linear
   program. Its single global error constraint produces a scalar dual variable
   `lambda`, interpreted as the shadow price of error. At a fixed price, each
   item chooses the action minimizing `cost + lambda * loss`.
2. **Offline PAC labeling.** Replace unknown losses with fixed proxy losses,
   use a labeled calibration sample to certify the induced threshold policy,
   and select the least conservative feasible price. Under equal cheap-source
   costs, routing is independent of `lambda` and the policies are nested, so a
   monotonicity argument avoids a union bound over thresholds.
3. **Online audited labeling.** Maintain a time-varying price and audit a random
   subset of AI decisions. An inverse-probability, centered feedback signal
   updates the price. The theorem controls finite-horizon error by
   `epsilon + B_T`, where `B_T = O(T^{-1/2})`; it is not a cost-regret result.

## Contribution Status

The reference paper *Probably Approximately Correct Labels* by Candes, Ilyas,
and Zrnic already contains single-model PAC labeling, multi-model PAC routing,
learned uncertainty recalibration, and cost-sensitive routing. The current LP
view is primarily an optimization-first unification and explanation rather than
an established novelty claim.

Candidate contributions that still need to be established include:

- a genuinely new online audited formulation or stronger online guarantee;
- routing under real heterogeneous models and nonzero heterogeneous costs; or
- a new cost/error or robustness guarantee not already implied by PAC routing.

## Experimental Protocol and Data

- ImageNet contains 50,000 rows with base model error `0.21688`.
- ImageNetV2 contains 10,000 rows with base model error `0.3533`.
- Main experiments use `alpha = 0.05`, `epsilon` in `{0.05, 0.10, 0.15}`, and
  500 trials in the tracked results.
- Offline calibration uses `m = 0.2T` samples with replacement and 202 policies:
  the expert-only policy plus 201 thresholds from 0 to 1.

## Representative Tracked Results

Results below use `epsilon = 0.10`.

| Setting | Dataset | Method | Mean error | Violation rate | Budget saved |
|---|---|---|---:|---:|---:|
| One source | ImageNet | LP fixed price | 0.0873 | 0.0000 | 0.7848 |
| One source | ImageNetV2 | LP fixed price | 0.0718 | 0.0000 | 0.5457 |
| Two source | ImageNet | LP routing | 0.0873 | 0.0000 | 0.7848 |
| Two source | ImageNet | Best single, Bonferroni | 0.0879 | 0.0000 | 0.4746 |
| Two source | ImageNetV2 | LP routing | 0.0718 | 0.0000 | 0.5457 |
| Two source | ImageNetV2 | Best single, Bonferroni | 0.0720 | 0.0000 | 0.3587 |
| Online, audit `p=0.2` | ImageNet | Audited update | 0.0737 | 0.0000 | 0.6115 |
| Online, audit `p=0.2` | ImageNetV2 | Audited update | 0.0783 | 0.0000 | 0.4681 |

## Interpretation Constraints

The two-source result is a proof of concept, not real multi-model evidence. The
sources are synthesized using the parity of the **true class**: each source
retains the base predictor on one parity half and emits a low-confidence random
label on the other. This deliberately makes the sources complementary and
makes lower-proxy routing nearly oracle-quality.

The online results contain finite-sample failures at aggressive audit settings.
For example, ImageNetV2 at `epsilon=0.05` and `p=0.1` has a final violation rate
of `0.184`. Do not summarize the online sweep as uniformly controlling error at
the nominal `epsilon`. The experiments target `epsilon`, not the theorem-adjusted
target `epsilon - B_T`.

## Known Reproducibility and Paper Limitations

- `requirements.txt` lists package names without version pins. There is no
  lockfile, automated test suite, CI workflow, or standard lint command.
- The paper's abstract and discussion/conclusion are commented out. The title
  emphasizes online labeling even though much of the paper and evidence is
  offline.
- The repository has no documented license.
- The two-source experiment uses synthetic complementary labelers rather than
  multiple real models.
- The online theorem controls error with finite-horizon slack; it is not a
  cost-regret result, and the nominal-error experiments do not establish
  high-probability control at `epsilon`.

## Research Priorities

The project is a strong course-project report and an early research
prototype, but it is not yet a submission-ready research paper. Three
substantive gaps remain:

1. establish a novelty claim that survives comparison with PAC labeling,
   online learning-to-defer, partial-feedback conformal prediction, active
   labeling, and constrained online optimization;
2. prove a non-vacuous online cost-efficiency guarantee, with an explicit
   comparator and honest accounting for model calls, deferrals, audits, and
   corrections; and
3. run a real multi-source online benchmark with heterogeneous costs,
   distribution or source-reliability shift, and strong deployable and oracle
   baselines.

The highest-value next step is the novelty/comparator audit, followed by the
cost theorem. The real benchmark should be designed around that theorem
before substantial experimental effort is spent. See
[`RESEARCH_PRIORITIES.md`](RESEARCH_PRIORITIES.md) for the detailed roadmap,
literature lanes, theorem target, experimental requirements, and
research-ready completion criteria.
