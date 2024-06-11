#!/usr/bin/env python3
""" module provides an asynchronous coroutine """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collect 10 random numbers using an async comprehensing"""
    return [x async for x in async_generator()]
