# Model and results

A collective controller can rotate, squeeze, entangle and dissipatively reshape a spin ensemble without changing its total-spin sectors. Independent local noise changes those sectors. This project asks how much additional control that acts on individual spins, or on bounded groups of spins, is required to replenish the collective phase sensitivity after a long preparation period.

The output is a probe for a subsequent noiseless phase imprint. The result prices a specified local control budget during preparation. It does not assert stationary high sensitivity, a precision advantage during noisy interrogation, or an optimal implementation cost for the supplied collective controls.

[Complete converse](converse.md) · [Attaining probe preparation](construction.md) · [Resource interpretation](resources.md) · [Prior work](../references/RELATED_WORK.md)

## 1. Spins, noise and conventions

There are $`N\ge 1`$ physical sensor qubits, with Hilbert space $`\mathcal H_S=(\mathbb C^2)^{\otimes N}`$. Write

```math
S_a=\frac12\sum_{i=1}^N\sigma_i^a,\qquad
C=S_x^2+S_y^2+S_z^2,\qquad a\in\lbrace x,y,z\rbrace .
```

Identity operators on other registers are implicit. We use $`\hbar=1`$, operator norm $`\|\cdot\|`$, and

```math
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\lbrace L^\dagger L,\rho\rbrace .
```

The unavoidable preparation noise is independent isotropic depolarization,

```math
\mathcal N_\kappa
=\frac{\kappa}{4}\sum_{i=1}^N\sum_{a=x,y,z}\mathcal D[\sigma_i^a],
\qquad \kappa>0.
\tag{1}
```

This normalization makes each single-qubit Bloch component decay as $`e^{-\kappa t}`$. The noise acts on every sensor throughout preparation. It is neither collective depolarization nor a terminal noise layer.

A finite-dimensional protected register $`A`$ may contain ancillas or a controller. Its dimension can depend on $`N`$ and on the chosen protocol. The initial state $`\rho_{SA}(0)`$ may be arbitrary, including correlated and entangled states. An inaccessible reference can be included as a subfactor on which all controls act as the identity; the converse even allows access to the whole finite register. The phase will act only on the physical sensors, so retaining information in $`A`$ does not create another sensing carrier.

## 2. Free controls and charged repair

During preparation, the joint state has a piecewise continuous, finite-dimensional Lindblad evolution

```math
\dot\rho
=(\mathcal N_\kappa\otimes\operatorname{id}_A)(\rho)
+\mathcal K_t(\rho)+\mathcal R_t(\rho).
\tag{2}
```

Each finite preparation interval has a well-defined propagator. The coefficients may depend on $`N`$ and on the prescribed readout time.

### Sector-preserving controls

The supplied control generator is

```math
\mathcal K_t(\rho)
=-i[H_{0,t},\rho]+\sum_\nu\mathcal D[J_{\nu,t}](\rho),
\tag{3}
```

where every individual term satisfies

```math
[H_{0,t},C\otimes I_A]=0,\qquad
[J_{\nu,t},C\otimes I_A]=0.
\tag{4}
```

Their strengths, nonlinearities, number of terms and joint sensor–ancilla structure are unrestricted within a well-defined finite protocol. Ancilla-only operations are included.

Ordinary collective operators and their polynomials satisfy (4). The admitted class is deliberately more generous: some nonuniform, rotation-invariant exchange interactions also preserve $`C`$. Conversely, covariance of a complete noise channel under permutations does not imply (4) for its individual jump operators. The independent jumps in (1) provide an example of that distinction.

Finite instantaneous sector-preserving channels are also allowed as ideal supplied operations. It is sufficient that their Kraus operators commute with $`C\otimes I_A`$; such a channel preserves $`\operatorname{Tr}(C\rho)`$. The terminal collective gate used in the construction is one such operation. Its finite-pulse implementation and physical cost are treated separately in [resources](resources.md).

### Bounded-support repair

The additional controls have a specified decomposition

```math
\mathcal R_t(\rho)
=-i\left[\sum_X h_{X,t},\rho\right]
+\sum_{X,\mu}\mathcal D[L_{X\mu,t}](\rho).
\tag{5}
```

