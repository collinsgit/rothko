"""Types used in general simulated annealing applications."""

from typing import Callable, TypeVar

State = TypeVar("State")
NeighborFunc = Callable[[State], State]
EnergyFunc = Callable[[State], float]
TransProbFunc = Callable[[float, float, float], float]
TemperatureFunc = Callable[[float], float]