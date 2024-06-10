#!/usr/bin/env python3
"""Tasks"""

import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """spawn wait_random n times with the specified max_delay"""
    all_delays: list = [task_wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*all_delays)
    return result
