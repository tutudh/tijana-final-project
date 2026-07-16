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