from __future__ import annotations
from typing import Callable


class Function:
    function: Callable[[float], float]

    def __init__(self, function: Callable[[float], float]) -> None:
        self.function = function

    def value(self, x: float) -> float:
        return self.function(x)

    def derivative_range(self, x1: float, x2: float) -> float:
        y1 = self.value(x1)
        y2 = self.value(x2)
        derivative = (y2 - y1) / (x2 - x1)
        return derivative

    def derivative_left(self, x: float, d: ):