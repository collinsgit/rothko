"""Code to use simulated annealing to traverse a space and find extrema.

Generally this is a very poor use of simulated annealing, but it provides a
simple and understandable use case to begin with.
"""

import random
from typing import List

from rothko.anneal import anneal
from rothko.transition_probabilities import kirkpatrick


def one_dimensional_minimizer(hills: List[int]) -> int:
    s_0 = len(hills) // 2

    return anneal(
        s_0=s_0,
        neighbor=lambda s: random.randrange(len(hills)),
        energy=lambda s: hills[s],
        trans_prob=kirkpatrick,
        temp=lambda t: t
    )
