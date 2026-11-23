"""Reproduce finite integer and floating-point passive sensing checks."""

from cmath import exp
from collections import defaultdict
from itertools import product
from math import comb, cos, isclose, pi, sin, sqrt, tau


def charges(sites, degree):
    """Return the binomial moments through the degree being sensed."""
    return tuple(sum(comb(site, k) for site in sites) for k in range(degree + 1))


def sector_spectra(sensor_count, degree):
    """Map lower-moment sectors to bitsets of attainable signal charges."""
    spectra = {(0,) * degree: 1}
    for site in range(sensor_count):
        low = tuple(comb(site, k) for k in range(degree))
        signal = comb(site, degree)
        updated = defaultdict(int, spectra)
        for sector, bits in spectra.items():
            occupied = tuple(a + b for a, b in zip(sector, low))
            updated[occupied] |= bits << signal
        spectra = updated
    return dict(spectra)


def longest_run(bits):
    """Return the start and length of the longest consecutive support."""
    width = 1
    candidates = [bits]
    while (doubled := candidates[-1] & (candidates[-1] >> width)):
        candidates.append(doubled)
        width *= 2

    valid_starts = candidates.pop()
    extension = width // 2
    for valid_extensions in reversed(candidates):
        extended_starts = valid_starts & (valid_extensions >> width)
        if extended_starts:
            valid_starts = extended_starts
            width += extension
        extension //= 2
    start = (valid_starts & -valid_starts).bit_length() - 1
    return start, width


def spectrum_summary(sensor_count, degree):
    spectra = sector_spectra(sensor_count, degree)
    diameter = max(
        bits.bit_length() - (bits & -bits).bit_length()
        for bits in spectra.values()
    )
    length = max(longest_run(bits)[1] for bits in spectra.values())
    return diameter, length


def verify_integer_spectra():
    """Cross-check the recurrence against direct enumeration on small arrays."""
    for degree in (2, 3):
        brute_force = defaultdict(int)
        for occupation in product((0, 1), repeat=7):
            sites = [j for j, occupied in enumerate(occupation) if occupied]
            *sector, q = charges(sites, degree)
            brute_force[tuple(sector)] |= 1 << q
        assert sector_spectra(7, degree) == brute_force
        for bits in brute_force.values():
            start, length = longest_run(bits)
            support = f"{bits:b}"[::-1].split("0")
            assert length == max(map(len, support))
            run_mask = (1 << length) - 1
            assert ((bits >> start) & run_mask) == run_mask

    cases = [
        (8, 2, 16, 3),
        (12, 2, 54, 29),
        (16, 2, 128, 87),
        (24, 2, 432, 361),
        (32, 2, 1024, 919),
        (16, 3, 140, 1),
        (20, 3, 384, 2),
    ]
    for n, d, expected_diameter, expected_run in cases:
        diameter, run = spectrum_summary(n, d)
        assert (diameter, run) == (expected_diameter, expected_run)
        print(
            f"Degree {d:>2}, {n:>2} sensors: maximum diameter {diameter:>4}, "
            f"longest run {run:>4}"
        )


def encoded_sites(a, b):
    """Output the sites occupied by the eight-qubit basis encoder."""
    occupation = (1 ^ b, b, a ^ b, 1 ^ a, 1 ^ a ^ b, a, 1 ^ b, b)
    return tuple(j for j, value in enumerate(occupation) if value)


def verify_eight_sensor_receiver():
    addresses = ((0, 0), (0, 1), (1, 0), (1, 1))
    codewords = tuple(encoded_sites(a, b) for a, b in addresses)
    assert len(set(codewords)) == 4
    assert tuple((int(5 in w), int(7 in w)) for w in codewords) == addresses
    assert codewords[:3] == ((0, 3, 4, 6), (1, 2, 3, 7), (0, 2, 5, 6))
    code_charges = tuple(charges(sites, 2) for sites in codewords[:3])
    assert code_charges == ((4, 13, 24), (4, 13, 25), (4, 13, 26))

    # Ry(pi/3) on the first address bit, then a zero-controlled Ry on
    # the second with half-angle cosine 1/sqrt(3). The fourth amplitude vanishes.
    amplitudes = (
        cos(pi / 6) / sqrt(3),
        cos(pi / 6) * sqrt(2 / 3),
        sin(pi / 6),
    )
    sine_amplitudes = tuple(sqrt(1 / 2) * sin(pi * (q + 1) / 4) for q in range(3))
    assert all(isclose(a, b, abs_tol=1e-14) for a, b in zip(amplitudes, sine_amplitudes))

    # Each residue is an integer Fourier frequency. The four-point sum
    # for the first circular harmonic retains exactly the unit differences.
    assert all(
        ((p - q - 1) % 4 == 0) == (p - q == 1)
        for p in range(3)
        for q in range(3)
    )

    target_risk = 1 - 1 / sqrt(2)
    max_error = 0.0
    for step in range(257):
        phi = tau * step / 257
        alpha = tau * ((7 * step) % 257) / 257
        beta = tau * ((23 * step) % 257) / 257
        after_exposure = [
            a * exp(1j * (w * alpha + s * beta + q * phi))
            for a, (w, s, q) in zip(amplitudes, code_charges)
        ]
        probabilities = []
        risk = 0.0
        for reading in range(4):
            estimate = tau * reading / 4
            # The inverse encoding maps each phase-bearing codeword back to
            # its two-bit address. Read that address in the inverse QFT basis.
            amplitude = sum(
                value * exp(-1j * address * estimate)
                for address, value in enumerate(after_exposure)
            ) / 2
            probability = abs(amplitude) ** 2
            probabilities.append(probability)
            risk += probability * (1 - cos(estimate - phi))
        assert isclose(sum(probabilities), 1.0, rel_tol=0.0, abs_tol=1e-13)
        max_error = max(max_error, abs(risk - target_risk))

    assert max_error < 1e-13
    print(f"Eight-sensor Fourier risk: {target_risk:.12f}, maximum sample error {max_error:.2e}")


