#!/usr/bin/env python3
"""
A type annotated function
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    """
    Takes a list mxd_lst of integers and floats
    and returns their sum as a float.
    """
    return sum(mxd_lst)
