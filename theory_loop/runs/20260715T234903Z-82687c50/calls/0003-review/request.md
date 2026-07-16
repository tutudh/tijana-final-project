# Stage: review — independent adversarial referee report

You are an independent referee with fresh eyes. You did not write this proof,
and you must not trust it. Your only inputs are the research contracts, the
brief, the theorem candidate, and the proof candidate. Judge as a careful
AISTATS reviewer whose name is on the report.

Rules:

- Verify the mathematics step by step. Do not extend charity: a gap is a gap,
  an unproved "clearly" is a gap, a constant that appears from nowhere is a
  gap.
- Check admissibility, not only correctness: every active assumption must be
  problem-level per the assumption policy (no optimizer-local or
  proof-artifact conditions smuggled in); the comparator must satisfy the
  comparator policy; every cost component must be accounted on both sides;
  actions and audit probabilities must be predictable with respect to the
  stated filtration; the three losses must never be conflated.
- Check that claimed rates are actually derived, quantifiers are coherent,
  randomness is fully covered, and each cited external result is used within
  its stated conditions. You may search to verify a citation.
- Do not repair the proof. Identify the smallest concrete failure instead.
- Verdict meanings: `pass` — you would defend every step to a colleague; both
  the error and the cost guarantee hold as stated under admissible
  assumptions. `revise` — the approach appears sound but at least one
  identified step is broken or incomplete and looks repairable. `reject` — a
  fatal flaw: the theorem is false or unsupported at its core, an assumption
  is inadmissible, or the comparator or cost accounting is unsound.

Output format — the FIRST line of your reply must be exactly one of:

VERDICT: pass
VERDICT: revise
VERDICT: reject

Then use exactly these sections:

## Verdict rationale

(The decisive reasons for the verdict.)

## Step-by-step audit

(Each lemma and each main-proof step: verified / gap / error, with the
specific line of reasoning checked.)

## Smallest failure

(For revise or reject: the most concrete minimal broken step, with a
counterexample to the step where possible. For pass: the weakest surviving
step and why it nevertheless holds.)

## Required author action

(For revise: exactly what must be fixed, point by point. For reject: why the
flaw is not repairable within this candidate. For pass: none.)

# Context: contracts/research-constitution.md

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

# Context: contracts/assumption-policy.md

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

# Context: contracts/comparator-policy.md

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

# Context: contracts/literature-policy.md

# Targeted Literature Policy

Search has two permitted triggers.

1. **Mechanism search** follows a failed impossibility or algorithm derivation
   when no credible candidate remains. Its input must state the desired result,
   exact obstruction, excluded approaches, and the kind of tool needed.
2. **Proof search** follows a precise blocked lemma, concentration step,
   partial-feedback estimate, regret step, or other proof obligation. It is not
   a broad novelty survey.

Search the most relevant lane first, using this default order when the
obligation does not dictate otherwise:

1. online risk control;
2. intermittent or partial-feedback conformal methods;
3. online stochastic linear programming;
4. revenue management;
5. constrained contextual bandits;
6. online learning with long-term constraints;
7. label-efficient prediction;
8. online selective classification; and
9. online learning to defer.

For every source, record the primary paper and stable URL, exact theorem,
lemma, proposition, or section, arrival and feedback models, comparator,
assumptions, probability semantics, error/cost/regret guarantee, whether the
supporting full text was checked, and a condition-by-condition mapping to the
current obligation. A mismatch is an `analogy`, never reusable proof evidence.

`ref/RELATED_WORK_REPORT_ZH.md` is a search index only. It does not become proof
evidence without verification against the primary full text. Search output
cannot establish novelty or repair a proof.

# Context: research brief

# Research brief: online labeling with joint error and cost guarantees

Venue target: AISTATS 2026. This brief frames the standing goal for every
stage. The research constitution and the assumption, comparator, and
literature policies included in context are binding.

## Problem setting

Items arrive online at rounds `t = 1, ..., T`. For each item the learner
chooses among one or more cheap labeling sources (for example model
predictions with raw confidence scores; losses normalized to `[0, 1]`; costs
possibly heterogeneous and nonzero) and a costly expert whose label is
authoritative (reference instantiation: unit cost, zero loss). The learner may
audit an AI-labeled item: pay the expert cost, observe the true label, and
release the corrected label. Feedback is partial — expert labels are observed
only on deferred or audited items. Decisions and audit probabilities must be
predictable with respect to the natural filtration, and released-label loss,
counterfactual source loss, and estimated feedback must be kept distinct. The
precise instantiation (number of sources, cost structure, score model) is the
designer's choice and must be stated per the constitution.

## Target

An online labeling algorithm and a theorem establishing, simultaneously and
under admissible problem-level assumptions:

1. **Error guarantee**: released-label error at most `epsilon * T + o(T)`
   (high probability preferred; state the exact semantics), and
2. **Cost guarantee**: total cost — every paid model call, expert deferral,
   audit, and correction — at most the cost of an explicit admissible
   comparator plus `o(T)`.

An impossibility result (for example an audit-cost lower bound at a weaker
assumption rung) paired with a positive result at the next admissible rung is
an acceptable, potentially stronger, contribution shape.

## Mechanism directions for this run (binding)

The previous run produced an explore-then-commit theorem (APS-LP, listed
below) whose strength is carried by two crutches: a full-audit calibration
prefix followed by a frozen deployment policy, and a finite preregistered
policy library that treats raw confidence scores as arbitrary given
quantities. This run must explore the two directions that remove exactly
those crutches. A candidate that reduces to explore-then-commit with a
full-audit prefix, or whose policy class is an arbitrary preregistered
finite library over uninterpreted scores, is retired by default and must
not be proposed.

1. **Online calibration of uncertainty — scores are learned, not given.**
   Raw confidence scores carry no assumed meaning. For each cheap source, the
   algorithm must estimate that source's conditional error rate (its
   uncertainty score) from the true losses observed on audited or deferred
   rounds — for example online binning or isotonic-style calibration on the
   score space — and route on the *calibrated* estimate. Distributional
   regularity of the raw score (stated on the data distribution, checkable in
   principle from data) is admissible; a margin or separation condition at an
   unknown optimal threshold is not. Discretization grids, bin widths, and
   calibration update schedules are algorithm choices whose approximation and
   estimation costs must appear explicitly in the bounds.

2. **FTRL-style adaptive selection — no learning/deployment phase split.**
   At each round the routing rule is chosen by follow-the-regularized-leader
   (or online mirror descent / online primal-dual) applied to cumulative
   *estimated* cost and risk built only from feedback observed on audited or
   deferred rounds, with importance weighting driven by the predictable audit
   probabilities. Audit probabilities must be adaptive and may decay over
   time; forced-audit floors are algorithm choices whose cost must be charged
   in full. The cost guarantee must survive adaptivity: sublinear regret in
   total cost against the admissible comparator, with the error constraint
   held anytime or at horizon (state which).