Here $`X`$ is a nonempty subset of physical sensors, $`r_X=|X|\le k`$, and every $`h_X`$ or $`L_{X\mu}`$ acts trivially on sensors outside $`X`$. It may act jointly on the protected register $`A`$. Spatial adjacency is not assumed: $`k`$ bounds the number of sensors touched by one charged term.

The instantaneous control budget is

```math
\begin{aligned}
b(t)
&=\sum_X r_X\|h_{X,t}\|
+\sum_{X,\mu}r_X\|L_{X\mu,t}\|^2,\\
b(t)&\le B
\qquad\text{for every preparation time.}
\end{aligned}
\tag{6}
```

The jump amplitudes include their rates; for example, $`\sqrt{\Gamma}\,\sigma_i^+`$ costs $`\Gamma`$. Hamiltonian norms and squared jump norms both have units of inverse time. The locality $`k`$ is fixed when discussing asymptotic order in $`N`$.

Equation (6) is a **hard instantaneous cap**, not a bound on a long-time average or on total action. It prices the supplied local decomposition. No invariance under arbitrary changes of Lindblad representation, or optimum over physical implementations of that representation, is claimed. Terms that satisfy (4) can be included in the free generator; the theorem holds for every remaining decomposition obeying (5)–(6).

A reset of $`A`$ alone is free in this budget. A coupling that transfers purity from $`A`$ into a bounded sensor set is subject to (6) unless it preserves the sensor Casimir. A sensor reset, replacement or noncollective instantaneous pulse is not an additional free operation.

## 3. Output task

The initial state and every preparation choice are independent of the unknown phase. The readout time $`T`$ is prescribed and deterministic. After preparation, imprint

```math
U_\theta=e^{-i\theta G},\qquad
G=\mathbf n\cdot\mathbf S\otimes I_A,\qquad
\|\mathbf n\|_2=1.
\tag{7}
```

The sensitivity is the symmetric-logarithmic-derivative quantum Fisher information

```math
F_Q(\rho_{SA}(T),G).
```

This is a local phase-sensitivity metric for the prepared probe. We do not identify it with a global minimax estimation guarantee, a total repetition cost, or frequency sensitivity while noise continues to act during parameter encoding.

The homogeneous generator in (7) is load-bearing. A bound using the global Casimir does not automatically cover a spatially varying or differential signal. In particular, an inter-ensemble singlet can have zero global spin and large differential sensitivity.

Define the initial second moment

```math
x_0=\operatorname{Tr}[C\rho_S(0)],
\qquad
0\le x_0\le\frac{N(N+2)}4.
\tag{8}
```

This quantity records the initial sensor resource even when the initial state or the protected register has been supplied without a preparation charge.

## 4. Main finite-time converse

**Theorem 1.** Every protocol in Sections 1–3 obeys

```math
\begin{aligned}
F_Q(\rho_{SA}(T),G)
\le \min\Bigg\lbrace N^2,\;&4e^{-\kappa T}x_0\\
&+(1-e^{-\kappa T})
\left[
6N+12\left(\frac B\kappa\right)^2
+12k\frac B\kappa
\right]\Bigg\rbrace .
\end{aligned}
\tag{9}
```

The bound is uniform over the free control strengths, the finite protected register, and the allowed local repair terms. It does not require a unique stationary state or convergence to one.

With no repair, the sharper exact moment identity is

```math
\operatorname{Tr}[C\rho_S(T)]
=\frac{3N}{4}
+\left(x_0-\frac{3N}{4}\right)e^{-2\kappa T}.
\tag{10}
```

Consequently every stationary joint state without repair satisfies

```math
F_Q(\rho_{SA,*},G)\le \min\lbrace N^2,3N\rbrace .
\tag{11}
```

For general $`B`$, any stationary state obeys (9) with the initial exponential term removed. These stationary upper bounds do not supply a stationary attaining construction.

The [proof](converse.md) establishes the operator noise identity, a local repair drift bound, and the conversion of the resulting moment bound to QFI.

## 5. Uniform preparation frontier

The finite-time initial-resource term in (9) becomes at most $`N`$ whenever

```math
T\ge \frac{\log(N+2)}{\kappa}.
\tag{12}
```

