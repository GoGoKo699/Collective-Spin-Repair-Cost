# Converse: total-spin loss and local repair

This page proves the finite-time converse in [the model](model.md). The proof uses an exact second-moment balance. It does not estimate a Liouvillian gap or assume that a control scheme approaches a unique stationary state.

Throughout, $S_a$ and $C=\sum_a S_a^2$ act on the physical sensors and are tensored with the identity on every protected register. Write

$$
x(t)=\operatorname{Tr}[C\rho_{SA}(t)].
$$

## 1. Exact action of independent depolarization

For a Pauli operator on one sensor,

$$
\frac{\kappa}{4}\sum_{a=x,y,z}
\left(\sigma_i^a\sigma_i^b\sigma_i^a-\sigma_i^b\right)
=-\kappa\sigma_i^b.
\tag{1}
$$

A Pauli product supported on two distinct sensors therefore decays at rate $2\kappa$ under the adjoint noise generator. Expanding the Casimir gives

$$
C=\frac{3N}{4}I
+\frac14\sum_{i\ne j}\sum_{a=x,y,z}
\sigma_i^a\sigma_j^a.
\tag{2}
$$

The identity part is fixed, so

$$
\boxed{
\mathcal N_\kappa^\dagger(C)
=-2\kappa\left(C-\frac{3N}{4}I\right).
}
\tag{3}
$$

This is an operator identity on the full sensor Hilbert space. No permutation symmetry of the state is required.

If $[H_0,C]=0$ and $[J,C]=0$, then

$$
i[H_0,C]=0,\qquad
\mathcal D[J]^\dagger(C)
=J^\dagger C J-\frac12\lbrace J^\dagger J,C\rbrace =0.
\tag{4}
$$

The second equality uses the individual jump commutation condition, which also implies $[J^\dagger,C]=0$. Consequently the free control generator contributes exactly zero to the Casimir drift.

Without repair, (3)–(4) give

$$
\dot x=-2\kappa\left(x-\frac{3N}{4}\right),
$$

and hence

$$
x(t)=\frac{3N}{4}
+\left(x(0)-\frac{3N}{4}\right)e^{-2\kappa t}.
\tag{5}
$$

For a trace-preserving instantaneous free channel with Kraus operators $K_j$ commuting with $C$,

$$
\sum_j K_j^\dagger C K_j
=C\sum_jK_j^\dagger K_j=C.
\tag{6}
$$

Thus (5), and the comparison bounds below, continue across finite inserted free channels.

## 2. The effect of one bounded-support term

Let $X$ contain $q$ physical sensors, and split

$$
S_a=S_{X,a}+S_{X^c,a},
\qquad
S_{X,a}=\frac12\sum_{i\in X}\sigma_i^a.
$$

A term $O_X$ supported on $X$ and an arbitrary protected ancilla commutes with $S_{X^c,a}$. Since $\|S_{X,a}\|=q/2$,

$$
\|[S_a,O_X]\|
=\|[S_{X,a},O_X]\|
\le q\|O_X\|.
\tag{7}
$$

The ancilla dimension does not change this estimate.

For a Hamiltonian term, the derivation rule gives

$$
i[h_X,S_a^2]
=\lbrace S_a,i[h_X,S_a]\rbrace ,
\qquad
\|i[h_X,S_a]\|\le q\|h_X\|.
\tag{8}
$$

For a jump $L_X$, its adjoint dissipator obeys

$$
\mathcal D[L_X]^\dagger(S_a)
=\frac12\left(
L_X^\dagger[S_a,L_X]
+[L_X^\dagger,S_a]L_X
\right).
\tag{9}
$$

Equations (7)–(9) imply

$$
\|\mathcal D[L_X]^\dagger(S_a)\|
\le q\|L_X\|^2.
\tag{10}
$$

The dissipative product identity is

$$
\begin{aligned}
\mathcal D[L_X]^\dagger(S_a^2)
={}&\lbrace S_a,\mathcal D[L_X]^\dagger(S_a)\rbrace \\
&+[S_a,L_X]^\dagger[S_a,L_X].
\end{aligned}
\tag{11}
$$