A single candidate combining both directions is preferred; a candidate that
delivers one direction cleanly is acceptable. An impossibility result showing
one direction is unattainable at an admissible rung (for example, no
adaptive-audit algorithm achieves `o(T)` cost regret without a stated
admissible condition) paired with a positive result under that condition is a
strong outcome. Beating APS-LP's `T^{2/3}` cost-regret rate with an adaptive
mechanism, or proving `T^{2/3}` unimprovable for an admissible class, are
both valid targets.

## Assumption discipline (binding)

Admissible assumptions are about the problem itself: i.i.d. or otherwise
stochastic non-adversarial arrivals, stationarity or an explicit mixing
condition, bounded losses and costs, distributional regularity of confidence
scores stated on the data distribution and checkable in principle from data, a
known safe expert. Inadmissible: optimizer-local or proof-artifact conditions
— anything defined only around an unknown optimal policy, price, or threshold
(strict complementarity, uniqueness of an optimal dual price, local
nondegeneracy or curvature at the optimum, a margin defined only at the
unknown optimizer), and any condition introduced solely to close a proof that
lacks an operational interpretation and diagnostic. A borderline condition
must be classified honestly and flagged for human review, never assumed
silently.

## What already exists (do not re-derive as a contribution)

- Candes, Ilyas, and Zrnic, "Probably Approximately Correct Labels": offline
  single-model PAC labeling, multi-model PAC routing, learned uncertainty
  recalibration, and cost-sensitive routing.
- This project's current online theorem: audited price updates control
  finite-horizon released-label error at `epsilon + B_T` with
  `B_T = O(T^{-1/2})` under predictable audits with a probability floor. It
  has NO cost guarantee.
- Run 20260715T214657Z-2d6432b6 (APS-LP, pending human review):
  explore-then-commit with a full-audit prefix of length `T^{2/3}` over a
  finite preregistered policy library; joint high-probability guarantees of
  released error `epsilon*T + O(sqrt(T log T))` and cost regret
  `O(G (1 + 1/epsilon) T^{2/3} sqrt(log(N T)))` against the
  distribution-aware LP comparator over the library. Its mechanism —
  full-audit prefix, one-shot empirical LP, frozen deployment mixture — is
  retired for this run.
- The offline LP / dual-price view is an explanatory reformulation, not a
  novelty claim.

## Literature lanes

Online risk control; intermittent or partial-feedback conformal methods;
online calibration and calibeating; label-efficient prediction and selective
sampling; bandits with knapsacks and constrained contextual bandits; online
learning with long-term constraints and online primal-dual methods; online
stochastic linear programming; revenue management; online learning to defer.
Follow the literature policy's exact-source discipline; absence of found
prior work is never evidence of novelty.

## Honesty

Every model output is a theorem or proof candidate. A reviewer `pass` is a
workflow status, not an established result. Promotion into the paper or the
research-state documents requires human review.

# Context: theorem candidate

STATUS: proposed

## Setting and assumption ladder

Consider one cheap model and one authoritative expert. Calling the cheap model costs \(c_M\in[0,1]\) and reveals its prediction \(\widehat Y_t\) and raw score \(S_t\in[0,1]\). Define the unobserved counterfactual cheap-source loss
\[
L_t=\mathbf 1\{\widehat Y_t\neq Y_t\}.
\]
An expert call costs \(1\), returns \(Y_t\), and has zero released-label loss. Correcting an audited error has additional cost \(c_R\in[0,1]\).

Let \(\mathcal F_{t-1}\) contain past model outputs, actions, audit coins, released labels, costs, and expert labels only from deferred or audited rounds. At round \(t\):

1. Before the model call, the learner computes an \(\mathcal F_{t-1}\)-measurable routing policy.
2. It pays \(c_M\), then observes \((\widehat Y_t,S_t)\), but not \(Y_t\) or \(L_t\).
3. It randomizes between cheap routing and expert deferral.
4. Conditional on cheap routing, it chooses an audit probability using only \(\mathcal F_{t-1}\), \((\widehat Y_t,S_t)\), and the routing probability.
5. If deferred or audited, it pays the expert, observes \(Y_t\), and releases \(Y_t\). Otherwise it releases \(\widehat Y_t\).
6. Correction cost \(c_R\) is incurred exactly when an audited cheap prediction is wrong.
7. Only then are calibration and FTRL statistics updated.

Thus routing and audit probabilities are predictable before the current expert label and cheap-source loss.

The assumption ladder is: bounded stationary data with arbitrary score-error relation fails by non-identifiability; the proposed rung adds only global smoothness of the conditional error curve.

**A1 — Stationary stochastic arrivals**

- Mathematical statement: \((S_t,\widehat Y_t,Y_t)_{t\ge1}\) are i.i.d. from an unknown distribution \(P\). The cheap model is fixed during the horizon.
- Operational meaning: workload composition and model behavior do not drift during deployment.
- Diagnostic or falsification: compare score histograms and importance-weighted error estimates across time blocks; apply preregistered change-point or two-sample tests.
- Required by: converting past calibrated risk estimates into conditional risk guarantees for each new routing policy.
- Optimizer-local: `no`
- Classification: `problem`

**A2 — Bounded loss, known costs, safe expert**

- Mathematical statement: \(L_t\in\{0,1\}\); the expert returns \(Y_t\) correctly; \(c_M,c_R\in[0,1]\) and the expert cost \(1\) are fixed and known.
- Operational meaning: expert labels are the deployment reference standard and all paid operations have logged bounded costs.
- Diagnostic or falsification: double-label a random expert sample, adjudicate disagreements, and reconcile model, expert, audit, and correction invoices.
- Required by: released-error validity, concentration, and complete cost accounting.
- Optimizer-local: `no`
- Classification: `problem`

**A3 — Global score-error smoothness**

- Mathematical statement: a version of
  \[
  m(s)=\Pr(L_t=1\mid S_t=s)
  \]
  exists and satisfies \(|m(s)-m(s')|\le L|s-s'|\) for all score-support points, for a finite constant \(L\). No monotonicity or calibration identity such as \(m(s)=1-s\) is assumed.
- Operational meaning: numerically nearby raw scores may be badly calibrated, but their true error rates cannot change arbitrarily abruptly.
- Diagnostic or falsification: on a held-out or importance-weighted audited stream, construct simultaneous binwise error intervals and test whether neighboring-bin differences exceed \(L\) times their separation.
- Required by: competing with all measurable score-routing policies rather than only the algorithm’s histogram class.
- Optimizer-local: `no`
- Classification: `problem`

## Algorithm

Call the method **adaptive calibration-UCB FTRL (ACU-FTRL)**.

For known horizon \(T\), confidence \(\delta\), and target \(\epsilon>0\), set
\[
K=\lceil T^{1/4}\rceil,\qquad
\gamma_t=t^{-1/4},\qquad
z=\log\frac{32KT}{\delta},
\]
and partition \([0,1]\) into \(K\) equal bins \(B_1,\ldots,B_K\).

For each bin \(j\), maintain
\[
N_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\},\quad
H_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\}\frac{O_sL_s}{p_s},\quad
V_{t,j}=\sum_{s<t}\mathbf1\{S_s\in B_j\}\frac1{p_s},
\]
where \(O_s\) indicates that an expert label was observed and \(p_s\) was its predictable probability. When \(O_s=0\), the contribution to \(H\) is recorded as zero without observing \(L_s\).

