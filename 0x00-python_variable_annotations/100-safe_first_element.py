#!/usr/bin/env python3
''' type-annotated function safe_first_element'''
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''return first element of list or none'''
    if lst:
        return lst[0]
    else:
        return None
