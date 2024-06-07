#!/usr/bin/env python3
"""Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    takes a list of floats and returns their sum as float
    """
    return float(sum(input_list))
