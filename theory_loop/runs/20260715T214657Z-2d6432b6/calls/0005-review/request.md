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
predictions with confidence scores; losses normalized to `[0, 1]`; costs
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
  has NO cost guarantee. The missing joint error-plus-cost theorem (or the
  impossibility/positive pair) is precisely the contribution target.
- The offline LP / dual-price view is an explanatory reformulation, not a
  novelty claim.

## Literature lanes

Online risk control; intermittent or partial-feedback conformal methods;
online stochastic linear programming; revenue management; constrained
contextual bandits; online learning with long-term constraints;
label-efficient prediction; online selective classification; online learning
to defer. Follow the literature policy's exact-source discipline; absence of
found prior work is never evidence of novelty.

## Honesty

Every model output is a theorem or proof candidate. A reviewer `pass` is a
workflow status, not an established result. Promotion into the paper or the
research-state documents requires human review.

# Context: theorem candidate

STATUS: proposed

## Setting and assumption ladder

Let \(W_t=(X_t,Y_t,O_t)\), where \(X_t\) is the pre-call context, \(Y_t\) is the authoritative label, and \(O_t=(\widehat Y_t,S_t)\) is the potential output and confidence score of one cheap model. The cheap-source counterfactual loss is

\[
\ell_t=\mathbf 1\{\widehat Y_t\neq Y_t\}.
\]

At each round the available actions are:

- \(E\): skip the model, pay unit expert cost, and release \(Y_t\).
- \(C\): call the model for cost \(c_M>0\) and release \(\widehat Y_t\) without observing \(Y_t\).
- \(A\): call the model, decide to audit before seeing \(Y_t\), pay unit expert cost, correct an error for additional cost \(\kappa\ge 0\), and release the corrected label.

Thus final released-label loss and total round cost are

\[
\lambda_t=\ell_t\mathbf 1\{a_t=C\},
\]

\[
g_t=c_M\mathbf 1\{a_t\in\{C,A\}\}
+\mathbf 1\{a_t\in\{E,A\}\}
+\kappa\ell_t\mathbf 1\{a_t=A\}.
\]

Every model call, expert call, audit, and paid correction is included. Let \(G=c_M+1+\kappa\).

**Information timeline.** Given history \(\mathcal F_{t-1}\), \(X_t\) is revealed. The model-call gate \(D_t\in\{E,M\}\) is measurable with respect to \(\sigma(\mathcal F_{t-1},X_t)\). If \(D_t=M\), the model cost is incurred and \(O_t\) is revealed. The post-call choice \(C\) or \(A\) is measurable with respect to \(\sigma(\mathcal F_{t-1},X_t,O_t)\), before \(Y_t\) is revealed. The expert label becomes observable only under \(E\) or \(A\); correction and release occur afterward, followed by the update. Comparator policies obey the identical timeline.

The policy library \(\Pi=\{\pi_1,\ldots,\pi_N\}\) consists of deterministic two-stage policies. Each \(\pi\) has a pre-call gate \(d_\pi(X)\in\{E,M\}\) and, when it calls the model, a post-call rule \(h_\pi(X,O)\in\{C,A\}\). It contains the always-expert policy \(\pi_E\). Randomized policies are distributions \(q\in\Delta(\Pi)\).

The assumption ladder was:

1. Bounded but arbitrary arrivals: rejected for this mechanism because an audited prefix need not represent the unaudited suffix.
2. I.i.d. arrivals with unrestricted routers: rejected because a router class can shatter the audited prefix and have uncontrolled deployment risk.
3. I.i.d. arrivals with a finite deterministic class: direct conservative empirical selection can have linear cost loss at a risk-boundary discontinuity.
4. Active rung: i.i.d., finite registered class, known expert, positive error budget, with randomized safe-policy mixing. The third obstruction is escaped by an algorithm choice, not a margin or optimizer-local assumption.

**Assumption A1 — stationary, action-independent arrivals**

- Mathematical statement: \(W_1,\ldots,W_T\overset{\mathrm{i.i.d.}}{\sim}P\) for an unknown \(P\). The potential \(O_t\) is defined independently of the routing action; calling the model reveals it but does not change \((Y_t,O_t)\).
- Operational meaning: the item population and deployed model are stationary, and routing does not alter the correct label or model response.
- Diagnostic or falsification: rolling two-sample tests, change-point tests, residual autocorrelation, and repeated-call stability checks can falsify stationarity or action independence.
- Required by: transfer from the audited prefix to the deployment suffix and concentration around the distribution-aware comparator.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A2 — bounded accounting and authoritative expert**

- Mathematical statement: \(\ell_t\in\{0,1\}\), \(c_M>0\) and \(\kappa\ge0\) are known, and the unit-cost expert always returns \(Y_t\), yielding zero released loss. Hence \(0\le g_t\le G\).
- Operational meaning: invoices have bounded known components and the designated expert is the reference standard.
- Diagnostic or falsification: reconcile call/audit/correction logs against invoices; test expert reliability using duplicate adjudication.
- Required by: concentration, complete cost accounting, and the globally safe policy.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A3 — preregistered learnable routing class**

- Mathematical statement: \(\Pi\) is fixed before the stream, finite with \(2\le N<\infty\), and contains \(\pi_E\).
- Operational meaning: deployment chooses among a registered library of router versions rather than fitting an unrestricted router on the calibration prefix.
- Diagnostic or falsification: inspect the router registry and hashes; post-prefix creation or modification of a policy violates the assumption.
- Required by: simultaneous policy evaluation and the explicit comparator.
- Optimizer-local: `no`
- Classification: `problem`