At \(t=1\), use the expert. For \(t\ge2\), let \(n=t-1\),
\[
\widehat\pi_{t,j}=\frac{N_{t,j}}n,\qquad
\widehat a_{t,j}=\frac{H_{t,j}}n,
\]
and define
\[
r_{t,j}
=
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}{n}
+\sqrt{\frac{z}{2n}},
\qquad
U_{t,j}=\min\{1,\max\{0,\widehat a_{t,j}+r_{t,j}\}\}.
\]
Here \(\widehat a_{t,j}\) estimates the joint error mass
\(\Pr(S\in B_j,L=1)\). The learned conditional calibration is
\[
\widehat m_{t,j}
=
\operatorname{clip}_{[0,1]}
\left(\frac{H_{t,j}}{N_{t,j}\vee1}\right).
\]
The ratios \(U_{t,j}/(\widehat\pi_{t,j}\vee1/n)\), rather than the raw scores, are the confidence-robust calibrated error scores used for routing.

Before seeing \(S_t\), choose the complete routing vector by constrained FTRL:
\[
x_t\in\arg\min_{\substack{x\in[0,1]^K\\
                         \sum_jU_{t,j}x_j\le\epsilon}}
\left\{
\sum_{j=1}^K N_{t,j}(1-x_j)+\frac12\lVert x\rVert_2^2
\right\}.
\]
The first term is cumulative observable expert-deferral cost; the constraint uses cumulative importance-weighted risk feedback. The quadratic term gives deterministic tie-breaking.

After the model call, let \(J_t\) satisfy \(S_t\in B_{J_t}\), set \(x=x_{t,J_t}\), and draw \(D_t\sim\mathrm{Bernoulli}(x)\), where \(D_t=1\) means cheap routing.

- If \(D_t=0\), defer to the expert.
- If \(D_t=1\), audit with probability
  \[
  q_t(x)=
  \begin{cases}
  \displaystyle\frac{[\gamma_t-(1-x)]_+}{x},&x>0,\\
  0,&x=0.
  \end{cases}
  \]

Let \(A_t\) be the audit indicator on a cheap-routed round. Then
\[
O_t=1-D_t+D_tA_t,\qquad
p_t=\Pr(O_t=1\mid\mathcal F_{t-1},S_t)
     =\max\{1-x,\gamma_t\}.
\]
Hence the rule audits only the shortfall between feedback already supplied by expert deferrals and the desired observation floor. Its expected audit probability is
\[
xq_t(x)=[x+\gamma_t-1]_+\le\gamma_t.
\]

The three losses are distinct:

\[
\text{counterfactual cheap loss}=L_t,\qquad
\text{released loss}=R_t=D_t(1-A_t)L_t,\qquad
\text{feedback estimate}=\widetilde L_t=\frac{O_tL_t}{p_t}.
\]

Total cost is
\[
C_T=c_MT+\sum_{t=1}^TO_t
       +c_R\sum_{t=1}^TD_tA_tL_t.
\]

The uniform grid, \(K\), \(\gamma_t\), confidence radii, and quadratic regularizer are algorithm choices. Their audit, estimation, and approximation costs appear separately below.

## Theorem candidate

For a Borel policy \(a:[0,1]\to[0,1]\), let \(a(s)\) be its probability of releasing the cheap label after observing score \(s\). Define the distribution-aware comparator
\[
C_T^\star
=
T\left[
c_M+
\inf_{\substack{a:[0,1]\to[0,1]\ \mathrm{Borel}\\
                  \mathbb E[a(S)m(S)]\le\epsilon}}
\mathbb E[1-a(S)]
\right].
\]
The comparator knows \(P\), but at action time observes only the same model output and score as the learner, never \(Y_t\) or \(L_t\). It has the same deferral, audit, correction, and release actions. Auditing is weakly dominated by immediate expert deferral because both obtain the expert label at the same expert cost while auditing may additionally incur \(c_R\); hence an optimal comparator can use no audits. When deployed on the i.i.d. stream, every feasible comparator has the same \(\epsilon T+O(\sqrt T)\) high-probability released-error semantics.

For \(n\ge1\), define
\[
A_n=\sum_{s=1}^n\gamma_s^{-1},
\]
and, for \(t\ge2\) with \(n=t-1\),
\[
w_t=
\frac{2\sqrt{2KzA_n}}{n}
+\frac{2Kz}{3n\gamma_n}
+2K\sqrt{\frac{z}{2n}}.
\]
Finally let
\[
\begin{aligned}
B_T={}&1+(1+c_R)
 \left(\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}\right)\\
&+\sum_{t=2}^T
 \left(
 2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
 \right)
+\frac1\epsilon
 \left(
 \frac{LT}{K}+\sum_{t=2}^Tw_t
 \right).
\end{aligned}
\]

**Candidate theorem.** For every \(T\ge16\), \(\epsilon\in(0,1]\), \(\delta\in(0,1/4)\), \(c_M,c_R\in[0,1]\), finite \(L\), and every distribution satisfying A1–A3, ACU-FTRL satisfies, simultaneously with probability at least \(1-\delta\) over the i.i.d. arrivals and all learner routing and audit coins,
\[
\sum_{t=1}^T R_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}},
\]
and
\[
C_T\le C_T^\star+B_T.
\]
Moreover, for a universal constant \(C_0\),
\[
B_T
\le
C_0\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\]
Thus, for fixed \((\epsilon,L,c_M,c_R,\delta)\), released error is
\(\epsilon T+O(\sqrt{T\log T})\) and complete cost regret is
\(O(T^{3/4}\log T)=o(T)\), at the fixed horizon \(T\).

## Why this can work: proof plan

1. **Adaptive importance-weighted calibration.** Conditional on the score and past,
   \[
   \mathbb E[O_tL_t/p_t\mid S_t,L_t,\mathcal F_{t-1}]=L_t.
   \]
   Decompose \(\widehat a_{t,j}-a_j\) into an i.i.d. bin-loss fluctuation and an audit martingale. Freedman’s inequality gives, simultaneously over \(t,j\),
   \[
   a_j=\Pr(S\in B_j,L=1)\le U_{t,j}.
   \]

2. **Per-round population safety.** Since \(x_t\) is computed before the current score and \(U_t^\top x_t\le\epsilon\),
   \[
   \mathbb E[x_{t,J_t}L_t\mid\mathcal F_{t-1}]
   =\sum_ja_jx_{t,j}\le\epsilon.
   \]
   Auditing can only reduce released loss. A stopped Azuma argument then yields the stated realized-error bound.

3. **Comparator discretization.** For any feasible measurable \(a\), set
   \(b_j=\mathbb E[a(S)\mid S\in B_j]\). This preserves expected deferral cost. Lipschitzness gives
   \[
   \sum_ja_jb_j\le\mathbb E[a(S)m(S)]+\frac LK
   \le\epsilon+\frac LK.
   \]

