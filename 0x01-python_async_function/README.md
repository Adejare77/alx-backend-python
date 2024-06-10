# Introduction to Python - Async I/O

Async IO is a programming approach that allows a program to perform other tasks while waiting for I/O operations (like reading from a file or writing for a network responses) to complete. This is particularly useful for tasks that involves a lot of waiting.
Unlike multiprocessing(parallelism) and Concurrency(Threading), Async IO typically uses Single CPU and Single Thread. It achieves concurrency through event loop that manages and runs tasks simultaneously. This allows efficient handling of many I/O-bound tasks without the overhead of creating multiple threads or processes

## Common methods used with asyncio

asyncio.run()
asyncio.create_task()
asyncio.gather()
asyncio.sleep()
