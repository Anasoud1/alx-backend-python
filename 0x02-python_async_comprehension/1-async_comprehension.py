#!/usr/bin/env python3
'''async_comprehension module'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''return list of 10 random numbers'''
    new = [i async for i in async_generator()]
    return new
