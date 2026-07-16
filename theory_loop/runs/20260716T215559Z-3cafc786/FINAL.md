# Surviving proof candidate — pending human review

This artifact was produced by an autonomous loop. It is a model-
generated proof candidate that passed 2 independent fresh-context review(s). It is NOT an established theorem or novelty claim until a human reviews and
promotes it.

- Run: 20260716T215559Z-3cafc786
- Candidate: calls/0001-propose
- Proof: calls/0002-prove
- Calls made: 4; total cost: $0.00

## Theorem candidate

STATUS: proposed

## Setting and assumption ladder

**Candidate: Camouflaged Independent-Cell Apple Tasting (CICAT) lower bound.** This is an impossibility candidate, so the “algorithm” below specifies the full learner class quantified by the theorem rather than prescribing one learner.

Fix horizon \(T\ge 8\), risk budget \(\epsilon=1/4\), Lipschitz bound \(L=1\), and

\[
M=\lfloor T^{1/3}\rfloor,\qquad
\delta=\frac{1}{64(M+1)},\qquad
\Theta_T=\{-1,+1\}^{M}.
\]

For \(\theta\in\Theta_T\), write \(\bar\theta=M^{-1}\sum_i\theta_i\). The common score marginal has:

\[
\Pr(S=0)=\tfrac14,\qquad
\Pr(S=\tfrac12)=\tfrac12,\qquad
\Pr\!\left(S=s_i\right)=\frac{1}{4M},
\]

where

\[
s_i=\frac12+\frac{i}{2(M+1)},\qquad i=1,\ldots,M.
\]

The cheap model always outputs \(\widehat Y=0\). Conditional on \(S=s\),

\[
Y=L\sim\operatorname{Bernoulli}(m_\theta(s)),
\]

with support-point means

\[
m_\theta(0)=\frac18-\delta\bar\theta,\qquad
m_\theta(\tfrac12)=\frac12,\qquad
m_\theta(s_i)=\frac12+\theta_i\delta.
\]

Between support points, define \(m_\theta\) by linear interpolation and extend it constantly after \(s_M\). Every \(m_\theta\) is globally \(1\)-Lipschitz: the largest hard-cell slope is \(4\delta(M+1)=1/16\), while the slope from \(0\) to \(1/2\) is below \(1\).

The anchor at \(S=0\) camouflages aggregate error:

\[
\mathbb E_\theta[Y]
=\frac14m_\theta(0)
 +\frac{1}{4M}\sum_i m_\theta(s_i)
 +\frac12m_\theta(\tfrac12)
=\frac{13}{32}
\]

for every \(\theta\). Thus the joint law of \((S,\widehat Y)\) and the score-blind label mean are identical throughout the family.

**Information timeline.** Let \(\mathcal H_{t-1}\) contain all past scores, actions, internal randomness, released labels, costs, and expert labels from deferred or audited rounds.

1. The learner pays \(c_M=0\) and observes \((S_t,\widehat Y_t)\).
2. Using only \((\mathcal H_{t-1},S_t,\widehat Y_t)\) and fresh internal randomness, it chooses release, defer, or audit-and-correct.
3. On release, it outputs \(\widehat Y_t\), pays no expert cost, and never observes \(Y_t\).
4. On defer, it pays one, observes \(Y_t\), and releases the expert label.
5. On audit, it pays one, observes \(Y_t\), corrects if necessary, and releases \(Y_t\). Here \(c_R=0\).
6. Only then may the learner update its state.

Define the three losses separately:

\[
L_t=\mathbf 1\{\widehat Y_t\ne Y_t\}=Y_t
\]

is the counterfactual cheap-source loss,

\[
R_t=L_t\mathbf 1\{A_t=\mathrm{release}\}
\]

is final released-label loss, and any estimate constructed from revealed labels is merely learner feedback and is not used in either \(R_t\) or cost accounting.

**Assumption ladder.**

- With only bounded stationary feedback and no regularity, arbitrarily many unrelated score cells could make regret nearly linear; this does not resolve the A1–A3 rate.
- Adding i.i.d. arrivals but no score regularity leaves the same obstruction.
- At the target A1–A3 rung, global Lipschitzness limits independent cells of gap \(\delta\) to \(M=O(1/\delta)\). Balancing \(M\asymp1/\delta\) with \(T/M\asymp1/\delta^2\) yields the candidate \(T^{2/3}\) obstruction. No stronger assumption is added.

**A1 — i.i.d. stochastic arrivals**

- Mathematical statement: Conditional on fixed \(\theta\), \((S_t,Y_t,\widehat Y_t)_{t=1}^T\) are i.i.d. with the law above.
- Operational meaning: The deployment population is stationary and has no adaptive drift.
- Diagnostic or falsification: Test score frequencies and audited conditional error rates for temporal drift, serial dependence, or change points.
- Required by: Exact parity with OBSR and the product-form sequential KL calculation.
- Optimizer-local: no.
- Classification: problem.

**A2 — bounded costs and perfect expert**

- Mathematical statement: \(L_t\in\{0,1\}\), \(c_M=c_R=0\), and every defer or audit costs exactly one and reveals the authoritative \(Y_t\).
- Operational meaning: Expert review is reliable and has a known normalized fee; the model call and post-audit correction are free in this clean lower-bound instance.
- Diagnostic or falsification: Measure expert disagreement on repeated labels and audit invoices for action-dependent or time-varying costs.
- Required by: Common cost accounting, the reduction of defer and audit to the same revealing action, and A2 parity.
- Optimizer-local: no.
- Classification: problem.

**A3 — global score regularity**

