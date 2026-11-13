# From an open-system master equation to a repair frontier

[Learning route](README.md) · [30-milestone map](MILESTONES.md) · [Scientific guide](../science/README.md)

Consider an ensemble of spins being prepared for a later phase measurement. A collective device can rotate, entangle or dissipatively reshape them. Independent noise also acts on each spin. The central distinction is between reshaping the ensemble inside its total-spin sectors and replenishing the sector resource that local noise removes. This bridge develops that distinction from the language of the selected textbook.

The sole educational anchor is **[Breuer–Petruccione, *The Theory of Open Quantum Systems* (2002)](https://academic.oup.com/book/27757)**. Chapter 2 supplies density operators, composite systems and physical state transformations. Chapter 3, Sections **3.2.1, 3.2.2 and 3.2.3**, supplies quantum dynamical semigroups, quantum Markov master equations and their adjoint form. The pointers identify the relevant framework; the project-specific inequalities below are not attributed to textbook equations or pages.

## 1. States and generators

A density operator $\rho$ describes the spin ensemble, including a mixed state. An observable $O$ has mean $\langle O\rangle=\operatorname{Tr}(\rho O)$. A Markov master equation specifies the instantaneous change of the state,

$$
\dot\rho=\mathcal L(\rho),
\qquad
\mathcal L(\rho)=-i[H,\rho]+\sum_\mu\mathcal D[L_\mu](\rho),
$$

where this project uses

$$
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\lbrace L^\dagger L,\rho\rbrace .
$$

The Hamiltonian gives coherent evolution. Each dissipator gives an allowed irreversible contribution. For a time-independent generator, the propagators form a semigroup. The project also permits piecewise continuous time-dependent controls; it retains the same instantaneous generator form without assuming one time-independent semigroup for the entire preparation.

Rates are included in the jump operators. A term written as $\Gamma\mathcal D[M]$ can be written as $\mathcal D[\sqrt\Gamma M]$. If another convention places an extra factor of two in a dissipator, its numerical rate must be translated before comparing formulas. Here $\hbar=1$: a Hamiltonian norm and a squared jump norm both have units of inverse time.

The protected auxiliary register $A$ is part of a joint density operator $\rho_{SA}$. Noise acts on the sensors as $\mathcal N_\kappa\otimes\operatorname{id}_A$. Joint entanglement with $A$ is allowed. A coupling that moves a resource from $A$ into the sensors must still obey the specified control conditions; adding a protected register does not remove its sensor support from the budget. In particular, the preserved observable is the sensors' $C\otimes I_A$. Preserving a different total spin formed from sensors and controller would permit transfers between their individual sectors and would change the model. The protected system strengthens the converse's allowance without becoming another carrier of the later signal.

## 2. Translate the noise rate through one observable

For $N$ spin-half sensors, the preparation noise is

$$
\mathcal N_\kappa
=\frac\kappa4\sum_{i=1}^N\sum_{a=x,y,z}\mathcal D[\sigma_i^a].
$$

The factor $1/4$ fixes what the symbol $\kappa$ means. For one spin, the adjoint action on $Z$ is

$$
\frac\kappa4\sum_{a=x,y,z}
(\sigma^a Z\sigma^a-Z)=-\kappa Z.
$$

The $X$ and $Y$ components obey the same equation. Thus a Bloch vector decays as $e^{-\kappa t}$. Equivalently, one spin undergoes replacement by $I/2$ at generator rate $\kappa$. This is independent isotropic noise, rather than a single common fluctuating field applied to every spin.

The adjoint generator is defined by trace duality,

$$
\operatorname{Tr}[O\mathcal L(\rho)]
=\operatorname{Tr}[\mathcal L^\dagger(O)\rho].
$$

For the chosen convention,

$$
\mathcal L^\dagger(O)
=i[H,O]+\sum_\mu
\left(L_\mu^\dagger O L_\mu
-\frac12\lbrace L_\mu^\dagger L_\mu,O\rbrace \right).
$$

This is the useful link to the book's adjoint master equation: instead of solving for every matrix entry of $\rho$, the proof follows one observable whose evolution closes.

## 3. The observable that collective processing preserves

Define the collective spin and its Casimir,

$$
S_a=\frac12\sum_i\sigma_i^a,
\qquad
C=S_x^2+S_y^2+S_z^2.
$$

On a total-spin-$j$ sector, $C$ has value $j(j+1)$. In the allowed free class, every Hamiltonian and every individual jump commutes with $C$. Substituting those commutators into the adjoint equation gives exactly zero contribution to $\mathcal L^\dagger(C)$. Stronger sector-preserving processing therefore cannot directly replenish $\langle C\rangle$.

Independent noise acts differently. Expanding the Casimir gives

$$
C=\frac{3N}{4}I
+\frac14\sum_{i\ne j}\sum_a\sigma_i^a\sigma_j^a.
$$

Every two-spin Pauli product in this expression decays at rate $2\kappa$. Consequently

$$
\mathcal N_\kappa^\dagger(C)
=-2\kappa\left(C-\frac{3N}{4}I\right).
$$

Writing $x(t)=\langle C\rangle_t$, preparation without charged repair has the exact solution

$$
x(t)=\frac{3N}{4}
+\left(x(0)-\frac{3N}{4}\right)e^{-2\kappa t}.
$$

This identity holds with arbitrary allowed collective dynamics and protected auxiliaries. Permutation symmetry of a complete noise channel is insufficient: the proof needs the stated commutation condition on each free jump.

## 4. A complete two-spin noise example

For $N=2$,

$$
C=\frac32I+\frac12(X\otimes X+Y\otimes Y+Z\otimes Z).
$$

The triplet sector has $C=2$, and the singlet has $C=0$. Start from $|00\rangle$, so $x(0)=2$, and apply only the independent noise. At time $t$ the state is $\tau_q\otimes\tau_q$, where $\tau_q=(I+qZ)/2$ and $q=e^{-\kappa t}$. Directly evaluating the three correlations gives

$$
x(t)=\frac32+\frac12q^2
=\frac32+\frac12e^{-2\kappa t}.
$$

The singlet probability is $(1-q^2)/4$; the remaining probability lies in the triplet. The limiting moment is $3/2$, not zero: the fully mixed two-spin state still has triplet weight $3/4$.

This example also separates the moment from actual sensitivity. The product state commutes with $S_z$, so a later $z$-phase leaves it unchanged and its phase-QFI is zero. A large $x$ supplies a ceiling on useful sensitivity; it does not guarantee that a state already uses that ceiling.

## 5. From the moment to phase-QFI

After preparation ends, the unknown phase acts as $e^{-i\theta G}$ with $G=\mathbf n\cdot\mathbf S\otimes I_A$ and a fixed unit axis $\mathbf n$. Here $\theta$ is the later signal parameter, not the preparation time $t$.

Quantum Fisher information quantifies the best local phase sensitivity over measurements. For eigenvalues $\lambda_r$ of the prepared state,

$$
F_Q(\rho,G)
=2\sum_{\lambda_r+\lambda_s>0}
\frac{(\lambda_r-\lambda_s)^2}{\lambda_r+\lambda_s}
|G_{rs}|^2.
$$

The standard variance bound and $G^2\le C\otimes I_A$ give

$$
F_Q\le4\operatorname{Var}(G)\le4x.
$$

Also $G$ has spectral range $N$, including on the joint sensor–auxiliary space, so $F_Q\le N^2$. These are local-QFI statements; they do not by themselves establish a globally unambiguous phase estimate or a complete sensing runtime.

## 6. What local repair must pay

A charged term touches a set $X$ of at most $k$ physical sensors. Its support-weighted contribution is $|X|\|h_X\|$ for a Hamiltonian or $|X|\|L_X\|^2$ for a jump. Their sum is bounded by $B$ at every instant. The squared norm appears because a dissipator is quadratic in its jump amplitude. For example, $\sqrt\kappa|0\rangle\langle1|$ on one spin costs $\kappa$.

The book's generator framework does not itself provide the needed repair inequality. The project adds a local commutator estimate and the dissipative product identity,

$$
\mathcal D[L]^\dagger(S_a^2)
=\lbrace S_a,\mathcal D[L]^\dagger(S_a)\rbrace 
+[S_a,L]^\dagger[S_a,L].
$$

Because a term touching $|X|$ sensors obeys $\|[S_a,L_X]\|\le|X|\|L_X\|$, Cauchy–Schwarz bounds the complete drift by

$$
\dot x\le-2\kappa\left(x-\frac{3N}{4}\right)
+2\sqrt3B\sqrt x+3kB.
$$

The repair term grows as $B\sqrt x$. Balancing it against the loss $\kappa x$ produces the scale $(B/\kappa)^2$. Integrating the inequality retains the initial resource explicitly; it cannot be discarded at an arbitrary short time. At every prescribed $T\ge\log(N+2)/\kappa$, the matching optimal order is

$$
F_Q^{\mathrm{opt}}
=\Theta_k\!\left(\min\lbrace N^2,N+(B/\kappa)^2\rbrace \right).
$$

The [converse](../science/converse.md) supplies the proof and record-assisted extension. The hard budget, fixed locality order, homogeneous signal and deterministic output time are part of this statement.

The signal restriction has a direct physical meaning: every spin sees the same unknown phase along the same axis. A difference between two ensembles' phases has a different generator. An inter-ensemble singlet can have zero global $C$ yet respond strongly to that differential signal, so the displayed global-Casimir bound cannot simply be reused. Likewise, a preparation record selected only on favorable outcomes must retain its acceptance probability. The project proves a bound on probability-weighted conditional QFI at the prescribed output time, rather than granting an uncharged wait until a useful branch appears. These boundaries follow the operational task, not a change of textbook notation.

## 7. A counted repair-and-cat example

Pump both spins of the two-spin example with jumps $\sqrt\kappa|0\rangle\langle1|$. Starting from $I/4$, the charged budget is $B=2\kappa$, and after a finite time $s$ the input is $\tau_p\otimes\tau_p$ with

$$
p=\frac{1-e^{-2\kappa s}}2.
$$

Its moment is $x=3/2+p^2/2$. For the ideal unitary step, apply the supplied sector-preserving gate $U=e^{-i\pi X\otimes X/4}$. It leaves $x$ unchanged but converts the polarization into phase sensitivity. The input eigenvalues for $00$ and $11$ are $(1+p)^2/4$ and $(1-p)^2/4$. The conjugated signal couples that pair, giving

$$
F_Q(U\tau_p^{\otimes2}U^\dagger,S_z)
=\frac{8p^2}{1+p^2}.
$$

As $s$ tends to infinity, $p$ tends to $1/2$ and this QFI tends to $8/5$. At finite $s$ the displayed expression is exact for this ideal unitary step; the later finite noisy pulse has a separately bounded error. Before the cat gate, the diagonal product state has zero $z$-phase QFI.

The general construction pumps $m=\lfloor B/\kappa\rfloor$ spins and obtains QFI of order $N+m^2$. Its cat amplification mechanism is inherited mixed-state metrology. The project establishes matching budget accounting and a finite pulse whose noise error is controlled by a fixed-measurement witness. At very small $B$, the linear baseline uses a separate global spin-sector reset allowed by the broad free class. These collective operations are supplied, potentially expensive resources.

Continue with [Construction](../science/construction.md) for the full binomial formula and pulse strengths, and [Resources](../science/resources.md) for their implementation limits. The contribution concerns preparation for a subsequent phase imprint; it does not promise a stationary quadratic-QFI sensor or protection during noisy frequency encoding.