4. **Robust-feasibility scaling without an optimizer margin.** On the confidence event,
   \(U_t^\top b\le\epsilon+L/K+w_t\). Therefore
   \[
   y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
   \]
   is feasible for the round-\(t\) FTRL problem, and its extra expert cost is at most
   \((L/K+w_t)/\epsilon\). This uses the globally safe expert, not strict complementarity or a margin at an unknown threshold.

5. **FTRL cost comparison.** Hoeffding bounds for the fully observed bin frequencies and FTRL optimality imply
   \[
   \mathbb E[1-x_{t,J_t}]
   \le
   \mathbb E[1-a(S)]
   +2K\sqrt{\frac{z}{2(t-1)}}
   +\frac{K}{2(t-1)}
   +\frac{L/K+w_t}{\epsilon}.
   \]

6. **Audit and realized-cost accounting.** The adaptive rule adds at most \(\gamma_t\) expected expert calls and \(c_R\gamma_t\) expected correction cost. A bounded martingale controls realized cost. Balancing
   \[
   \sum_t\gamma_t,\quad
   \sum_t w_t,\quad
   K\sqrt T,\quad
   \frac{T}{K}
   \]
   with \(K=T^{1/4}\) and \(\gamma_t=t^{-1/4}\) gives \(T^{3/4}\) up to logarithms.

The riskiest step is the simultaneous binwise Freedman bound under the feedback probability \(p_t=\max\{1-x_{t,J_t},\gamma_t\}\), because the same importance-weighted observations subsequently determine both \(U_t\) and the FTRL action. A stopped-filtration proof must verify this without conditioning on a future confidence event.

## Attack log

- **A1–A2 without score regularity failed.** Partition the score space into \(M\) regions whose error rates are independently either \(0\) or \(2\epsilon\). A distribution-aware comparator releases cheaply exactly on the safe regions. With \(M\) comparable to \(T\), sublinear expert feedback leaves a constant fraction unidentified: releasing there can violate the error target, while deferring there causes linear cost regret. This is an identifiability obstruction, not a claimed formal lower-bound theorem. It motivated A3.

- **A raw-score threshold was rejected.** No monotonic relationship between score magnitude and error is assumed. Routing uses learned binwise conditional errors, and the continuum comparator may select disjoint score regions.

- **Naive plug-in calibration failed.** Downward estimation errors can make an adaptively selected policy violate the risk constraint. Replacing plug-in estimates with simultaneous joint-error upper bounds makes every deployed policy conditionally safe.

- **Oblivious auditing was wasteful.** A floor \(\gamma_t\) applied after every cheap action wastes labels when FTRL already defers frequently. The chosen rule makes the overall observation probability exactly \(\max\{1-x,\gamma_t\}\), auditing only the shortfall.

- **Faster audit decay failed the variance balance.** With \(K\) bins and observation floor \(t^{-a}\), importance-weighted calibration contributes approximately
  \(\sqrt K\,T^{(1+a)/2}\), audits contribute \(T^{1-a}\), and discretization contributes \(T/K\). Balancing these terms gives \(a=1/4\) and \(K=T^{1/4}\).

- **An exact-boundary comparator initially appeared to require a margin.** Rather than assume separation or strict complementarity at its unknown threshold, the proof scales its binned policy toward the known safe expert, paying the explicit \(1/\epsilon\) sensitivity factor.

- **Cost leakage checks passed.** The comparator also pays every model call. Learner deferrals, audits, and audited corrections are all charged. Exploration audits remain entirely in regret.

- **Phase-split and finite-library checks passed.** Calibration and routing update every round; there is no full-audit prefix or frozen deployment phase. The \(K\)-bin class is a structural approximation to all measurable score policies, not an arbitrary preregistered policy library.

## Relation to known results

