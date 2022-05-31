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

    def integral_riemann_left(self, x1: float, x2: float, steps: int) -> float:
        step = (x2 - x1) / steps
        integral = 0
        for n in range(steps):
            x = x1 + n * step
            y = self.value(x)
            integral += y * step
        return integral

    def integral_riemann_right(self, x1: float, x2: float, steps: int) -> float:
        step = (x2 - x1) / steps
        integral = self.integral_riemann_left(x1 + step, x2 + step, steps)
        return integral

    def integral_riemann_center(self, x1: float, x2: float, steps: int) -> float:
        step = (x2 - x1) / steps
        integral = self.integral_riemann_left(x1 + step / 2, x2 + step / 2, steps)
        return integral
