#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """loop 10 times, each asynchronously wait 1 sec and
    yield random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