Thus, for every such prescribed readout time,

```math
F_Q\le
\min\left\lbrace 
N^2,\;
7N+12\left(\frac B\kappa\right)^2
+12k\frac B\kappa
\right\rbrace .
\tag{13}
```

For any fixed $`k\ge1`$ and every

```math
B\ge0,
\tag{14}
```

the optimal order in the supplied-control model is

```math
\boxed{
F_{N,k}^{\mathrm{opt}}(B,\kappa,T)
=\Theta_k\!\left(
\min\left\lbrace N^2,\;
N+\left(\frac B\kappa\right)^2
\right\rbrace 
\right).
}
\tag{15}
```

Here the optimum is over the admissible preparation protocols, initial states and finite protected registers for any fixed prescribed unit signal axis. The upper bound permits arbitrary initial sensor states and protected finite ancillas. The [lower construction](construction.md) starts from maximally mixed sensors and uses the same hard repair cap. For $`\kappa\le B\le\kappa N`$, it pumps $`\lfloor B/\kappa\rfloor`$ selected individual spins, then applies a supplied sector-preserving collective gate at the deterministic output time. For $`B>\kappa N`$, pumping all sensors saturates the quadratic order. For $`B\lt \kappa`$, a supplied global spin-sector reset generator attains linear QFI with no charged repair; its highly structured jumps have an explicitly growing supplied rate. Constants are uniform in $`N`$, $`B`$ and $`\kappa`$ under (12), with $`k`$ fixed; $`k`$ enters the converse constants. Whenever charged repair is used, the construction needs only one-sensor repair terms.

Equation (15) concerns endpoint probe preparation with the stated collective operations supplied. It is not a claim that those operations can be engineered at an $`N`$-independent laboratory cost. No stationary quadratic-QFI construction or noisy-interrogation advantage is inferred from the endpoint protocol.

A consequence of the upper bound is architectural: to maintain a fixed positive fraction of $`N^2`$ endpoint QFI after the initial resource has decayed, one needs

```math
B=\Omega(\kappa N)
\qquad(N\to\infty,\ k\text{ fixed}).
\tag{16}
```

For example, if only $`r`$ physical sensors participate in charged control and the total incident Hamiltonian/jump budget at each such sensor is at most $`\Gamma`$, then $`B\le r\Gamma`$. Equation (16) gives $`r\Gamma=\Omega(\kappa N)`$. Increasing only the strength of the free sector-preserving controls cannot replace that local budget.

## 6. Preparation records and heralding

A finite preparation record can be retained, and subsequent controls can depend on it. The version covered here has finitely many prescribed intervention times, finite outcome sets, and a hard cap (6) on every feedback branch. Free intervention Kraus operators commute with $`C\otimes I_A`$. Ancilla-only instruments satisfy this condition.

The upper bounds then hold for the joint classical–quantum output, with $`x_0`$ interpreted as the initial average moment. They therefore cover the average conditional QFI when the preparation record is available. The phase is introduced only after the record has been generated, so its probabilities are independent of $`\theta`$. The [record proof](converse.md#6-finite-record-feedback-and-heralding) makes these conditions explicit.

If a heralding event at the prescribed time has probability $`p_{\mathrm{acc}}`$, its accepted output satisfies the yield bound

```math
p_{\mathrm{acc}}\,
F_Q(\rho_{\mathrm{acc}},G)
\le \text{the right-hand side of (9)}.
\tag{17}
```

The accepted state may retain its preparation record. Discarding that record cannot increase its QFI.

These statements do not cover arbitrary random stopping times. Waiting until a favorable outcome and then declaring that time to be the output is a different task; its waiting-time or success-probability cost requires its own accounting.

## 7. What is inherited and what is added

Leakage from the maximal-spin sector under independent local noise, the distinction between local and collective decoherence, and amplification of phase sensitivity from mixed probes are established ingredients. The quantitative statement developed here is the bound on **all** bounded-support repair strategies despite unrestricted sector-preserving processing, together with its matching endpoint resource order.

The actual novelty comparison and the limits of the imported constructions are in [related work](../references/RELATED_WORK.md). The mathematical result does not establish exhaustive priority or a journal acceptance prediction.