It follows by expanding both sides; the last term is positive. In particular,

$$
0\le [S_a,L_X]^\dagger[S_a,L_X]
\le q^2\|L_X\|^2 I.
\tag{12}
$$

These estimates apply to the actual Hamiltonian and jump decomposition in the budget. They do not require an interpretation of individual jumps as observed events.

## 3. The repair drift inequality

At a fixed time, let $\mathcal R$ be the sum of all charged terms, and set

$$
A_a=\mathcal R^\dagger(S_a).
$$

Each $A_a$ is Hermitian. From the budget definition and (8), (10),

$$
\|A_a\|
\le
\sum_X q\|h_X\|
+\sum_{X,\mu}q\|L_{X\mu}\|^2
=b(t).
\tag{13}
$$

Summing (8) and (11) over all terms gives

$$
\mathcal R^\dagger(C)
=\sum_a\lbrace S_a,A_a\rbrace 
+\sum_{X,\mu,a}
[S_a,L_{X\mu}]^\dagger[S_a,L_{X\mu}].
\tag{14}
$$

For every density operator, the weighted operator Cauchy–Schwarz inequality gives

$$
\begin{aligned}
\left|\operatorname{Tr}(\rho S_a A_a)\right|
&\le
\sqrt{\operatorname{Tr}(\rho S_a^2)}
\sqrt{\operatorname{Tr}(\rho A_a^2)}\\
&\le b(t)\sqrt{\langle S_a^2\rangle}.
\end{aligned}
\tag{15}
$$

Therefore

$$
\begin{aligned}
\sum_a\langle\lbrace S_a,A_a\rbrace \rangle
&\le 2b(t)\sum_a\sqrt{\langle S_a^2\rangle}\\
&\le 2\sqrt3\,b(t)\sqrt{x}.
\end{aligned}
\tag{16}
$$

Using $q\le k$ in the positive remainder of (14),

$$
\begin{aligned}
\sum_{X,\mu,a}
\left\langle
[S_a,L_{X\mu}]^\dagger[S_a,L_{X\mu}]
\right\rangle
&\le3\sum_{X,\mu}q^2\|L_{X\mu}\|^2\\
&\le3k\,b(t).
\end{aligned}
\tag{17}
$$

Combining (3), (4), (14)–(17) and $b(t)\le B$ proves

$$
\boxed{
\dot x
\le
-2\kappa\left(x-\frac{3N}{4}\right)
+2\sqrt3\,B\sqrt{x}+3kB.
}
\tag{18}
$$

The estimate includes coherent local control, dissipative repair, protected ancillary systems and arbitrarily strong free sector-preserving dynamics. It does not assume independent repair operations or a product state.

The square-root dependence in the repair term is consequential. Replacing it by a rough operator-norm estimate proportional to $NB$ would lose the intermediate $B^2$ frontier.

## 4. Integrating the bound

Young's inequality gives

$$
2\sqrt3\,B\sqrt{x}
\le \kappa x+\frac{3B^2}{\kappa}.
\tag{19}
$$

Thus

$$
\dot x
\le
-\kappa x+\frac{3\kappa N}{2}
+\frac{3B^2}{\kappa}+3kB.
\tag{20}
$$

Multiplying by $e^{\kappa t}$ and integrating yields

$$
\boxed{
x(T)\le
e^{-\kappa T}x_0
+(1-e^{-\kappa T})
\left[
\frac{3N}{2}
+3\left(\frac B\kappa\right)^2
+3k\frac B\kappa
\right].
}
\tag{21}
$$

At every finite insertion satisfying (6), $x$ is unchanged, so the same integrating-factor comparison holds over the full prescribed interval.

For any stationary joint state, (20) with $\dot x=0$ implies the bracketed upper bound in (21). If $B=0$, the exact identity (3) improves that stationary moment to $x=3N/4$. Neither conclusion requires uniqueness or an attraction rate.

