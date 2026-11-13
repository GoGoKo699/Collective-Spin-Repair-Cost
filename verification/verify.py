#!/usr/bin/env python3
"""Deterministic finite checks of the collective-spin repair account.

Run from any directory with Python 3.10+, NumPy and SciPy. No files are
modified unless --json PATH is supplied. These checks supplement the
analytical proofs; they do not prove arbitrary-N or optimality statements.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.sparse.linalg import LinearOperator, expm_multiply


ATOL = 2e-9
RNG = np.random.default_rng(20261113)
I2 = np.eye(2, dtype=complex)
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.diag([1, -1]).astype(complex),
)


def kron_all(operators):
    answer = np.ones((1, 1), dtype=complex)
    for operator in operators:
        answer = np.kron(answer, operator)
    return answer


def embed(operator, support, n, aux_dim=1):
    """Embed on arbitrary physical support and the complete protected auxiliary."""
    support = tuple(support)
    assert len(set(support)) == len(support)
    assert all(0 <= site < n for site in support)
    dimensions = [2] * n + [aux_dim]
    selected = list(support) + [n]
    remaining = [site for site in range(n) if site not in support]
    order = selected + remaining
    selected_dimensions = [dimensions[site] for site in selected]
    expected = math.prod(selected_dimensions)
    assert operator.shape == (expected, expected)
    reordered = np.kron(operator, np.eye(2 ** len(remaining)))
    current_dimensions = [dimensions[site] for site in order]
    inverse = np.argsort(order)
    axes = list(inverse) + [len(order) + int(site) for site in inverse]
    return reordered.reshape(current_dimensions * 2).transpose(axes).reshape(
        math.prod(dimensions), math.prod(dimensions)
    )


def spin_operators(n, aux_dim=1):
    physical = [
        sum(kron_all([p if site == chosen else I2 for site in range(n)])
            for chosen in range(n)) / 2
        for p in PAULI
    ]
    spins = [np.kron(operator, np.eye(aux_dim)) for operator in physical]
    casimir = sum(operator @ operator for operator in spins)
    return spins, casimir


def replace_site_by_maximally_mixed(rho, n, site, aux_dim=1):
    """Partial-trace replacement, independent of the Pauli-jump implementation."""
    dimensions = [2] * n + [aux_dim]
    rest = [index for index in range(n + 1) if index != site]
    order = [site] + rest
    axes = order + [index + n + 1 for index in order]
    rest_dimension = rho.shape[0] // 2
    permuted = rho.reshape(dimensions * 2).transpose(axes).reshape(
        2, rest_dimension, 2, rest_dimension
    )
    reduced = np.trace(permuted, axis1=0, axis2=2)
    replacement = np.kron(I2 / 2, reduced)
    current_dimensions = [dimensions[index] for index in order]
    inverse = np.argsort(order)
    inverse_axes = list(inverse) + [index + n + 1 for index in inverse]
    return replacement.reshape(current_dimensions * 2).transpose(inverse_axes).reshape(rho.shape)


def depolarization(rho, n, kappa=1.0, aux_dim=1):
    return kappa * sum(
        replace_site_by_maximally_mixed(rho, n, site, aux_dim) - rho
        for site in range(n)
    )


def finite_depolarizing_channel(rho, n, t, kappa=1.0, aux_dim=1):
    answer = rho.copy()
    contraction = np.exp(-kappa * t)
    for site in range(n):
        answer = contraction * answer + (1 - contraction) * replace_site_by_maximally_mixed(
            answer, n, site, aux_dim
        )
    return answer


def dissipator_adjoint(jump, observable):
    square = jump.conj().T @ jump
    return jump.conj().T @ observable @ jump - (square @ observable + observable @ square) / 2


def random_state(dimension):
    factor = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(size=(dimension, dimension))
    rho = factor @ factor.conj().T
    return rho / np.trace(rho)


def qfi(rho, generator):
    eigenvalues, vectors = np.linalg.eigh((rho + rho.conj().T) / 2)
    transformed = vectors.conj().T @ generator @ vectors
    denominator = eigenvalues[:, None] + eigenvalues[None, :]
    coefficient = np.divide(
        (eigenvalues[:, None] - eigenvalues[None, :]) ** 2,
        denominator,
        out=np.zeros_like(denominator),
        where=denominator > 1e-13,
    )
    return float(2 * np.sum(coefficient * np.abs(transformed) ** 2).real)


def sld(rho, generator):
    eigenvalues, vectors = np.linalg.eigh((rho + rho.conj().T) / 2)
    derivative = -1j * (generator @ rho - rho @ generator)
    transformed = vectors.conj().T @ derivative @ vectors
    denominator = eigenvalues[:, None] + eigenvalues[None, :]
    coefficients = np.divide(2 * transformed, denominator, out=np.zeros_like(transformed), where=denominator > 1e-13)
    return vectors @ coefficients @ vectors.conj().T


def fixed_measurement_fi(rho, generator, witness):
    _, vectors = np.linalg.eigh((witness + witness.conj().T) / 2)
    derivative = -1j * (generator @ rho - rho @ generator)
    probabilities = np.diag(vectors.conj().T @ rho @ vectors).real
    derivatives = np.diag(vectors.conj().T @ derivative @ vectors).real
    return float(np.sum(np.divide(derivatives ** 2, probabilities, out=np.zeros_like(probabilities), where=probabilities > 1e-13)))


def evolve(rho, action, adjoint_action, duration):
    dimension = rho.shape[0]

    def forward(vector):
        return action(np.asarray(vector).reshape(dimension, dimension)).reshape(-1)

    def backward(vector):
        return adjoint_action(np.asarray(vector).reshape(dimension, dimension)).reshape(-1)

    linear = LinearOperator((dimension ** 2, dimension ** 2), matvec=forward, rmatvec=backward, dtype=complex)
    result = expm_multiply(duration * linear, rho.reshape(-1), traceA=0).reshape(rho.shape)
    return (result + result.conj().T) / 2


def cat_formula(n, m, polarization):
    a = np.arctanh(polarization)
    return sum(
        math.comb(m, down)
        * ((1 - polarization) / 2) ** down
        * ((1 + polarization) / 2) ** (m - down)
        * np.tanh(a * (m - 2 * down)) ** 2
        * ((m - 2 * down) ** 2 + n - m)
        for down in range(m + 1)
    )


def cat_state(n, m, polarization):
    dimension = 2 ** n
    tau = np.diag([(1 + polarization) / 2, (1 - polarization) / 2])
    prepared = kron_all([tau] * m + [I2 / 2] * (n - m))
    pauli_string = kron_all([PAULI[0]] * n)
    unitary = (np.eye(dimension) - 1j * pauli_string) / np.sqrt(2)
    return prepared, unitary @ prepared @ unitary.conj().T, pauli_string


def check_noise_and_auxiliary():
    largest_residual = 0.0
    largest_qfi_ratio = 0.0
    cases = 0
    for n in range(1, 7):
        spins, casimir = spin_operators(n)
        identity = np.eye(2 ** n)
        noise_adjoint = sum(
            dissipator_adjoint(kron_all([p if i == site else I2 for i in range(n)]), casimir)
            for site in range(n) for p in PAULI
        ) / 4
        residual = np.linalg.norm(noise_adjoint + 2 * (casimir - 3 * n * identity / 4))
        assert residual < ATOL
        largest_residual = max(largest_residual, float(residual))
    for n, aux_dim in ((1, 2), (2, 3), (3, 2), (4, 2)):
        spins, casimir = spin_operators(n, aux_dim)
        for _ in range(3):
            rho = random_state(2 ** n * aux_dim)
            x = float(np.trace(rho @ casimir).real)
            drift = float(np.trace(depolarization(rho, n, aux_dim=aux_dim) @ casimir).real)
            residual = abs(drift + 2 * (x - 3 * n / 4))
            assert residual < ATOL
            for t in (0.03, 0.4, 1.7):
                output = finite_depolarizing_channel(rho, n, t, aux_dim=aux_dim)
                actual = float(np.trace(output @ casimir).real)
                expected = 3 * n / 4 + (x - 3 * n / 4) * np.exp(-2 * t)
                assert abs(actual - expected) < ATOL
            generator = (spins[0] + 2 * spins[1] - spins[2]) / np.sqrt(6)
            actual_qfi = qfi(rho, generator)
            assert actual_qfi <= min(4 * x, n ** 2) + ATOL
            largest_qfi_ratio = max(largest_qfi_ratio, actual_qfi / max(4 * x, 1e-15))
            largest_residual = max(largest_residual, residual)
            cases += 1

        # A maximally entangled physical/reference pair is a deliberately nonproduct test.
        if aux_dim == 2:
            vector = np.zeros(2 ** n * 2, dtype=complex)
            vector[0], vector[2 ** n * 2 - 1] = 1 / np.sqrt(2), 1 / np.sqrt(2)
            rho = np.outer(vector, vector.conj())
            x = float(np.trace(rho @ casimir).real)
            assert qfi(rho, spins[2]) <= 4 * x + ATOL

        # Arbitrary protected-auxiliary couplings are free only when they commute with C.
        aux_h = np.diag(np.arange(aux_dim))
        physical_sz = spin_operators(n)[0][2]
        hamiltonian = np.kron(physical_sz @ physical_sz, aux_h)
        auxiliary_jump = np.ones((aux_dim, aux_dim), dtype=complex) / aux_dim
        jump = (spins[0] - 1j * spins[1]) @ np.kron(np.eye(2 ** n), auxiliary_jump)
        assert np.linalg.norm(hamiltonian @ casimir - casimir @ hamiltonian) < ATOL
        assert np.linalg.norm(jump @ casimir - casimir @ jump) < ATOL
        free_drift = 1j * (hamiltonian @ casimir - casimir @ hamiltonian) + dissipator_adjoint(jump, casimir)
        assert np.linalg.norm(free_drift) < ATOL

        # Noncommuting nonlinear free processing, interleaved with physical noise,
        # must leave the exact elapsed-noise-time moment law unchanged.
        initial = random_state(2 ** n * aux_dim)
        state = initial.copy()
        initial_x = float(np.trace(initial @ casimir).real)
        elapsed = 0.0
        free_unitary = expm(-0.17j * hamiltonian)
        for duration in (0.03, 0.2, 0.6):
            state = finite_depolarizing_channel(state, n, duration, aux_dim=aux_dim)
            state = free_unitary @ state @ free_unitary.conj().T
            elapsed += duration
            expected = 3 * n / 4 + (initial_x - 3 * n / 4) * np.exp(-2 * elapsed)
            assert abs(np.trace(state @ casimir).real - expected) < ATOL
    return {"noise_identity_N": [1, 6], "density_matrix_auxiliary_cases": cases,
            "maximum_identity_residual": largest_residual, "largest_tested_QFI_over_4C": largest_qfi_ratio}


def check_repair():
    cases = 0
    largest_leibniz_residual = 0.0
    largest_young_eigenvalue = -np.inf
    for n, aux_dim, support in ((2, 2, (0,)), (3, 2, (0, 2)), (4, 1, (1, 3)), (4, 2, (0, 2, 3))):
        spins, casimir = spin_operators(n, aux_dim)
        local_dimension = 2 ** len(support) * aux_dim
        for _ in range(4):
            raw_h = RNG.normal(size=(local_dimension, local_dimension)) + 1j * RNG.normal(size=(local_dimension, local_dimension))
            local_h = (raw_h + raw_h.conj().T) / 2
            local_h /= np.linalg.norm(local_h, 2)
            local_jump = RNG.normal(size=(local_dimension, local_dimension)) + 1j * RNG.normal(size=(local_dimension, local_dimension))
            local_jump /= np.linalg.norm(local_jump, 2)
            hamiltonian = embed(local_h, support, n, aux_dim)
            jump = embed(local_jump, support, n, aux_dim)
            support_size = len(support)
            budget = support_size * (np.linalg.norm(local_h, 2) + np.linalg.norm(local_jump, 2) ** 2)
            derivative = 1j * (hamiltonian @ casimir - casimir @ hamiltonian) + dissipator_adjoint(jump, casimir)
            for spin in spins:
                commutator = spin @ jump - jump @ spin
                lhs = dissipator_adjoint(jump, spin @ spin)
                a = dissipator_adjoint(jump, spin)
                rhs = spin @ a + a @ spin + commutator.conj().T @ commutator
                residual = float(np.linalg.norm(lhs - rhs))
                assert residual < ATOL
                largest_leibniz_residual = max(largest_leibniz_residual, residual)
                a_total = 1j * (hamiltonian @ spin - spin @ hamiltonian) + a
                assert np.linalg.norm(a_total, 2) <= budget + ATOL
            for kappa in (0.2, 1.0, 5.0):
                upper = kappa * casimir + (3 * budget ** 2 / kappa + 3 * support_size * budget) * np.eye(casimir.shape[0])
                maximum = float(np.linalg.eigvalsh((derivative - upper + (derivative - upper).conj().T) / 2).max())
                assert maximum <= ATOL
                largest_young_eigenvalue = max(largest_young_eigenvalue, maximum)
            for _ in range(3):
                rho = random_state(casimir.shape[0])
                x = float(np.trace(rho @ casimir).real)
                actual = float(np.trace(rho @ derivative).real)
                assert actual <= 2 * np.sqrt(3) * budget * np.sqrt(x) + 3 * support_size * budget + ATOL
            cases += 1
    return {"operator_cases_with_noncontiguous_support_and_auxiliary": cases,
            "maximum_Leibniz_residual": largest_leibniz_residual,
            "largest_Young_operator_excess_eigenvalue": largest_young_eigenvalue}


def check_cat():
    cases = 0
    largest_residual = 0.0
    smallest_lower_ratio = np.inf
    for n in range(1, 7):
        spins, casimir = spin_operators(n)
        for m in range(1, n + 1):
            for polarization in (0.2, 0.5, 0.8):
                _, rho, pauli_string = cat_state(n, m, polarization)
                assert np.linalg.norm(pauli_string @ casimir - casimir @ pauli_string) < ATOL
                actual = qfi(rho, spins[2])
                expected = cat_formula(n, m, polarization)
                residual = abs(actual - expected)
                assert residual < ATOL
                assert actual <= n + polarization ** 2 * m * (m - 1) + ATOL
                if polarization <= 0.5:
                    assert actual >= polarization ** 4 * (n + m ** 2) - ATOL
                if m == 1:
                    assert abs(actual - polarization ** 2 * n) < ATOL
                if polarization == 0.5:
                    assert actual >= (n + m ** 2) / 16 - ATOL
                    smallest_lower_ratio = min(smallest_lower_ratio, actual / (n + m ** 2))
                largest_residual = max(largest_residual, residual)
                cases += 1
    return {"spectral_vs_binomial_points": cases, "maximum_QFI_residual": largest_residual,
            "smallest_F_over_N_plus_m_squared_at_p_half": smallest_lower_ratio}


def check_finite_pulse():
    results = []
    p_floor = (1 - np.exp(-2)) / 2
    for n, m in ((1, 1), (2, 1), (3, 1), (3, 2), (4, 4)):
        spins, _ = spin_operators(n)
        kappa = 1.0
        omega = 2 * np.pi * kappa * n ** 3 / (p_floor ** 4 * (n + m ** 2))
        duration = np.pi / (4 * omega)
        total_duration = np.log(n + 2) / kappa
        pump_duration = total_duration - duration
        assert pump_duration >= 1 / kappa
        polarization = (1 - np.exp(-2 * kappa * pump_duration)) / 2
        assert polarization >= p_floor
        prepared, ideal, pauli_string = cat_state(n, m, polarization)
        ideal_f = qfi(ideal, spins[2])
        assert ideal_f >= p_floor ** 4 * (n + m ** 2) - ATOL
        hamiltonian = omega * pauli_string

        def action(rho):
            return -1j * (hamiltonian @ rho - rho @ hamiltonian) + depolarization(rho, n, kappa)

        def adjoint_action(observable):
            # The local depolarizing generator is self-adjoint in Hilbert-Schmidt inner product.
            return 1j * (hamiltonian @ observable - observable @ hamiltonian) + depolarization(observable, n, kappa)

        actual = evolve(prepared, action, adjoint_action, duration)
        distance = float(np.linalg.norm(actual - ideal, ord="nuc") / 2)
        conservative_distance = kappa * n * duration
        assert abs(np.trace(actual) - 1) < ATOL
        assert np.linalg.eigvalsh(actual).min() >= -ATOL
        assert distance <= conservative_distance + ATOL
        assert conservative_distance <= ideal_f / (8 * n ** 2) + ATOL
        witness = sld(ideal, spins[2])
        assert np.linalg.norm(witness, 2) <= n + ATOL
        attained_f = fixed_measurement_fi(actual, spins[2], witness)
        actual_f = qfi(actual, spins[2])
        assert attained_f >= 9 * ideal_f / 20 - ATOL
        assert attained_f <= actual_f + ATOL
        results.append({"N": n, "m": m, "Omega_over_kappa": omega, "duration_times_kappa": duration,
                        "total_preparation_time_times_kappa": total_duration,
                        "finite_pump_polarization": polarization,
                        "ideal_QFI": ideal_f, "actual_QFI": actual_f, "fixed_ideal_SLD_measurement_FI": attained_f,
                        "half_trace_distance": distance, "distance_upper_bound": conservative_distance})
    return results


def sector_cat_reset(n):
    """An explicit finite C-preserving reset map used only for the linear baseline."""
    spins, casimir = spin_operators(n)
    eigenvalues, vectors = np.linalg.eigh(casimir)
    two_j_labels = np.rint(np.sqrt(1 + 4 * eigenvalues) - 1).astype(int)
    sectors = []
    kraus = []
    lowering = spins[0] - 1j * spins[1]
    sz_diagonal = np.diag(spins[2]).real
    for two_j in sorted(set(two_j_labels)):
        j = two_j / 2
        selected = vectors[:, two_j_labels == two_j]
        projector = selected @ selected.conj().T
        support = np.flatnonzero(np.isclose(sz_diagonal, j))
        reduced = casimir[np.ix_(support, support)]
        weights, basis = np.linalg.eigh(reduced)
        candidates = np.flatnonzero(np.isclose(weights, j * (j + 1)))
        assert len(candidates) > 0
        highest = np.zeros((2 ** n, len(candidates)), dtype=complex)
        highest[support, :] = basis[:, candidates]
        lowest = highest.copy()
        weight_bases = [highest]
        for _ in range(two_j):
            lowest = lowering @ lowest
            lowest /= np.linalg.norm(lowest, axis=0)[None, :]
            weight_bases.append(lowest)
        cat_basis = highest if two_j == 0 else (highest + lowest) / np.sqrt(2)
        for weight_basis in weight_bases:
            operator = cat_basis @ weight_basis.conj().T
            assert np.linalg.norm(operator @ casimir - casimir @ operator) < ATOL
            kraus.append(operator)
        sectors.append((j, projector))

    assert np.linalg.norm(sum(operator.conj().T @ operator for operator in kraus) - np.eye(2 ** n)) < ATOL

    def channel(rho):
        return sum(operator @ rho @ operator.conj().T for operator in kraus)

    def adjoint(observable):
        return sum(operator.conj().T @ observable @ operator for operator in kraus)

    return channel, adjoint, sectors


def check_zero_repair_baseline():
    results = []
    for n in (1, 2, 3, 4):
        spins, casimir = spin_operators(n)
        channel, channel_adjoint, sectors = sector_cat_reset(n)
        dimension = 2 ** n
        assert np.linalg.norm(channel_adjoint(casimir) - casimir) < ATOL
        probe = random_state(dimension)
        assert np.linalg.norm(channel(channel(probe)) - channel(probe)) < ATOL
        gamma = 64 * n ** 2

        def action(rho):
            return gamma * (channel(rho) - rho) + depolarization(rho, n)

        # Directly solve the stationary linear equations rather than taking
        # a large-time numerical limit.
        generator_columns = []
        for index in range(dimension ** 2):
            unit = np.zeros(dimension ** 2, dtype=complex)
            unit[index] = 1
            generator_columns.append(action(unit.reshape(dimension, dimension)).reshape(-1))
        generator = np.column_stack(generator_columns)

        # Check the actual finite-time statement from maximally mixed sensors,
        # at t=1/kappa, in addition to the stationary consistency check below.
        finite = expm_multiply(generator, (np.eye(dimension) / dimension).reshape(-1)).reshape(dimension, dimension)
        finite = (finite + finite.conj().T) / 2
        finite_ideal = channel(finite)
        finite_ideal_f = qfi(finite_ideal, spins[2])
        finite_distance = float(np.linalg.norm(finite - finite_ideal, ord="nuc") / 2)
        finite_witness = sld(finite_ideal, spins[2])
        finite_attained = fixed_measurement_fi(finite, spins[2], finite_witness)
        assert abs(np.trace(finite @ casimir).real - 3 * n / 4) < ATOL
        assert finite_ideal_f >= n - ATOL
        assert finite_distance <= np.exp(-gamma) + 2 * n / gamma + ATOL
        assert finite_attained >= 9 * finite_ideal_f / 20 - ATOL

        linear = generator.copy()
        trace_row = np.eye(dimension).reshape(-1)
        linear[0, :] = trace_row
        rhs = np.zeros(dimension ** 2, dtype=complex)
        rhs[0] = 1
        state = np.linalg.solve(linear, rhs).reshape(dimension, dimension)
        state = (state + state.conj().T) / 2
        assert np.linalg.eigvalsh(state).min() > -ATOL
        assert np.linalg.norm(action(state)) < ATOL
        assert abs(np.trace(state @ casimir).real - 3 * n / 4) < ATOL
        ideal = channel(state)
        ideal_f = qfi(ideal, spins[2])
        explicit_f = sum(4 * j ** 2 * np.trace(projector @ state).real for j, projector in sectors)
        assert abs(ideal_f - explicit_f) < ATOL
        assert ideal_f >= n - ATOL
        distance = float(np.linalg.norm(state - ideal, ord="nuc") / 2)
        assert distance <= n / gamma + ATOL
        witness = sld(ideal, spins[2])
        assert np.linalg.norm(witness, 2) <= n + ATOL
        attained = fixed_measurement_fi(state, spins[2], witness)
        assert attained >= 9 * ideal_f / 20 - ATOL
        results.append({"N": n, "Gamma_over_kappa": gamma, "stationary_C": 3 * n / 4,
                        "finite_time_times_kappa": 1.0, "finite_time_QFI": qfi(finite, spins[2]),
                        "finite_time_fixed_SLD_measurement_FI": finite_attained,
                        "finite_time_half_trace_distance_to_sector_reset": finite_distance,
                        "ideal_sector_reset_QFI": ideal_f, "stationary_QFI": qfi(state, spins[2]),
                        "fixed_ideal_SLD_measurement_FI": attained, "half_trace_distance_to_sector_reset": distance})
    return results


def check_model_boundaries():
    # A singlet has zero global C but nonzero differential-signal QFI.
    spins, casimir = spin_operators(2)
    singlet_vector = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
    singlet = np.outer(singlet_vector, singlet_vector.conj())
    differential = (np.kron(PAULI[2], I2) - np.kron(I2, PAULI[2])) / 2
    assert abs(np.trace(singlet @ casimir)) < ATOL
    assert abs(qfi(singlet, differential) - 4) < ATOL

    # One-axis dephasing does not have the isotropic Casimir-loss identity.
    n = 4
    _, casimir = spin_operators(n)
    ghz_vector = np.zeros(2 ** n, dtype=complex)
    ghz_vector[0] = ghz_vector[-1] = 1 / np.sqrt(2)
    ghz = np.outer(ghz_vector, ghz_vector.conj())
    one_axis_drift = sum(
        np.trace(ghz @ dissipator_adjoint(kron_all([PAULI[2] if i == site else I2 for i in range(n)]), casimir)).real / 4
        for site in range(n)
    )
    isotropic_drift = np.trace(depolarization(ghz, n) @ casimir).real
    assert abs(one_axis_drift) < ATOL
    assert abs(isotropic_drift + 6) < ATOL
    return {"singlet_global_C": 0.0, "singlet_differential_QFI": 4.0,
            "four_spin_GHZ_one_axis_C_drift": float(one_axis_drift),
            "four_spin_GHZ_isotropic_C_drift": float(isotropic_drift)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="write the finite-check report to this exact path")
    arguments = parser.parse_args()
    report = {
        "scope": "Deterministic finite-dimensional numerical checks, not arbitrary-N proofs or a priority certification.",
        "noise_and_reference": check_noise_and_auxiliary(),
        "repair": check_repair(),
        "cat": check_cat(),
        "finite_pulse": check_finite_pulse(),
        "zero_repair_stationary_linear_baseline": check_zero_repair_baseline(),
        "model_boundary_counterexamples": check_model_boundaries(),
    }
    if arguments.json:
        arguments.json.parent.mkdir(parents=True, exist_ok=True)
        arguments.json.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    print("PASS: all finite checks satisfy the stated tolerances and scope.")


if __name__ == "__main__":
    main()
