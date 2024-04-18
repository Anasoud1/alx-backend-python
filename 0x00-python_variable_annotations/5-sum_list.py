#!/usr/bin/env python3
'''type-annotated function sum_list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''function that return sum of a list'''
    return float(sum(input_list))
