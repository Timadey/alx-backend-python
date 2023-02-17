#!/usr/bin/env python3
"""
A type annotated function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier
    """
    def func(fl: float) -> float:
        return fl * multiplier
    return func
