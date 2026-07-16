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