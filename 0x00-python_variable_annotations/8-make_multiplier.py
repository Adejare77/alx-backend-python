#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable

MultiplierFunction = Callable[[float], float]


def make_multiplier(multiplier: float) -> MultiplierFunction:
    """
    takes a float multiplier and returns a function that
    multiplies float by multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
