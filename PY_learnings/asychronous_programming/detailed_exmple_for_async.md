## Asynchronous Programming in Python — Complete Deep Dive

---

## Why Async Exists — The Core Problem

```python
# SYNCHRONOUS — each step BLOCKS the next one
import time

def fetch_user():
    time.sleep(2)      # waiting... CPU sits idle doing NOTHING
    return "user data"

def fetch_orders():
    time.sleep(2)      # waiting again... still idle
    return "orders"

def fetch_payments():
    time.sleep(2)      # still waiting...
    return "payments"

# Total time = 2 + 2 + 2 = 6 seconds — wasteful
fetch_user()
fetch_orders()
fetch_payments()
```

The CPU isn't doing anything during those `sleep` calls — it's just **waiting**. Async lets the CPU do other work while waiting for I/O (network, disk, DB).

---

## The Mental Model — Restaurant Analogy

```
SYNCHRONOUS waiter:
  Takes order from Table 1 → goes to kitchen → STANDS there waiting
  → brings food → then goes to Table 2

ASYNC waiter:
  Takes order from Table 1 → gives to kitchen → takes Table 2 order
  → gives to kitchen → checks Table 1 (ready!) → serves → checks Table 2...

The waiter = your program thread
Kitchen    = network / DB / disk I/O
```

---

## Core Building Blocks

### 1. Coroutine Object — the heart of async

```python
import asyncio

# 'async def' creates a COROUTINE FUNCTION
async def greet(name: str):
    print(f"Hello {name}")
    await asyncio.sleep(1)       # suspend here, let others run
    print(f"Goodbye {name}")

# CRITICAL: calling it does NOT run it
result = greet("Naveen")
print(type(result))   # <class 'coroutine'>
print(result)         # <coroutine object greet at 0x...>

# It's just an OBJECT at this point — not executed yet
# You must await it or schedule it
```

A **coroutine object** is like a paused function — it holds all its local state, knows where it paused, and can be resumed later. Think of it like a generator that can suspend execution at `await` points.

---

### 2. `await` — the suspension point

```python
async def main():
    print("start")
    await asyncio.sleep(2)   # ← suspend THIS coroutine, let others run
    print("resumed after 2s")

# await can ONLY be used inside async def
# It says: "pause me here, do other things, come back when this is done"
```

---

### 3. Event Loop — the scheduler

```python
import asyncio

async def my_coroutine():
    await asyncio.sleep(1)
    return "done"

# Event loop runs coroutines
asyncio.run(my_coroutine())   # Python 3.7+ — creates loop, runs, closes
```

The **event loop** is the traffic controller — it decides which coroutine runs next, watches for I/O completion, and resumes the right coroutine when its awaited operation finishes.

```
Event Loop internal cycle:
  1. Pick a ready coroutine
  2. Run it until it hits 'await'
  3. Register the I/O operation (don't block)
  4. Pick next ready coroutine
  5. When I/O completes → mark original coroutine as ready
  6. Resume it from where it paused
```

---

## Coroutine Lifecycle — Step by Step

```python
import asyncio
import inspect

async def example():
    print("Step 1")
    await asyncio.sleep(1)
    print("Step 2")
    return "final value"

# Step 1: Create coroutine object (NOT running)
coro = example()
print(inspect.iscoroutine(coro))   # True
print(coro.cr_running)             # False — not running yet

# Step 2: Schedule it on event loop
asyncio.run(coro)
# Output:
# Step 1
# (1 second pause — other coroutines could run here)
# Step 2
```

---

## Three Key Objects — Coroutine vs Task vs Future

```python
import asyncio

async def work(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} done")
    return f"{name} result"


async def main():

    # ── 1. COROUTINE OBJECT ────────────────────────────────────────────────
    # Just an object, not scheduled yet
    coro = work("A", 1)
    print(type(coro))          # <class 'coroutine'>

    # ── 2. TASK ────────────────────────────────────────────────────────────
    # Wraps coroutine + schedules it on event loop IMMEDIATELY
    # Runs CONCURRENTLY with other tasks
    task = asyncio.create_task(work("B", 2))
    print(type(task))          # <class 'Task'>

    # ── 3. FUTURE ──────────────────────────────────────────────────────────
    # Low-level object representing a value not yet computed
    # Tasks are built on top of Future
    # You rarely create Future directly — asyncio manages it
    future = asyncio.get_event_loop().create_future()
    print(type(future))        # <class 'Future'>

asyncio.run(main())
```

---

## Real Power — Running Concurrently

```python
import asyncio
import time

async def fetch_user(user_id: int):
    print(f"Fetching user {user_id}...")
    await asyncio.sleep(2)           # simulates DB/API call
    return {"id": user_id, "name": f"User_{user_id}"}

async def fetch_orders(user_id: int):
    print(f"Fetching orders for {user_id}...")
    await asyncio.sleep(2)
    return [f"order_{i}" for i in range(3)]

async def fetch_payments(user_id: int):
    print(f"Fetching payments for {user_id}...")
    await asyncio.sleep(2)
    return [f"payment_{i}" for i in range(2)]


# ── SEQUENTIAL (bad) — 6 seconds ──────────────────────────────────────────
async def slow_way():
    start = time.time()
    user     = await fetch_user(1)
    orders   = await fetch_orders(1)
    payments = await fetch_payments(1)
    print(f"Sequential: {time.time() - start:.1f}s")   # ~6.0s


# ── CONCURRENT (good) — 2 seconds ─────────────────────────────────────────
async def fast_way():
    start = time.time()

    # All three START at the same time
    user, orders, payments = await asyncio.gather(
        fetch_user(1),
        fetch_orders(1),
        fetch_payments(1)
    )
    print(f"Concurrent: {time.time() - start:.1f}s")   # ~2.0s
    return user, orders, payments

asyncio.run(fast_way())
```

