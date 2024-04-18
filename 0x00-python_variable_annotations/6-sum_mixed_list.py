#!/usr/bin/env python3
'''type-annotated function sum_mixed_list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function that return sum of a list'''
    return float(sum(mxd_lst))
