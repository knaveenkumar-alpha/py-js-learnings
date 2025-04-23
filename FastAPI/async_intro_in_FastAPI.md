
# ⚙️ Asynchronous Programming in Python and FastAPI

Asynchronous programming allows your application to handle many I/O-bound tasks **concurrently**, without waiting for each task to finish one-by-one.

---

## ✅ Why Use Async Programming?

- **Non-blocking I/O**: Don't pause your app waiting for responses (e.g., DB, API calls).
- **Better scalability**: Handle thousands of requests without blocking threads.
- **Efficient resource use**: Perfect for network- or disk-bound operations.

---

## 🔄 Async Core Concepts

| Concept        | Description |
|----------------|-------------|
| `async def`    | Defines a coroutine |
| `await`        | Waits for a coroutine to finish |
| `asyncio`      | Core async library in Python |
| Event loop     | Schedules and runs async tasks |

---

## 📦 Example: Async HTTP Requests

```python
import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Fetched {len(data)} characters from {url}")
            return data

async def main():
    url1 = "https://jsonplaceholder.typicode.com/posts"
    url2 = "https://jsonplaceholder.typicode.com/comments"

    task1 = asyncio.create_task(fetch_data(url1))
    task2 = asyncio.create_task(fetch_data(url2))

    await task1
    await task2

# Start the event loop
asyncio.run(main())
```

In this example:
- Two requests are made **concurrently**.
- No thread is blocked waiting.

---

## 🚀 Async in FastAPI

FastAPI is built on Starlette and **natively supports async** endpoints.

### 🔧 Basic Example

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/wait")
async def wait_and_respond():
    await asyncio.sleep(2)
    return {"message": "Waited asynchronously for 2 seconds!"}
```

✔️ FastAPI uses `await` internally so that multiple requests can be handled simultaneously.

---

## 🔄 Blocking vs Async

| Blocking (Sync)        | Non-blocking (Async)     |
|------------------------|--------------------------|
| `time.sleep(2)`        | `await asyncio.sleep(2)` |
| Freezes entire thread  | Frees up event loop      |
| Bad for concurrency    | Ideal for APIs           |

---

## 🧪 Advanced FastAPI Async: DB Query Example

```python
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_async_session

app = FastAPI()

@app.get("/users")
async def read_users(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute("SELECT * FROM users")
    users = result.fetchall()
    return users
```

> 🧠 `get_async_session()` is an async generator that gives a DB session.

---

## 📌 Summary

- Async = More requests, less waiting.
- FastAPI makes async integration seamless.
- Use `async def`, `await`, `asyncio`, and async-compatible libraries (like `aiohttp`, `httpx`, `asyncpg`, etc).