**Assumption A4 — positive risk service level**

- Mathematical statement: the target satisfies fixed \(\epsilon\in(0,1]\).
- Operational meaning: the labeling SLA permits a specified nonzero average error budget.
- Diagnostic or falsification: falsified as an applicable model if the deployment requirement is exactly zero error.
- Required by: safe-policy shrinkage incurs cost proportional to \(1/\epsilon\). Exact zero risk cannot be obtained by this argument.
- Optimizer-local: `no`
- Classification: `problem`

**Choice C1 — prefix length, convexification, and confidence tightening**

- Mathematical statement: use \(n=\min\{T,\lceil T^{2/3}\rceil\}\) paired model–expert rounds, optimize over \(\Delta(\Pi)\), and tighten empirical risk by a uniform confidence radius.
- Operational meaning: front-load a sublinear calibration expense and deploy a stationary randomized router afterward.
- Diagnostic or falsification: directly check audit logs, LP inputs, mixture weights, and randomization frequencies.
- Required by: the proposed \(T^{2/3}\) cost remainder.
- Optimizer-local: `no`
- Classification: `algorithm`

No uniqueness, strict complementarity, local curvature, or margin at the unknown optimizer is assumed. Such conditions would be optimizer-local and are classified as `rejected`.

## Algorithm

Call the algorithm **Audited-Prefix Safe-Mixture LP (APS-LP)**.

For confidence \(\delta\in(0,1)\), set

\[
n=\min\{T,\lceil T^{2/3}\rceil\},\qquad H=T-n,
\qquad
a_n=\sqrt{\frac{\log(12N/\delta)}{2n}}.
\]

**Calibration rounds \(t\le n\).**

1. Call the cheap model and observe \(O_t\).
2. Audit with probability one, predictably before seeing \(Y_t\).
3. Observe \(Y_t\), correct if necessary, release the corrected label, and incur
   \(c_M+1+\kappa\ell_t\). Therefore calibration-round released loss is zero.
4. For every \(\pi\in\Pi\), reconstruct its counterfactual action and record

\[
r_t(\pi)=\ell_t\mathbf 1\{\pi(W_t)=C\},
\]

\[
c_t(\pi)=
\mathbf 1\{\pi(W_t)=E\}
+c_M\mathbf 1\{\pi(W_t)\in\{C,A\}\}
+\mathbf 1\{\pi(W_t)=A\}
+\kappa\ell_t\mathbf 1\{\pi(W_t)=A\}.
\]

Here \(r_t(\pi)\) is counterfactual cheap-source released risk, not the algorithm’s released loss. Because the calibration audit probability is one, the estimated feedback is exactly \(\widetilde r_t(\pi)=r_t(\pi)\); no importance weighting is used.

Define, linearly for \(q\in\Delta(\Pi)\),

\[
\widehat R_n(q)=\frac1n\sum_{t=1}^n\sum_{\pi}q_\pi r_t(\pi),
\qquad
\widehat C_n(q)=\frac1n\sum_{t=1}^n\sum_{\pi}q_\pi c_t(\pi).
\]

If \(a_n\le\epsilon/2\), solve the finite LP

\[
\widehat q\in
\arg\min_{q\in\Delta(\Pi)}\widehat C_n(q)
\quad\text{subject to}\quad
\widehat R_n(q)\le\epsilon-a_n,
\]

using a fixed deterministic tie-break. The expert policy makes this LP feasible. If \(a_n>\epsilon/2\), set \(\widehat q=\delta_{\pi_E}\).

**Deployment rounds \(t>n\).**

Sample \(J_t\sim\widehat q\) independently at the start of the round and execute \(\pi_{J_t}\):

- If its gate chooses \(E\), skip the model, obtain \(Y_t\), and release it.
- Otherwise call the model and observe \(O_t\). Then execute the policy’s predictable \(C/A\) decision.
- Under \(A\), audit before seeing \(Y_t\), correct, and release; under \(C\), release without feedback.

The induced audit probability after observing \((X_t,O_t)\) is the \(\widehat q\)-mass of policies choosing \(A\) there, hence is predictable. Labels observed during deployment may be logged but do not change \(\widehat q\); this independence is deliberate.

## Theorem candidate

For a distribution \(P\), define

\[
R(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi r(\pi;W)\right],
\qquad
C(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi c(\pi;W)\right].
\]

Let the distribution-aware comparator be

\[
q^\star\in\arg\min_{q\in\Delta(\Pi)}
\{C(q):R(q)\le\epsilon\},
\]

with fixed tie-breaking. It knows \(P\) but, on every action, sees only the same current information as APS-LP. It has the same actions and pays the same model, expert, audit, and correction costs. It has no learning audits unless prescribed by its sampled policy.

For an actual comparator run on the same item stream, independently sample \(J_t^\star\sim q^\star\) each round and let \(L_T^\star,C_T^\star\) be its realized released loss and total cost. Define

\[
d_m=\sqrt{\frac{m}{2}\log\frac6\delta},\qquad d_0=0,
\]

and

\[
\Gamma_T=
\begin{cases}
G\!\left[
n+2H a_n(1+\epsilon^{-1})+d_H+d_T
\right],
& a_n\le\epsilon/2,\\[3pt]
GT,&a_n>\epsilon/2.
\end{cases}
\]

**Candidate theorem.** For every \(N\ge2\), every \(P\) satisfying A1–A2, every policy class satisfying A3, every \(\epsilon\in(0,1]\), every horizon \(T\ge1\), and every \(\delta\in(0,1)\), with probability at least \(1-\delta\), jointly over \(W_{1:T}\), APS-LP’s randomization, and the comparator’s independent randomization,

