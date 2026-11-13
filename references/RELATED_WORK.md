# Attribution and related work

The contribution is a bound on the strength of **microscopic repair during noisy
probe preparation**. It is not the discovery of spin-sector leakage, mixed-state
metrological amplification, or the fragility of a probe after a terminal noise
channel. Those ingredients have substantial antecedents.

The [model](../science/model.md) allows arbitrarily strong processing that
preserves the sensor Casimir $`C=S^2`$, while charging every bounded-support term
that can change it. Under independent isotropic depolarization, the
[converse](../science/converse.md) bounds the collective-phase QFI by the available
spin moment and repair strength. The
[construction](../science/construction.md) combines local polarization with an
inherited cat-style amplification mechanism. Its supplied collective gate and
finite-pulse costs are kept explicit in the
[resource account](../science/resources.md).

## Comparison map

| Earlier result | Ingredient credited here | Distinction of the present task |
| --- | --- | --- |
| Chase–Geremia (2008), Baragiola–Chase–Geremia (2010), Shammah et al. (2018) | Identical local noise can move population between total-spin sectors; permutation invariance does not confine a state to the maximal-spin sector. | A universal repair-strength bound, including coherent and dissipative local repair interleaved with arbitrary Casimir-preserving processing. |
| Modi et al. (2011), Cable–Gu–Modi (2016) | Mixed-state cat/GHZ-diagonal probes can amplify a limited polarization supply into collective phase QFI. | Relating the polarization that survives persistent noise to a hard instantaneous repair budget; the amplification principle is inherited. |
| López-Incera–Sekatski–Dür (2019) | Bounds on QFI after specified independent local-noise channels, and preparation bounds under covariance of the signal generator. | Casimir preservation is weaker than covariance under the signal rotation. Interleaved regeneration is allowed throughout preparation. |
| Chu et al. (2026) | Collective decay and ensemble-selective coherent controls prepare useful differential-sensing states. | Their controls preserve each ensemble's spin length while changing the global total-spin sector. A global-Casimir homogeneous-signal bound cannot be applied to their differential signal. |
| Ho et al. (2026) | Explicit linear/nonlinear Hamiltonian controls can improve particular noisy spin-sensing protocols. | The present result quantifies over all allowed preparation controls and charges symmetry-changing repair; it does not optimize a fixed sensing-control family. |
| Sur et al. (2026) | Ancilla-mediated purification can overcome collective symmetry restrictions through inhomogeneous couplings. | The present bound prices those symmetry-changing couplings against persistent depolarization and a final probe-QFI objective. |

Bibliographic data are in [references.bib](references.bib). The statements below
identify the primary-source boundaries used in these comparisons.

## Local decoherence and spin-sector leakage

