#!/usr/bin/env python3
"""Exhaustively falsify the candidate claims using the literal parallel rule.

Python 3.10+; standard library only. No network, random sampling, or paid API.
The simulator never calls the proposed block or optimization formulas.
"""
import argparse
import hashlib
import json
import platform
import sys
import time
from math import isqrt
from pathlib import Path


def simulate(n, blue, leak=None, trace=False):
    """One fixed vertex cannot force; it can still be colored.

    Every force in a round uses the SAME pre-round blue set. None means stuck.
    An integer bit mask records each labeled initial set exactly once.
    """
    full = (1 << n) - 1
    neighbors = [(1 << ((u - 1) % n)) | (1 << ((u + 1) % n))
                 for u in range(n)]
    leak_bit = 0 if leak is None else 1 << leak
    steps = 0
    history = [blue]
    while blue != full:
        additions = 0
        active = blue & ~leak_bit
        while active:
            bit = active & -active
            u = bit.bit_length() - 1
            active ^= bit
            white_neighbors = neighbors[u] & ~blue
            if white_neighbors and not (white_neighbors & (white_neighbors - 1)):
                additions |= white_neighbors
        if not additions:
            return (None, history) if trace else None
        blue |= additions
        steps += 1
        history.append(blue)
    return (steps, history) if trace else steps


def blocks(n, blue):
    """Find long initial blue runs, then intervening arcs, without dynamics."""
    bits = [(blue >> u) & 1 for u in range(n)]
    if all(bits):
        return []
    cut = bits.index(0)
    runs, current = [], []
    for j in range(1, n + 1):
        u = (cut + j) % n
        if bits[u]:
            current.append(u)
        else:
            if len(current) >= 2:
                runs.append(current)
            current = []
    result = []
    for i, run in enumerate(runs):
        a = run[-1]
        b = runs[(i + 1) % len(runs)][0]
        arc = []
        u = (a + 1) % n
        while u != b:
            arc.append(u)
            u = (u + 1) % n
        result.append({"left": a, "right": b, "vertices": arc,
                       "white_count": sum(1 - bits[v] for v in arc)})
    return result


def set_time_formula(n, blue):
    if blue == (1 << n) - 1:
        return 0
    arcs = blocks(n, blue)
    return max(a["white_count"] for a in arcs) if arcs else None


def optimum_time_formula(n, k):
    if k == n:
        return 0
    if k < 2:
        return None
    r = k // 2
    return (n - k + r - 1) // r


def ceil_div(a, b):
    return (a + b - 1) // b


def deadline_formula(n, t):
    return min(2 * ceil_div(n, t + 2),
               2 * ceil_div(n - 1, t + 2) + 1)


def throttle_formula(n):
    s = isqrt(8 * n)
    return s + (s * s < 8 * n) - 2


