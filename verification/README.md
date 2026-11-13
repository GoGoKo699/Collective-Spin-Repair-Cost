# Reproduce the finite checks

The analytical proofs are in [Converse](../science/converse.md) and
[Construction](../science/construction.md). The deterministic program below
tests their consequential finite-dimensional identities, the ancillary-system
extension, and the actual finite-pulse construction.

From the repository root, use Python 3.12 and run:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/verify.py
```

The reference execution used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0.
The script requires no network access once its dependencies are installed.
Its default command prints the results without modifying files. To regenerate
the supplied numerical record explicitly, run:

```bash
python3 verification/verify.py --json verification/finite_checks.json
```

The final line on a successful run is:

```text
PASS: all finite checks satisfy the stated tolerances and scope.
```

## What is checked

| Check | Method and finite scope |
| --- | --- |
| Depolarizing Casimir identity | Direct Pauli adjoint calculation for $`N=1,\ldots,6`$; an independently implemented partial-trace replacement generator acts on density matrices with protected auxiliaries of dimensions two and three. |
| Exact finite-time moment law | Tensor-product depolarizing channels at several times, also interleaved with nonlinear Casimir-preserving sensor–auxiliary unitary controls. |
| Protected-reference QFI cap | Joint-state spectral QFI for mixed states and deliberately entangled physical/reference states, with phase acting only on the sensors. |
| Local repair proof | The Lindblad product identity, commutator norm estimates, and the Young-inequality operator bound for sixteen Hamiltonian/jump examples, including noncontiguous physical supports and joint protected-auxiliary couplings. The operator bound checks every input state for each tested generator. |
| Mixed-state cat formula | Sixty-three direct spectral versus binomial evaluations, $`N=1,\ldots,6`$, all nonempty pumped-register sizes, and polarizations $`0.2,0.5,0.8`$; lower bounds are tested only in their stated polarization range. Both even and odd $`N`$ are included. |
| Finite preparation and cat pulse | Five protocols at the actual horizon $`T=\log(N+2)/\kappa`$, using finite-time pumping and evolution with the pulse Hamiltonian and continuing independent depolarization simultaneously. The classical FI of the ideal SLD measurement verifies the stated robustness witness. |
| No-repair linear baseline | Explicit multiplicity-preserving spin-sector reset Kraus operators for $`N=1,\ldots,4`$; finite-time evolution from maximally mixed sensors at $`t=1/\kappa`$ and a separate direct stationary linear solve. These are global supplied controls, not local reservoir implementations. |
| Model boundaries | A singlet has zero global Casimir and nonzero differential-signal QFI. Four-spin GHZ states have zero Casimir drift under one-axis dephasing, while isotropic depolarization has the claimed nonzero drift. |

The [saved report](finite_checks.json) contains numerical values. The Casimir
and product-identity residuals are below $`2\times10^{-14}`$ in the reference
run, and the largest cat-QFI discrepancy is below $`3\times10^{-14}`$.
Assertions use an absolute tolerance of $`2\times10^{-9}`$ to accommodate
ordinary floating-point and linear-algebra differences.

## Verification limits

The finite checks do not prove arbitrary-$`N`$ statements, sharp asymptotic
orders, exhaustive prior-work coverage, or an experimental implementation.
The universal all-control theorem rests on its written commutator,
Cauchy–Schwarz and integrating-factor proof. Random generator samples are
reproducible examples rather than a completeness argument.

The finite pulse uses the explicitly supplied $`N`$-body Hamiltonian and its
stated sufficient norm. Passing this check does not make that Hamiltonian
cheap to synthesize. The phase is introduced after preparation; these checks
do not establish precision during noisy frequency encoding or Fisher
information for an entire measurement transcript.
