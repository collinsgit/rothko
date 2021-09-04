"""Tests for generalized simulated annealing."""

from rothko.applications.extrema import one_dimensional_minimizer


def test_one_dimensional_minimizer():
    hills = [1, 2, 3, 4, 2, -1, 5]
    s = one_dimensional_minimizer(hills)

    assert isinstance(s, int)
    assert 0 <= s < len(hills)
