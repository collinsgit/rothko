"""Transition probability functions.

Give a probability of state transition given current state energy, new state energy,
and the current temperature.

All functions take in the floats e, e_new, and temp. e and e_new should follow the same
distribution, but otherwise there are no conditions on the range of these values.
temp should be in the range (0, 1]. The returned float will be a probability,
thus it will fall in the range [0, 1].
"""

import numpy as np


def kirkpatrick(e: float, e_new: float, temp: float) -> float:
    if e_new < e:
        return 1.
    return np.e ** -((e_new - e) / temp)
