"""Generalized code to perform simulated annealing."""

import random
from typing import List

from rothko.types import (
    State,
    NeighborFunc,
    EnergyFunc,
    TransProbFunc,
    TemperatureFunc,
)
from rothko.transition_probabilities import kirkpatrick


def anneal(
    s_0: State,
    neighbor: NeighborFunc,
    energy: EnergyFunc,
    trans_prob: TransProbFunc,
    temp: TemperatureFunc,
    max_iters: int = 100,
) -> State:
    best_state: State = s_0
    best_energy: float = energy(s_0)
    s: State = s_0

    for i in range(max_iters):
        t = temp(1. - i / max_iters)
        s_new = neighbor(s)

        new_energy = energy(s_new)
        if random.random() < trans_prob(best_energy, new_energy, t):
            s = s_new

            if new_energy < best_energy:
                best_state = s
                best_energy = new_energy

    return best_state
