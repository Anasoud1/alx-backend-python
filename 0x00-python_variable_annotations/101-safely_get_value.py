#!/usr/bin/env python3
''' type-annotated function safely_get_value'''
from typing import Union, Any, TypeVar, Mapping


T = TypeVar('T')
Def = Union[T, None]
Ret = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Ret:
    '''Retrieves a value from a dict using a given key.'''
    if key in dct:
        return dct[key]
    else:
        return default
