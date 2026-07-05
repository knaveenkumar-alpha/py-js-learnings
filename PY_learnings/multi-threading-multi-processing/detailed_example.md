## Multi-threading & Multi-processing in Python — Complete Deep Dive

---

## Start Here — The GIL (Everything depends on this)

```
GIL = Global Interpreter Lock

It's a mutex (lock) inside CPython that allows only ONE thread
to execute Python bytecode at a time — even on multi-core CPUs.

Thread 1 ──► gets GIL ──► runs ──► releases GIL
Thread 2 ──► waits   ──► gets GIL ──► runs ──► releases GIL

Result: threads take turns, never truly parallel for CPU work
```

This one fact explains **everything** about when to use threading vs multiprocessing.

---

## The Three Concurrency Models — Side by Side

```
                 Threading        Multiprocessing     Async
─────────────────────────────────────────────────────────────
Parallelism      ❌ (GIL blocks)  ✅ (separate GIL)   ❌
Best for         I/O bound        CPU bound           I/O bound
Memory           Shared           Separate            Shared
Overhead         Low              High                Lowest
Processes/cores  1 process        Multiple processes  1 process
Communication    Direct (shared)  Queue/Pipe          await
```

---

## Part 1 — Multi-threading

### Basic Thread

```python
import threading
import time

def download_file(filename: str, delay: int):
    print(f"[{threading.current_thread().name}] Starting: {filename}")
    time.sleep(delay)      # simulates I/O wait (network, disk)
    print(f"[{threading.current_thread().name}] Done: {filename}")


# ── Without threading — sequential ────────────────────────────────────────
start = time.time()
download_file("file_A.csv", 2)
download_file("file_B.csv", 2)
download_file("file_C.csv", 2)
print(f"Sequential: {time.time() - start:.1f}s")   # 6.0s


# ── With threading — concurrent ────────────────────────────────────────────
start = time.time()

t1 = threading.Thread(target=download_file, args=("file_A.csv", 2), name="T1")
t2 = threading.Thread(target=download_file, args=("file_B.csv", 2), name="T2")
t3 = threading.Thread(target=download_file, args=("file_C.csv", 2), name="T3")

t1.start()   # launches thread
t2.start()
t3.start()

t1.join()    # main thread waits here until T1 finishes
t2.join()
t3.join()

print(f"Threaded: {time.time() - start:.1f}s")    # ~2.0s
```

---

### Thread Lifecycle

```
CREATED     → threading.Thread(target=func)
STARTED     → t.start()   — OS creates actual thread
RUNNING     → thread executes target function
BLOCKED     → waiting for lock / I/O / sleep
TERMINATED  → function returned or raised exception

t.is_alive()   → True if STARTED and not TERMINATED
t.join()       → blocks caller until this thread TERMINATES
t.daemon=True  → thread dies when main program exits (background tasks)
```

---

### Thread with Return Value — using `Queue`

```python
import threading
import queue
import time

# Threads can't return values directly
# Solution: use a Queue to collect results

def fetch_data(source: str, delay: int, result_queue: queue.Queue):
    time.sleep(delay)
    result = f"data from {source}"
    result_queue.put((source, result))   # push result into queue


result_q = queue.Queue()

threads = [
    threading.Thread(target=fetch_data, args=("DB",  2, result_q)),
    threading.Thread(target=fetch_data, args=("API", 1, result_q)),
    threading.Thread(target=fetch_data, args=("S3",  3, result_q)),
]

for t in threads:
    t.start()

for t in threads:
    t.join()

# Collect all results
results = {}
while not result_q.empty():
    source, data = result_q.get()
    results[source] = data

print(results)
# {'API': 'data from API', 'DB': 'data from DB', 'S3': 'data from S3'}
```

---

### Thread Safety — Race Condition Problem

```python
import threading

# UNSAFE — race condition
counter = 0

def increment_unsafe():
    global counter
    for _ in range(100_000):
        counter += 1    # READ counter → ADD 1 → WRITE back
                        # Another thread can interrupt between READ and WRITE!

threads = [threading.Thread(target=increment_unsafe) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)   # Should be 500,000 but you get: 312,847 (random!)
```

```python
import threading

# SAFE — using Lock
counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100_000):
        with lock:        # only ONE thread enters this block at a time
            counter += 1  # now atomic — no interruption possible

threads = [threading.Thread(target=increment_safe) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)   # 500,000 — always correct
```

---

### All Synchronization Primitives

