#!/usr/bin/env python3
"""
A type annotated function
"""
from typing import Any, Union, Mapping, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function that safely gets a value
    """
    if key in dct:
        return dct[key]
    else:
        return default