- **Offline PAC labeling.** Candès, Ilyas, and Zrnic, [“Probably Approximately Correct Labels”](https://arxiv.org/abs/2506.10908), Theorem 1 and Corollary 1, give high-probability error control on a fixed transductive dataset; Section 2.1 learns recalibrated uncertainty using a small labeled subset. Feedback is collected offline, there is no online cost-regret comparator, and cost-sensitive routing is not accompanied by this candidate’s adaptive regret theorem. Full text checked. The present candidate differs by continuously learning calibration from predictable partial feedback and comparing total sequential cost with a distribution-aware policy.

- **Active sequential risk control.** Xu, Karampatziakis, and Mineiro, [“Active, Anytime-Valid Risk Controlling Prediction Sets”](https://papers.nips.cc/paper_files/paper/2024/file/6eb05d8bc6bd7bb6868c64b5802125bd-Paper-Conference.pdf), Theorem 2, considers an i.i.d. stream, predictable covariate-dependent label probabilities with a floor, and importance-weighted e-processes. It guarantees population risk control simultaneously over time with probability \(1-\alpha\); its label budget is separate and it has no total-cost regret against a routing comparator. Full text checked. It supports the predictability and importance-weighting mechanism, but not the FTRL cost claim.

- **Label-efficient prediction.** Cesa-Bianchi, Lugosi, and Stoltz, [“Minimizing Regret With Label Efficient Prediction,” IEEE TIT 51(6), 2005](https://cesa-bianchi.di.unimi.it/Pubblicazioni/J22.pdf), Theorems 1–2, use Bernoulli label queries and importance-weighted losses for bounded individual outcome sequences. Against the best of finitely many constant predictors, they obtain expected and high-probability regret of order \(T\sqrt{\log N/m}\) with \(m\) queried labels. They have no released-label correction, risk constraint, score calibration, or complete cost comparator. Full text checked. Their query-variance tradeoff is an analogy for the audit term.

- **Constrained online optimization.** Mahdavi, Jin, and Yang, [“Trading Regret for Efficiency: Online Convex Optimization with Long Term Constraints,” JMLR 13, 2012](https://www.jmlr.org/papers/volume13/mahdavi12a/mahdavi12a.pdf), Theorem 8, gives zero cumulative violation and \(O(T^{3/4})\) regret for full-information convex online optimization. It assumes known constraints and Assumption 1, a nonzero boundary-gradient condition. That condition is inadmissible here because it is local to a tightened constraint boundary. Full text checked. ACU-FTRL instead learns the constraint from partial labels and uses upper-confidence feasibility plus scaling toward the safe expert.

- **Concentration tool.** Freedman, [“On Tail Probabilities for Martingales,” Annals of Probability 3(1), 1975](https://projecteuclid.org/euclid.aop/1176996396), Theorem 1.6, is the intended predictable-variance inequality. The original full text was not checked in this run, so this primary citation is marked **unverified**; the exact scalar statement was checked through Tropp’s Theorem 1.1 restatement. It is proof machinery, not evidence of novelty.

No absence-of-prior-work claim is made; novelty and correctness require human review.

# Context: proof candidate under review

STATUS: complete

## Exact theorem

**Candidate theorem.** For every \(T\ge16\), \(\epsilon\in(0,1]\), \(\delta\in(0,1/4)\), \(c_M,c_R\in[0,1]\), finite \(L\), and every distribution satisfying A1–A3, ACU-FTRL satisfies, simultaneously with probability at least \(1-\delta\) over the i.i.d. arrivals and all learner routing and audit coins,
\[
\sum_{t=1}^T R_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}},
\]
and
\[
C_T\le C_T^\star+B_T.
\]
Moreover, for a universal constant \(C_0\),
\[
B_T
\le
C_0\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\]
Thus, for fixed \((\epsilon,L,c_M,c_R,\delta)\), released error is
\(\epsilon T+O(\sqrt{T\log T})\) and complete cost regret is
\(O(T^{3/4}\log T)=o(T)\), at the fixed horizon \(T\).

## Notation and standing assumptions

Let
\[
\pi_j=\Pr(S\in B_j),\qquad
\theta_j=\Pr(S\in B_j,L=1).
\]
Thus \(\theta_j=\mathbb E[\mathbf1\{S\in B_j\}m(S)]\).

Bins are taken half-open except for the last bin, so every score has a unique bin and every bin has diameter at most \(1/K\).

For analysis at round \(t\), use an enlarged filtration that reveals the latent current triple \((S_t,\widehat Y_t,Y_t)\) before the routing and audit coins. This is only an analytical filtration: the learner’s decisions remain measurable with respect to the smaller information set in the theorem. Conditional on this enlarged pre-coin filtration,
\[
O_t\sim{\rm Bernoulli}(p_t),\qquad
p_t=\max\{1-x_{t,J_t},\gamma_t\},
\]
and \(p_t\) does not depend on \(L_t\).

At \(t=1\), set analytically
\[
D_1=0,\quad A_1=0,\quad O_1=1,\quad p_1=1.
\]
This is exactly the prescribed initial expert action.

Write
\[
A_n=\sum_{s=1}^n \gamma_s^{-1}
=\sum_{s=1}^n s^{1/4}.
\]
Then
\[
A_n\le n^{5/4}.
\]

All comparator expectations are with respect to the stationary distribution \(P\). The comparator benchmark is deterministic expected cost; the learner’s bound is a high-probability realized-cost bound.

## Lemmas

### Lemma 1 — Bernstein exponential supermartingale

Let \((X_s)\) be martingale differences, \(X_s\le b\), and let
\[
V_n=\sum_{s=1}^n\mathbb E[X_s^2\mid\mathcal G_{s-1}].
\]
For \(0<\lambda<3/b\),
\[
\exp\left\{
\lambda\sum_{s=1}^nX_s
-\frac{\lambda^2}{2(1-\lambda b/3)}V_n
\right\}
\]
is a nonnegative supermartingale.

If \(V_n\le v\) deterministically, then
\[
\Pr\left(
\sum_{s=1}^nX_s
>
\sqrt{2vz}+\frac{2bz}{3}
\right)\le e^{-z}.
\]

#### Proof

For \(x\le b\) and \(0<\lambda<3/b\),
\[
e^{\lambda x}
\le
1+\lambda x+
\frac{\lambda^2x^2}{2(1-\lambda b/3)}.
\]
For \(x\le0\), this follows from \(e^u-1-u\le u^2/2\). For \(0\le x\le b\), expand the exponential and use
\(k!\ge2\cdot3^{k-2}\) for \(k\ge2\).

Taking conditional expectations and using
\(\mathbb E[X_s\mid\mathcal G_{s-1}]=0\), followed by \(1+u\le e^u\), proves the supermartingale assertion.

Chernoff optimization gives the standard Freedman bound
\[
\Pr\left(\sum_{s=1}^nX_s\ge x\right)
\le
\exp\left(
-\frac{x^2}{2(v+bx/3)}
\right).
\]
For
\[
x=\sqrt{2vz}+\frac{2bz}{3},
\]
direct expansion shows
\[
x^2\ge2z(v+bx/3).
\]
Hence the displayed probability is at most \(e^{-z}\). ∎

### Lemma 2 — Adaptive importance-weighted underestimation

Fix a bin \(j\), and define
\[
M_{n,j}
=
\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Simultaneously for every \(1\le n\le T\),
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{z}{3\gamma_n}
\]
except on an event of probability at most \(Te^{-z}\).

#### Proof

Let
\[
X_{s,j}
=
\mathbf1\{S_s\in B_j\}L_s
\left(1-\frac{O_s}{p_s}\right).
\]
Conditional on the enlarged pre-coin filtration,
\[
\mathbb E[X_{s,j}\mid\mathcal G_{s,-}]=0,
\qquad X_{s,j}\le1,
\]
and
\[
\mathbb E[X_{s,j}^2\mid\mathcal G_{s,-}]
=
\mathbf1\{S_s\in B_j\}L_s\left(\frac1{p_s}-1\right)
\le \frac{\mathbf1\{S_s\in B_j\}}{p_s}.
\]
Thus \(V_{n,j}\) is a predictable variance upper bound.

Lemma 1 implies that for every \(\mu>0\), with
\[
\lambda=\frac{\mu}{1+\mu/3}\in(0,3),
\]
the process
\[
\exp\left\{
\lambda M_{n,j}
-\frac{\lambda^2}{2(1-\lambda/3)}V_{n,j}
\right\}
\]
is a supermartingale. Ville’s inequality consequently gives
\[
M_{n,j}
\le
\frac{\mu V_{n,j}}2+\frac z\mu+\frac z3
\tag{1}
\]
simultaneously in \(n\), except with probability \(e^{-z}\), for each fixed \(\mu\).

We discretize \(\mu\). Let
\[
\mu_{\min}=\sqrt{\frac{2z}{A_T}},
\qquad
\mu_{\max}=\sqrt{2z},
\qquad
r=1+T^{-1/2},
\]
and take the multiplicative grid from \(\mu_{\min}\) to \(\mu_{\max}\) with ratio \(r\), including both endpoints. Since
\[
A_T\le T^{5/4},
\]
the number \(M\) of grid points satisfies
\[
M\le
2+\frac{(5/8)\log T}{\log(1+T^{-1/2})}
\le T
\]
for \(T\ge16\).

If \(V_{n,j}=0\), then \(M_{n,j}=0\). Otherwise
\(1\le V_{n,j}\le A_T\), and the optimizer of the first two terms on the right of (1) is
\[
\mu^\star=\sqrt{\frac{2z}{V_{n,j}}}\in[\mu_{\min},\mu_{\max}].
\]
Choose a grid point \(\mu=\rho\mu^\star\) with \(1\le\rho\le r\). Then
\[
\frac{\mu V}{2}+\frac z\mu
=
\sqrt{2Vz}\,\frac{\rho+\rho^{-1}}2
\le
\sqrt{2Vz}+\frac{\sqrt{2Vz}}{2T}.
\]
Because \(V_{n,j}\le A_n\le n^{5/4}\),
\[
\frac{\sqrt{2V_{n,j}z}}{2T}
\le
\frac{\sqrt{2z}\,n^{5/8}}{2T}.
\]
For \(z\ge8\), \(T\ge16\), and \(2\le n\le T\),
\[
\frac{\sqrt{2z}\,n^{5/8}}{2T}
\le
\frac{(n^{1/4}-1)z}{3}.
\tag{2}
\]
For \(n=2,3,4\), (2) follows directly from \(T\ge16\); for \(n\ge5\), use \(T\ge n\) and
\[
\frac34n^{-3/8}\le n^{1/4}-1.
\]
At \(n=1\), \(p_1=O_1=1\), hence \(M_{1,j}=0\).

Combining (1) and (2),
\[
M_{n,j}
\le
\sqrt{2V_{n,j}z}+\frac{n^{1/4}z}{3}
=
\sqrt{2V_{n,j}z}+\frac z{3\gamma_n}.
\]
A union bound over at most \(T\) grid points gives failure probability at most \(Te^{-z}\). ∎

### Lemma 3 — Simultaneous one-sided calibration validity

Except on an event of probability at most \(2KTe^{-z}\), for every \(t\ge2\) and every bin \(j\),
\[
\theta_j\le U_{t,j}.
\]

#### Proof

Let \(n=t-1\) and
\[
E_{n,j}=\sum_{s=1}^n
\mathbf1\{S_s\in B_j\}L_s.
\]
Since the triples are i.i.d. and each summand lies in \([0,1]\),
\[
\Pr\left(
\theta_j-\frac{E_{n,j}}n
>
\sqrt{\frac z{2n}}
\right)\le e^{-z}.
\]
A union bound over \(j,n\) costs at most \(KTe^{-z}\).

By Lemma 2, simultaneously over \(n\), except with probability \(Te^{-z}\) per bin,
\[
E_{n,j}-H_{t,j}
\le
\sqrt{2V_{t,j}z}+\frac z{3\gamma_n}.
\]
Therefore
\[
\theta_j
\le
\frac{H_{t,j}}n
+
\frac{\sqrt{2V_{t,j}z}+z/(3\gamma_n)}n
+\sqrt{\frac z{2n}}
=
\widehat a_{t,j}+r_{t,j}.
\]
Because \(0\le\theta_j\le1\), clipping preserves this upper bound:
\(\theta_j\le U_{t,j}\). ∎

### Lemma 4 — Population safety and released-error concentration

With probability at least \(1-2KTe^{-z}-e^{-z}\),
\[
\sum_{t=1}^T R_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\]

#### Proof

At \(t\ge2\), define the predictable analytical indicator
\[
G_t=\mathbf1\{\theta_j\le U_{t,j}\text{ for all }j\},
\]
and let \(G_1=1\). Although \(\theta_j\) is unknown to the learner, it is a fixed population quantity, so \(G_t\) is \(\mathcal F_{t-1}\)-measurable.

When \(G_t=1\),
\[
\begin{aligned}
\mathbb E[D_tL_t\mid\mathcal F_{t-1}]
&=\sum_{j=1}^K x_{t,j}\theta_j\\
&\le\sum_{j=1}^Kx_{t,j}U_{t,j}
\le\epsilon.
\end{aligned}
\]
Since \(R_t=D_t(1-A_t)L_t\le D_tL_t\),
\[
\mathbb E[G_tR_t\mid\mathcal F_{t-1}]\le\epsilon G_t\le\epsilon.
\]
The variables
\[
G_tR_t-\mathbb E[G_tR_t\mid\mathcal F_{t-1}]
\]
are martingale differences of conditional range length at most \(1\). Hence Hoeffding–Azuma gives
\[
\sum_{t=1}^T G_tR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

On the event of Lemma 3, \(G_t=1\) for all \(t\), and the left side is exactly \(\sum_tR_t\). This stopping construction avoids conditioning the martingale inequality on a future confidence event. ∎

### Lemma 5 — Existence and discretization of an optimal comparator

There is a Borel optimizer \(a^\star\) attaining the infimum in \(C_T^\star\). Define, for \(\pi_j>0\),
\[
b_j=\mathbb E[a^\star(S)\mid S\in B_j],
\]
and set \(b_j=0\) when \(\pi_j=0\). Then
\[
\sum_j\pi_j(1-b_j)
=
\mathbb E[1-a^\star(S)]
\tag{3}
\]
and
\[
\sum_j\theta_jb_j
\le
\epsilon+\frac LK.
\tag{4}
\]

#### Proof

By A3, the Lipschitz version of \(m\) on the score support admits a Borel Lipschitz extension to \([0,1]\). Thus \(m(S)\) may be treated as a Borel random variable.

An optimizer is obtained by releasing on the lowest values of \(m(S)\). If \(\mathbb E[m(S)]\le\epsilon\), take \(a^\star\equiv1\). Otherwise choose a threshold \(\lambda>0\) and \(\rho\in[0,1]\) such that
\[
a^\star(s)
=
\mathbf1\{m(s)<\lambda\}
+\rho\,\mathbf1\{m(s)=\lambda\},
\qquad
\mathbb E[a^\star(S)m(S)]=\epsilon.
\]
Existence follows by taking a quantile of the finite measure
\(\mathbb E[m(S)\mathbf1\{m(S)\in\cdot\}]\).

For any feasible \(a\),
\[
(a-a^\star)(m-\lambda)\ge0
\]
pointwise. Hence
\[
\mathbb E[am]-\mathbb E[a^\star m]
\ge
\lambda\big(\mathbb E[a]-\mathbb E[a^\star]\big).
\]
The left side is nonpositive, so
\(\mathbb E[a]\le\mathbb E[a^\star]\). Thus \(a^\star\) is optimal.

Equation (3) follows from conditional expectation.

Within bin \(j\), all support points are at distance at most \(1/K\), so the oscillation of \(m\) is at most \(L/K\). Therefore
\[
\begin{aligned}
\sum_j\theta_jb_j-\mathbb E[a^\star(S)m(S)]
&=
\sum_j\pi_j\left(
\mathbb E[m\mid B_j]\mathbb E[a^\star\mid B_j]
-\mathbb E[a^\star m\mid B_j]
\right)\\
&\le \frac LK\sum_j\pi_j
=\frac LK.
\end{aligned}
\]
Feasibility of \(a^\star\) proves (4). ∎

### Lemma 6 — Comparator-directed upper estimate

For the fixed vector \(b\) from Lemma 5, except on an event of probability at most \(2Te^{-z}\), simultaneously for every \(t\ge2\), with \(n=t-1\),
\[
b^\top\left(\frac{H_t}{n}-\theta\right)
\le
\frac{\sqrt{2A_nz}}n
+\frac{2z}{3n\gamma_n}
+\sqrt{\frac z{2n}}.
\tag{5}
\]

#### Proof

Decompose
\[
b^\top H_t-nb^\top\theta
=
\sum_{s=1}^n b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)
+
\sum_{s=1}^n
\big(b_{J_s}L_s-b^\top\theta\big).
\]

For the first sum, at fixed \(n\), the increments are martingale differences bounded above by
\[
p_s^{-1}\le\gamma_s^{-1}\le\gamma_n^{-1}.
\]
Their predictable quadratic variation is at most
\[
\sum_{s=1}^n \frac1{p_s}\le A_n.
\]
Lemma 1 therefore gives
\[
\sum_{s=1}^n b_{J_s}L_s\left(\frac{O_s}{p_s}-1\right)
\le
\sqrt{2A_nz}+\frac{2z}{3\gamma_n}
\]
except with probability \(e^{-z}\).

The second sum consists of i.i.d. centered variables in \([-1,1]\), with the uncentered variables in \([0,1]\). Hoeffding’s inequality gives the upper bound \(\sqrt{nz/2}\) except with probability \(e^{-z}\).

Union over \(n\le T-1\) proves (5) with failure probability at most \(2Te^{-z}\). ∎

### Lemma 7 — Robust comparator feasibility

On the event of Lemma 6, for every \(t\ge2\),
\[
U_t^\top b\le\epsilon+\frac LK+w_t.
\tag{6}
\]
Consequently,
\[
y_t=\frac{\epsilon}{\epsilon+L/K+w_t}\,b
\]
is feasible for the round-\(t\) FTRL problem, and
\[
\sum_j\pi_j(1-y_{t,j})
\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon}.
\tag{7}
\]

#### Proof

Since \(H_{t,j}\ge0\) and \(r_{t,j}\ge0\),
\[
U_{t,j}\le \frac{H_{t,j}}n+r_{t,j}.
\]
Moreover,
\[
\begin{aligned}
\sum_jr_{t,j}
&\le
\frac{\sqrt{2Kz\sum_jV_{t,j}}}{n}
+\frac{Kz}{3n\gamma_n}
+K\sqrt{\frac z{2n}}\\
&\le
\frac{\sqrt{2KzA_n}}n
+\frac{Kz}{3n\gamma_n}
+K\sqrt{\frac z{2n}}
=\frac{w_t}{2}.
\end{aligned}
\tag{8}
\]
Here Cauchy–Schwarz was used, followed by
\[
\sum_jV_{t,j}=\sum_{s=1}^n\frac1{p_s}\le A_n.
\]

Because \(K=\lceil T^{1/4}\rceil\ge2\), the right side of (5) is at most \(w_t/2\). Combining this with (8) and Lemma 5,
\[
U_t^\top b
\le
\theta^\top b+w_t
\le
\epsilon+\frac LK+w_t.
\]
This proves (6), and hence \(U_t^\top y_t\le\epsilon\).

Finally,
\[
\begin{aligned}
\pi^\top(1-y_t)
&=\pi^\top(1-b)
+\left(1-\frac{\epsilon}{\epsilon+L/K+w_t}\right)\pi^\top b\\
&\le
\mathbb E[1-a^\star(S)]
+\frac{L/K+w_t}{\epsilon},
\end{aligned}
\]
which is (7). ∎

### Lemma 8 — FTRL deferral comparison

Except on an event of probability at most \(2KTe^{-z}\), simultaneously for all \(t\ge2\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
\le
\mathbb E[1-a^\star(S)]
+2K\sqrt{\frac z{2(t-1)}}
+\frac{K}{2(t-1)}
+\frac{L/K+w_t}{\epsilon}.
\tag{9}
\]

#### Proof

Hoeffding’s inequality and a union bound give
\[
\max_j|\widehat\pi_{t,j}-\pi_j|
\le
d_n:=\sqrt{\frac z{2n}}
\]
simultaneously over \(t,j\), except with probability \(2KTe^{-z}\).

By FTRL optimality against the feasible \(y_t\),
\[
n\widehat\pi_t^\top(1-x_t)+\frac12\|x_t\|_2^2
\le
n\widehat\pi_t^\top(1-y_t)+\frac12\|y_t\|_2^2.
\]
Since \(\|y_t\|_2^2\le K\),
\[
\widehat\pi_t^\top(1-x_t)
\le
\widehat\pi_t^\top(1-y_t)+\frac K{2n}.
\]
For every \(u\in[0,1]^K\),
\[
|\pi^\top(1-u)-\widehat\pi_t^\top(1-u)|
\le Kd_n.
\]
Thus
\[
\pi^\top(1-x_t)
\le
\pi^\top(1-y_t)+2Kd_n+\frac K{2n}.
\]
Apply (7). Since the current score is independent of \(\mathcal F_{t-1}\),
\[
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
=\pi^\top(1-x_t).
\]
This proves (9). ∎

### Lemma 9 — Complete realized-cost concentration

Except with probability \(e^{-z}\),
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+\sum_{t=2}^T
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]\\
&+(1+c_R)\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\tag{10}
\]