def construct(n, k):
    if k == n:
        return (1 << n) - 1
    if not 2 <= k < n:
        raise ValueError("Require 2 <= k <= n")
    whites = n - k
    r = min(k // 2, whites)
    lengths = [2] * r
    lengths[0] += k - 2 * r
    q, rem = divmod(whites, r)
    bits = []
    for i in range(r):
        bits.extend([1] * lengths[i])
        bits.extend([0] * (q + (i < rem)))
    if len(bits) != n or sum(bits) != k:
        raise AssertionError("Construction is malformed")
    return sum(bit << u for u, bit in enumerate(bits))


def run(max_n):
    started = time.perf_counter()
    count_sets = count_scenarios = count_size_optima = count_deadlines = 0
    rows = []
    for n in range(3, max_n + 1):
        optimum, witnesses = {}, {}
        worst_leak_witnesses = 0
        for blue in range(1 << n):
            # Literal dynamics for every possible, fixed, one-vertex leak.
            times = [simulate(n, blue, leak) for leak in range(n)]
            count_scenarios += n
            actual = None if None in times else max(times)
            predicted = set_time_formula(n, blue)
            if actual != predicted:
                raise AssertionError(("set-time", n, blue, actual, predicted, times))
            # Check the adversarial endpoint used by the lower-bound proof.
            arcs = blocks(n, blue)
            if arcs:
                largest = max(arcs, key=lambda a: a["white_count"])
                if times[largest["right"]] != predicted:
                    raise AssertionError(("worst-leak witness", n, blue, largest, times))
                worst_leak_witnesses += 1
            count_sets += 1
            k = blue.bit_count()
            if actual is not None and (k not in optimum or actual < optimum[k]):
                optimum[k], witnesses[k] = actual, blue
        for k in range(n + 1):
            if optimum.get(k) != optimum_time_formula(n, k):
                raise AssertionError(("fixed-k optimum", n, k, optimum.get(k)))
            count_size_optima += 1
        for t in range(n + 1):
            actual = min(k for k, time_ in optimum.items() if time_ <= t)
            if actual != deadline_formula(n, t):
                raise AssertionError(("deadline", n, t, actual))
            count_deadlines += 1
        throttle = min(k + time_ for k, time_ in optimum.items())
        if throttle != throttle_formula(n):
            raise AssertionError(("throttling", n, throttle))
        # The explicit general upper-bound construction, checked dynamically.
        for k in range(2, n + 1):
            blue = construct(n, k)
            times = [simulate(n, blue, leak) for leak in range(n)]
            expected = optimum_time_formula(n, k)
            if None in times or max(times) != expected:
                raise AssertionError(("construction", n, k, times))
        rows.append({"n": n, "time_by_seed_count": optimum,
                     "witness_masks": witnesses, "throttling": throttle,
                     "adversarial_endpoint_witnesses": worst_leak_witnesses})

    # Small model-discrimination controls; excluded from exhaustive-run counts.
    pair = (1 << 0) | (1 << 1)
    if simulate(6, pair) != 2 or simulate(6, pair, 0) != 4:
        raise AssertionError("Parallel/leak control")
    if simulate(6, 1 << 1) is not None:
        raise AssertionError("Deleting a seed must be distinguished from a leak")
    blue = pair | (1 << 3)
    singleton_time, singleton_trace = simulate(5, blue, 0, True)
    if singleton_time != 2:
        raise AssertionError("A singleton seed must not launch on its own")
    if simulate(3, pair, 2) != 1:
        raise AssertionError("An initially white leak must still be colorable")
    if simulate(6, (1 << 0) | (1 << 2) | (1 << 4), 0) is not None:
        raise AssertionError("No adjacent seeds must stall")
    if simulate(3, 7, 0) != 0:
        raise AssertionError("All-blue time must be zero")

    large_n, large_k = 100, 14
    large_blue = construct(large_n, large_k)
    large_times = [simulate(large_n, large_blue, leak) for leak in range(large_n)]
    if None in large_times or max(large_times) != 13:
        raise AssertionError("C100 witness")

    return {
        "status": "PASS",
        "version": "0.1",
        "runtime": {"python": sys.version.split()[0], "system": platform.system()},
        "scope": {"min_n": 3, "max_n": max_n,
                  "all_labeled_initial_sets": True, "all_fixed_vertex_leaks": True},
        "exhaustive_counts": {"initial_sets": count_sets,
                              "set_leak_scenarios": count_scenarios,
                              "size_optima_including_infeasible_sizes": count_size_optima,
                              "deadline_optima": count_deadlines},
        "rows": rows,
        "controls": {"parallel_no_leak_C6_pair": 2,
                     "fixed_leak_C6_pair": 4,
                     "deleted_seed_C6_pair": None,
                     "C5_singleton_mask": blue,
                     "C5_singleton_leak": 0,
                     "C5_singleton_time": singleton_time,
                     "C5_singleton_trace_masks": singleton_trace,
                     "white_leak_is_colorable": True,
                     "no_adjacent_seeds_stalls": True,
                     "all_blue_time_zero": True},
        "C100_witness": {"n": large_n, "k": large_k,
                         "mask": str(large_blue), "worst_time": max(large_times),
                         "time_by_leak": large_times,
                         "optimal_sum": throttle_formula(large_n)},
        "verification_seconds": time.perf_counter() - started,
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitations": ["Finite computation does not replace the general proof.",
                        "Author-side checks, not an independent external audit.",
                        "Windows execution is not certified by this Linux run.",
                        "No historical novelty is established by this run."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=14,
                        help="All n from 3 through this value; default 14")
    parser.add_argument("--output", type=Path,
                        help="Optional fresh JSON log; default does not modify the package")
    args = parser.parse_args()
    if not 3 <= args.max_n <= 22:
        parser.error("Require 3 <= --max-n <= 22; work grows exponentially")
    result = run(args.max_n)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "scope": result["scope"],
                      "counts": result["exhaustive_counts"],
                      "seconds": result["verification_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