## 5. Converting the moment into phase sensitivity

For a finite-dimensional density operator $\rho=\sum_r\lambda_r|r\rangle\langle r|$ and a Hermitian generator $G$, our QFI convention is

$$
F_Q(\rho,G)
=
2\sum_{\lambda_r+\lambda_s>0}
\frac{(\lambda_r-\lambda_s)^2}{\lambda_r+\lambda_s}
|\langle r|G|s\rangle|^2.
\tag{22}
$$

The inequality $(\lambda_r-\lambda_s)^2\le(\lambda_r+\lambda_s)^2$, applied after replacing $G$ by $G-\langle G\rangle I$, gives the standard bound

$$
F_Q(\rho,G)\le4\operatorname{Var}_\rho(G).
\tag{23}
$$

For $G=\mathbf n\cdot\mathbf S\otimes I_A$ with $\|\mathbf n\|_2=1$, a collective rotation of coordinates gives

$$
G^2\le C\otimes I_A.
$$

Hence

$$
F_Q(\rho_{SA},G)\le4\langle C\rangle=4x.
\tag{24}
$$

The spectrum of $G$ lies in $[-N/2,N/2]$, also on the joint sensor–ancilla space. Its variance is at most $N^2/4$, giving the independent cap

$$
F_Q(\rho_{SA},G)\le N^2.
\tag{25}
$$

Substituting (21) in (24) and taking the minimum with (25) proves Theorem 1, equation (9) of the [model](model.md).

The Casimir spectrum is $j(j+1)$, $j\le N/2$, so $4x_0\le N(N+2)$. If $T\ge\log(N+2)/\kappa$, then

$$
4e^{-\kappa T}x_0\le N.
\tag{26}
$$

Using $1-e^{-\kappa T}\le1$ proves the uniform finite-time bound

$$
F_Q\le
\min\left\lbrace 
N^2,\;
7N+12(B/\kappa)^2+12kB/\kappa
\right\rbrace .
\tag{27}
$$

Write $b=B/\kappa$. For every $b\ge0$ and $N\ge1$, the inequality $b\le(N+b^2)/2$ gives

$$
7N+12b^2+12kb
\le (12+6k)(N+b^2).
$$

This proves the upper order for the full $B\ge0$ frontier at fixed $k$. The [construction](construction.md) supplies the lower order, with the collective-operation resource qualification made explicit. The intermediate regime $1\le b\le N$ uses counted local pumps and a terminal collective pulse; the linear baseline at $b\lt 1$ uses supplied global sector-reset jumps.

## 6. Finite record feedback and heralding

We now consider the stated finite-record extension. Between finitely many prescribed intervention times, each branch evolves as in (2)–(6), with $b_r(t)\le B$ on every branch. At an intervention, a finite-outcome instrument has Kraus operators commuting with $C$; later controls may depend on the accumulated record. The record is generated before the phase is introduced.

Write the normalized state on branch $r$ as $\rho_r(t)$, its probability as $p_r$, and

$$
x_r(t)=\operatorname{Tr}[C\rho_r(t)],\qquad
\bar x(t)=\sum_rp_r x_r(t).
$$

Between interventions, branchwise (18) gives

$$
\begin{aligned}
\dot{\bar x}
&\le-2\kappa\left(\bar x-\frac{3N}{4}\right)
+2\sqrt3\sum_rp_r b_r(t)\sqrt{x_r}
+3k\sum_rp_r b_r(t)\\
&\le-2\kappa\left(\bar x-\frac{3N}{4}\right)
+2\sqrt3 B\sqrt{\bar x}+3kB.
\end{aligned}
\tag{28}
$$

The last inequality uses the hard branchwise cap and the concavity of the square root.

At a free intervention, summing over all outcomes preserves $\bar x$ by (6). Thus (21) applies to the full average moment, through every intervention. This proof covers arbitrarily large finite outcome sets and any finite number of such interventions; it does not silently admit a cost-free local measurement or local reset that changes $C$.

The final retained-record state is