#### Proof

For \(t\ge2\), let
\[
W_t=O_t+c_RD_tA_tL_t.
\]
Conditional on \(S_t,L_t\) and the past,
\[
\begin{aligned}
\mathbb E[W_t]
&=(1-x_{t,J_t})
+x_{t,J_t}q_t(x_{t,J_t})(1+c_RL_t)\\
&\le
(1-x_{t,J_t})+(1+c_R)\gamma_t,
\end{aligned}
\]
because \(xq_t(x)\le\gamma_t\).

After averaging over the current i.i.d. arrival,
\[
\mathbb E[W_t\mid\mathcal F_{t-1}]
\le
\mathbb E[1-x_{t,J_t}\mid\mathcal F_{t-1}]
+(1+c_R)\gamma_t.
\]
Also \(0\le W_t\le1+c_R\). Hoeffding–Azuma yields
\[
\sum_{t=2}^TW_t
\le
\sum_{t=2}^T\mathbb E[W_t\mid\mathcal F_{t-1}]
+(1+c_R)\sqrt{\frac{Tz}{2}}
\]
except with probability \(e^{-z}\).

The first round costs one expert call, and every round costs \(c_M\). Enlarging \(\sum_{t=2}^T\gamma_t\) to \(\sum_{t=1}^T\gamma_t\) proves (10). ∎

