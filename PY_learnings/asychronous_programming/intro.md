# Asynchronous Programming in Python

Asynchronous programming in Python lets you run multiple tasks concurrently without blocking execution, making it ideal for I/O-bound operations like network requests, database queries, or file handling.

The core library for this is `asyncio`, which uses the `async`/`await` syntax to manage coroutines and event loops efficiently.

## Key Concepts

- `async def`: Defines a coroutine function.
- `await`: Pauses execution until an awaited coroutine completes.
- `Event loop`: Schedules and runs coroutines.
- `asyncio.create_task()`: Runs coroutines concurrently.

## Concepts in Asynchronous Programming

### Coroutines  
Special functions defined with `async def` that can be paused and resumed using `await`.

### Event Loop  
The central scheduler that runs `coroutines`, handles tasks, and manages I/O operations.

### Tasks  
Wrappers around `coroutines` that allow them to run concurrently.

### Await  
Suspends execution of a `coroutine` until the `awaited task` completes, freeing the `event loop` to run other tasks.

## Example

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return 'data'

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())

    result1 = await task1
    result2 = await task2
    print(result1, result2)

asyncio.run(main())
```

## When to use

- Network requests
- Database operations
- File I/O
- Any task that waits on external resources

## Benefits

- Better responsiveness
- Efficient concurrency for I/O-bound workloads
- Cleaner code compared to callback-based async patterns

