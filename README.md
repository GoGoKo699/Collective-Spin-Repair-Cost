# Collective Spin Repair Cost

**How much local repair is needed to prepare a collective spin probe under persistent independent noise?**

Collective control can reshape a spin ensemble without changing its total-spin sectors. Local depolarization changes those sectors. This project gives a quantitative limit on how much bounded-support repair can replenish the collective phase sensitivity, even when sector-preserving processing is arbitrarily powerful.

## Main result

For $N$ physical spin-half sensors with independent depolarization at Bloch-decay rate $\kappa$, let $B$ cap the instantaneous support-weighted strength of local Hamiltonian and dissipative repair. Each charged term touches at most a fixed number $k$ of sensors. At every prescribed output time

$$
T\ge\frac{\log(N+2)}{\kappa},
$$

the optimal QFI for a subsequent homogeneous collective phase imprint has order

$$
\boxed{
F_Q^{\rm opt}(N,B,T)
=\Theta_k\!\left(
\min\left\{N^2,\;N+\left(\frac B\kappa\right)^2\right\}
\right).
}
$$

The [exact model and theorem](science/model.md) specify the allowed controls, fixed output-time contract, initial-resource term and constants. The converse permits arbitrary initial states, protected finite ancillas and finite preparation records. The construction starts from maximally mixed sensors. Its collective controls are supplied resources with separately stated strength and implementation limits.

| Scientific consequence | Supported statement |
| --- | --- |
| Arbitrarily powerful sector-preserving processing | Cannot replace the local repair budget in the converse. |
| Increasing gain over linear QFI | Requires $B/(\kappa\sqrt N)\to\infty$ after the initial resource has decayed. |
| A fixed fraction of $N^2$ probe QFI | Requires and, in the supplied-control model, admits $B=\Theta(\kappa N)$. |
| Heralding at a prescribed output time | The accepted QFI is weighted by the actual acceptance probability. |
| Finite collective pulse | A fixed-measurement witness preserves a constant fraction of ideal QFI while noise remains active; sufficient pulse strengths are explicit. |

The task is **probe preparation**, with the phase imprinted afterward. The result does not establish a stationary Heisenberg sensor or precision during a noisy frequency-interrogation interval. Highly engineered collective controls, their bandwidth and their physical realization retain their own costs.

## Read the science

Start with the [scientific guide](science/README.md), or follow the direct route:

1. [Model and results](science/model.md): charged repair, supplied controls, noise, readout and complete statements.
2. [Converse](science/converse.md): exact Casimir loss, local repair drift, initial-resource decay and heralding yield.
3. [Construction](science/construction.md): finite pumping, mixed-state cat QFI, finite noisy pulses and the low-budget baseline.
4. [Resources](science/resources.md): explicit strength/time ledger and operational boundaries.
5. [Interpretation](science/interpretation.md): the two repair scales and concrete signal, noise and timing limits.

Spin-sector leakage and mixed-state metrological amplification are established ingredients. The contribution is the all-control repair-strength frontier under the stated assumptions, together with a matching endpoint preparation account. The [primary-source comparison](references/RELATED_WORK.md) and [bibliography](references/references.bib) identify those inherited results and distinguish the closest preparation theorems.

## Learn the project

The [learning guide](learning/README.md) connects Breuer–Petruccione, *The Theory of Open Quantum Systems* (2002), to this result. Use the [source-to-project bridge](learning/BRIDGE.md) for notation, the missing collective-spin and metrology steps, and worked examples. The [30-milestone map](learning/MILESTONES.md) follows the background ideas into the repair converse, matching construction and physical limits.

## Reproduce the checks

With Python 3.12:

```bash
python -m pip install -r verification/requirements.txt
python verification/verify.py --json verification/finite_checks.json
```

The [verification guide](verification/README.md) records the tested finite systems, numerical residuals and limits. Analytical proofs establish the general statements; finite calculations check their operator conventions, constructions and consequential boundaries.

The [LLM reading guide](llms.txt) maps questions to the authoritative files.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The existing [MIT license](LICENSE) is retained.
