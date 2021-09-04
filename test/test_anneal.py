"""Tests for generalized simulated annealing."""

from rothko.anneal import anneal


def test_anneal():
    assert anneal(3) == 4