---

## `asyncio.gather` vs `asyncio.create_task` — Know the Difference

```python
import asyncio

async def job(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"


async def main():

    # ── gather: runs all, waits for ALL to finish ──────────────────────────
    results = await asyncio.gather(
        job("A", 1),
        job("B", 2),
        job("C", 3),
    )
    print(results)   # ['A done', 'B done', 'C done'] — after ~3s total


    # ── create_task: schedule now, await later ─────────────────────────────
    task_a = asyncio.create_task(job("X", 1))   # starts immediately
    task_b = asyncio.create_task(job("Y", 2))   # starts immediately

    # do other work here while tasks run in background
    print("Tasks are running in background...")

    result_a = await task_a   # wait for X
    result_b = await task_b   # wait for Y
    print(result_a, result_b)


    # ── as_completed: process results AS THEY ARRIVE ───────────────────────
    tasks = [job("fast", 1), job("slow", 3), job("medium", 2)]
    async for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Got: {result}")   # prints: fast → medium → slow


asyncio.run(main())
```

---

## Exception Handling in Async

```python
import asyncio

async def risky_task(n: int):
    await asyncio.sleep(1)
    if n == 2:
        raise ValueError(f"Task {n} failed!")
    return f"Task {n} success"


async def main():

    # ── gather with return_exceptions=True ────────────────────────────────
    # Without this, one failure cancels ALL tasks
    results = await asyncio.gather(
        risky_task(1),
        risky_task(2),   # this fails
        risky_task(3),
        return_exceptions=True   # ← don't cancel others on failure
    )

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i+1} failed: {result}")
        else:
            print(f"Task {i+1} succeeded: {result}")

    # Output:
    # Task 1 succeeded: Task 1 success
    # Task 2 failed: Task 2 failed!
    # Task 3 succeeded: Task 3 success

asyncio.run(main())
```

---

## Async Context Managers and Iterators

```python
import asyncio

# ── Async Context Manager ──────────────────────────────────────────────────
class AsyncDBConnection:
    async def __aenter__(self):
        print("Opening DB connection...")
        await asyncio.sleep(0.1)   # simulate connection time
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Closing DB connection...")
        await asyncio.sleep(0.1)

    async def query(self, sql: str):
        await asyncio.sleep(0.2)
        return f"Results of: {sql}"


# ── Async Generator / Iterator ─────────────────────────────────────────────
async def stream_records(limit: int):
    for i in range(limit):
        await asyncio.sleep(0.1)   # simulate fetching each record
        yield {"id": i, "data": f"record_{i}"}


async def main():
    # async with → calls __aenter__ and __aexit__ asynchronously
    async with AsyncDBConnection() as db:
        result = await db.query("SELECT * FROM users")
        print(result)

    # async for → iterates over async generator
    async for record in stream_records(5):
        print(record)


asyncio.run(main())
```

---

## Real FastAPI Example — How You Already Use This

```python
from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()

# FastAPI runs in an async event loop
# Every 'async def' route is a coroutine
@app.get("/dashboard/{user_id}")
async def get_dashboard(user_id: int):

    # These 3 calls happen CONCURRENTLY — not one by one
    async with httpx.AsyncClient() as client:
        user_task     = asyncio.create_task(client.get(f"/users/{user_id}"))
        orders_task   = asyncio.create_task(client.get(f"/orders/{user_id}"))
        payments_task = asyncio.create_task(client.get(f"/payments/{user_id}"))

        user, orders, payments = await asyncio.gather(
            user_task,
            orders_task,
            payments_task
        )

    return {
        "user":     user.json(),
        "orders":   orders.json(),
        "payments": payments.json()
    }
    # Response time = slowest of the 3 calls, not sum of all 3
```

---

## Complete Mental Map

```
async def          → defines a coroutine function
calling async def  → returns coroutine OBJECT (not executed)
await              → suspend here, let event loop run others
asyncio.run()      → create event loop + run one root coroutine
create_task()      → schedule coroutine on loop (runs concurrently)
gather()           → run multiple coroutines concurrently, wait all
as_completed()     → process results as each one finishes
async with         → async context manager (__aenter__/__aexit__)
async for          → iterate async generator (yield one by one)

Coroutine  → paused function with saved state
Task       → coroutine + scheduled on event loop
Future     → low-level "promise" of a value (Task inherits it)
Event Loop → the scheduler that runs everything
```

---

## When to Use Async vs Not

| Use Async | Don't Use Async |
|---|---|
| HTTP calls to APIs | CPU-heavy math/ML |
| Database queries | Image/video processing |
| File I/O | Number crunching |
| WebSocket connections | Pure computation |
| Waiting for multiple services | `numpy`/`pandas` operations |

For CPU-heavy work, use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor` — async won't help there since the GIL is still held during computation.

---

The key insight: **async is about waiting efficiently, not about doing things faster**. Your FastAPI + Databricks API work is a perfect use case because you're always waiting on network or DB — async lets your server handle hundreds of requests on a single thread while all of them are in various stages of waiting.