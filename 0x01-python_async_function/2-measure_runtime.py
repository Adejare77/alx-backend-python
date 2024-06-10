#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns the total_time / n taken by function wait_n"""
    result: float = asyncio.run(main(n, max_delay))
    return result


async def main(n: int, max_delay: int) -> float:
    """returns total_time/n to measure_time"""
    start_time: float = time.perf_counter()
    await wait_n(n, max_delay)
    total_time: float = time.perf_counter() - start_time
    return total_time / n
