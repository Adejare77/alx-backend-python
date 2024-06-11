# Asyncio for

We have two types of Asyncio function: Coroutine function and Async Generator:

1. Coroutine: These are asynchronous function that contains `await` and/or `return`, but DO NOT `yield` multiple values over time.

2. Async Generator: These are also asynchronous function that can yield multiple values asynchronously. The contain `await` and `yield`.

`Async for` is used in Python to iterate over asynchronous Iterables or generators. That is, they work on Async Generator or any Async iterable

## What is an Asynchronous Iterable?

An asynchronous iterable is an object that implements the '__aiter__()' method, which must return an asynchronous iterator. An asynchronous iterator is an object/instance that implements two methods:

1. __anext__(): an asynchronous that returns the next item of the iteration. if there are no more items, it should raise a `StopAsyncIteration` exception
2. __aenter__() and __aexit__() (Optional): These methods are used to support asynchronous context management
