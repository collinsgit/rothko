"""Code to use simulated annealing to traverse a space and find extrema.

Generally this is a very poor use of simulated annealing, but it provides a
simple and understandable use case to begin with.
"""

import random
from typing import Any, List, Union

from rothko.anneal import anneal
from rothko.temperature import linear_temp
from rothko.transition_probabilities import kirkpatrick
from rothko.types import TemperatureFunc, TransProbFunc

Dimensions = List[int]
# We would like to include this recursive n-d space type, but it doesn't work with mypy
# NDimensionalSpace = Union[List[Union[int, float]], List["NDimensionalSpace"]]
NDimensionalSpace = List[Any]


def _get_random_neighbor(bounds: Dimensions) -> Dimensions:
    """Given n-dimensional space bounds, sample a random location."""
    if not bounds:
        return []
    return [random.randrange(bounds[0])] + _get_random_neighbor(bounds[1:])


def _get_adjacent_neighbor(dims: Dimensions, bounds: Dimensions) -> Dimensions:
    """Given n-dimensional location and space bounds, sample an adjacent location."""
    # select axis of variation
    new_dims = dims.copy()
    varying_axis = random.randrange(len(dims))

    # increment or decrement with equal likelihood
    if random.random() < 0.5:
        # decrement case
        if new_dims[varying_axis] > 0:
            new_dims[varying_axis] -= 1
        else:
            new_dims[varying_axis] += 1
    else:
        # increment case
        if new_dims[varying_axis] < bounds[varying_axis] - 1:
            new_dims[varying_axis] += 1
        else:
            new_dims[varying_axis] -= 1

    return new_dims


def one_dimensional_minimizer(
    hills: List[int],
    trans_prob: TransProbFunc = kirkpatrick,
    temp: TemperatureFunc = linear_temp,
) -> int:
    """Naive attempt to find minima of one dimensional input.

    Starts in the middle, but gets neighbor uniformly at random.
    (Note that this is absolutely worse than scanning the list)
    """
    # start in the middle
    s_0 = len(hills) // 2

    # try to minimize hill value, randomly select next state
    return anneal(
        s_0=s_0,
        neighbor=lambda s: _get_random_neighbor([len(hills)])[0],
        energy=lambda s: hills[s],
        trans_prob=trans_prob,
        temp=temp,
    )


def _get_n_dimensional_bounds(space: NDimensionalSpace) -> Dimensions:
    bounds = []
    while isinstance(space, List):
        bounds.append(len(space))
        space = space[0]

    return bounds


def get_val_at_dim(space: NDimensionalSpace, dims: Dimensions) -> Union[float, int]:
    for dim in dims:
        space = space[dim]

    assert isinstance(space, float) or isinstance(space, int)
    return space


def n_dimensional_minimizer(
    hills,
    trans_prob: TransProbFunc = kirkpatrick,
    temp: TemperatureFunc = linear_temp,
) -> Dimensions:
    """Attempts to find location of minima in N-dimensional input.

    Assumes that there is some locality to data, such that adjacent locations have
    similar values. Specifically, the neighbor function samples adjacent locations.
    """
    # get bounds
    bounds = _get_n_dimensional_bounds(hills)

    # start in the middle
    s_0 = [b // 2 for b in bounds]

    # traverse adjacent neighbors to find minimum energy point
    return anneal(
        s_0=s_0,
        neighbor=lambda s: _get_adjacent_neighbor(s, bounds),
        energy=lambda s: get_val_at_dim(hills, s),
        trans_prob=trans_prob,
        temp=temp,
    )
