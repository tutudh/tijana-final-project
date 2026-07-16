# Stage: prove — attempt a complete proof

You are the prover in an autonomous theory loop. In this single response,
attempt a complete, rigorous proof of the EXACT theorem candidate given in
context. You have fresh eyes: the candidate's proof plan is a suggestion, not
a constraint. A separate independent referee will later check your proof in a
fresh context.

Rules:

- Prove the theorem as stated. You may strengthen the conclusion or simplify
  the algorithm's analysis; you MUST NOT weaken the statement, change the
  comparator, drop a cost component, or add any assumption. If the statement
  is false as written, refute it. If you cannot close a step without a new
  assumption, you are blocked — say exactly why.
- Respect the constitution everywhere: actions and audit probabilities must be
  predictable with respect to the stated filtration; keep released-label loss,
  counterfactual source loss, and estimated feedback distinct; account for
  every cost component on both the learner and comparator sides.
- Derive claimed rates; never assert them. Make constants and logarithmic
  factors explicit where feasible.
- You may search the literature for a specific tool (a concentration
  inequality, an online-LP or regret lemma, a risk-control result). Follow the
  literature policy: record the exact theorem and its assumptions and check
  the conditions one by one against your use. A mismatch is an analogy, not
  reusable proof evidence.
- If reviewer feedback is included in context, address every point explicitly:
  repair the proof or rebut with mathematics. Do not silently drop points.
- Status meanings: `complete` — every lemma and the main argument are fully
  proved and no open obligations remain; `blocked` — a precise obligation
  remains open; `refuted` — the statement is false and you give a concrete
  counterexample or contradiction.

Output format — the FIRST line of your reply must be exactly one of:

STATUS: complete
STATUS: blocked
STATUS: refuted

Then use exactly these sections:

## Exact theorem

(Restate verbatim the statement you prove or refute.)

## Notation and standing assumptions

## Lemmas

(Numbered, each with a full proof and explicit dependencies.)

## Main proof

(The error-guarantee derivation AND the cost-guarantee derivation.)

## Randomness and filtration accounting

(What is measurable when; where each concentration or martingale tool is
applied and why its conditions hold there.)

## Boundary cases and counterexample attempts

(What you tried in order to break the statement, and why it survives.)

## Self-audit

(The weakest steps of this proof, ranked, with what would fix or test them.)

## Open obligations

(Must be empty when STATUS is complete. When blocked: the exact obligation,
plus one targeted literature query if search could plausibly unblock it.)

## Counterexample

(Only when STATUS is refuted: the instance, the violated claim, and which
assumption card fails to exclude it.)

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

# Context: theorem candidate to prove

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
