#!/usr/bin/env python3
""" script defines an asynchronous coroutine """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that executes the task_wait_random 'n' times
    """
    # sorted(await gather(*list(map(lambda _:wait_random(max_delay),range(n))))
    x = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*x))
