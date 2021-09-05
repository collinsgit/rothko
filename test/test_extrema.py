"""Tests for simulated annealing applications to extrema finding.

Generally, we avoid checking for whether the solution is correct, as simulated
annealing makes no such guarantees. Instead, we can check that the algorithm
returns a valid state and that it is at least as good as our initial state.
"""

import random

from rothko.applications.extrema import (
    Dimensions,
    get_val_at_dim,
    n_dimensional_minimizer,
    one_dimensional_minimizer,
)
from rothko.temperature import get_power_temp_func


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
    s = one_dimensional_minimizer(
        hills,
        temp=get_power_temp_func(4.0),
    )

    # check that the state is valid
    assert isinstance(s, int)
    assert 0 <= s < len(hills)

    # check that the new state is at least as good
    assert hills[s] <= hills[len(hills) // 2]


def test_n_dimensional_minimizer_small():
    """Test minima finding on a small 3 x 3 of ints"""
    hills = [
        [1, 2, 3],
        [3, 0, 1],
        [1, 0, -1],
    ]
    s = n_dimensional_minimizer(hills)

    # check that the state is valid
    assert len(s) == 2
    assert 0 <= s[0] < 3 and 0 <= s[1] < 3

    # check that the new state is at least as good
    assert get_val_at_dim(hills, s) <= 0


def _generate_space(bounds: Dimensions):
    if len(bounds) == 1:
        return [random.randint(-10000, 10000) for _ in range(bounds[0])]
    else:
        return [_generate_space(bounds[1:]) for _ in range(bounds[0])]


def test_n_dimensional_minimizer_large():
    """Test minima finding on a large, randomly generated 4 dimensional space."""
    bounds = [random.randint(10, 20) for _ in range(4)]
    hills = _generate_space(bounds)
    s_0 = [b // 2 for b in bounds]
    e_0 = get_val_at_dim(hills, s_0)

    s = n_dimensional_minimizer(hills)

    # check that the state is valid
    assert len(s) == 4
    for d, b in zip(s, bounds):
        assert 0 <= d < b

    # check that the new state is at least as good
    assert get_val_at_dim(hills, s) <= e_0