$$
\omega_{RSA}=\sum_rp_r|r\rangle\langle r|_R\otimes\rho_r.
$$

Because the phase acts only afterward, the probabilities $p_r$ are independent of $\theta$. The block-diagonal QFI formula gives

$$
F_Q(\omega_{RSA},I_R\otimes G)
=\sum_rp_rF_Q(\rho_r,G)
\le4\bar x.
\tag{29}
$$

Every summand also satisfies (25), so the full minimum bound of Theorem 1 applies. Tracing out the record or any protected subsystem is parameter-independent processing and cannot increase QFI.

For an accepted set $E$ with $p_{\mathrm{acc}}=\sum_{r\in E}p_r>0$, retain the accepted record if desired. Then

$$
\begin{aligned}
p_{\mathrm{acc}}F_Q(\omega_{\mathrm{acc}},I_R\otimes G)
&=\sum_{r\in E}p_rF_Q(\rho_r,G)\\
&\le\sum_rp_rF_Q(\rho_r,G).
\end{aligned}
\tag{30}
$$

Equations (21), (25) and (29) prove the heralding-yield statement (17) of the model. A high conditional QFI on a rare branch is therefore consistent with the converse.

The same proof allows an initial finite classical mixture with known record: $x_0$ is its average initial Casimir moment. An unrecorded mixture only has smaller QFI than its recorded version.

## 7. Why a deterministic output time matters

The proof averages over all preparation outcomes at one prescribed time. It does not bound a sensor sampled only when its record first enters a favorable set.

A concrete scope check illustrates the issue. Consider preparation with $B=0$ and free measurements of the total-spin sector every fixed interval $\Delta>0$. For one interval of independent depolarization, write $\eta=e^{-\kappa\Delta}$. The tensor-product noise channel contains the complete replacement channel $\rho_S\mapsto I_S/2^N$ with probability $(1-\eta)^N$. Therefore the conditional probability of observing the maximal-spin sector at the next measurement is at least

$$
q_N=(1-\eta)^N\frac{N+1}{2^N}>0,
\tag{31}
$$

irrespective of the previous sensor state. The sector projector has rank $N+1$. Repeating indefinitely eventually gives this outcome with probability one; the expected number of attempts is at most $1/q_N$. At that random success time, an ideal free reset within the measured maximal-spin sector can prepare a GHZ state, since the entire sector has the same Casimir eigenvalue.

This produces $N^2$ terminal QFI in a random-time task while paying a possibly very large waiting time. It does not contradict the deterministic-time bound. The accepted fraction at any fixed attempt is still subject to (30). The example explains why waiting for success cannot be treated as an uncharged replacement for the prescribed-time output.

## 8. Consequences and proof boundary

If the initial contribution has decayed as in (26), attaining $F_Q\ge cN^2$ for a fixed $c>0$ implies, from (27),

$$
12(B/\kappa)^2+12kB/\kappa
\ge cN^2-7N.
\tag{32}
$$

For fixed $k$ and sufficiently large $N$, this requires $B=\Omega_c(\kappa N)$. The conclusion is independent of how strongly the free sector-preserving generator is driven.

Define the incident charged load at sensor $i$ by

$$
g_i(t)=
\sum_{X\ni i}
\left(
\|h_{X,t}\|+\sum_\mu\|L_{X\mu,t}\|^2
\right).
$$

Then $\sum_i g_i(t)=b(t)$. If charged controls touch only $r$ sensors and every such sensor has load at most $\Gamma$, their total cap is $B\le r\Gamma$. Equation (32) gives the addressed-strength requirement $r\Gamma=\Omega(\kappa N)$.

The proof is specific to the stated independent isotropic noise and homogeneous signal. The free class preserves the *sensor* Casimir; preserving the total spin of sensors plus a controller is a different condition. The lower construction establishes a probe at its endpoint, and does not establish a stationary quadratic-QFI attaining state. The scientific attribution and the comparison with existing local-noise, symmetry and mixed-probe results are kept in [related work](../references/RELATED_WORK.md).

