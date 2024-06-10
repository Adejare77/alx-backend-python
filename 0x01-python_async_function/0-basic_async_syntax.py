#!/usr/bin/env python3
"""The basic of async"""

import asyncio
import random


async def wait_random(max_delay=10):
    """returns the delayed time value"""
    delay_value = random.uniform(0, max_delay)
    await asyncio.sleep(delay_value)
    return delay_value