\[
\boxed{\quad
L_T^{\mathrm{APS}}
=\sum_{t=1}^T\lambda_t
\le \epsilon T+d_H
\quad}
\]

and

\[
\boxed{\quad
C_T^{\mathrm{APS}}\le C_T^\star+\Gamma_T.
\quad}
\]

On the same event the comparator itself satisfies the probability-parity bound

\[
L_T^\star\le\epsilon T+d_T.
\]

For fixed \(N,G,\epsilon\), taking \(\delta_T=T^{-2}\) gives probability at least \(1-T^{-2}\),

\[
L_T^{\mathrm{APS}}
\le\epsilon T+O(\sqrt{T\log T}),
\]

\[
C_T^{\mathrm{APS}}
\le C_T^\star+
O\!\left(
G(1+\epsilon^{-1})T^{2/3}\sqrt{\log(NT)}
\right).
\]

Both remainders are \(o(T)\). More generally this remains true when
\(\log(N/\delta_T)=o(T^{2/3})\).

## Why this can work: proof plan

1. **Uniform prefix evaluation.** Hoeffding’s inequality and a union bound over the \(N\) base policies give, with failure probability at most \(\delta/3\),

\[
\sup_{q\in\Delta(\Pi)}
|\widehat R_n(q)-R(q)|\le a_n,
\qquad
\sup_{q\in\Delta(\Pi)}
|\widehat C_n(q)-C(q)|\le Ga_n.
\]

Linearity extends the bound from base policies to every mixture.

2. **Global safe shrinkage.** When \(a_n\le\epsilon/2\), set

\[
\theta=\frac{2a_n}{\epsilon},
\qquad
q^-=(1-\theta)q^\star+\theta\delta_{\pi_E}.
\]

Since \(R(\pi_E)=0\),

\[
R(q^-)\le(1-\theta)\epsilon=\epsilon-2a_n,
\]

so the uniform event implies
\(\widehat R_n(q^-)\le\epsilon-a_n\). Thus \(q^-\) is empirically feasible without any optimizer-local margin. Moreover,

\[
C(q^-)\le C(q^\star)+\theta G.
\]

3. **Population guarantees for the selected LP solution.** Empirical optimality and the two uniform deviations imply

\[
R(\widehat q)\le\epsilon,
\]

\[
C(\widehat q)
\le C(q^\star)+2Ga_n(1+\epsilon^{-1}).
\]

4. **Released-loss concentration.** Calibration contributes zero released loss. Conditional on the prefix, deployment rounds are i.i.d. with mean released loss at most \(\epsilon\). Hoeffding yields

\[
L_T^{\mathrm{APS}}\le \epsilon H+d_H\le\epsilon T+d_H.
\]

5. **Complete cost comparison.** Prefix cost is at most \(nG\). Conditional deployment-cost concentration gives

\[
C_T^{\mathrm{APS}}
\le nG+H C(q^\star)
+2GH a_n(1+\epsilon^{-1})+Gd_H.
\]

A lower-tail bound for the actual comparator gives
\(C_T^\star\ge TC(q^\star)-Gd_T\), producing the stated \(\Gamma_T\). Two analogous comparator bounds establish probability parity. The five events are allocated probabilities \(\delta/3,\delta/6,\delta/6,\delta/6,\delta/6\).

The single riskiest step is the safe-shrinkage-to-actual-comparator calculation: the prover must check that empirical feasibility, all factors of \(G\), and the lower-tail coupling to \(C_T^\star\) remain valid under the two-stage call/audit filtration. No local optimality property is available to repair an error there.

## Attack log

- **Nonstationary suffix attack.** Make every audited-prefix model prediction correct and every unaudited-suffix prediction wrong. A prefix-selected cheap router then violates the error target. This directly motivated A1. It does not establish that all continuously auditing adversarial algorithms are impossible.
- **Adaptive-output attack.** If model responses change depending on whether the system intends to audit, the calibration record does not identify deployment loss. A1 therefore includes action-independent potential outputs.
- **Unrestricted-router attack.** A router class that memorizes the \(n\) audited contexts can have zero empirical risk and arbitrarily high population risk. This motivated the preregistered finite library A3.
- **Risk-boundary cost jump.** Suppose a cheap policy has \(R=\epsilon\) and low cost while the expert has zero risk and unit cost. A deterministic empirical constraint tightened below \(\epsilon\) can discard the cheap policy and suffer \(\Theta(T)\) excess cost. Adding a margin or curvature assumption would be optimizer-local. Convex mixing with the expert instead creates the globally valid \(O(a_n/\epsilon)\) cost bridge.
- **Zero-budget attack.** The same bridge diverges at \(\epsilon=0\). Distinguishing an exactly zero-risk cheap source from one with arbitrarily small positive risk cannot be handled by this theorem, so A4 is explicit.
- **Hidden-cost attack.** Counting only expert calls makes calibration appear free. Here every prefix model call, expert audit, and erroneous-label correction is charged; the comparator uses identical accounting, and the learner’s extra calibration expense remains in \(\Gamma_T\).
- **Comparator-information attack.** The comparator knows \(P\), but not \(Y_t\) or \(\ell_t\) before acting. Its policy is executed through the same pre-call and post-call information nodes. Its lack of learning audits is legitimate, and the learner’s prefix audits appear as regret.
- **Rate attack.** With \(n\) prefix audits, the leading excess cost is \(Gn+GT\sqrt{\log N/n}\). Balancing these terms gives \(n\asymp T^{2/3}\); a shorter prefix worsens estimation cost, while a longer prefix directly increases audit cost.

