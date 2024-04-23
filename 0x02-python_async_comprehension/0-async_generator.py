#!/usr/bin/env python3
'''async_generator module'''
import asyncio
import random


async def async_generator():
    '''function that loop 10 times and yield a random number (0<=x<=10)'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
