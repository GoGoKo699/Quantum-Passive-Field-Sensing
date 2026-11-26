"""Check the translated-stencil receiver and its finite curvature benchmark."""

from cmath import exp
from fractions import Fraction
from itertools import product
from math import cos, factorial, isclose, pi, sin, sqrt, tau
from random import Random


def stencil_words(degree, stride, start):
    """Return the negative and positive occupation words of a finite difference."""
    words = ([], [])
    for pattern in product((0, 1), repeat=degree):
        site = start + stride * sum(bit * 2**i for i, bit in enumerate(pattern))
        positive = (degree - sum(pattern)) % 2 == 0
        words[positive].append(site)
    return tuple(tuple(word) for word in words)


def verify_translated_stencils():
    sensor_count = 513
    for degree in range(1, 7):
        stride = sensor_count // 2**degree
        coords = [Fraction(j, sensor_count - 1) for j in range(sensor_count)]
        gap = (
            factorial(degree)
            * Fraction(stride, sensor_count - 1) ** degree
            * 2 ** (degree * (degree - 1) // 2)
        )
        used = set()
        for start in range(stride):
            negative, positive = stencil_words(degree, stride, start)
            support = set(negative).union(positive)
            assert len(support) == 2**degree and used.isdisjoint(support)
            used.update(support)
            moments = tuple(
                sum(coords[j] ** power for j in positive)
                - sum(coords[j] ** power for j in negative)
                for power in range(degree + 1)
            )
            assert moments == (0,) * degree + (gap,)
        assert used == set(range(stride * 2**degree))
    print("Translated-stencil packing and physical moments passed for degrees 1–6.")


def fourier_distribution(state, bins):
    """Return the output phasors and Born probabilities of the finite readout."""
    distribution = []
    for reading in range(bins):
        angle = tau * reading / bins
        amplitude = sum(
            value * exp(-1j * q * angle) for q, value in enumerate(state)
        )
        distribution.append((exp(1j * angle), abs(amplitude) ** 2 / bins))
    return distribution


def verify_fourier():
    rng = Random(73)
    max_error = 0.0
    for block_size in range(1, 51):
        length = block_size + 1
        bins = 1 << length.bit_length()
        contrast = cos(pi / (length + 1))
        amplitudes = [
            sqrt(2 / (length + 1)) * sin(pi * (q + 1) / (length + 1))
            for q in range(length)
        ]
        weights = [a * b for a, b in zip(amplitudes, amplitudes[1:])]
        assert isclose(sum(weights), contrast, abs_tol=1e-14)
        assert all(
            ((q - r - 1) % bins == 0) == (q - r == 1)
            for q in range(length)
            for r in range(length)
        )
        for _ in range(4):
            angle = rng.uniform(-2.0, 2.0)
            # The signed errors can differ on every stencil, even within a group.
            errors = [rng.uniform(-0.07, 0.07) for _ in range(block_size)]
            phase = 0.0
            state = [amplitudes[0]]
            for amplitude, error in zip(amplitudes[1:], errors):
                phase += angle + error
                state.append(amplitude * exp(1j * phase))
            distribution = fourier_distribution(state, bins)
            assert isclose(sum(p for _, p in distribution), 1, abs_tol=1e-12)
            moment = sum(phasor * p for phasor, p in distribution)
            mode = sum(w * exp(1j * error) for w, error in zip(weights, errors))
            max_error = max(max_error, abs(moment - exp(1j * angle) * mode))
            error_bound = max(map(abs, errors))
            assert abs(moment / contrast - exp(1j * angle)) <= error_bound + 1e-12
            variance = 1 / contrast**2 - abs(moment / contrast)**2
            assert variance <= 1 / contrast**2 - 1 + sin(error_bound)**2 + 1e-12
    assert max_error < 1e-12
    print(f"Fourier moment matched 200 direct Born calculations, max error {max_error:.2e}.")


def verify_product_preparation():
    for degree in (1, 2, 3):
        sensor_count = 2**degree
        negative, positive = stencil_words(degree, stride=1, start=0)
        codewords = [sum(1 << site for site in word) for word in (negative, positive)]
        coords = [j / (sensor_count - 1) for j in range(sensor_count)]
        tolerance = 0.02
        errors = [tolerance * sin(j * sqrt(2)) for j in range(sensor_count)]
        target = 0.8
        phases = [
            target * x**degree + sum((a + 1) * x**a for a in range(degree)) + error
            for x, error in zip(coords, errors)
        ]
        amplitude = 2 ** (-sensor_count / 2)
        after_exposure = [
            amplitude * exp(1j * sum(
                phase for site, phase in enumerate(phases) if state & (1 << site)
            ))
            for state in range(2**sensor_count)
        ]
        projected = [after_exposure[word] for word in codewords]
        success = sum(abs(a)**2 for a in projected)
        assert isclose(success, 2 ** (1 - sensor_count), abs_tol=1e-15)
        # Failures contribute zero. The four readout probabilities sum to the
        # acceptance probability before dividing by success times the contrast.
        distribution = fourier_distribution(projected, bins=4)
        assert isclose(sum(p for _, p in distribution), success, abs_tol=1e-15)
        mean = sum(phasor * p for phasor, p in distribution) / (success / 2)
        gap = factorial(degree) * 2 ** (degree * (degree - 1) // 2)
        gap /= (sensor_count - 1) ** degree
        shift = sum(errors[j] for j in positive) - sum(errors[j] for j in negative)
        assert abs(mean - exp(1j * (gap * target + shift))) < 1e-12
    print("Product-state projection preserves the conditional Fourier moment and charges failures.")


def verify_curvature_benchmark():
    sensor_count, depth = 1024, 128
    stride, block_size = sensor_count // 4, depth // 4
    group_count = stride // block_size
    assert 4 * block_size * group_count == sensor_count
    tolerance = Fraction(1, 100)
    gap = Fraction(4 * stride**2, (sensor_count - 1)**2)
    # The target interval is [-1, 1]. Use pi**2 < 10 and elementary
    # sine/cosine bounds throughout to retain exact rational inequalities.
    angle_squared = Fraction(10, (block_size + 2)**2)
    tangent_squared = angle_squared / (1 - angle_squared / 2)**2
    shift_squared = (4 * tolerance)**2
    cosine_lower = 1 - gap**2 / 2
    upper = (
        (tangent_squared + shift_squared) / group_count + shift_squared
    ) / (gap * cosine_lower)**2

    centered_squares = [
        (Fraction(j, sensor_count - 1) - Fraction(1, 2))**2
        for j in range(sensor_count)
    ]
    mean = sum(centered_squares) / sensor_count
    residual_norm = sum((value - mean)**2 for value in centered_squares)
    lower = 1 / (10 + residual_norm)
    assert upper < Fraction(4911, 100_000) < Fraction(6364, 100_000) < lower
    print(
        f"Curvature benchmark: robust upper {float(upper):.9f}, "
        f"ideal-phase separable lower {float(lower):.9f}."
    )


def verify_geometry_warp():
    tolerance = 0.005
    for degree in (2, 3, 6):
        for orientation in (-1, 1):
            gradient, target = 0.8 * orientation, 0.6 * orientation
            for direction in (-1, 1):
                shift = direction * tolerance / 2

                def perturbed(x):
                    return (gradient - shift) * x + (target + shift) * x**degree

                assert isclose(perturbed(0), 0, abs_tol=1e-15)
                assert isclose(perturbed(1), gradient + target, abs_tol=1e-15)
                previous = -1.0
                for j in range(129):
                    x = j / 128
                    nominal = gradient * x + target * x**degree
                    lo, hi = 0.0, 1.0
                    for _ in range(52):
                        mid = (lo + hi) / 2
                        if orientation * (perturbed(mid) - nominal) < 0:
                            lo = mid
                        else:
                            hi = mid
                    actual = (lo + hi) / 2
                    assert previous < actual and abs(actual - x) <= tolerance
                    assert isclose(perturbed(actual), nominal, abs_tol=1e-14)
                    if j in (0, 128):
                        assert isclose(actual, x, abs_tol=1e-15)
                    previous = actual
    print("Geometry warp passed fixed-endpoint, ordering and phase checks.")


def main():
    verify_translated_stencils()
    verify_fourier()
    verify_product_preparation()
    verify_curvature_benchmark()
    verify_geometry_warp()
    print("All calibration checks passed.")


if __name__ == "__main__":
    main()