## Relation to known results

- Angelopoulos, Bates, Fisch, Lei, and Schuster, [“Conformal Risk Control,” Theorem 1, Section 2.1](https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-risk.pdf), control the expected next-sample risk of an exchangeable, fully observed monotone loss family. The guarantee is in expectation, with no routing-cost comparator or partial expert feedback. The full text was checked. APS-LP instead controls realized cumulative released loss and realized total cost, while explicitly charging calibration audits. This source is an analogy for calibration, not proof evidence for the joint theorem.
- Cesa-Bianchi, Lugosi, and Stoltz, [“Minimizing Regret with Label Efficient Prediction,” Theorems 2 and 13](https://stoltz.perso.math.cnrs.fr/Publications/CBLS-LabelEff.pdf), study arbitrary outcome sequences with labels revealed only on queries. Theorem 2 gives high-probability regret of order \(T\sqrt{\log(N/\delta)/m}\) using at most \(m\) labels; Theorem 13 gives a matching expected lower bound against the best constant action. The full text was checked. Their comparator has no risk constraint, expert correction action, or complete labeling-cost objective; their rates nevertheless explain the audit-versus-estimation balance used here.
- Pacchiano, Ghavamzadeh, Bartlett, and Jiang, [“Stochastic Bandits with Linear Constraints,” Theorem 2](https://proceedings.mlr.press/v130/pacchiano21a/pacchiano21a.pdf), obtain high-probability sublinear pseudo-regret for stochastic contextual linear bandits under stage-wise expected constraints and a known safe action with positive slack. Pulled actions reveal their reward and cost. The full text was checked. APS-LP shares the safe-action geometry but replaces linear realizability and stage-wise expected feasibility with audited label feedback, sample-path cumulative error, correction semantics, and total-cost comparison.
- Candès, Ilyas, and Zrnic, [“Probably Approximately Correct Labels,” Theorem 1, Corollary 1, and Section 3](https://arxiv.org/abs/2506.10908), treat a fixed transductive dataset, sample expert labels for calibration, and provide high-probability labeling-error control; Section 3 develops multi-model and cost-sensitive routing. Probabilities are over the labeling procedure rather than an online arrival process, and no online cost-regret theorem against a distribution-aware policy is given. The primary full text was checked. APS-LP’s proposed difference is the online two-stage information structure and a simultaneous realized cost guarantee that explicitly absorbs learning audits and corrections.

These comparisons identify nearby mechanisms only. They do not establish novelty; that requires a broader human-reviewed search and proof verification.

# Context: proof candidate under review

STATUS: complete

## Exact theorem

For a distribution \(P\), define

\[
R(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi r(\pi;W)\right],
\qquad
C(q)=\mathbb E_P\!\left[\sum_{\pi}q_\pi c(\pi;W)\right].
\]

Let the distribution-aware comparator be

\[
q^\star\in\arg\min_{q\in\Delta(\Pi)}
\{C(q):R(q)\le\epsilon\},
\]

with fixed tie-breaking. It knows \(P\) but, on every action, sees only the same current information as APS-LP. It has the same actions and pays the same model, expert, audit, and correction costs. It has no learning audits unless prescribed by its sampled policy.

For an actual comparator run on the same item stream, independently sample \(J_t^\star\sim q^\star\) each round and let \(L_T^\star,C_T^\star\) be its realized released loss and total cost. Define

\[
d_m=\sqrt{\frac{m}{2}\log\frac6\delta},\qquad d_0=0,
\]

and

\[
\Gamma_T=
\begin{cases}
G\!\left[
n+2H a_n(1+\epsilon^{-1})+d_H+d_T
\right],
& a_n\le\epsilon/2,\\[3pt]
GT,&a_n>\epsilon/2.
\end{cases}
\]

**Candidate theorem.** For every \(N\ge2\), every \(P\) satisfying A1–A2, every policy class satisfying A3, every \(\epsilon\in(0,1]\), every horizon \(T\ge1\), and every \(\delta\in(0,1)\), with probability at least \(1-\delta\), jointly over \(W_{1:T}\), APS-LP’s randomization, and the comparator’s independent randomization,

\[
\boxed{\quad
L_T^{\mathrm{APS}}
=\sum_{t=1}^T\lambda_t
\le \epsilon T+d_H
\quad}
\]

and

\[
\boxed{\quad
C_T^{\mathrm{APS}}\le C_T^\star+\Gamma_T.
\quad}
\]

On the same event the comparator itself satisfies the probability-parity bound

\[
L_T^\star\le\epsilon T+d_T.
\]

For fixed \(N,G,\epsilon\), taking \(\delta_T=T^{-2}\) gives probability at least \(1-T^{-2}\),

\[
L_T^{\mathrm{APS}}
\le\epsilon T+O(\sqrt{T\log T}),
\]

\[
C_T^{\mathrm{APS}}
\le C_T^\star+
O\!\left(
G(1+\epsilon^{-1})T^{2/3}\sqrt{\log(NT)}
\right).
\]

Both remainders are \(o(T)\). More generally this remains true when
\(\log(N/\delta_T)=o(T^{2/3})\).

## Notation and standing assumptions

For each deterministic policy \(\pi\), let \(A_\pi(W)\in\{E,C,A\}\) denote the counterfactual action obtained from its pre-call gate and, when appropriate, its post-call rule. Although written as a function of \(W=(X,Y,O)\), the action itself depends only on \(X\), and on \(O\) after a model call; it never depends on \(Y\).

Write

\[
r_\pi(W)=\ell(W)\mathbf 1\{A_\pi(W)=C\},
\]

and

\[
c_\pi(W)
=\mathbf 1\{A_\pi(W)=E\}
+c_M\mathbf 1\{A_\pi(W)\in\{C,A\}\}
+\mathbf 1\{A_\pi(W)=A\}
+\kappa\ell(W)\mathbf 1\{A_\pi(W)=A\}.
\]

Then

\[
0\le r_\pi(W)\le1,\qquad 0\le c_\pi(W)\le G,
\quad G=c_M+1+\kappa.
\]

For the always-expert policy,

\[
R(\delta_{\pi_E})=0,\qquad C(\delta_{\pi_E})=1.
\]

The feasible population set is nonempty because it contains \(\delta_{\pi_E}\). It is a closed subset of the compact simplex \(\Delta(\Pi)\), so \(q^\star\) exists. The empirical LP is also feasible whenever it is solved, because \(a_n\le\epsilon/2\) implies

\[
\widehat R_n(\delta_{\pi_E})=0\le\epsilon-a_n.
\]

We work on the product probability space carrying:

- i.i.d. potential observations \(W_1,\ldots,W_T\sim P\);
- independent APS-LP mixture seeds \(J_t\);
- independent comparator mixture seeds \(J_t^\star\).

The two seed sequences are mutually independent and independent of \(W_{1:T}\). The comparator and APS-LP may therefore be dependent through their common item stream, but none of the proof uses independence between their realized totals.

The three relevant losses remain distinct:

- APS-LP’s calibration released loss is zero because every prefix item is corrected;
- \(r_t(\pi)\) is a counterfactual released loss for policy \(\pi\);
- the prefix feedback estimate is \(\widetilde r_t(\pi)=r_t(\pi)\), because every prefix item is audited.

No deployment loss under \(C\) needs to be observed for the theorem.

## Lemmas

**Lemma 1 (bounded Hoeffding inequality).**  
Let \(Z_1,\ldots,Z_m\) be independent random variables taking values in \([0,b]\), and let \(\mu_i=\mathbb E Z_i\). For every \(x\ge0\),

\[
\Pr\!\left\{\sum_{i=1}^m(Z_i-\mu_i)\ge x\right\}
\le \exp\!\left(-\frac{2x^2}{mb^2}\right),
\]

and the same bound holds for the lower tail. Consequently,

\[
\Pr\!\left\{
\left|\frac1m\sum_{i=1}^mZ_i-\frac1m\sum_{i=1}^m\mu_i\right|\ge u
\right\}
\le2e^{-2mu^2/b^2}.
\]

The same conclusions hold conditionally whenever conditional on a sigma-field the variables are independent, bounded in \([0,b]\), and have the stated conditional means.

*Proof.* Put \(s=\lambda b\) and \(p=\mathbb EZ/b\). Convexity of \(z\mapsto e^{\lambda z}\) on \([0,b]\) gives

\[
\mathbb E e^{\lambda(Z-\mathbb EZ)}
\le e^{-sp}(1-p+pe^s).
\]

If

\[
f(s)=\log(1-p+pe^s)-ps,
\]

then \(f(0)=f'(0)=0\), while

\[
f''(s)=p_s(1-p_s)\le\frac14
\]

for a suitable \(p_s\in[0,1]\). Integrating this second-derivative bound yields \(f(s)\le s^2/8\), and hence

\[
\mathbb E e^{\lambda(Z-\mathbb EZ)}
\le e^{\lambda^2b^2/8}.
\]

Independence, Markov’s inequality, and optimization over \(\lambda>0\) give

\[
\Pr\!\left\{\sum_i(Z_i-\mu_i)\ge x\right\}
\le\inf_{\lambda>0}
\exp\!\left(-\lambda x+\frac{m\lambda^2b^2}{8}\right)
=\exp\!\left(-\frac{2x^2}{mb^2}\right).
\]

Apply the same argument to \(b-Z_i\) for the lower tail, and take a union bound for the two-sided statement. Applying the argument to each regular conditional distribution proves the conditional version. ∎

Dependencies: boundedness and independence only.

---

**Lemma 2 (simultaneous prefix evaluation).**  
Define the event

\[
\mathcal E_0=
\left\{
\sup_{q\in\Delta(\Pi)}
|\widehat R_n(q)-R(q)|\le a_n
\right\}
\cap
\left\{
\sup_{q\in\Delta(\Pi)}
|\widehat C_n(q)-C(q)|\le Ga_n
\right\}.
\]

Then

\[
\Pr(\mathcal E_0)\ge1-\frac{\delta}{3}.
\]

*Proof.* For a fixed \(\pi\), the variables \(r_t(\pi)\), \(t\le n\), are i.i.d. in \([0,1]\). Lemma 1 gives

\[
\Pr\{|\widehat R_n(\pi)-R(\pi)|>a_n\}
\le 2e^{-2na_n^2}
=2e^{-\log(12N/\delta)}
=\frac{\delta}{6N}.
\]

A union bound over \(N\) policies shows that, except on an event of probability \(\delta/6\),

\[
\max_{\pi\in\Pi}|\widehat R_n(\pi)-R(\pi)|\le a_n.
\]

Likewise, \(c_t(\pi)\in[0,G]\), so

\[
\Pr\{|\widehat C_n(\pi)-C(\pi)|>Ga_n\}
\le2e^{-2na_n^2}
=\frac{\delta}{6N}.
\]

A second union bound gives the simultaneous base-policy cost bound with failure probability at most \(\delta/6\).

For any mixture \(q\),

\[
|\widehat R_n(q)-R(q)|
=
\left|\sum_\pi q_\pi
(\widehat R_n(\pi)-R(\pi))\right|
\le\max_\pi|\widehat R_n(\pi)-R(\pi)|.
\]

The same argument applies to cost. Combining the risk and cost events proves the claim. ∎

Dependencies: A1 for i.i.d. prefix observations, A2 for boundedness, A3 for finiteness and preregistration.

---

**Lemma 3 (safe mixture bridge and selected-policy guarantees).**  
Suppose \(a_n\le\epsilon/2\). On \(\mathcal E_0\),

\[
R(\widehat q)\le\epsilon
\]

and

\[
C(\widehat q)
\le C(q^\star)+2Ga_n(1+\epsilon^{-1}).
\]

*Proof.* Set

\[
\theta=\frac{2a_n}{\epsilon}\in[0,1],
\qquad
q^-=(1-\theta)q^\star+\theta\delta_{\pi_E}.
\]

Because \(R(q^\star)\le\epsilon\) and \(R(\delta_{\pi_E})=0\),

\[
R(q^-)
=(1-\theta)R(q^\star)
\le(1-\theta)\epsilon
=\epsilon-2a_n.
\]

On \(\mathcal E_0\),

\[
\widehat R_n(q^-)
\le R(q^-)+a_n
\le\epsilon-a_n.
\]

Thus \(q^-\) is feasible for the empirical LP. Empirical optimality of \(\widehat q\) gives

\[
\widehat C_n(\widehat q)\le\widehat C_n(q^-).
\]

Moreover, empirical feasibility and the risk deviation bound imply

\[
R(\widehat q)
\le\widehat R_n(\widehat q)+a_n
\le\epsilon.
\]

For cost,

\[
\begin{aligned}
C(\widehat q)
&\le \widehat C_n(\widehat q)+Ga_n\\
&\le \widehat C_n(q^-)+Ga_n\\
&\le C(q^-)+2Ga_n.
\end{aligned}
\]

Finally,

\[
\begin{aligned}
C(q^-)
&=(1-\theta)C(q^\star)+\theta C(\delta_{\pi_E})\\
&=C(q^\star)+\theta\bigl(C(\delta_{\pi_E})-C(q^\star)\bigr)\\
&\le C(q^\star)+\theta G\\
&=C(q^\star)+\frac{2Ga_n}{\epsilon},
\end{aligned}
\]

where \(0\le C(q^\star),C(\delta_{\pi_E})\le G\). Combining the last two displays yields

\[
C(\widehat q)
\le C(q^\star)+2Ga_n+\frac{2Ga_n}{\epsilon}.
\]

This is the claimed bound. ∎

Dependencies: Lemma 2, the always-expert policy from A3, the positive budget in A4, and linearity of \(R,C\).

---

**Lemma 4 (APS-LP deployment concentration).**  
Conditional on the prefix \(W_{1:n}\), the deployment loss and cost satisfy

\[
\Pr\!\left\{
\sum_{t=n+1}^T\lambda_t
>H R(\widehat q)+d_H
\,\middle|\,W_{1:n}
\right\}\le\frac{\delta}{6},
\]

and

\[
\Pr\!\left\{
\sum_{t=n+1}^Tg_t
>H C(\widehat q)+Gd_H
\,\middle|\,W_{1:n}
\right\}\le\frac{\delta}{6}.
\]

For \(H=0\), both inequalities hold deterministically.

*Proof.* The fixed tie-break makes \(\widehat q\) a function of the audited prefix. Conditional on \(W_{1:n}\), it is fixed. By A1, the suffix observations remain i.i.d. with distribution \(P\), and the suffix mixture seeds are i.i.d. with distribution \(\widehat q\), independently of those observations.

If \(J_t=\pi\), execution of \(\pi\) produces exactly

\[
\lambda_t=r_\pi(W_t),\qquad g_t=c_\pi(W_t).
\]

Indeed, \(E\) and \(A\) have zero released loss, while \(C\) has released loss \(\ell_t\); the three action costs agree term by term with \(c_\pi\).

It follows that, conditionally on the prefix, the deployment losses are i.i.d. in \([0,1]\) with mean \(R(\widehat q)\), and the deployment costs are i.i.d. in \([0,G]\) with mean \(C(\widehat q)\). Lemma 1 and

\[
e^{-2d_H^2/H}
=e^{-\log(6/\delta)}
=\frac{\delta}{6}
\]

give both results. ∎

Dependencies: A1, A2, the independence of deployment seeds, and the fact that deployment does not update \(\widehat q\).

---

**Lemma 5 (actual comparator concentration).**  
With failure probability at most \(\delta/6\) for each inequality,

\[
L_T^\star\le T R(q^\star)+d_T
\le\epsilon T+d_T,
\]

and

\[
C_T^\star\ge T C(q^\star)-Gd_T.
\]

*Proof.* The pairs \((W_t,J_t^\star)\) are i.i.d. The comparator’s released loss is \(r_{J_t^\star}(W_t)\in[0,1]\), with mean \(R(q^\star)\le\epsilon\), and its total round cost is \(c_{J_t^\star}(W_t)\in[0,G]\), with mean \(C(q^\star)\). Apply the upper and lower one-sided forms of Lemma 1, respectively. The chosen deviation satisfies

\[
e^{-2d_T^2/T}=\delta/6.
\]

The shared item stream with APS-LP does not affect either marginal concentration statement. ∎

Dependencies: A1, A2, feasibility of \(q^\star\), and independent comparator randomization.

## Main proof

First suppose \(a_n\le\epsilon/2\). Consider the intersection of:

1. the prefix event \(\mathcal E_0\);
2. the APS-LP deployment-loss event from Lemma 4;
3. the APS-LP deployment-cost event from Lemma 4;
4. the comparator-cost lower-tail event from Lemma 5;
5. the comparator-loss upper-tail event from Lemma 5.

Their total failure probability is at most

\[
\frac{\delta}{3}
+4\frac{\delta}{6}
=\delta.
\]

No independence among these events is required.

On this intersection, calibration contributes no released loss. Lemmas 3 and 4 therefore give

\[
\begin{aligned}
L_T^{\mathrm{APS}}
&=\sum_{t=n+1}^T\lambda_t\\
&\le H R(\widehat q)+d_H\\
&\le\epsilon H+d_H\\
&\le\epsilon T+d_H.
\end{aligned}
\]

This proves the APS-LP error guarantee.

The comparator-loss event gives simultaneously

\[
L_T^\star
\le T R(q^\star)+d_T
\le\epsilon T+d_T.
\]

For cost, every prefix round costs

\[
c_M+1+\kappa\ell_t\le G,
\]

so the entire calibration prefix costs at most \(nG\). Lemmas 3 and 4 imply

\[
\begin{aligned}
C_T^{\mathrm{APS}}
&\le nG+H C(\widehat q)+Gd_H\\
&\le nG+H C(q^\star)
  +2GHa_n(1+\epsilon^{-1})+Gd_H.
\end{aligned}
\]

Since costs are nonnegative, \(C(q^\star)\ge0\), and hence

\[
H C(q^\star)
=(T-n)C(q^\star)
\le T C(q^\star).
\]

The comparator lower-tail event yields

\[
T C(q^\star)\le C_T^\star+Gd_T.
\]

Consequently,

\[
\begin{aligned}
C_T^{\mathrm{APS}}
&\le C_T^\star+
G\left[n+2Ha_n(1+\epsilon^{-1})+d_H+d_T\right]\\
&=C_T^\star+\Gamma_T.
\end{aligned}
\]

This proves both finite-horizon claims in the first branch.

Now suppose \(a_n>\epsilon/2\). APS-LP chooses \(\widehat q=\delta_{\pi_E}\). Its prefix released loss is zero by correction and its deployment released loss is zero because it always uses the expert. Thus

\[
L_T^{\mathrm{APS}}=0\le\epsilon T+d_H.
\]

Its prefix cost is at most \(nG\), and its deployment cost is \(H\). Since \(G=c_M+1+\kappa>1\),

\[
C_T^{\mathrm{APS}}
\le nG+H
\le nG+HG
=GT.
\]

Because \(C_T^\star\ge0\),

\[
C_T^{\mathrm{APS}}
\le C_T^\star+GT
=C_T^\star+\Gamma_T.
\]

Only the comparator-loss upper-tail event is needed in this branch, and it has probability at least \(1-\delta/6\ge1-\delta\). Thus all finite-horizon conclusions hold in both branches.

For the rate specialization, take \(T\ge2\) and \(\delta_T=T^{-2}\). Then

\[
a_n=\sqrt{\frac{\log(12NT^2)}{2n}}.
\]

For all \(T\ge1\),

\[
T^{2/3}\le n\le T^{2/3}+1\le2T^{2/3}.
\]

Therefore \(a_n\to0\), so for fixed \(\epsilon>0\), the first branch holds for all sufficiently large \(T\). Moreover,

\[
2Ha_n
\le
2T\sqrt{\frac{\log(12NT^2)}{2T^{2/3}}}
=
\sqrt2\,T^{2/3}\sqrt{\log(12NT^2)}.
\]

Also,

\[
d_H+d_T
\le
2\sqrt{\frac{T}{2}\log(6T^2)}
=
\sqrt{2T\log(6T^2)}.
\]

Thus

\[
\Gamma_T
\le
G\left[
2T^{2/3}
+\sqrt2(1+\epsilon^{-1})
T^{2/3}\sqrt{\log(12NT^2)}
+\sqrt{2T\log(6T^2)}
\right],
\]

which is

\[
O\!\left(
G(1+\epsilon^{-1})T^{2/3}\sqrt{\log(NT)}
\right).
\]

Likewise,

\[
d_H\le\sqrt{\frac{T}{2}\log(6T^2)}
=O(\sqrt{T\log T}).
\]

Both quantities are \(o(T)\).

More generally, suppose

\[
\log(N/\delta_T)=o(T^{2/3}).
\]

Then

\[
a_n
=
O\!\left(
\sqrt{\frac{\log(N/\delta_T)+1}{T^{2/3}}}
\right)
=o(1),
\]

so eventually \(a_n\le\epsilon/2\). Furthermore,

\[
\frac{n}{T}=O(T^{-1/3})=o(1),
\qquad
\frac{Ha_n}{T}\le a_n=o(1),
\]

and, because \(\log(1/\delta_T)\le\log(N/\delta_T)\),

\[
\frac{d_T}{T}
=
O\!\left(
\sqrt{\frac{\log(1/\delta_T)+1}{T}}
\right)
=o(1),
\]

with the same conclusion for \(d_H/T\). Hence both remainders remain \(o(T)\).

## Randomness and filtration accounting

There are two useful filtration levels.

Before the round’s fresh mixture seed is exposed, the routing kernel is measurable with respect to the observed history and current \(X_t\). After sampling \(J_t\), enlarge this sigma-field by the seed. The realized gate

\[
D_t=d_{\pi_{J_t}}(X_t)
\]

is then measurable before either \(O_t\) or \(Y_t\) is observed. If it chooses \(M\), the model cost is paid and \(O_t\) is revealed. The post-call choice

\[
h_{\pi_{J_t}}(X_t,O_t)
\]

is measurable in the enlarged post-call sigma-field and is determined before \(Y_t\) is revealed.

Equivalently, the seeds may be sampled at the boundary immediately preceding each round. This makes the realized actions predictable in the execution filtration without changing their joint law.

At a pre-randomization node, the joint probability of routing to \(A\) at a hypothetical \((X_t,O_t)\) is

\[
\sum_\pi \widehat q_\pi
\mathbf 1\{d_\pi(X_t)=M,\ h_\pi(X_t,O_t)=A\},
\]

which is predictable. If one conditions on the fact that the model gate selected \(M\) but does not reveal the sampled policy, the post-call audit probability is the predictable normalized quantity

\[
\frac{
\sum_\pi \widehat q_\pi
\mathbf 1\{d_\pi(X_t)=M,\ h_\pi(X_t,O_t)=A\}
}{
\sum_\pi \widehat q_\pi
\mathbf 1\{d_\pi(X_t)=M\}
},
\]

whenever the denominator is positive. If \(J_t\) is included in the execution filtration, the audit probability is simply \(0\) or \(1\). In all formulations, the audit decision is made before \(Y_t\). The theorem’s concentration argument does not require a positive deployment audit floor.

During calibration, the gate is deterministically \(M\) and the audit probability is one. Consequently, \(X_t,O_t,Y_t\) are all observed, and every registered policy’s \(r_t(\pi)\) and \(c_t(\pi)\) can be reconstructed. A1’s potential-output condition is what makes these reconstructed model outputs valid counterfactuals for policies that would have called the model.

The empirical LP depends only on the fully observed prefix. Deployment labels under \(C\) are neither observed nor used. Conditional concentration in Lemma 4 conditions on the audited prefix—not on future seeds—and then applies Hoeffding to the independent suffix pairs \((W_t,J_t)\).

The comparator is executed through the same information nodes. Knowledge of \(P\) determines only the fixed mixture \(q^\star\); its round-\(t\) policy still cannot use \(Y_t\) or \(\ell_t\) before acting. Its unobserved loss under \(C\) is a mathematical performance variable, not feedback available to it.

## Boundary cases and counterexample attempts

- If \(H=0\), deployment sums are empty and \(d_H=0\). APS-LP has zero released loss, and the prefix-cost argument remains valid.

- If \(a_n>\epsilon/2\), statistical selection is bypassed. The always-expert fallback makes both learner claims deterministic; only comparator probability parity requires concentration.

- A policy lying exactly on \(R(q^\star)=\epsilon\) does not break the proof. Mixing it with the globally safe expert by weight \(2a_n/\epsilon\) creates population slack \(2a_n\), enough to absorb one empirical risk deviation while costing at most \(2Ga_n/\epsilon\).

- No optimizer margin, strict complementarity, uniqueness, or local curvature is used. The bridge is global and follows only from convex mixing with \(\pi_E\).

- A nonstationary construction with a correct prefix and erroneous suffix would break Lemma 4, but violates A1.

- A model whose potential output changes depending on whether it will be audited would invalidate prefix reconstruction, but violates A1’s action-independent potential-output condition.

- A router created after seeing the prefix could overfit it and invalidate the finite union bound. A3 excludes that construction by fixing and preregistering \(\Pi\).

- The argument cannot be extended by continuity to \(\epsilon=0\), since \(2a_n/\epsilon\) is undefined. This case is explicitly excluded by A4.

- Calibration is not free: its model calls, audits, and corrections contribute the entire \(nG\) term. The comparator’s model, expert, audit, and correction costs are all represented by the same function \(c_\pi(W)\).

- APS-LP and the comparator share \(W_{1:T}\), so their totals are generally dependent. The proof uses marginal concentration and a union bound, which require no cross-process independence.

## Self-audit

1. The most delicate point is the two-stage randomized filtration. The unnormalized \(\widehat q\)-mass of \(A\)-policies is a joint pre-randomization routing probability; conditional on reaching the model node it must be normalized. Either representation is predictable, and the proof uses only the realized-policy execution law.

2. The safe-mixture cost calculation is the critical optimization step. It uses exactly two cost deviations, giving \(2Ga_n\), and the mixing penalty is \(2Ga_n/\epsilon\). No factor of \(G\), \(2\), or \(\epsilon^{-1}\) is omitted.

3. Coupling to the realized comparator uses

\[
HC(q^\star)\le TC(q^\star)\le C_T^\star+Gd_T.
\]

The first inequality relies only on nonnegative cost. It does not compare the learner and comparator on each individual item.

4. The prefix union bound uses two-sided deviations for both risk and cost, each costing \(\delta/6\); the four one-sided deployment/comparator events cost \(4\delta/6\). The total is exactly \(\delta\).

5. The general \(o(T)\) claim requires fixed positive \(\epsilon\), as stated. Under \(\log(N/\delta_T)=o(T^{2/3})\), \(a_n=o(1)\), so the fallback branch can occur only finitely often.

## Open obligations

None.