### Lemma 10 — Comparator action and risk parity

Any comparator policy with cheap-release probability \(a(S)\) has expected expert-call cost at least \(\mathbb E[1-a(S)]\), correction cost at least zero, and released-error mean \(\mathbb E[a(S)m(S)]\). Equality in the cost lower bound is achieved without audits.

Moreover, every feasible comparator satisfies
\[
\Pr\left(
\sum_{t=1}^T R_t^{\rm comp}
>
\epsilon T+\sqrt{\frac{Tu}{2}}
\right)\le e^{-u}.
\]

#### Proof

A label not released cheaply must be replaced by the expert label, either by deferral or audit, so its expert-call probability is \(1-a(S)\). Auditing has the same unit expert cost as deferral and can additionally incur \(c_R\), hence replacing each audit by a coupled immediate deferral cannot increase cost or error.

Without audit, released error is the cheap-release indicator times \(L\), with mean \(\mathbb E[a(S)m(S)]\). Across i.i.d. rounds and independent comparator coins, these losses are independent \([0,1]\)-valued variables, so Hoeffding gives the stated tail bound. ∎

## Main proof

Intersect the following events:

1. Lemma 3’s simultaneous safety event;
2. Lemma 6’s comparator-directed upper-estimate event;
3. Lemma 8’s bin-frequency event;
4. Lemma 4’s released-error martingale event;
5. Lemma 9’s cost martingale event.

