#!/usr/bin/env python3
""" module provides an asynchronous coroutine """
import asyncio
import random
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """ coroutine that loops 10 times asynchronously wait 1 second,
        then yield a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
