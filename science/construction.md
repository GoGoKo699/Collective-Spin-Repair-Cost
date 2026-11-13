# Matching probe preparation

[Model](model.md) · [Converse](converse.md) · [Physical resources](resources.md)

The upper bound permits arbitrary controls that preserve the total-spin Casimir. Its order can be reached by preparing a partially polarized mixed state and applying a supplied collective cat pulse. Mixed-state cat metrology is an inherited mechanism; the construction here fixes its role in the repair-budget problem, proves the needed finite-parameter bound, and keeps the pulse time and continuing noise explicit.

Throughout, $`S_a=\frac12\sum_{i=1}^N\sigma_i^a`$, $`C=\sum_a S_a^2`$, and the independent noise is

```math
\mathcal D_\kappa=\frac\kappa4\sum_{i=1}^N\sum_{a=x,y,z}\mathcal D[\sigma_i^a].
```

A single-qubit Bloch vector therefore decays at rate $`\kappa`$. The estimated phase is imprinted **after preparation** by $`e^{-i\theta S_z}`$. Preparation records carry no information about $`\theta`$. No noisy frequency-encoding interval is included in this task.

## 1. A counted local pump

Let $`b=B/\kappa`$ and first assume $`1\le b\le N`$. Choose

```math
m=\lfloor b\rfloor.
```

On $`m`$ selected spins apply the independent jumps

```math
L_i=\sqrt\kappa\,|0\rangle\langle1|_i,
\qquad 1\le i\le m.
```

Their charged repair budget is $`m\kappa\le B`$. The other spins receive no repair. Starting from $`I/2^N`$, pumping for a time $`s`$ produces exactly

```math
\rho_{p,m}=\tau_p^{\otimes m}\otimes(I/2)^{\otimes(N-m)},
\qquad
\tau_p=\frac{I+pZ}{2},
\qquad
p=p(s)=\frac{1-e^{-2\kappa s}}2.
```

Indeed, each addressed polarization obeys $`\dot p=\kappa-2\kappa p`$. The limiting polarization is $`1/2`$, but the proof below uses finite $`s`$: if $`s\ge\kappa^{-1}`$, then

```math
p\ge p_*:=\frac{1-e^{-2}}2>0.
```

The maximally mixed initialization supplies no initial spin polarization or high-spin moment. It is part of the constructive protocol, not a restriction on the arbitrary initial states allowed in the converse.

## 2. Exact mixed-state cat formula

Put $`P=X^{\otimes N}`$ and apply

```math
U_{\rm cat}=e^{-i\pi P/4}.
```

The operator $`P`$ is a global $`\pi`$ rotation up to a known phase, so $`[P,C]=0`$ and $`U_{\rm cat}`$ belongs to the free Casimir-preserving control class. This assertion does not make its many-body implementation inexpensive. Its finite-duration implementation is treated in Section 4.

Let $`\sigma_{p,m}=U_{\rm cat}\rho_{p,m}U_{\rm cat}^\dagger`$. Write $`K`$ for the sum of $`m`$ independent signs of mean $`p`$, and set $`a=\mathrm{atanh}p`$. Then

**Equation (1).**

```math
F_{p,m}:=F_Q(\sigma_{p,m},S_z)
=\mathbb E\!\left[(K^2+N-m)\tanh^2(aK)\right].
```

Here $`F_Q(\rho,G)`$ denotes the quantum Fisher information of $`e^{-i\theta G}\rho e^{i\theta G}`$.

To verify (1), label a computational-basis string by signs $`s_i\in\lbrace \pm1\rbrace `$. Its input eigenvalue and magnetization are

```math
\lambda_s=2^{-N}\prod_{i\le m}(1+ps_i),
\qquad
g_s=\frac12\sum_{i=1}^Ns_i.
```

Let $`\bar s=-s`$. Since $`PG=-GP`$ for $`G=S_z`$,

```math
U_{\rm cat}^\dagger G U_{\rm cat}=iPG.
```

This operator couples only $`s`$ and $`\bar s`$, with squared matrix element $`g_s^2`$. Moreover,

```math
\frac{\lambda_s-\lambda_{\bar s}}
     {\lambda_s+\lambda_{\bar s}}
=\tanh\!\left(a\sum_{i\le m}s_i\right).
```

Substituting these expressions into

```math
F_Q(\rho,G)
=2\sum_{r,t:\lambda_r+\lambda_t>0}
\frac{(\lambda_r-\lambda_t)^2}{\lambda_r+\lambda_t}
|G_{rt}|^2
```

gives $`F_{p,m}=4\mathbb E[g_s^2\tanh^2(aK)]`$. The unpumped signs have conditional mean zero and total variance $`N-m`$, which proves (1). The argument covers both parities of $`N`$ and does not assume a pure probe.

## 3. A uniform lower bound

For $`0\lt p\le1/2`$ and $`m\ge1`$,

**Equation (2).**

```math
p^4(N+m^2)\le F_{p,m}
\le N+p^2m(m-1).
```

For the upper bound, use $`\tanh^2\le1`$ and

