VERDICT: pass

## Verdict rationale

The proof is mathematically sound and satisfies the research contracts. Uniform prefix evaluation, safe-policy mixing, deployment concentration, and coupling to the realized comparator are all valid with the stated constants. The assumptions are problem-level and admissible; no optimizer-local condition is used.

Information and action parity hold, all model, expert, audit, and correction costs are counted symmetrically, and released loss, counterfactual loss, and learner feedback remain distinct. The probability space covers arrivals and both parties’ randomization. The fixed-horizon and asymptotic rates follow as claimed.

The cited literature is not used as proof evidence, so the theorem does not depend on any unverified external result.

## Step-by-step audit

- **Setting and cost definitions — verified.**  
  For \(E,C,A\), the formulas for released loss and cost match the stated execution semantics. In particular, \(A\) has zero released loss after correction but pays \(c_M+1+\kappa\ell_t\). Thus \(r_\pi\in[0,1]\) and \(c_\pi\in[0,G]\).

- **Assumptions and admissibility — verified.**  
  A1 is a global stationarity and action-independent potential-output assumption. A2 supplies bounded accounting and the safe expert. A3 is a finite preregistered policy-class assumption, not a condition localized around an optimizer. A4 is an explicit positive service-level restriction. Each has an operational interpretation and falsification route. The audit floor, prefix length, convexification, and tightening are correctly classified as algorithm choices.

- **Comparator — verified.**  
  The comparator knows \(P\), as explicitly disclosed, but its realized policies use only \(X_t\) and post-call \(O_t\). It has the same action space, correction semantics, and cost function. Its absence of learning audits is legitimate because the learner’s calibration audits remain in the regret term.

- **Filtration and predictability — verified.**  
  Before exposing the mixture seed, the routing kernel is history- and context-measurable. After exposing the seed, the realized gate is measurable before \(O_t,Y_t\), and the post-call action is measurable after \(O_t\) but before \(Y_t\). The conditional audit probability is correctly normalized when conditioning on reaching the model node.

- **Lemma 1 — verified.**  
  The proof is the standard Hoeffding-lemma argument for variables in \([0,b]\), producing the stated one- and two-sided constants. The conditional version applies to the suffix after conditioning on the prefix.

- **Lemma 2 — verified.**  
  For each base policy, the prefix observations are i.i.d. and bounded. With
  \[
  2e^{-2na_n^2}=\delta/(6N),
  \]
  union bounds give failure \(\delta/6\) for risk and \(\delta/6\) for cost. Linearity and nonnegative mixture weights extend the maximum base-policy deviation to every \(q\in\Delta(\Pi)\). Total failure is \(\delta/3\).

- **Lemma 3 — verified.**  
  Under \(a_n\le\epsilon/2\), \(\theta=2a_n/\epsilon\in[0,1]\). Mixing \(q^\star\) with the expert gives
  \[
  R(q^-)\le\epsilon-2a_n,
  \]
  so one empirical deviation makes \(q^-\) feasible at level \(\epsilon-a_n\). Empirical feasibility gives \(R(\widehat q)\le\epsilon\). Two cost deviations contribute \(2Ga_n\), while safe mixing contributes at most \(2Ga_n/\epsilon\), yielding exactly
  \[
  C(\widehat q)\le C(q^\star)+2Ga_n(1+\epsilon^{-1}).
  \]

- **Lemma 4 — verified.**  
  Conditional on the audited prefix, \(\widehat q\) is fixed and suffix pairs \((W_t,J_t)\) are i.i.d. Execution gives exactly
  \[
  \lambda_t=r_{J_t}(W_t),\qquad g_t=c_{J_t}(W_t).
  \]
  Hoeffding with deviations \(d_H\) and \(Gd_H\) gives failure \(\delta/6\) for each upper tail. The \(H=0\) convention is correct.

- **Lemma 5 — verified.**  
  Comparator pairs \((W_t,J_t^\star)\) are i.i.d. despite sharing \(W_t\) with APS-LP. Marginal Hoeffding bounds therefore give the stated loss upper tail and cost lower tail. No independence between learner and comparator totals is needed.

- **Main proof, event accounting — verified.**  
  The prefix event costs \(\delta/3\), and the four one-sided events cost \(4\delta/6\), totaling exactly \(\delta\).

- **Main proof, learner loss — verified.**  
  Calibration loss is zero. Deployment loss is at most
  \[
  HR(\widehat q)+d_H\le\epsilon H+d_H\le\epsilon T+d_H.
  \]

- **Main proof, comparator loss — verified.**  
  Feasibility of \(q^\star\) gives
  \[
  L_T^\star\le TR(q^\star)+d_T\le\epsilon T+d_T.
  \]

- **Main proof, cost comparison — verified.**  
  Prefix cost is at most \(nG\). Deployment concentration and Lemma 3 give
  \[
  C_T^{\mathrm{APS}}
  \le nG+HC(q^\star)+2GHa_n(1+\epsilon^{-1})+Gd_H.
  \]
  Nonnegative costs imply \(HC(q^\star)\le TC(q^\star)\), and the comparator lower-tail event implies
  \[
  TC(q^\star)\le C_T^\star+Gd_T.
  \]
  Substitution produces precisely the stated \(\Gamma_T\).

- **Fallback branch — verified.**  
  The learner releases only corrected or expert labels, hence has zero loss. Its cost is at most \(nG+H\le GT\), so the cost claim follows from \(C_T^\star\ge0\). Only comparator-loss concentration is needed for the joint theorem in this branch.

- **Rate specialization — verified.**  
  With \(n\asymp T^{2/3}\) and \(\delta_T=T^{-2}\), the terms are
  \[
  n=O(T^{2/3}),\quad Ha_n=O(T^{2/3}\sqrt{\log(NT)}),\quad
  d_H+d_T=O(\sqrt{T\log T}).
  \]
  These give the claimed cost rate and are \(o(T)\) for fixed \(N,G,\epsilon\). The more general condition \(\log(N/\delta_T)=o(T^{2/3})\) likewise makes \(a_n=o(1)\), \(Ha_n=o(T)\), and \(d_T,d_H=o(T)\).

## Smallest failure

The weakest surviving point is the randomized two-stage filtration. A careless formulation could make the realized action appear non-predictable because it depends on the fresh seed. Here it nevertheless holds: the pre-seed routing kernel is predictable, and after adjoining the independently sampled seed, the realized gate and audit decision are measurable before the relevant model output or expert label. This is sufficient for the execution semantics and for all conditional concentration arguments.

## Required author action

None.