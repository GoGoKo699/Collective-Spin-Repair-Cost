# What the repair frontier means

[Model](model.md) · [Proof](converse.md) · [Construction](construction.md) · [Resource ledger](resources.md)

## Spin length and useful orientation are separate resources

An ensemble of spin-half particles has many total-spin sectors. Collective rotations and nonlinear collective operations can change the state's orientation and correlations within those sectors. Independent local depolarization also moves weight between sectors. Under the free controls in this model, the exact balance is

```math
\frac{d}{dt}\langle S^2\rangle
=-2\kappa\left(\langle S^2\rangle-\frac{3N}{4}\right)
```

when no charged repair is present. This identity concerns the full physical Hilbert space; the probe need not remain in the permutation-symmetric sector.

The signal generator is one homogeneous spin component. Its QFI cannot exceed four times the available second moment. Repeatedly reshaping the state inside its current sectors therefore cannot restore a quadratic collective phase resource once that moment has decayed to order $`N`$.

Local repair changes the moment at a rate bounded by a term of order $`B\sqrt{\langle S^2\rangle}`$, plus a bounded-locality correction. Balancing this against the noise loss gives the scale $`(B/\kappa)^2`$. The [converse](converse.md) makes this argument a finite-time inequality, including arbitrary protected auxiliaries and coherent as well as dissipative repair.

## The two repair scales

After the stated initial-resource decay, the supplied-control optimum has order

```math
F_Q^{\rm opt}
=\Theta_k\!\left(\min\lbrace N^2,\;N+(B/\kappa)^2\rbrace \right).
```

The locality order $`k`$ is fixed, the output time is prescribed, and the budget is capped at every instant. The exact hypotheses and constants are in the [model](model.md).

| Repair strength | Order of optimal endpoint QFI | Consequence |
| --- | --- | --- |
| $`B=O(\kappa\sqrt N)`$ | $`\Theta(N)`$ | Collective processing supplies at most a bounded factor over linear QFI. |
| $`\kappa\sqrt N\ll B\ll\kappa N`$ | $`\Theta((B/\kappa)^2)`$ | The available repair produces an increasing collective phase gain. |
| $`B=\Omega(\kappa N)`$ | $`\Theta(N^2)`$ | A fixed fraction of Heisenberg-order probe QFI becomes possible in the supplied-control model. |

For example, repair strength $`B=\kappa N^{3/4}`$ supports endpoint QFI of order $`N^{3/2}`$. If at most $`r`$ sensors have bounded incident local strength $`\Gamma_{\rm site}`$, then $`B\le r\Gamma_{\rm site}`$ and quadratic probe QFI requires $`r\Gamma_{\rm site}=\Omega(\kappa N)`$.

These are phase-QFI orders. They do not by themselves determine a global estimation risk, the number of repetitions, measurement complexity or a laboratory precision per unit time.

## A mixed probe can use a limited polarization supply

The constructive protocol pumps $`m`$ individual spins to a fixed positive polarization while the other spins remain maximally mixed. The final supplied collective cat operation turns that state into a useful probe. For polarization $`p`$, its exact ideal QFI is

```math
F_{p,m}=\mathbb E\!\left[(K^2+N-m)
\tanh^2(\operatorname{atanh}(p)K)\right],
```

where $`K`$ is a sum of $`m`$ independent signs of mean $`p`$. With one pumped spin, this reduces to $`p^2N`$. For fixed positive $`p`$ and growing $`m`$, its order is $`N+m^2`$. The [construction](construction.md) derives the formula and gives a uniform lower bound.

Mixed-state amplification is an inherited metrological mechanism. Its role here is to match the repair converse: at fixed noise rate, maintaining $`m`$ polarized spins uses local strength proportional to $`m\kappa`$.

The zero-repair linear baseline uses the broader free class explicitly: highly engineered jumps reset the spin state within each existing sector while preserving its weight. Their global structure and sufficient rate are reported. That baseline establishes the mathematical optimum under the declared free resources; it does not assert that local reservoirs implement those jumps cheaply.

## Four boundaries that change the question

**Initial resources.** An initially high-spin state can retain an order-$`N^2`$ moment for a fixed time of order $`\kappa^{-1}`$. The finite-time bound retains this contribution. The uniform frontier from arbitrary initial states uses $`T\ge\kappa^{-1}\log(N+2)`$; the time hypothesis must travel with the scaling law.

**Success-selected waiting.** At a fixed time, a rare high-spin branch may have high conditional QFI, but its probability multiplies that QFI in the yield bound. Repeating until a favorable fluctuation appears changes the output-time contract. Converse Section 7 gives an explicit eventual-success example and keeps its waiting cost visible.

**The signal.** A global spin singlet has zero $`S^2`$ and hence zero homogeneous-spin QFI. Two spin-$`j`$ ensembles in a singlet nevertheless have

```math
F_Q(S_{1z}-S_{2z})=\frac{16}{3}j(j+1),
```

because the differential generator is not bounded by the global Casimir. Applying the result to several ensembles requires tracking their separate Casimirs and checking the free-control hypotheses for each. The homogeneous-signal theorem does not rule out differential-sensing constructions.

**The noise.** Independent isotropic depolarization is essential to the exact drift. Pure one-axis dephasing can flip GHZ phase states while keeping them in the maximal-spin sector; a sufficiently broad sector-preserving controller can act on those errors without replenishing spin length. The depolarization theorem therefore cannot be quoted as a theorem for every local noise process.

## What is supplied in the matching result

The final entangling pulse has finite duration, and independent noise remains active during it. The sufficient norm bound grows with $`N`$. A fixed-measurement witness proves that this finite pulse retains a constant fraction of the ideal probe QFI without assuming uniform QFI continuity near small eigenvalues.

The result consequently establishes an endpoint preparation frontier with explicit additional supplied collective resources. Parameter encoding follows preparation. A bounded-bandwidth apparatus, a stationary quadratic-QFI sensor, or an interrogation interval with continuing depolarization requires a separate performance analysis.