```python
import threading

# ── Lock — basic mutual exclusion ─────────────────────────────────────────
lock = threading.Lock()
with lock:
    # only 1 thread at a time
    pass

# ── RLock — reentrant lock (same thread can acquire multiple times) ────────
rlock = threading.RLock()
with rlock:
    with rlock:   # won't deadlock — same thread can re-enter
        pass

# ── Semaphore — limit N threads in a section ──────────────────────────────
semaphore = threading.Semaphore(3)   # max 3 threads at once (DB pool!)
with semaphore:
    # at most 3 threads here simultaneously
    pass

# ── Event — signal between threads ────────────────────────────────────────
event = threading.Event()

def worker():
    print("Worker waiting for signal...")
    event.wait()       # blocks until event.set() is called
    print("Worker got signal, proceeding!")

def controller():
    import time
    time.sleep(2)
    event.set()        # unblocks all waiting threads

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=controller)
t1.start(); t2.start()
t1.join();  t2.join()

# ── Condition — wait for a condition to be true ───────────────────────────
condition = threading.Condition()
items = []

def producer():
    with condition:
        items.append("item")
        condition.notify_all()   # wake up all waiting consumers

def consumer():
    with condition:
        condition.wait_for(lambda: len(items) > 0)  # sleep until condition
        print(f"Consumed: {items.pop()}")
```

---

### ThreadPoolExecutor — Production Way

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def process_record(record_id: int) -> dict:
    time.sleep(0.5)    # simulate DB/API call
    return {"id": record_id, "status": "processed"}


# ── Basic usage ────────────────────────────────────────────────────────────
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(process_record, i) for i in range(20)]

    # Wait for ALL and collect results in order
    results = [f.result() for f in futures]


# ── Process as they COMPLETE (not in order) ────────────────────────────────
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(process_record, i): i for i in range(10)}

    for future in as_completed(futures):
        record_id = futures[future]
        try:
            result = future.result()
            print(f"Record {record_id}: {result}")
        except Exception as e:
            print(f"Record {record_id} failed: {e}")


# ── map — simplest when you don't need futures ────────────────────────────
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(process_record, range(20)))
    # blocks until all done, returns results in INPUT order
```

---

## Part 2 — Multi-processing

### Why Multiprocessing — GIL is bypassed

```
Each Process gets:
  ├── its own Python interpreter
  ├── its own GIL
  ├── its own memory space
  └── its own copy of all variables

Result: TRUE parallelism across CPU cores
Cost:   higher memory, slower startup, harder communication
```

---

### Basic Process

```python
import multiprocessing
import time
import os

def cpu_heavy_task(n: int) -> int:
    """Simulates pure CPU work — no I/O"""
    print(f"PID {os.getpid()} computing...")
    total = sum(i * i for i in range(n))
    return total


if __name__ == "__main__":   # ← REQUIRED on Windows/Mac — always add this!

    # ── Sequential ────────────────────────────────────────────────────────
    start = time.time()
    results = [cpu_heavy_task(5_000_000) for _ in range(4)]
    print(f"Sequential: {time.time() - start:.1f}s")   # ~8s


    # ── Multiprocessing ───────────────────────────────────────────────────
    start = time.time()

    p1 = multiprocessing.Process(target=cpu_heavy_task, args=(5_000_000,))
    p2 = multiprocessing.Process(target=cpu_heavy_task, args=(5_000_000,))
    p3 = multiprocessing.Process(target=cpu_heavy_task, args=(5_000_000,))
    p4 = multiprocessing.Process(target=cpu_heavy_task, args=(5_000_000,))

    for p in [p1, p2, p3, p4]: p.start()
    for p in [p1, p2, p3, p4]: p.join()

    print(f"Multiprocessing: {time.time() - start:.1f}s")   # ~2s (4 cores)
```

---

### Getting Return Values — Queue and Pipe

```python
import multiprocessing

# ── Using Queue (multiple producers/consumers) ─────────────────────────────
def square_numbers(numbers: list, result_queue: multiprocessing.Queue):
    results = [n ** 2 for n in numbers]
    result_queue.put(results)


if __name__ == "__main__":
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_numbers, args=([1,2,3], q))
    p2 = multiprocessing.Process(target=square_numbers, args=([4,5,6], q))

    p1.start(); p2.start()
    p1.join();  p2.join()

    all_results = []
    while not q.empty():
        all_results.extend(q.get())

    print(sorted(all_results))   # [1, 4, 9, 16, 25, 36]


# ── Using Pipe (two-way communication between 2 processes) ────────────────
def worker_pipe(conn):
    data = conn.recv()           # receive from parent
    result = [x ** 2 for x in data]
    conn.send(result)            # send back to parent
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    p = multiprocessing.Process(target=worker_pipe, args=(child_conn,))
    p.start()

    parent_conn.send([1, 2, 3, 4, 5])   # send data to child
    result = parent_conn.recv()          # wait for result
    p.join()

    print(result)   # [1, 4, 9, 16, 25]
```

---

### Shared Memory — sharing state between processes

```python
import multiprocessing

# Processes have SEPARATE memory — normal variables aren't shared
# Use Value or Array for shared state

def increment_shared(shared_counter, lock, n: int):
    for _ in range(n):
        with lock:
            shared_counter.value += 1