Chase and Geremia, [Phys. Rev. A **78**, 052101
(2008)](https://doi.org/10.1103/PhysRevA.78.052101), develop a reduced
representation for identical local decoherence beyond the symmetric subspace.
The detailed article is available as
[arXiv:0805.2911](https://arxiv.org/abs/0805.2911). The spin-sector leakage
mechanism and reduced representation are inherited ingredients.

Baragiola, Chase and Geremia, [Phys. Rev. A **81**, 032104
(2010)](https://doi.org/10.1103/PhysRevA.81.032104), analyze partially polarized
and locally decohered ensembles. Their [preprint
v1](https://arxiv.org/abs/0910.3897v1), Sec. IV, Eqs. (50)–(52) and Figs. 3–6,
explicitly contrasts local and collective depolarization and the resulting
spin-sector populations and collective uncertainties.

Shammah et al., [Phys. Rev. A **98**, 063815
(2018)](https://doi.org/10.1103/PhysRevA.98.063815), provide the PIQS framework
for local and collective Lindblad processes. The inspected
[preprint v5](https://arxiv.org/abs/1805.05129v5), Sec. II, Eq. (1), separates
homogeneous local emission, pumping and dephasing from their collective
counterparts. These works supply the representation and physical distinction.
The present Casimir drift is derived directly with the rate convention of our
model; a new observation of leakage is not claimed.

## Mixed-state amplification

Modi, Cable, Williamson and Vedral, [Phys. Rev. X **1**, 021022
(2011)](https://doi.org/10.1103/PhysRevX.1.021022), compare phase-estimation
strategies at fixed input mixedness. In [preprint
v4](https://arxiv.org/abs/1003.1174v4), Sec. III D, Eq. (12), the Q2 strategy
evaluates complementary-string contributions to the QFI of a GHZ-diagonal
probe. The polarization-dependent collective enhancement is an antecedent of
our spectral calculation.

Cable, Gu and Modi, [Phys. Rev. A **93**, 040304(R)
(2016)](https://doi.org/10.1103/PhysRevA.93.040304), allow pure, partly polarized
and maximally mixed registers with bulk controlled operations. Their
[preprint v2](https://arxiv.org/html/1504.02460v2), Eqs. (4)–(11), gives the
resulting QFI, including the one-pure-qubit standard-quantum-limit case.
Their input model supplies a pure control qubit; our construction instead
evaluates the particular partly polarized sensor state produced by repair.
Neither mixed-state amplification nor the use of mostly mixed probes is
claimed as new.

One-axis twisting is the established mechanism of Kitagawa and Ueda,
[Phys. Rev. A **47**, 5138
(1993)](https://doi.org/10.1103/PhysRevA.47.5138). Its use as an implementation
route does not make its strength or duration free in a hardware resource claim.

## Terminal noise and covariant preparation

López-Incera, Sekatski and Dür, [Quantum **3**, 118
(2019)](https://doi.org/10.22331/q-2019-01-25-118), bound QFI after specified
independent local channels, including depolarization, with channel-dependent
exceptions.

Their [published PDF](https://quantum-journal.org/papers/q-2019-01-25-118/pdf/),
Sec. 5, Eqs. (47)–(54), separately assumes instrument covariance under
$`A_{\rm tot}=A_{\rm sys}+A_{\rm RF}`$; data processing bounds average output
QFI by the supplied system-plus-reference QFI.

Our free controls preserve $`S^2`$, not $`\mathbf n\cdot S`$; a cat gate can
increase signal QFI while preserving $`S^2`$. Thus the reference-frame theorem
does not imply this repair bound. Coherent-reference costs remain physical
resources. A terminal-channel bound also cannot simply be reapplied to
arbitrarily strong interleaved regeneration; our moment inequality addresses
that interleaving.

## Multiple ensembles and differential signals

Chu, Mamaev, Koppenhöfer, Yuan and Clerk, [Phys. Rev. X **16**, 021047
(2026)](https://doi.org/10.1103/qdh9-2pc7), combine collective decay with
ensemble-dependent detunings and chiral exchange. In the inspected
[preprint v2](https://arxiv.org/html/2510.07616v2), Eq. (2), every term preserves
each sub-ensemble Casimir $`S_l^2`$. The detuning and exchange terms need not
preserve the global $`(\sum_l S_l)^2`$. Sec. III B, Eq. (10), evaluates a
differential signal; Sec. III C examines single-spin decay, and Appendix B
analyzes relaxation time.

For example, a total singlet can have quadratic differential QFI despite zero
global Casimir. Our homogeneous-signal statement does not forbid this.
A multi-ensemble application must track separate Casimirs, preserved by each
free control. Their amplitude-decay/cooperativity analysis also differs from
the present isotropic-noise, all-control repair-budget problem.

## Controlled sensing and ancilla purification

Ho, Duong, Takahashi and Matsueda, [Phys. Rev. A **114**, 032206
(2026)](https://doi.org/10.1103/sxxg-77b1), study GHZ and multi-GHZ probes,
local/collective emission, pumping and dephasing, and coherent protection
during encoding. In the inspected [preprint
v1](https://arxiv.org/html/2603.22734v1), Sec. IV and Appendix B, the explicit
controls include $`\chi J_x`$ and $`\chi J_x^2`$. These examples show the utility
of collective control in specified sensing models. Our final phase is
imprinted after preparation, and our bound applies to the entire admissible
control class rather than those particular Hamiltonians. We do not infer a
continuous noisy-frequency sensing bound from endpoint probe QFI.

Sur et al., [npj Quantum Information **12**, 109
(2026)](https://doi.org/10.1038/s41534-026-01228-9), overcome purification
obstructions using an intermittently reset ancilla and alternating resonant
and dispersive interactions. The inspected [preprint
v1](https://arxiv.org/html/2603.03917v1), Secs. II D–E, Eqs. (18)–(27),
uses inhomogeneous spin–ancilla couplings to connect otherwise invariant
sectors. In our support convention, each sensor–ancilla bond is a
one-sensor-support term. Its symmetry-changing part is charged repair,
including when a uniform Casimir-preserving component is separated off.
Their purification task does not impose our persistent independent
depolarization or final QFI objective. The physical symmetry-breaking route is
an antecedent, not a counterexample to a bound that charges it.

## Scope of the comparison

The added result is the quantitative local-repair frontier under the stated
noise, support, instantaneous-budget and readout assumptions. The comparison
does not claim exhaustive priority certification. It does not turn a
preparation-QFI bound into a bound on every sensing protocol, nor does it
establish an end-to-end hardware advantage. Scientific statements and proof
dependencies are maintained in the linked science files.

