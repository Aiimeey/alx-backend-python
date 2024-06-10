#!/usr/bin/env python3
""" script defines an asynchronous coroutine """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Asynchronous coroutine that gives total time of wait_n execution
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
