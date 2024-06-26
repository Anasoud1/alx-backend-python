#!/usr/bin/env python3
'''wait_random module'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''function that waits for a random delay between 0 and max_delay
    and return it'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
