"""Temperature value functions.

Take in the proportion of iterations remaining, with a domain of (0, 1]. Returns
a temperature value, which we constrain to (0, 1] for simplicity. The other constraint
is that the temperature function must be monotonically increasing with the remaining
proportion. This is to say that the temperature must decrease as simulation proceeds.
"""

from rothko.types import TemperatureFunc


def linear_temp(p: float) -> float:
    """Simply return the proportion of iterations remaining."""
    return p


def get_power_temp_func(power: float) -> TemperatureFunc:
    """Simple power-based temperature function creator."""

    def temp_func(p: float) -> float:
        return p ** power

    return temp_func
