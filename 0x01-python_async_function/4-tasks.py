#!/usr/bin/env python3
'''wait_n module'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''function that return a list of all delays'''
    new = []
    for i in range(n):
        val = await wait_random(max_delay)
        new.append(val)
    return sorted(new)