Since
\[
e^{-z}=\frac{\delta}{32KT},
\]
their total failure probability is at most
\[
2KTe^{-z}+2Te^{-z}+2KTe^{-z}+2e^{-z}<\delta.
\]

On this intersection, Lemma 4 directly gives
\[
\sum_{t=1}^TR_t
\le
\epsilon T+\sqrt{\frac{Tz}{2}}.
\]

For cost, combine Lemmas 8 and 9:
\[
\begin{aligned}
C_T
\le{}&c_MT+1
+(T-1)\mathbb E[1-a^\star(S)]\\
&+\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)\\
&+\frac1\epsilon
\sum_{t=2}^T\left(\frac LK+w_t\right)\\
&+(1+c_R)\left(
\sum_{t=1}^T\gamma_t+\sqrt{\frac{Tz}{2}}
\right).
\end{aligned}
\]
Since
\[
(T-1)\mathbb E[1-a^\star(S)]
\le
T\mathbb E[1-a^\star(S)]
\]
and
\[
\sum_{t=2}^T\frac LK\le\frac{LT}{K},
\]
the right side is at most
\[
T\left[c_M+\mathbb E[1-a^\star(S)]\right]+B_T
=C_T^\star+B_T.
\]

It remains to derive the announced rate. Put
\[
\ell=\log\frac{32T}{\delta}.
\]
For \(T\ge16\),
\[
T^{1/4}\le K\le2T^{1/4},
\qquad
z\le\frac32\ell,
\]
and
\[
\sum_{t=1}^Tt^{-1/4}\le\frac43T^{3/4}.
\]
Also,
\[
\sum_{n=1}^{T-1}n^{-1/2}\le2T^{1/2},\quad
\sum_{n=1}^{T-1}n^{-3/8}\le\frac85T^{5/8},
\]
\[
\sum_{n=1}^{T-1}n^{-3/4}\le4T^{1/4},\quad
\sum_{n=1}^{T-1}n^{-1}\le1+\log T.
\]

Using \(A_n\le n^{5/4}\),
\[
\begin{aligned}
\sum_{t=2}^Tw_t
&\le
\frac{16}{5}\sqrt{2Kz}\,T^{5/8}
+\frac83KzT^{1/4}
+2\sqrt2K\sqrt{zT}\\
&\le
27\,T^{3/4}\ell.
\end{aligned}
\]
Similarly,
\[
\sum_{t=2}^T
\left(
2K\sqrt{\frac{z}{2(t-1)}}+\frac{K}{2(t-1)}
\right)
\le 10T^{3/4}\ell,
\]
and
\[
\frac{LT}{K}\le LT^{3/4}.
\]
Finally,
\[
\sqrt{\frac{Tz}{2}}\le T^{3/4}\ell.
\]

Collecting terms yields, for example,
\[
B_T
\le
64\left(
1+c_R+\frac{1+L}{\epsilon}
\right)
T^{3/4}\log\frac{32T}{\delta}.
\]
Thus the theorem holds with the universal constant \(C_0=64\).

## Randomness and filtration accounting

The learner’s action-time filtration contains only past observable information. Before \(S_t\), \(x_t\) is determined by past \(N,H,V\), so it is \(\mathcal F_{t-1}\)-measurable. After \(S_t\), \(x_{t,J_t}\), \(q_t\), and \(p_t\) are measurable without access to \(Y_t\) or \(L_t\).

For importance weighting, the proof uses an enlarged filtration that mathematically reveals the latent current \(L_t\) before the routing and audit coins. This does not grant that information to the algorithm. Conditional on this enlarged pre-coin filtration,
\[
\mathbb E\left[\frac{O_tL_t}{p_t}\right]=L_t.
\]
Therefore both
\[
L_t\left(1-\frac{O_t}{p_t}\right)
\quad\text{and}\quad
L_t\left(\frac{O_t}{p_t}-1\right)
\]
are valid martingale differences in their respective orientations.

The adaptive observation probabilities may depend on all prior importance-weighted feedback. Lemma 2 handles this without conditioning on future confidence events: it constructs exponential supermartingales for fixed tuning parameters, applies Ville’s inequality, and only then unions over a deterministic grid.

The released-error proof uses the predictable indicator \(G_t\). Thus concentration is applied to a stopped/predictably masked process, not to a process conditioned on the future event that all confidence bounds succeed.

The three losses remain distinct throughout:

- \(L_t\) enters population risk and importance-weighted calibration;
- \(R_t=D_t(1-A_t)L_t\) is the released-label loss;
- \(O_tL_t/p_t\) is estimated feedback only.

The cost martingale contains every learner-side paid component:
the model call, expert deferrals, audits, and audited-error corrections. The comparator also pays every model call and all expert calls; its optimal representative uses no audits and hence no corrections.

## Boundary cases and counterexample attempts

Empty bins cause no problem: \(\pi_j=\theta_j=0\), and \(b_j\) may be set to zero.

Atoms at bin boundaries are handled by the fixed half-open partition. Atoms of \(m(S)\) at the comparator threshold are handled by the randomization coefficient \(\rho\).

If \(m\equiv0\), the comparator releases every cheap prediction; the confidence radii may initially force deferrals, but all such cost is included in \(B_T\).

If \(\epsilon=1\), the safety constraint and scaling argument remain valid. If \(L=0\), the discretization term vanishes. Costs \(c_M=0,1\) and \(c_R=0,1\) are all covered.

The principal attempted break was adaptivity of \(V_{t,j}\). Substituting a random predictable variance into a fixed-variance Freedman inequality would not be justified. Lemma 2 avoids that invalid substitution through a deterministic tuning grid and Ville’s inequality. The factor \(z/(3\gamma_n)\) supplies exactly the discretization slack needed for the curved variance boundary.

No monotonicity or semantic interpretation of the raw score is used. Lipschitzness enters only in the continuum-to-bin comparator approximation.

## Self-audit

1. The most delicate step is Lemma 2’s variance-adaptive grid argument. Its key numerical requirements are \(T\ge16\), \(z\ge8\), and \(p_t\ge t^{-1/4}\); all three are explicit theorem or algorithm conditions.

2. The cost proof deliberately does not require two-sided simultaneous binwise confidence bounds. Upper control is needed only in the fixed optimal-comparator direction \(b\), where deterministic-variance Freedman suffices. This prevents an unjustified adaptive random-variance upper-tail step.

3. Comparator attainment uses the scalar threshold structure of the one-constraint population problem. The atom-randomization argument covers noncontinuous distributions.

4. The final constant \(64\) is intentionally loose; all powers of \(T\), \(L/\epsilon\), audit cost, and correction cost are retained.

## Open obligations
