#!/usr/bin/env python3
'''
function:
    make_multiplier that takes a float multiplier as argument.
returns:
    function that multiplies a float by multiplier.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