if __name__ == "__main__":
    # 'i' = integer type, initial value = 0
    counter = multiprocessing.Value('i', 0)
    lock    = multiprocessing.Lock()

    processes = [
        multiprocessing.Process(
            target=increment_shared,
            args=(counter, lock, 10_000)
        )
        for _ in range(4)
    ]

    for p in processes: p.start()
    for p in processes: p.join()

    print(counter.value)   # 40,000 — correct with lock

    # ── Shared Array ──────────────────────────────────────────────────────
    arr = multiprocessing.Array('i', [0, 0, 0, 0, 0])
    # typecodes: 'i'=int, 'd'=double/float, 'c'=char
```

---

### ProcessPoolExecutor — Production Way

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def heavy_computation(n: int) -> dict:
    """Pure CPU work — benefits from multiprocessing"""
    result = sum(i ** 2 for i in range(n))
    return {"input": n, "result": result}


if __name__ == "__main__":

    inputs = [1_000_000, 2_000_000, 3_000_000, 4_000_000]

    # ── map — simple, ordered results ─────────────────────────────────────
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(heavy_computation, inputs))
        print(results)

    # ── submit — more control, handle errors ──────────────────────────────
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {
            executor.submit(heavy_computation, n): n
            for n in inputs
        }

        for future in as_completed(futures):
            n = futures[future]
            try:
                result = future.result()
                print(f"n={n}: {result}")
            except Exception as e:
                print(f"n={n} failed: {e}")
```

---

## Part 3 — Real World Examples (Your Use Cases)

### Databricks Pipeline — Parallel File Processing

```python
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time

# ── Use ThreadPool for I/O (uploading files to ADLS/S3) ───────────────────
def upload_to_adls(file_path: str) -> str:
    time.sleep(1)   # simulate network I/O
    return f"Uploaded: {file_path}"

def parallel_upload(file_paths: list) -> list:
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(upload_to_adls, file_paths))
    return results


# ── Use ProcessPool for CPU (transforming/compressing data) ───────────────
def transform_partition(partition_data: list) -> list:
    # heavy data transformation — CPU bound
    return [row.upper() + "_transformed" for row in partition_data]

def parallel_transform(partitions: list) -> list:
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(transform_partition, partitions))
    return results


if __name__ == "__main__":
    files = [f"file_{i}.parquet" for i in range(20)]
    uploaded = parallel_upload(files)
    print(f"Uploaded {len(uploaded)} files")

    partitions = [["row1", "row2", "row3"] for _ in range(8)]
    transformed = parallel_transform(partitions)
    print(f"Transformed {len(transformed)} partitions")
```

---

### FastAPI — Background CPU Task with ProcessPool

```python
from fastapi import FastAPI, BackgroundTasks
from concurrent.futures import ProcessPoolExecutor
import asyncio

app = FastAPI()
process_pool = ProcessPoolExecutor(max_workers=4)


def heavy_cpu_task(data: list) -> dict:
    """Runs in a separate process — doesn't block FastAPI"""
    result = sum(x ** 2 for x in data)
    return {"sum_of_squares": result, "count": len(data)}


@app.post("/compute")
async def compute(data: list[int]):
    loop = asyncio.get_event_loop()

    # Run CPU task in process pool WITHOUT blocking async event loop
    result = await loop.run_in_executor(
        process_pool,
        heavy_cpu_task,
        data
    )
    return result


@app.on_event("shutdown")
def shutdown():
    process_pool.shutdown(wait=True)
```

---

## Decision Tree — Which to Use

```
You need concurrency?
│
├─► What kind of work?
│     │
│     ├─► I/O bound (network, DB, file, API calls)
│     │     │
│     │     ├─► Many connections, lightweight?
│     │     │     └─► asyncio (best — lowest overhead)
│     │     │
│     │     └─► Existing sync code, can't use async?
│     │           └─► ThreadPoolExecutor (good for I/O)
│     │
│     └─► CPU bound (math, compression, ML inference)
│           └─► ProcessPoolExecutor (only real option)
│
└─► Need shared mutable state?
      ├─► Yes → Threading + Lock (careful with GIL)
      └─► No  → Multiprocessing (cleanest isolation)
```

---

## Complete Summary

```
threading.Thread        → manual thread, for simple cases
ThreadPoolExecutor      → pool of threads, production I/O work
multiprocessing.Process → manual process, for simple cases
ProcessPoolExecutor     → pool of processes, production CPU work
multiprocessing.Queue   → safe communication between processes
multiprocessing.Pipe    → two-way channel between 2 processes
multiprocessing.Value   → single shared variable across processes
multiprocessing.Array   → shared array across processes
threading.Lock          → mutex — only 1 thread in section
threading.Semaphore     → allow N threads in section
threading.Event         → signal between threads
threading.Condition     → wait for condition to be true

GIL                     → threading can't parallelize CPU work
                          multiprocessing bypasses GIL entirely
```

The rule of thumb for your work: **FastAPI endpoints → async**. **File uploads / API calls in pipelines → ThreadPool**. **Data transformation / ML scoring at scale → ProcessPool**. All three have their lane — knowing which to pick is a Staff Engineer skill.