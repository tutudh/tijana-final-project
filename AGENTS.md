# Cost-Aware PAC Labeling: Agent Instructions

This file contains durable instructions for agents modifying the repository.
Keep project setup and commands in `README.md`, and keep the dated research
snapshot in `docs/RESEARCH_STATE.md`. Keep the detailed research roadmap in
`docs/RESEARCH_PRIORITIES.md`. Keep all slide-deck sources, compiled outputs,
and presenter notes together under `slides/`.

## Read Before Acting

- Always inspect `git status` before editing and preserve unrelated or
  untracked user work.
- Read `README.md` when a task involves setup, dependencies, data paths,
  document builds, experiment commands, or reproduction.
- Read the relevant `.tex` source when editing the paper or the presentation;
  slide and presenter-note sources live under `slides/`.
- Read `docs/RESEARCH_STATE.md` when a task involves the research question,
  theorem assumptions, experimental design, reported evidence,
  interpretation, limitations, or the concise priority summary.
- Read `docs/RESEARCH_PRIORITIES.md` when a task involves novelty, related-work
  coverage, target cost guarantees, future benchmark design, research
  priorities, or paper-readiness criteria.
- Inspect the generating script and result file before changing any reported
  number, table, or plot.

## Contribution Boundary

Be conservative about novelty claims. The reference paper *Probably
Approximately Correct Labels* by Candes, Ilyas, and Zrnic already contains:

- single-model PAC labeling;
- multi-model PAC routing;
- learned uncertainty recalibration; and
- cost-sensitive routing.

Do not present those ideas alone as new contributions. The current LP view is
primarily an optimization-first unification and explanation. When editing the
paper, explicitly distinguish a reformulation, a new theorem, and an empirical
contribution.

## Proof and Interpretation Invariants

- Offline proxy scores must be fixed before the final calibration indices are
  sampled. If labels are reused to fit proxies and certify policies, use sample
  splitting, cross-fitting, or a uniform argument that accounts for
  adaptivity.
- Calibration indices in the current finite-pool theorem are sampled uniformly
  with replacement.
- The no-union-bound argument relies on equal cheap-source costs: the selected
  cheap source then does not change with `lambda`, and increasing `lambda` only
  moves items from a cheap source to the expert.
- Under unequal cheap-source costs, source selection can change with `lambda`.
  Do not reuse the monotone proof without justification; a uniformly certified
  finite price grid is the documented fallback.
- Online decisions and audit probabilities must be predictable. Audits are
  conditionally independent Bernoulli draws with probability at least
  `p_min`, and proxy losses are floored by a positive `rho`.
- Audited AI labels are corrected to the expert label. Distinguish final
  released-label loss from the counterfactual AI loss used for feedback.
- The online experiments target `epsilon` directly rather than
  `epsilon - B_T`. They do not empirically establish high-probability control
  at `epsilon`; interpret them against the theorem's `epsilon + B_T` bound.
- The two-source experiment is synthetic and uses the parity of the true class
  to construct complementary sources. Always disclose this when reporting or
  interpreting its results.

## Repository-Safe Working Rules

- Treat `ref/pac label.pdf`, modified PDFs, tracked result files, and untracked
  material as active user work unless the task explicitly places them in
  scope.
- Do not silently strengthen theorem statements. Preserve the distinction
  between finite-pool, population, and online guarantees.
- Use the commands documented in `README.md`; do not maintain a second command
  list here.
- Run smoke experiments into `/private/tmp`. Do not overwrite tracked
  500-trial outputs unless the task explicitly requests regeneration.
- For diagnostic LaTeX builds, use an output directory under `/private/tmp`
  unless updating compiled PDFs is part of the requested deliverable.
- Keep new slide sections, slide build artifacts, and presenter-note files
  under `slides/`; do not add them back at the repository root.
- Keep paper tables, CSV summaries, plots, and script defaults synchronized.
- When changing an experiment, record the seed, number of trials, calibration
  size, confidence level, threshold grid, dataset construction, and output
  path.
- Explicitly label synthetic data, oracle quantities, counterfactual metrics,
  and post-audit corrected metrics in prose and figures.

## Documentation Ownership

- Update `README.md` when setup, paths, supported commands, or repository
  entry points change.
- Update `docs/RESEARCH_STATE.md` when the research question, active approach,
  experimental evidence, limitations, or concise priority summary changes.
- Update `docs/RESEARCH_PRIORITIES.md` when the novelty boundary, target
  theorem, related-work plan, future benchmark requirements, or paper-readiness
  criteria change.
- Update this file only when durable agent behavior, proof safeguards, or
  repository safety rules change.
