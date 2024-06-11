#!/usr/bin/env python3
""" module provides an asynchronous coroutine """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Coroutine that will execute async_comprehension 4 times in parallel
        using asyncio.gather
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time()-start