def signed_stencil(shifts):
    """Expand a product of (1 - z**step) with unique subset sums."""
    stencil = {0: 1}
    for shift in shifts:
        shifted = {site + shift: -sign for site, sign in stencil.items()}
        assert stencil.keys().isdisjoint(shifted)
        stencil.update(shifted)
    return stencil


def signed_gap(stencil, degree, offset):
    moments = tuple(
        sum(sign * comb(site + offset, order) for site, sign in stencil.items())
        for order in range(degree + 1)
    )
    assert moments[:-1] == (0,) * degree
    return moments[-1]


def balanced_shifts(degree, exponent):
    base = degree * (degree - 1) // 2
    offset, remainder = divmod(exponent - base, degree)
    assert offset >= 0
    return [2 ** (offset + i + (i >= degree - remainder)) for i in range(degree)]


def check_bank(degree, coarse_count):
    """Pack fine dyadic and coarse stencils and check all encoded charges."""
    occupied = set()

    def check_block(stencil, offset, expected_gap):
        support = {offset + site for site in stencil}
        assert occupied.isdisjoint(support)
        occupied.update(support)
        assert abs(signed_gap(stencil, degree, offset)) == expected_gap

    base = degree * (degree - 1) // 2
    two = signed_stencil([2**i for i in range(degree)])
    three = signed_stencil([3**i for i in range(degree)])
    a, b = 2**base, 3**base
    coefficient_two = pow(a, -1, b)
    coefficient_three = (1 - coefficient_two * a) // b
    unit_gap = coefficient_two * a + coefficient_three * b
    assert unit_gap == 1

    bank_gaps = []
    offset = 0
    coarse_gap = a * coarse_count**degree
    for exponent in range(coarse_gap.bit_length() - 1):
        gap = 2**exponent
        if exponent < base:
            # Each unit gadget is a collection of disjoint base stencils.
            # A negative coefficient swaps the two logical words of its copies.
            for stencil, coefficient, order_gap in (
                (two, coefficient_two, a),
                (three, coefficient_three, b),
            ):
                for _ in range(gap * abs(coefficient)):
                    check_block(stencil, offset, order_gap)
                    offset += max(stencil) + 1
        else:
            stencil = signed_stencil(balanced_shifts(degree, exponent))
            check_block(stencil, offset, gap)
            offset += max(stencil) + 1
        bank_gaps.append(gap)

    coarse = signed_stencil([coarse_count * 2**i for i in range(degree)])
    for translate in range(coarse_count - 1):
        check_block(coarse, offset + translate, coarse_gap)

    fine_charges = {0}
    for gap in bank_gaps:
        fine_charges |= {q + gap for q in fine_charges}
    assert fine_charges == set(range(coarse_gap))
    all_charges = {
        q + height * coarse_gap
        for height in range(coarse_count)
        for q in fine_charges
    }
    assert all_charges == set(range(coarse_count * coarse_gap))
    print(f"Degree {degree} packed stencil example: {len(all_charges)} consecutive charges")


def verify_stencils():
    for degree in range(2, 8):
        base = degree * (degree - 1) // 2
        for exponent in range(base, base + 18):
            stencil = signed_stencil(balanced_shifts(degree, exponent))
            assert abs(signed_gap(stencil, degree, offset=9)) == 2**exponent

    check_bank(degree=2, coarse_count=8)
    check_bank(degree=3, coarse_count=4)


def verify_mirror_moves():
    """Check the exact quadratic bulk span and its maximum step size."""
    for pair_count in (1, 2, 7, 15):
        bulk_size = 4 * pair_count
        initial_radii = list(range(pair_count))

        def moments(radii):
            sites = [
                site
                for r in radii
                for site in (bulk_size // 2 - 1 - r, bulk_size // 2 + r)
            ]
            return charges(sites, 2)

        radii = initial_radii.copy()
        weight, first, initial_signal = moments(radii)
        previous_signal = initial_signal
        for i in range(pair_count - 1, -1, -1):
            for _ in range(pair_count):
                radii[i] += 1
                assert radii == sorted(set(radii))
                new_weight, new_first, signal = moments(radii)
                assert (new_weight, new_first) == (weight, first)
                assert 0 < signal - previous_signal <= bulk_size
                previous_signal = signal
        assert previous_signal - initial_signal == 2 * pair_count**3
    print("Quadratic mirror moves preserve lower moments and attain the exact bulk span.")


def main():
    verify_integer_spectra()
    verify_eight_sensor_receiver()
    verify_stencils()
    verify_mirror_moves()
    print("All finite checks passed.")


if __name__ == "__main__":
    main()
