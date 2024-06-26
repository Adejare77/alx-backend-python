#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    all_delays = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*all_delays)
    return sorted(result)
