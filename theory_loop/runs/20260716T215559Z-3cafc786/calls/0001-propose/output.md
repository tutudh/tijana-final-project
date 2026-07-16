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