#!/usr/bin/env python3
'''type-annotated function sum_list'''


def sum_list(input_list: list[float]) -> float:
    '''function that return sum of a list'''
    return float(sum(input_list))