from random import random
from math import hypot


def approximate_pi(points_count: int) -> float:
    """Simulate pi with Monte Carlo Method
    by placing points randomly in a square
    and checking if they are inside the
    inscribed circle (Warning: Extremely Inefficient)"""
    inside = 0
    outside = 0
    for p in range(points_count):
        if hypot(2 * random() - 1, 2 * random() - 1) < 1:
            inside += 1
        else:
            outside += 1
    ratio = inside / (inside + outside)
    return 4 * ratio

print(approximate_pi(1000))