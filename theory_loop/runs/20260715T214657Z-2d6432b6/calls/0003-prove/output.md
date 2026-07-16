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