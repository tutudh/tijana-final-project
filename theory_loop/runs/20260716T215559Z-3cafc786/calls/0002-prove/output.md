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