```math
\mathbb E K^2=m+p^2m(m-1).
```

For the lower bound, $`K`$ is an integer, so $`\tanh^2(aK)\ge p^2`$ whenever $`K\ne0`$. Also $`\Pr(K\ne0)\ge1/2`$: it is one for odd $`m`$, while for $`m=2r`$,

```math
\Pr(K=0)=\binom{2r}{r}
\left(\frac{1-p^2}{4}\right)^r
\le\binom{2r}{r}4^{-r}\le\frac12.
```

Consequently,

```math
\begin{aligned}
F_{p,m}
&\ge p^2\left[m+p^2m(m-1)+\frac{N-m}{2}\right]\\
&=p^4m^2+\frac{p^2N}{2}
  +p^2\left(\frac12-p^2\right)m\\
&\ge p^4(N+m^2).
\end{aligned}
```

At the limiting pump polarization $`p=1/2`$, the first inequality is $`(N+m^2)/16`$. At finite $`s\ge\kappa^{-1}`$ it remains valid with the fixed constant $`p_*^4`$. Since $`\lfloor b\rfloor\ge b/2`$ for $`b\ge1`$,

**Equation (3).**

```math
F_{p,m}\ge\frac{p_*^4}{4}(N+b^2),
\qquad 1\le b\le N.
```

Together with the converse and the universal bound $`F_Q\le N^2`$, this establishes the order of the intermediate repair frontier. If $`B\ge\kappa N`$, one can keep $`m=N`$ and obtain a constant fraction of $`N^2`$ with the same construction.

For example, with one pumped spin the formula is exactly $`F_{p,1}=p^2N`$. With $`m`$ growing at fixed $`p`$, the quadratic contribution is of order $`m^2`$, rather than the number of fully polarized spins being $`N`$.

## 4. A finite collective pulse under continuing noise

An instantaneous cat pulse is a convenient supplied-control limit. The same scaling is attainable with a finite pulse whose sufficient strength can be stated explicitly.

Turn the local pumps off during the pulse and use

```math
H_{\rm pulse}=\Omega P,
\qquad
\tau=\frac\pi{4\Omega}.
```

The phase-independent depolarization continues. If $`\rho_{\rm out}`$ is the actual output and $`\sigma_{p,m}`$ the ideal cat output from the same input, a channel hybrid/Duhamel bound gives

**Equation (4).**

```math
\delta:=\frac12\Vert \rho_{\rm out}-\sigma_{p,m}\Vert _1
\le\kappa N\tau.
```

For this estimate, write the noise as $`\kappa\sum_i(\mathcal T_i-\mathrm{id})`$, with $`\mathcal T_i`$ replacing spin $`i`$ by $`I/2`$. Each summand has diamond norm at most $`2\kappa`$. Unitary interaction pictures and the remaining channels are norm contractions. Equation (4) is a sufficient error estimate, not an optimal pulse-noise law.

The following fixed-measurement argument avoids assuming uniform continuity of QFI near small eigenvalues. Let $`L`$ be the ideal probe's symmetric logarithmic derivative for $`S_z`$. In the input eigenbasis it has only complementary-string blocks, with off-diagonal magnitude

```math
2|g_s|\,|\tanh(aK)|\le N.
```

Thus $`\Vert L\Vert \le N`$, $`\mathrm{Tr}(\sigma_{p,m}L^2)=F_{p,m}`$, and the derivative of its mean at $`\theta=0`$ is $`F_{p,m}`$. Since $`\Vert S_z\Vert =N/2`$, trace-distance duality gives for the actual probe

```math
\left|\left.\partial_\theta\langle L\rangle\right|_0-F_{p,m}\right|
\le2\delta N^2,
\qquad
\mathrm{Var}_{\rho_{\rm out}}L
\le F_{p,m}+2\delta N^2.
```

The classical Fisher information of the fixed projective measurement of $`L`$ is at least the squared derivative of its mean divided by its variance. Hence

**Equation (5).**

```math
F_Q(\rho_{\rm out},S_z)
\ge\frac{(F_{p,m}-2\delta N^2)_+^2}
           {F_{p,m}+2\delta N^2}.
```

In particular, $`\delta\le F_{p,m}/(8N^2)`$ implies

**Equation (6).**

```math
F_Q(\rho_{\rm out},S_z)\ge\frac9{20}F_{p,m}.
```

It therefore suffices to choose

**Equation (7).**

```math
\tau\le\frac{p_*^4(N+m^2)}{8\kappa N^3},
\qquad
\Omega\ge\frac{2\pi\kappa N^3}{p_*^4(N+m^2)}.
```

This is a conservative polynomial strength bound. It is not claimed optimal or affordable on a specified platform. The pulse is an $`N`$-body Casimir-preserving Hamiltonian; its operator norm is $`\Omega`$. A synthesis using a different collective interaction has its own strength, duration and gate costs.

