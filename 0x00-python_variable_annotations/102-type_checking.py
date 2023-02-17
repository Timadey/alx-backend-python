#!/usr/bin/env python3
"""
A type annotated function
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    An function that takes a tuple and an int
    """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List = [12, 72, 91]

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3.0)
