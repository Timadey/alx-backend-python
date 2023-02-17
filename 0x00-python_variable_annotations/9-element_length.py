#!/usr/bin/env python3
"""
A type annotated function
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return the length of the list for each list
    """
    return [(i, len(i)) for i in lst]