For a prescribed output time $`T\ge\kappa^{-1}\log(N+2)`$, pump for $`s=T-\tau`$ and use the final interval for this pulse. Since $`m\le N`$ and $`p_*\lt 1/2`$, (7) gives $`\tau\le1/(64\kappa)`$, whereas $`\log(N+2)\ge\log3>1+1/64`$. Therefore $`s\ge\kappa^{-1}`$ for all $`N\ge1`$. Thus (3) and (6) apply at the same deterministic output time as the late-time converse. This is an actual finite-duration preparation, with noise present throughout.

## 5. The SQL baseline with no charged repair

This optional construction uses the full free-control class and explains the $`N`$ floor at arbitrarily small $`B`$. It does not assert an efficient laboratory implementation.

Decompose the spin Hilbert space into irreducible spin and multiplicity spaces,

```math
\mathcal H=\bigoplus_j(\mathcal V_j\otimes\mathcal M_j).
```

For $`j>0`$ define $`|\chi_j\rangle=(|j,j\rangle+|j,-j\rangle)/\sqrt2`$, and take $`|\chi_0\rangle=|0,0\rangle`$. The channel $`\Pi`$ discards coherences between different $`j`$, resets $`\mathcal V_j`$ to $`|\chi_j\rangle`$, and retains its multiplicity state. It is idempotent and has Kraus operators

```math
K_{j,m}=|\chi_j\rangle\langle j,m|\otimes I_{\mathcal M_j},
\qquad -j\le m\le j,
```

extended by zero outside their $`j`$ block. Every Kraus operator commutes with $`C`$, and $`\sum_{j,m}K_{j,m}^\dagger K_{j,m}=I`$. Therefore

```math
\Gamma(\Pi-\mathrm{id})=\sum_{j,m}\mathcal D[\sqrt\Gamma K_{j,m}]
```

is an allowed free generator. It is even permutation invariant, because it acts as the identity on multiplicity spaces.

Run $`\Gamma(\Pi-\mathrm{id})+\mathcal D_\kappa`$ from $`I/2^N`$. The exact Casimir identity gives $`\mathrm{Tr}(\rho(t)C)=3N/4`$ at every time. Set $`\sigma(t)=\Pi\rho(t)`$. Its phase-QFI is

```math
F_Q(\sigma(t),S_z)=4\sum_j q_j(t)j^2
\ge\frac43\sum_jq_j(t)j(j+1)=N,
```

using $`j^2\ge j(j+1)/3`$ for every permitted $`j>0`$. The state in each spin block is a cat, while the untouched multiplicity state does not carry the signal.

Let $`R=\mathrm{id}-\Pi`$. Since $`\Pi^2=\Pi`$,

```math
\frac{d}{dt}R\rho=-\Gamma R\rho+R\mathcal D_\kappa\rho.
```

For Hermitian inputs, $`\Pi`$ contracts trace norm and $`\Vert \mathcal D_\kappa\rho\Vert _1\le2\kappa N`$. Variation of constants therefore yields

```math
\frac12\Vert \rho(t)-\sigma(t)\Vert _1
\le e^{-\Gamma t}+\frac{2\kappa N}{\Gamma}.
```

The ideal block-cat SLD also has norm at most $`N`$, so (5) applies. For example, $`\Gamma=64\kappa N^2`$ and $`t\ge\kappa^{-1}`$ make the last display at most $`1/(8N)`$, and give

```math
F_Q(\rho(t),S_z)\ge\frac9{20}N.
```

These global spin-sector resets spend no charged symmetry-breaking repair. Their highly structured jumps and large supplied rate are the price within the free-control model. They close the baseline in that model; they do not provide a local reservoir implementation.

Combining this baseline for $`0\le b\lt 1`$, the pumped construction for $`1\le b\le N`$, and $`m=N`$ for $`b>N`$, gives a single uniform constructive consequence: at every prescribed $`T\ge\kappa^{-1}\log(N+2)`$ there is an allowed preparation from $`I/2^N`$ satisfying

**Equation (8).**

```math
F_Q(\rho(T),S_z)
\ge c\min\lbrace N^2,N+b^2\rbrace ,
\qquad c=\frac{9p_*^4}{80}>0.
```

The constant is conservative and independent of $`N`$, $`B`$, $`\kappa`$ and $`T`$. At small $`B`$ it uses the supplied global reset controls; it is not a claim that local pumping alone attains an order-$`N`$ floor as its rate tends to zero.

## 6. Attribution and limits

Mixed-state metrological amplification and one-clean-spin protocols precede this work; see Modi et al., *Quantum Correlations in Mixed-State Metrology*, [PRX 1, 021022 (2011)](https://doi.org/10.1103/PhysRevX.1.021022), and the related-work comparison. The cat pulse and the possibility of useful mixed probes are not claimed as new. What the construction supplies here is a matching protocol under the specified repair cap, including a finite-time lower bound and sufficient finite-pulse resources.

The lower bound is a state-preparation result. Its QFI is evaluated for a later ideal phase imprint. No claim is made about an optimal readout implementation, a whole noisy sensing trajectory, a stationary Heisenberg-order state, a finite-bandwidth laboratory optimum, or a total-runtime quantum advantage.
