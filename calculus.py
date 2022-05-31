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

    def derivative(self, xc: float, step: float) -> float:
        x1 = xc - step / 2
        x2 = xc + step / 2
        derivative = self.derivative_range(x1, x2)
        return derivative

    def derivative_forward(self, xl: float, step: float) -> float:
        derivative = self.derivative(xl + step / 2, step)
        return derivative

    def derivative_backward(self, xl: float, step: float) -> float:
        derivative = self.derivative(xl - step / 2, step)
        return derivative
