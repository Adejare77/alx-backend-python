#!/usr/bin/env python3
"""The basic of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns the delayed time value"""
    delay_value: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_value)
    return delay_value
