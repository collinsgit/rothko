"""Tests for simulated annealing applications to extrema finding.

Generally, we avoid checking for whether the solution is correct, as simulated
annealing makes no such guarantees. Instead, we can check that the algorithm
returns a valid state and that it is at least as good as our initial state.
"""

import random

from rothko.applications.extrema import one_dimensional_minimizer


def test_one_dimensional_minimizer_simple():
    """Test minima finding on a small list of ints."""
    hills = [1, 2, 3, 4, 2, -1, 5]
    s = one_dimensional_minimizer(hills)

    # check that the state is valid
    assert isinstance(s, int)
    assert 0 <= s < len(hills)

    # check that the new state is at least as good
    assert hills[s] <= hills[len(hills) // 2]


def test_one_dimensional_minimzer_large():
    """Test minima finding on a large, random list of ints."""
    hills = list(range(1000))
    random.shuffle(hills)
    s = one_dimensional_minimizer(hills)

    # check that the state is valid
    assert isinstance(s, int)
    assert 0 <= s < len(hills)

    # check that the new state is at least as good
    assert hills[s] <= hills[len(hills) // 2]
