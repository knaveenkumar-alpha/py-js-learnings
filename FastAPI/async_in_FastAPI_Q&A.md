# Asynchronous Programming in Python - Interview Q&A

## 1. What is asynchronous programming in Python?

Asynchronous programming allows a program to perform tasks concurrently, especially useful for I/O-bound operations like file I/O, network calls, or database access.

It uses coroutines (`async def`) and the `await` keyword to run operations without blocking the main thread.

---

## 2. What is the `asyncio` module?

`asyncio` is a standard Python library used to write asynchronous programs. It provides:

- Event loop
- Coroutines
- Tasks
- Future objects

---

## 3. Difference between a coroutine and a normal function?

| Feature        | Coroutine (`async def`) | Normal Function (`def`) |
|----------------|--------------------------|--------------------------|
| Syntax         | `async def`              | `def`                    |
| Execution      | Returns coroutine object | Executes immediately     |
| Awaitable?     | Yes, using `await`       | No                       |

---

## 4. How does `asyncio.run()` work?

`asyncio.run(main())` runs the top-level coroutine `main()` and manages the event loop lifecycle (setup, execution, and teardown).

```python
async def main():
    await something()

asyncio.run(main())
```


## 5. What is the event loop?

The event loop orchestrates the execution of asynchronous tasks. It:
a. Manages scheduling of coroutines
b. Listens for completed I/O operations
c. Switches context between tasks

## 6. What’s the difference between await, asyncio.gather(), and asyncio.create_task()?
await: Waits for a coroutine to finish.

asyncio.gather(): Runs multiple coroutines concurrently and waits for all of them.

asyncio.create_task(): Schedules a coroutine to run in the background.

```python

task = asyncio.create_task(coroutine())
await task
```
## 7. What happens if you call await on a non-async function?
It raises a TypeError. Only await-able objects like coroutines or objects with __await__() can be awaited.

## 8. Can you mix threading and asyncio?
Yes, but cautiously. Use asyncio.to_thread() to run blocking I/O in a thread without blocking the event loop.

```python
import asyncio

def blocking_func():
    return "done"

async def main():
    result = await asyncio.to_thread(blocking_func)
```
## 9. How to handle exceptions in async code?
Use try/except around await expressions, or use asyncio.gather(..., return_exceptions=True) to collect them safely.

## 10. Example: Make two async API calls in parallel
```python
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://api1.com', 'https://api2.com']
    results = await asyncio.gather(*(fetch(url) for url in urls))
    print(results)

asyncio.run(main())
```

## Bonus: Tools for Async Python
aiohttp – Async HTTP client/server

aiomysql – Async MySQL

aioredis – Async Redis

FastAPI – Async web framework