- Mathematical statement: \(|m_\theta(s)-m_\theta(s')|\le |s-s'|\) for all \(s,s'\in[0,1]\), for every \(\theta\).
- Operational meaning: Nearby confidence scores have nearby conditional cheap-model error probabilities.
- Diagnostic or falsification: On an independently audited sample, construct simultaneous confidence intervals for binwise error rates and test whether adjacent-bin differences exceed score distance plus sampling uncertainty.
- Required by: Exact parity with OBSR and the relation \(M\delta=\Theta(1)\) that produces the \(T^{2/3}\) packing.
- Optimizer-local: no.
- Classification: problem.

No margin, uniqueness, curvature, strict complementarity, or condition defined around an unknown optimal policy is active.

## Algorithm

The theorem quantifies every randomized adaptive learner representable as follows.

Its state is \(Z_{t-1}\), initialized arbitrarily. After observing \(S_t\), it draws

\[
A_t\sim\pi_t(\,\cdot\mid Z_{t-1},S_t,\widehat Y_t),
\]

where \(\pi_t\) is any predictable stochastic kernel on

\[
\{\mathrm{release},\mathrm{defer},\mathrm{audit}\}.
\]

Let

\[
I_t=\mathbf 1\{A_t\in\{\mathrm{defer},\mathrm{audit}\}\}.
\]

Then the total cost is exactly

\[
C_T=\sum_{t=1}^T I_t,
\]

including all expert deferrals and audits. The update is any measurable rule

\[
Z_t=U_t(Z_{t-1},S_t,A_t,I_tY_t,I_t).
\]

Thus the lower bound includes zero audit probability, forced floors, confidence-triggered audits, posterior sampling, sequential tests, and algorithms that know \(T,\epsilon,L\), the score marginal, and the entire family \(\Theta_T\) except the unknown \(\theta\). Audit floors and estimators are algorithm choices; none is assumed of the data.

The distribution-aware comparator uses a Borel release probability \(a:[0,1]\to[0,1]\) and the same current score, action semantics, and costs:

\[
C^\star_{\theta,T}
=T\inf_{\substack{a\ {\rm Borel}\\
\mathbb E_\theta[a(S)m_\theta(S)]\le1/4}}
\mathbb E_\theta[1-a(S)].
\]

Auditing is unnecessary for this comparator because audit and defer have identical cost, feedback-independent final loss, and release semantics.

Its explicit optimum releases the anchor, releases every cell with \(\theta_i=-1\), defers every cell with \(\theta_i=+1\), and releases the boundary atom \(S=1/2\) with probability

\[
\alpha_\theta
=\frac{1/4-r_\theta}{1/4}=1-4r_\theta,
\]

where

\[
r_\theta
=\frac14m_\theta(0)
 +\frac{1}{4M}\sum_{i:\theta_i=-1}m_\theta(s_i)
=\frac{3}{32}-\frac{\delta}{8}
 -\bar\theta\left(\frac1{16}+\frac{\delta}{8}\right).
\]

Since \(r_\theta\in[1/32-\delta/4,5/32]\), one has \(0<\alpha_\theta<1\). Consequently, the comparator’s expected released error is exactly \(T/4\) on every instance: the constraint is binding.

## Theorem candidate

**Theorem (CICAT priced minimax lower bound).** For every integer \(T\ge8\), let \(\mathcal F_T=\{P_\theta:\theta\in\Theta_T\}\) be the finite i.i.d. family above. Every randomized adaptive algorithm obeying the stated protocol satisfies, with exchange rate \(\eta=2\),

\[
\max_{\theta\in\Theta_T}
\left\{
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
+2\left(
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
-\frac{T}{4}
\right)
\right\}
\ge
\frac{1}{2048}T^{2/3}.
\]

Expectations cover the i.i.d. arrivals, Bernoulli labels, and learner randomization. This is a fixed-horizon expected guarantee; the learner may know the horizon and the family.

Consequently, setting

\[
c_1(1/4,1)=\frac1{2048},
\qquad
c_0=\frac{c_1}{2\eta}=\frac1{8192},
\]

any algorithm satisfying

\[
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
\le \frac{T}{4}+\frac1{8192}T^{2/3}
\qquad\text{for every }\theta\in\Theta_T
\]

must, on at least one instance, satisfy the cost lower bound

\[
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
\ge \frac1{4096}T^{2/3}.
\]

Thus, if proved, CICAT and the standing OBSR upper bound would identify the A1–A3 minimax exponent as \(2/3\), leaving a \(\sqrt{\log T}\)-type polylogarithmic gap.

## Why this can work: proof plan

1. **Comparator and supporting price.** At \(\eta=2\), the expected one-round priced costs are

   \[
   \begin{array}{c|cc}
   &\text{release}&\text{reveal}\\
   \hline
   S=0&2m_\theta(0)<1&1\\
   S=s_i,\ \theta_i=-1&1-2\delta&1\\
   S=1/2&1&1\\
   S=s_i,\ \theta_i=+1&1+2\delta&1 .
   \end{array}
   \]

   Hence the explicit constrained comparator is also a minimizer of the \(\eta\)-priced Lagrangian and has binding risk. The theorem’s left side is therefore its Lagrangian regret. Every wrong hard-cell action costs exactly \(2\delta\); anchor mistakes are nonnegative and the boundary atom is neutral.

2. **Adaptive divergence decomposition.** Pair \(\theta\) and \(\theta^{(i)}\), differing only in bit \(i\). Labels can distinguish them only when the learner reveals hard cell \(i\), or through the weak anchor perturbation \(2\delta/M\). The sequential KL chain rule and

   \[
   \operatorname{kl}(\operatorname{Ber}(p),\operatorname{Ber}(q))
   \le \frac{(p-q)^2}{q(1-q)}
   \]

   give

   \[
   D_{\rm KL}(P_\theta^{\mathcal A}\Vert
              P_{\theta^{(i)}}^{\mathcal A})
   \le
   17\delta^2\frac{T}{4M}
   +40\frac{\delta^2T}{M^2}
   <\frac1{100}.
   \]

   This already allows the learner to reveal every occurrence of cell \(i\), so ordinary deferrals and audits are fully covered.

3. **Testing-to-action lemma.** Pinsker gives pairwise total variation below \(0.071\). At every occurrence of cell \(i\), the sum of the probability of revealing under the safe sign and releasing under the unsafe sign is therefore at least \(3/4\). Since the cell occurs with probability \(1/(4M)\), paired expected wrong actions are at least \(3T/(16M)\).

4. **Hypercube averaging.** Averaging each pair over the uniform product prior on \(\Theta_T\), summing over \(i\), and multiplying by the \(2\delta\) priced gap yields

   \[
   \frac1{2^M}\sum_\theta
   \left[\text{priced regret on }\theta\right]
   \ge \frac{3\delta T}{16}
   =\frac{3T}{1024(M+1)}
   \ge \frac1{512}T^{2/3}.
   \]

   Taking the maximum and weakening the constant gives the stated \(1/2048\).

5. **Two-sided conversion.** On the instance attaining the priced lower bound, subtract at most
   \(2c_0T^{2/3}=c_1T^{2/3}/2\) for allowed error slack, leaving the claimed cost regret.

The riskiest step is formalizing the testing-to-action inequality for adaptive kernels after the current score is observed. The intended proof conditions on \(S_t=s_i\), applies data processing to the pre-action transcript, and uses that the algorithm’s action kernel is identical under the paired instances.

## Attack log

- **Aggregate-only two-point construction rejected.** If uncertainty changes only the amount released from a known boundary cell, the binding multiplier makes every boundary mixture have identical priced value. An algorithm need not learn the aggregate at all. This explains why a simple unknown-mean construction cannot prove the mandatory priced statement.

- **Paired sign swaps rejected.** A local constraint “one safe and one unsafe cell” lets a comparator-optimal deferral reveal one sign and determine its partner. CICAT uses a full product hypercube: learning a high-error cell reveals nothing about any other hard bit.

- **Independent signs without camouflage rejected.** Their aggregate error varies with \(\sum_i\theta_i\), exposing a score-blind diagnostic. The anchor cancels this variation exactly. Its per-bit signal is only \(2\delta/M\), and its contribution is included in the KL bound.

- **Fixed number of cells rejected.** With constant \(M\), one-sided stochastic testing gives only \(\Theta(\sqrt T)\). Global Lipschitzness permits \(M\asymp T^{1/3}\) cells at gap \(\delta\asymp T^{-1/3}\), producing \(M\) constant-difficulty tests and total \(T^{2/3}\) priced regret.

- **Free labels attacked.** On unsafe cells, comparator deferrals indeed reveal labels for free. In the paired comparison, however, the corresponding safe instance fully releases that same independent cell; obtaining its label then costs \(2\delta\) in priced regret. Even revealing all \(T/(4M)\) expected occurrences leaves pairwise KL below \(1/100\).

- **Adaptive audits attacked.** With \(c_R=0\), audit and defer have identical information, cost, and released loss. Combining both into \(I_t\) means the proof already grants the learner the strongest possible use of either action.

- **Camouflage leakage attacked.** Auditing the anchor can estimate \(\bar\theta\), but flipping one bit changes its mean by only \(2\delta/M\). Even \(T\) anchor labels contribute \(O(T\delta^2/M^2)=O(T^{-1/3})\) KL per bit.

- **Always-defer and deliberate error slack attacked.** Because \(\eta=2\) is a common supporting price, always deferring safe or anchor mass has nonnegative priced regret. The corollary allows error slack of the full \(T^{2/3}\) order with the required tied constant, rather than hiding it in a smaller-order condition.

No additional problem assumption was introduced during these repairs; the changes are entirely in the hard-instance mechanism.

## Relation to known results

- Cesa-Bianchi, Lugosi, and Stoltz, “Regret Minimization Under Partial Monitoring,” Theorem 5.1, prove expected cumulative regret at least \(n^{2/3}/7\) for an adversarial three-action label-efficient game, against the best fixed action. The full text and theorem were checked. Its arrivals, comparator, and unconstrained loss matrix differ, so it is an analogy rather than proof evidence; CICAT instead uses i.i.d. contextual instances, a distribution-aware risk-constrained comparator, and priced cost/error regret. [Primary paper](https://cesa-bianchi.di.unimi.it/Pubblicazioni/pmonitoring.pdf)

- Grant and Leslie, “Apple Tasting Revisited,” Theorem 1, obtain Bayesian regret \(O(\sqrt{dT\log T})\) for contextual logistic apple tasting with a fixed finite-dimensional parameter and Thompson sampling. The full text was checked. Its global parametric coupling lets every revealing observation inform the same parameter; CICAT’s \(M=\Theta(T^{1/3})\) Lipschitz cells carry independent nonparametric bits, and its comparator is constrained expected cost rather than a Bayesian roundwise oracle. [Primary paper](https://www.lancaster.ac.uk/staff/grantj/AppleTasting.pdf)

- Harris, Podimata, and Wu, “Strategic Apple Tasting,” Theorem B.1, give a high-probability \(\widetilde O(\sqrt T)\) strategic-regret bound under stochastic contexts with a density lower bound and linear rewards. The full text was checked. This again relies on shared finite-dimensional structure and implicit exploration and does not include a released-error constraint or the OBSR comparator. [NeurIPS paper](https://papers.neurips.cc/paper_files/paper/2023/file/fcd3909db30887ce1da519c4468db668-Paper-Conference.pdf)

- Cesari and Colomboni, “Two-Action Apple Tasting with Switching Costs,” Theorem 3, prove the oblivious minimax expected regret is exactly \(\Theta(\sqrt T)\), even with unit switching costs. The full text was checked. It rules out attributing CICAT’s exponent merely to the two-action revealing graph: CICAT’s proposed obstruction is the growing collection of independent Lipschitz score cells plus a constrained distribution-aware benchmark. [Primary preprint](https://arxiv.org/abs/2606.03851)

- Castro and Nowak, “Minimax Bounds for Active Learning,” Theorem 1 and Appendix A, use finite hypothesis testing and adaptive-sampling KL decompositions for Hölder boundary-fragment classes. The full text was checked. Their labels are acquired through actively selected feature locations, their comparator is a Bayes classifier, and their rate depends on boundary/noise assumptions absent here. Only the finite-packing proof architecture is analogous. [Primary paper](https://nowak.ece.wisc.edu/COLT07.pdf)

- Kleinberg, “Nearly Tight Bounds for the Continuum-Armed Bandit Problem,” Theorems 3.1 and 4.2, gives, for Lipschitz exponent one, an \(O(T^{2/3}\log^{1/3}T)\) upper bound and excludes every smaller polynomial exponent in stochastic and adversarial continuum-armed bandits. The full text was checked. Its mechanism is gap-priced spatial search with feedback from the chosen arm; CICAT uses one-sided paid labels and independent score cells straddling a common constraint price. The matching exponent is therefore not evidence of the same phenomenon. [Primary paper](https://www.cs.cornell.edu/~rdk/papers/ContArm.pdf)

- The standing OBSR result from run 20260716T183433Z-75ac21c9 supplies the corresponding \(O_{\epsilon,L}(T^{2/3}\sqrt{\log(T/\delta)})\) high-probability upper bound under the same A1–A3 assumptions and comparator. This rate was supplied in the brief but its internal proof artifact was not independently rechecked in this fresh context.

A targeted search also located An et al., “Efficient Algorithms for Contextual Apple Tasting with Log-Loss,” a DEMO 2026 workshop submission involving logistic contextual models and LLM cascading. Its full text could not be verified because the primary OpenReview PDF presented an access challenge, so its exact theorem and assumption mapping remain **unverified** and it is not used as proof evidence. [OpenReview record](https://openreview.net/forum?id=VlhBTulTYR)

These checks do not establish novelty; that remains for human review.

## Proof candidate

STATUS: complete

## Exact theorem

**Theorem (CICAT priced minimax lower bound).** For every integer \(T\ge8\), let \(\mathcal F_T=\{P_\theta:\theta\in\Theta_T\}\) be the finite i.i.d. family above. Every randomized adaptive algorithm obeying the stated protocol satisfies, with exchange rate \(\eta=2\),

\[
\max_{\theta\in\Theta_T}
\left\{
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
+2\left(
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
-\frac{T}{4}
\right)
\right\}
\ge
\frac{1}{2048}T^{2/3}.
\]

Expectations cover the i.i.d. arrivals, Bernoulli labels, and learner randomization. This is a fixed-horizon expected guarantee; the learner may know the horizon and the family.

Consequently, setting

\[
c_1(1/4,1)=\frac1{2048},
\qquad
c_0=\frac{c_1}{2\eta}=\frac1{8192},
\]

any algorithm satisfying

\[
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]
\le \frac{T}{4}+\frac1{8192}T^{2/3}
\qquad\text{for every }\theta\in\Theta_T
\]

must, on at least one instance, satisfy the cost lower bound

\[
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
\ge \frac1{4096}T^{2/3}.
\]

Thus, if proved, CICAT and the standing OBSR upper bound would identify the A1–A3 minimax exponent as \(2/3\), leaving a \(\sqrt{\log T}\)-type polylogarithmic gap.

## Notation and standing assumptions

Let

\[
M=\lfloor T^{1/3}\rfloor,\qquad
\delta=\frac1{64(M+1)},\qquad
\Theta_T=\{-1,+1\}^M.
\]

Because \(T\ge8\), \(M\ge2\) and \(\delta\le1/192\).

For an algorithm \(\mathcal A\), put

\[
I_t=\mathbf 1\{A_t\in\{\mathrm{defer},\mathrm{audit}\}\}.
\]

Thus \(I_t=0\) is release and \(I_t=1\) is a revealing action. Since both revealing actions cost one, return the expert label, and have \(c_R=0\),

\[
C_T=\sum_{t=1}^T I_t,\qquad
R_t=(1-I_t)Y_t.
\]

The counterfactual cheap-source loss is \(L_t=Y_t\), whether or not it is observed. It is distinct from \(R_t\). Any importance-weighted or otherwise estimated loss is only internal feedback and appears in neither definition.

For each \(\theta\), define the priced regret

\[
\Delta_\theta
:=
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
+2\left(
\mathbb E_\theta\!\left[\sum_{t=1}^T R_t\right]-\frac T4
\right).
\]

For a bit \(i\), write \(\theta^{(i)}\) for the vector obtained by flipping \(\theta_i\). When the remaining \(M-1\) bits are fixed, denote the paired vectors by \(\theta^-\) and \(\theta^+\), according as their \(i\)-th bit is \(-1\) or \(+1\).

The learner is fixed independently of the unknown \(\theta\). Its kernels may depend on \(T,\epsilon,L\), the score marginal, and the full description of the family.

## Lemmas

### Lemma 1 — Instance validity, Lipschitzness, and camouflage

Every \(P_\theta\) satisfies A1–A3 with the common parameters \(\epsilon=1/4\), \(L=1\), \(c_M=c_R=0\). Moreover,

\[
\mathbb E_\theta[Y]=\frac{13}{32}
\]

for every \(\theta\).

#### Proof

The support-point means lie in \([0,1]\), since

\[
m_\theta(0)\in[1/8-\delta,1/8+\delta],
\qquad
m_\theta(s_i)\in[1/2-\delta,1/2+\delta].
\]

Linear interpolation preserves this range. The rounds are i.i.d. by construction, establishing A1. The stated perfect expert and costs establish A2.

It remains to check A3. On \([0,1/2]\), the interpolation slope is

\[
\frac{1/2-(1/8-\delta\bar\theta)}{1/2}
=\frac34+2\delta\bar\theta,
\]

whose absolute value is at most \(3/4+2/192<1\).

Between \(1/2\) and \(s_1\), the absolute slope is

\[
\frac{\delta}{1/[2(M+1)]}
=2\delta(M+1)=\frac1{32}.
\]

Between successive hard cells, it is at most

\[
\frac{2\delta}{1/[2(M+1)]}
=4\delta(M+1)=\frac1{16}.
\]

After \(s_M\), the function is constant. A continuous piecewise-linear function whose slopes have absolute value at most one is globally \(1\)-Lipschitz.

Finally,

\[
\begin{aligned}
\mathbb E_\theta[Y]
&=\frac14\left(\frac18-\delta\bar\theta\right)
 +\frac1{4M}\sum_{i=1}^M\left(\frac12+\theta_i\delta\right)
 +\frac12\cdot\frac12\\
&=\frac1{32}-\frac{\delta\bar\theta}{4}
  +\frac18+\frac{\delta\bar\theta}{4}
  +\frac14\\
&=\frac{13}{32}.
\end{aligned}
\]

Thus the score marginal, model output, and score-blind label mean are all common to the family. ∎

### Lemma 2 — Comparator optimality and the priced-regret decomposition

The displayed comparator policy is feasible, has expected released error exactly \(1/4\) per round, and attains \(C^\star_{\theta,T}\). Furthermore,

\[
\Delta_\theta
\ge
2\delta\sum_{i=1}^M\mathbb E_\theta[W_i],
\]

where

\[
W_i
=
\sum_{t=1}^T
\mathbf 1\{S_t=s_i\}
\begin{cases}
I_t,&\theta_i=-1,\\
1-I_t,&\theta_i=+1.
\end{cases}
\]

#### Proof

Let \(n_-=\#\{i:\theta_i=-1\}=M(1-\bar\theta)/2\). The risk from releasing the anchor and all negative hard cells is

\[
\begin{aligned}
r_\theta
&=\frac14\left(\frac18-\delta\bar\theta\right)
 +\frac{n_-}{4M}\left(\frac12-\delta\right)\\
&=\frac3{32}-\frac{\delta}{8}
 -\bar\theta\left(\frac1{16}+\frac{\delta}{8}\right).
\end{aligned}
\]

This is decreasing in \(\bar\theta\), so

\[
\frac1{32}-\frac{\delta}{4}
\le r_\theta\le\frac5{32}.
\]

In particular \(0<r_\theta<1/4\). The boundary atom has probability \(1/2\) and mean \(1/2\), so releasing it with probability

\[
\alpha_\theta=1-4r_\theta
\]

adds \(\alpha_\theta/4=1/4-r_\theta\) risk. Hence the total risk is exactly \(1/4\), and \(0<\alpha_\theta<1\).

For any release probability \(a(s)\), define its one-round priced objective

\[
J_\theta(a)
=
\mathbb E_\theta[1-a(S)]
+2\mathbb E_\theta[a(S)m_\theta(S)].
\]

Pointwise, this is the expectation of

\[
h_\theta(s,a)=1-a+a\,2m_\theta(s)
=1+a(2m_\theta(s)-1).
\]

Thus a pointwise minimizer releases when \(m_\theta(s)<1/2\), reveals when \(m_\theta(s)>1/2\), and may take any mixture when \(m_\theta(s)=1/2\). The displayed comparator does exactly this and chooses its boundary mixture to make risk binding. Call it \(a_\theta^\star\).

If \(a\) is any feasible Borel policy, then pointwise optimality gives

\[
J_\theta(a)\ge J_\theta(a_\theta^\star).
\]

Since \(a\) has risk at most \(1/4\), while \(a_\theta^\star\) has risk exactly \(1/4\),

\[
\begin{aligned}
\mathbb E_\theta[1-a(S)]
&=J_\theta(a)-2\mathbb E_\theta[a(S)m_\theta(S)]\\
&\ge J_\theta(a_\theta^\star)-\frac12\\
&=\mathbb E_\theta[1-a_\theta^\star(S)].
\end{aligned}
\]

Therefore \(a_\theta^\star\) attains the benchmark.

Now consider the learner. Conditional on the pre-label information, current score, and action, \(Y_t\) remains Bernoulli with mean \(m_\theta(S_t)\). Hence

\[
\mathbb E_\theta[I_t+2R_t\mid\mathcal H_{t-1},S_t,A_t]
=
I_t+2(1-I_t)m_\theta(S_t).
\]

The comparator’s total priced objective is

\[
C^\star_{\theta,T}+2(T/4).
\]

Consequently, \(\Delta_\theta\) is the learner’s excess expected priced objective over the pointwise minimum.

On a hard cell with \(\theta_i=-1\), release has priced value \(1-2\delta\) and reveal has value \(1\); revealing incurs excess \(2\delta\). On a hard cell with \(\theta_i=+1\), reveal has value \(1\) and release has value \(1+2\delta\); releasing incurs excess \(2\delta\). At \(S=1/2\), both actions have value one. At the anchor, release is optimal, so any revealing action has nonnegative excess. Dropping that nonnegative anchor excess proves

\[
\Delta_\theta
\ge2\delta\sum_i\mathbb E_\theta[W_i].
\]
∎

### Lemma 3 — Uniform pairwise information bound

For every \(i\) and every paired \(\theta^-,\theta^+\),

\[
D_{\mathrm{KL}}\!\left(
P_{\theta^-}^{\mathcal A}\,\middle\|\,P_{\theta^+}^{\mathcal A}
\right)<\frac1{100},
\]

where \(P_\theta^{\mathcal A}\) may denote either the complete observable interaction law or any pre-action history law. Consequently,

\[
\operatorname{TV}\!\left(
P_{\theta^-}^{\mathcal A},P_{\theta^+}^{\mathcal A}
\right)<\frac14.
\]

#### Proof

First, for \(p,q\in(0,1)\), the inequality \(\log x\le x-1\) gives

\[
\begin{aligned}
\operatorname{kl}(\operatorname{Ber}(p),\operatorname{Ber}(q))
&\le
p\left(\frac pq-1\right)
+(1-p)\left(\frac{1-p}{1-q}-1\right)\\
&=\frac{(p-q)^2}{q(1-q)}.
\end{aligned}
\]

The two paired instances differ only at hard cell \(i\) and at the anchor.

At hard cell \(i\), the two means are \(1/2-\delta\) and \(1/2+\delta\). Since \(\delta\le1/192\),

\[
q(1-q)=\frac14-\delta^2>\frac4{17}.
\]

Therefore the hard-cell Bernoulli divergence, in either direction, is at most

\[
\frac{(2\delta)^2}{4/17}=17\delta^2.
\]

Flipping one bit changes \(\bar\theta\) by \(2/M\), so the anchor means differ by \(2\delta/M\). Every possible anchor mean lies in

\[
[1/8-\delta,1/8+\delta]\subseteq[23/192,25/192].
\]

Since \(q<1/2\),

\[
q(1-q)\ge \frac{23}{192}\frac{169}{192}
=\frac{3887}{36864}>\frac1{10}.
\]

Thus the anchor divergence is at most

\[
40\frac{\delta^2}{M^2}.
\]

Consider first the full latent i.i.d. sequence \((S_t,Y_t)_{t=1}^T\), even including labels that the learner never observes. Product additivity of KL yields

\[
\begin{aligned}
D_{\mathrm{KL}}(P_{\theta^-}^{\mathrm{latent}}
 \|P_{\theta^+}^{\mathrm{latent}})
&\le
T\left[
\frac1{4M}(17\delta^2)
+\frac14\left(40\frac{\delta^2}{M^2}\right)
\right]\\
&\le
17\delta^2\frac{T}{4M}
+40\frac{\delta^2T}{M^2}.
\end{aligned}
\]

The last expression deliberately loosens the anchor term. Because \(M=\lfloor T^{1/3}\rfloor\),

\[
T<(M+1)^3.
\]

Using \(\delta^2=1/[4096(M+1)^2]\),

\[
D_{\mathrm{KL}}
<
\frac{M+1}{4096}
\left(\frac{17}{4M}+\frac{40}{M^2}\right).
\]

For \(M\ge2\),

\[
(M+1)\left(\frac{17}{4M}+\frac{40}{M^2}\right)
=
\frac{17}{4}+\frac{177}{4M}+\frac{40}{M^2}
\le\frac{291}{8}.
\]

Hence

\[
D_{\mathrm{KL}}<\frac{291}{32768}<\frac1{100}.
\]

The algorithm’s internal random seed has the same law under both instances. Its observable histories and actions are measurable randomized transformations of the latent sequence and that seed. The data-processing inequality therefore transfers the same KL upper bound to the full observable interaction and to every truncated pre-action history.

Finally, Pinsker’s inequality gives

\[
\operatorname{TV}
\le\sqrt{\frac12D_{\mathrm{KL}}}
<\frac1{\sqrt{200}}<\frac14.
\]
∎

### Lemma 4 — Adaptive testing-to-action inequality

For every \(i\) and every paired \(\theta^-,\theta^+\),

\[
\mathbb E_{\theta^-}
 \sum_{t=1}^T\mathbf 1\{S_t=s_i\}I_t
+
\mathbb E_{\theta^+}
 \sum_{t=1}^T\mathbf 1\{S_t=s_i\}(1-I_t)
\ge
\frac{3T}{16M}.
\]

#### Proof

Let \(H_{t-1}\) denote the complete observable history before \(S_t\) is drawn, including the learner’s state and all previously revealed labels. Conditional on \(H_{t-1}=h\) and \(S_t=s_i\), let

\[
k_{t,i}(h)
=
\Pr_{\mathcal A}(I_t=1\mid H_{t-1}=h,S_t=s_i),
\]

where the probability integrates over fresh learner randomization. This is the same measurable function under both paired instances because the algorithm does not know the unknown sign.

Let \(\nu_t^-\) and \(\nu_t^+\) be the laws of \(H_{t-1}\) under the two instances. Lemma 3 and data processing imply

\[
\operatorname{TV}(\nu_t^-,\nu_t^+)<\frac14.
\]

Since \(0\le k_{t,i}\le1\),

\[
\left|
\int k_{t,i}\,d\nu_t^-
-\int k_{t,i}\,d\nu_t^+
\right|
\le\operatorname{TV}(\nu_t^-,\nu_t^+)<\frac14.
\]

Write these two integrals as \(q_t^-\) and \(q_t^+\). Then

\[
q_t^-+(1-q_t^+)
=1+q_t^--q_t^+
\ge\frac34.
\]

The current score is independent of \(H_{t-1}\) under both instances and has common probability

\[
\Pr(S_t=s_i)=\frac1{4M}.
\]

Therefore

\[
\begin{aligned}
&\mathbb E_{\theta^-}
 \sum_{t=1}^T\mathbf 1\{S_t=s_i\}I_t
+
\mathbb E_{\theta^+}
 \sum_{t=1}^T\mathbf 1\{S_t=s_i\}(1-I_t)\\
&\qquad
=\frac1{4M}\sum_{t=1}^T
\bigl(q_t^-+1-q_t^+\bigr)\\
&\qquad
\ge\frac1{4M}\cdot T\cdot\frac34
=\frac{3T}{16M}.
\end{aligned}
\]
∎

### Lemma 5 — Hypercube average

The uniform-prior average priced regret satisfies

\[
\frac1{2^M}\sum_{\theta\in\Theta_T}\Delta_\theta
\ge
\frac{3\delta T}{16}
\ge
\frac1{512}T^{2/3}.
\]

#### Proof

Fix \(i\). Partition the hypercube into its \(2^{M-1}\) unordered pairs differing only in coordinate \(i\). For each pair, Lemma 4 lower-bounds the sum of the two expected \(i\)-th wrong-action counts by \(3T/(16M)\). Hence

\[
\frac1{2^M}\sum_{\theta\in\Theta_T}
\mathbb E_\theta[W_i]
\ge
\frac{2^{M-1}}{2^M}\frac{3T}{16M}
=
\frac{3T}{32M}.
\]

Summing over \(i\),

\[
\frac1{2^M}\sum_\theta
\sum_{i=1}^M\mathbb E_\theta[W_i]
\ge\frac{3T}{32}.
\]

Lemma 2 now gives

\[
\frac1{2^M}\sum_\theta\Delta_\theta
\ge2\delta\frac{3T}{32}
=\frac{3\delta T}{16}
=\frac{3T}{1024(M+1)}.
\]

Let \(x=T^{1/3}\ge2\). Since \(M+1\le x+1\le3x/2\),

\[
\frac{3T}{1024(M+1)}
\ge
\frac{3x^3}{1024(3x/2)}
=
\frac{x^2}{512}
=
\frac1{512}T^{2/3}.
\]
∎

## Main proof

By Lemma 5, the maximum is at least the uniform average:

\[
\max_{\theta\in\Theta_T}\Delta_\theta
\ge
\frac1{2^M}\sum_{\theta\in\Theta_T}\Delta_\theta
\ge
\frac1{512}T^{2/3}.
\]

This is stronger than the claimed bound, and therefore

\[
\max_{\theta\in\Theta_T}
\left\{
\mathbb E_\theta[C_T]-C^\star_{\theta,T}
+2\left(
\mathbb E_\theta\!\left[\sum_tR_t\right]-\frac T4
\right)
\right\}
\ge
\frac1{2048}T^{2/3}.
\]

The error side is accounted for as follows. Lemma 2 proves that every comparator has expected released error exactly \(T/4\), so the primary inequality compares the learner’s released-label error to the binding comparator risk without replacing it by counterfactual loss or estimated feedback.

For the cost consequence, suppose the stated error guarantee holds on every \(\theta\). Choose an instance \(\widehat\theta\) attaining the priced lower bound. Then

\[
\begin{aligned}
\mathbb E_{\widehat\theta}[C_T]-C^\star_{\widehat\theta,T}
&=
\Delta_{\widehat\theta}
-2\left(
\mathbb E_{\widehat\theta}\!\left[\sum_tR_t\right]-\frac T4
\right)\\
&\ge
c_1T^{2/3}-2c_0T^{2/3}.
\end{aligned}
\]

Because \(c_0=c_1/(2\eta)=c_1/4\) and \(\eta=2\),

\[
2c_0=\frac{c_1}{2}.
\]

Consequently,

\[
\mathbb E_{\widehat\theta}[C_T]-C^\star_{\widehat\theta,T}
\ge
\frac{c_1}{2}T^{2/3}
=
\frac1{4096}T^{2/3}.
\]

This proves both assertions. ∎

## Randomness and filtration accounting

Before round \(t\), \(\mathcal H_{t-1}\) contains only past scores, actions, costs, released outputs, learner randomness already used, and expert labels revealed by earlier deferrals or audits. The current pair \((S_t,Y_t)\) is independent of \(\mathcal H_{t-1}\) conditional on \(\theta\).

After observing \(S_t\) and the constant output \(\widehat Y_t=0\), the learner applies a common predictable kernel, possibly using fresh independent randomness. Thus \(I_t\) is chosen without observing \(Y_t\), and

\[
\mathbb E_\theta[Y_t\mid\mathcal H_{t-1},S_t,A_t]
=m_\theta(S_t).
\]

This predictability justifies the priced conditional expectation in Lemma 2.

On a release, the learner observes no \(Y_t\); nevertheless \(R_t=Y_t\) is a well-defined latent released-label loss. On a revealing action, the expert label is observed and the released-label loss is zero. The proof never treats an unrevealed \(Y_t\) as learner feedback.

The KL argument deliberately compares the richer latent experiment in which all \(Y_t\) values are available. Observable histories are randomized transformations of that experiment, so data processing can only reduce their divergence. This covers every adaptive audit or deferral strategy without assuming an audit floor.

The testing step conditions on \(S_t=s_i\) only after comparing the pre-score history laws. Because \(S_t\) is independent of those histories and has the same marginal under both paired instances, no division by the small cell probability occurs in the total-variation bound.

No concentration inequality is used. All guarantees and intermediate comparisons are fixed-horizon statements in expectation over arrivals, labels, and learner randomization.

## Boundary cases and counterexample attempts

For \(T=8\), \(M=2\), so all denominator and floor estimates remain valid. The inequality \(M+1\le(3/2)T^{1/3}\) holds with equality at this endpoint.

The comparator’s boundary randomization is always valid: \(r_\theta\in(0,1/4)\), hence \(\alpha_\theta\in(0,1)\). Its risk constraint is binding even at \(\bar\theta=\pm1\).

An always-release learner avoids all expert cost but makes the priced mistake on every positive hard cell. An always-reveal learner avoids released errors but makes the priced mistake on every negative hard cell and at the anchor. Hypercube pairing shows that adaptive mixtures cannot avoid both errors.

Free labels from comparator-optimal deferrals on positive cells do not break the construction. Lemma 3 grants the learner the strictly richer experiment containing every hard-cell label under both signs, including labels from released rounds, and the paired divergence is still below \(1/100\).

Auditing the anchor cannot reveal a bit cheaply enough to invalidate the test. A bit flip changes its mean only by \(2\delta/M\), and the KL calculation includes all \(T/4\) expected anchor observations.

Score-blind randomized revealing also does not expose the instance through its aggregate mean, which is exactly \(13/32\) throughout the family. Score-dependent revealing is covered by the pairwise latent-data bound.

Deliberate error slack is handled by the priced statement. At the exchange rate two, boundary release and reveal are exactly neutral, while each wrong hard-cell action has gap \(2\delta\). The corollary converts only the explicitly allowed \(c_0T^{2/3}\) slack.

## Self-audit

1. The most delicate step is Lemma 4’s conditioning on the current rare score. It is closed by comparing pre-score histories, using i.i.d. independence of \(S_t\), and then applying the common action kernel. Applying total variation directly to the event \(\{S_t=s_i,I_t=1\}\) would not suffice.

2. The comparator proof depends on the sign of the Lagrange argument. This is closed by writing the priced objective explicitly and using feasibility only after the pointwise-minimum inequality.

3. The information bound must cover labels obtained through both audit and deferral. It does more: it bounds divergence in the experiment exposing every latent label, after which data processing handles arbitrary learner behavior.

4. Floor effects are largest at \(M=2\). The KL constant and the \(T^{2/3}\) conversion were both checked at that endpoint.

5. The proof establishes the stronger primary constant \(1/512\); weakening it to \(1/2048\) leaves no hidden asymptotic condition.

## Open obligations

None.

## Review: 0003-review

VERDICT: pass

## Verdict rationale

The lower bound is mathematically sound and satisfies the binding setting-parity requirements. The construction is i.i.d., globally \(1\)-Lipschitz, uses the stipulated information protocol and complete cost accounting, and compares against the correct distribution-aware Borel-policy benchmark.

The proof correctly establishes a stronger \(T^{2/3}/512\) priced lower bound before weakening the constant. The two-sided corollary follows with the stated tied slack constant. No optimizer-local or proof-artifact assumption is introduced.

## Step-by-step audit

- **Setting and filtration — verified.** Actions are selected after observing \(S_t,\widehat Y_t\) but before \(Y_t\). Deferral and audit both reveal \(Y_t\), cost one, and produce zero released-label loss. Release costs zero and incurs \(Y_t\). All learner kernels are predictable.

- **Loss separation and cost accounting — verified.** Counterfactual loss \(L_t=Y_t\), released loss \(R_t=(1-I_t)Y_t\), and learner feedback remain distinct. Model and correction costs are explicitly zero; every expert call is counted through \(I_t\).

- **Lemma 1 — verified.** The support probabilities sum to one, all Bernoulli means lie in \([0,1]\), and the interpolation slopes are bounded by \(1\). The cancellation yielding \(\mathbb E_\theta Y=13/32\) is algebraically correct.

- **Lemma 2 — verified.** The proposed policy releases precisely the cells with \(m_\theta(s)<1/2\), reveals those with \(m_\theta(s)>1/2\), and randomizes on the neutral boundary atom. The calculation of \(r_\theta\), the validity of \(\alpha_\theta\), and binding risk are correct. Pointwise minimization of
  \[
  1-a+2am_\theta(s)
  \]
  plus feasibility proves benchmark optimality. Each hard-cell wrong action contributes exactly \(2\delta\); discarded anchor excess is nonnegative.

- **Lemma 3 — verified.** Paired instances differ only at hard cell \(i\) and the anchor. The Bernoulli KL bounds, support weighting, floor calculation, and numerical constant \(291/32768<1/100\) are correct. Comparing with the richer full-latent-label experiment is legitimate, and data processing covers every adaptive audit/deferral strategy. Pinsker is used within its conditions.

- **Lemma 4 — verified.** The proof compares pre-score histories, so conditioning on the rare current score does not amplify total variation. Independence and the common score marginal justify multiplication by \(1/(4M)\). The common learner kernel gives
  \[
  q_t^-+(1-q_t^+)\ge 3/4,
  \]
  yielding the claimed paired wrong-action count.

- **Lemma 5 — verified.** Hypercube pairing and the factor \(2^{M-1}/2^M\) are correct. Summing over coordinates produces \(3T/32\) expected wrong actions. Multiplication by \(2\delta\) and the conversion using \(M+1\le(3/2)T^{1/3}\) give \(T^{2/3}/512\).

- **Main priced lower bound — verified.** The maximum dominates the uniform average, and weakening \(1/512\) to \(1/2048\) is valid.

- **Two-sided conversion — verified.** On an instance attaining the priced maximum, the uniform error guarantee subtracts at most \(2c_0T^{2/3}=c_1T^{2/3}/2\), leaving the stated \(T^{2/3}/4096\) cost regret.

- **Admissibility and comparator parity — verified.** A1–A3 are problem-level and diagnostically interpretable. The comparator uses the same score information and action costs, is explicitly distribution-aware, and does not observe the current label. No paid component or source of randomness is omitted.

## Smallest failure

The weakest surviving step is Lemma 4’s rare-score conditioning. It nevertheless holds because total variation is applied to the history before \(S_t\) is drawn; \(S_t\) is then independent of that history and identically distributed under the paired instances. Thus the proof never conditions two joint laws on a \(1/(4M)\)-probability event, and no inverse-probability loss occurs.

## Required author action

None.

## Review: 0004-review

VERDICT: pass

## Verdict rationale

The theorem and both consequences are established as stated. The hard-instance family satisfies A1–A3 with common parameters, the comparator has information/action/cost parity and a binding risk constraint, and the three losses remain distinct. The full-latent-experiment KL argument validly covers every adaptive audit or deferral strategy.

All constants, floor effects, probability semantics, and hypercube factors check out. The literature comparisons are explicitly non-load-bearing analogies.

## Step-by-step audit

- **Lemma 1 — verified.** Support means lie in \([0,1]\). The interpolation slopes are bounded respectively by \(3/4+2\delta<1\), \(1/32\), and \(1/16\). The camouflage cancellation gives exactly \(13/32\).

- **Lemma 2 — verified.** The formula and bounds for \(r_\theta\) are correct, so \(\alpha_\theta\in(0,1)\) and the comparator risk equals \(1/4\). The priced objective
  \[
  1+a(2m_\theta(s)-1)
  \]
  is minimized by releasing below \(1/2\), revealing above \(1/2\), and arbitrary mixing at \(1/2\). The feasibility argument correctly converts this pointwise minimum into constrained cost optimality. The learner’s conditional priced loss is justified by predictability, and each wrong hard-cell action has excess exactly \(2\delta\).

- **Lemma 3 — verified.** The Bernoulli-KL inequality is applied with denominators uniformly bounded away from zero. Only cell \(i\) and the anchor change under a bit flip. Substitution of \(T<(M+1)^3\) and \(\delta=1/[64(M+1)]\) gives
  \[
  D_{\mathrm{KL}}<291/32768<1/100.
  \]
  Comparing with the richer experiment containing every latent label is legitimate because the actual adaptive interaction is its randomized measurable transformation. Pinsker then yields the stated TV bound.

- **Lemma 4 — verified.** The pre-score history laws have TV below \(1/4\). The action kernel after observing \(s_i\) is the same measurable function under both paired instances. Since the current score is independent of the history and has common mass \(1/(4M)\), no conditioning penalty is missing. The lower bound \(3T/(16M)\) follows.

- **Lemma 5 — verified.** Pair averaging contributes the necessary factor \(1/2\), summation over \(M\) coordinates gives \(3T/32\), and multiplication by \(2\delta\) gives \(3\delta T/16\). For \(T^{1/3}\ge2\), the conversion to \(T^{2/3}/512\) is correct.

- **Main priced bound — verified.** The maximum dominates the uniform average, and weakening \(1/512\) to \(1/2048\) is valid.

- **Cost corollary — verified.** With \(\eta=2\) and \(c_0=c_1/(2\eta)\), subtracting the permitted error slack leaves \(c_1T^{2/3}/2\), hence the constant \(1/4096\).

- **Admissibility and accounting — verified.** Actions are predictable; unrevealed labels are never treated as feedback; released loss, counterfactual loss, and learner estimates are separated. Every expert reveal is charged on the learner side, and the comparator uses identical action semantics and complete costs. The assumptions are global problem-level conditions, not optimizer-local artifacts.

- **Quantifiers and randomness — verified.** The family may depend on the fixed horizon, while \(\epsilon\), \(L\), and costs are common across instances. Expectations cover arrivals, labels, and learner randomization.

## Smallest failure

The weakest surviving step is Lemma 4’s conditioning on a rare current score. It nevertheless holds because TV is applied to the pre-score history laws, the score is then drawn independently with the same marginal under both instances, and the common action kernel is evaluated afterward. Thus no invalid conditional-TV division by \(1/(4M)\) occurs.

## Required author action

None.
