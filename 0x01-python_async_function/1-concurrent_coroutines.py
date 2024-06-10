#!/usr/bin/env python3
""" script defines an asynchronous coroutine """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that executes the wait_random coroutine 'n' times
    """
    # x = []
    # for _ in range(n):
    #     x.append(wait_random(max_delay))
    x = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*x))
