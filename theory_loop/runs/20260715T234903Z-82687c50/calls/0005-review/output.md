VERDICT: revise

## Verdict rationale

The theorem appears mathematically plausible, and the comparator, cost accounting, assumptions, rates, and downstream optimization arguments are largely sound. However, the two importance-weighting arguments are not valid as written.

The claimed analytical sequence \(\mathcal G_{t,-}\) is not a filtration: it reveals the current latent \(Y_t\), but on an unaudited round that label is absent from \(\mathcal F_t\) and hence can disappear from \(\mathcal G_{t+1,-}\). Therefore the exponential process invoked in Lemma 2 is not shown to be adapted, so Lemma 1 and Ville’s inequality cannot be applied. Lemma 6 has the same defect.

This gap is decisive because Lemma 2 supports the released-error guarantee, while Lemma 6 supports comparator feasibility and the cost guarantee. It appears repairable by supplying a genuinely nested proof-only filtration and redoing the martingale arguments, so the appropriate verdict is `revise`, not `reject`.

## Step-by-step audit

- Setting and information timeline — **verified**. The routing vector is chosen from past information, and the realized routing and audit probabilities depend only on the past and current model output, not on \(Y_t\) or \(L_t\).

- Observation probability — **verified**:
  \[
  1-x+xq_t(x)=\max\{1-x,\gamma_t\}.
  \]
  The audit probability lies in \([0,1]\), and the expected audit incidence is at most \(\gamma_t\).

- Separation of losses — **verified**. Counterfactual loss \(L_t\), released loss \(R_t\), and feedback \(O_tL_t/p_t\) are not conflated.

- Assumptions A1–A3 — **verified as admissible**. They are global problem-level assumptions, not optimizer-local conditions. The Lipschitz condition is stated on the data distribution and is not a margin at an optimal threshold.

- Comparator — **verified**. It observes the same current score information, does not see \(Y_t\) before acting, and knows \(P\) explicitly. Auditing is indeed weakly dominated by deferral under the stated cost semantics.

- Complete cost accounting — **verified**. Both parties pay the model-call cost; learner deferrals, audits, and audited-error corrections are charged. Comparator audits are not silently removed from the action space; they are shown to be dominated.

- Lemma 1 — **verified**. The one-sided exponential bound and the stated Bernstein consequence follow with the given, slightly conservative, linear term.

- Lemma 2 — **gap**. The conditional calculation for one round is correct, but \(\mathcal G_{t,-}\) is not nested across \(t\). Consequently, the proof has not constructed a martingale or adapted exponential supermartingale to which Ville’s inequality applies. The random-variance grid calculations are otherwise consistent.

- Lemma 3 — **gap by dependency**. The i.i.d. Hoeffding component and the algebra \(E_{n,j}-H_{t,j}=M_{n,j}\) are correct. Simultaneous calibration validity nevertheless depends on the unproved Lemma 2.

- Lemma 4 — **verified conditional on Lemma 3**. The predictable masking argument avoids conditioning Azuma on a future confidence event. The conditional-risk computation and range-one concentration are correct.

- Lemma 5 — **verified**. Thresholding the scalar \(m(S)\), with randomization at an atom, attains the comparator optimum. The binning argument loses at most \(L/K\) in risk while preserving deferral cost.

- Lemma 6 — **gap**. Its first importance-weighted sum suffers from the same non-nested-filtration problem as Lemma 2. The fixed-\(n\) variance and increment bounds, the i.i.d. Hoeffding bound for the second sum, and the subsequent union bound are correct if a valid martingale filtration is supplied.

- Lemma 7 — **verified conditional on Lemma 6**. The Cauchy–Schwarz bound on \(\sum_jr_{t,j}\), the comparison with \(w_t/2\), feasibility scaling, and the \(1/\epsilon\) cost penalty are correct.

- Lemma 8 — **verified conditional on Lemmas 6–7**. Both empirical-frequency and importance-weighted comparator events are now included. FTRL optimality, the two empirical-to-population conversions, and the regularization penalty \(K/(2n)\) are correct.

- Lemma 9 — **verified**. The full random round cost is bounded and its conditional mean includes deferrals, audits, and corrections. The Azuma–Hoeffding constant is valid for range length \(1+c_R\).

- Lemma 10 — **verified**. Comparator expected cost and high-probability released-error semantics are derived under the explicitly stated fresh independent randomization.

- Main probability union — **verified arithmetically**, conditional on the disputed events being proved. With \(e^{-z}=\delta/(32KT)\), the displayed total is below \(\delta\).

- Main released-error conclusion — **gap by dependency**. It relies on Lemmas 2–3.

- Main cost conclusion — **gap by dependency**. It relies on Lemma 6 through robust comparator feasibility.

- Rate calculation — **verified**. The sums involving \(\gamma_t\), \(w_t\), frequency estimation, and discretization have the asserted \(T^{3/4}\) order. The universal constant \(C_0=27\) is consistent with the displayed coarse bounds.

- External citations — **not load-bearing**. The proof supplies its own concentration lemma and otherwise invokes standard Hoeffding–Azuma bounds; the literature comparisons are not used to close a mathematical step.

## Smallest failure

The smallest broken step is the sentence in Lemma 2:

> “Lemma 1 and Ville’s inequality show that …”

The conditioning fields used there are not a filtration. Specifically,
\[
\mathcal G_{s,-}=\sigma(\mathcal F_{s-1},S_s,\widehat Y_s,Y_s)
\]
contains \(Y_s\). If \(O_s=0\), then \(Y_s\) is not observed and is not included in \(\mathcal F_s\). Thus
\[
\mathcal G_{s,-}\not\subseteq\mathcal G_{s+1,-}
\]
in general.

For a concrete measurability failure, suppose an unaudited cheap release occurs and \(L_s\) remains random conditional on the observable history. Then
\[
X_{s,j}
=\mathbf1\{S_s\in B_j\}L_s
\]
on that event. This variable depends on the discarded latent \(Y_s\), so the accumulated exponential process after round \(s\) need not be measurable with respect to the purported conditioning field at round \(s+1\). It therefore has not been shown to be an adapted supermartingale, and Ville’s inequality is unavailable.

A valid one-round identity
\[
\mathbb E[X_{s,j}\mid\mathcal G_{s,-}]=0
\]
does not by itself establish a martingale when the conditioning fields are non-nested.

## Required author action

1. Define a genuinely nested proof-only filtration that retains all past latent arrivals, including \(Y_s\) and \(L_s\) from unaudited rounds, while preserving the algorithm’s stated observable filtration.

2. Reprove Lemma 2 relative to that filtration, including adaptation of the exponential process and predictability of the variance upper bound used by Ville’s inequality.

3. Reprove the first martingale term in Lemma 6 under the same nested construction.

4. Propagate the corrected event statements and failure probabilities through Lemmas 3, 7, 8, and the main proof. No new problem assumption should be introduced to close this proof-level gap.