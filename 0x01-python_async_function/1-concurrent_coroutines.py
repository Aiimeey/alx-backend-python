#!/usr/bin/env python3
"""  script defines an asynchronous coroutine """
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay) -> List[float]:
    """Asynchronous coroutine that executes the wait_random coroutine 'n' times
    """
    x = []
    for _ in range(n):
        x.append(await wait_random(max_delay))
    return x
