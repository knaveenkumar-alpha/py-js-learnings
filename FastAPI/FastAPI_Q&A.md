
# 💼 Top FastAPI Interview Questions & Answers

A collection of frequently asked interview questions on FastAPI with code examples and clear explanations.

---

## 1️⃣ What is FastAPI?

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on **standard Python type hints**.

- Built on **Starlette** for web parts and **Pydantic** for data validation.
- Asynchronous, fast, and easy to use.

---

## 2️⃣ How do you define an endpoint in FastAPI?

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

---

## 3️⃣ How does FastAPI handle request data validation?

Via **Pydantic models**:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

✅ FastAPI automatically validates and converts the input data.

---

## 4️⃣ What are dependencies in FastAPI?

Used to share logic like DB connections or security.

```python
from fastapi import Depends

def get_token():
    return "my-secret-token"

@app.get("/secure")
def secure_route(token: str = Depends(get_token)):
    return {"token": token}
```

---

## 5️⃣ How do you implement async endpoints?

```python
import asyncio

@app.get("/wait")
async def wait():
    await asyncio.sleep(2)
    return {"message": "Waited asynchronously"}
```

✔ Async is perfect for non-blocking I/O tasks.

---

## 6️⃣ How does FastAPI differ from Flask?

| Feature        | Flask       | FastAPI         |
|----------------|-------------|-----------------|
| Type Checking  | ❌ No       | ✅ Yes          |
| Async Support  | 🟡 Limited  | ✅ Native       |
| Data Validation| ❌ Manual   | ✅ Pydantic     |
| Speed          | 🟡 OK       | ✅ Very Fast    |

---

## 7️⃣ How do you handle query parameters and path parameters?

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

---

## 8️⃣ How do you create custom exception handlers?

```python
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": str(exc.detail)})
```

---

## 9️⃣ How do you document your API in FastAPI?

Auto-generated docs are available at:
- Swagger: `/docs`
- ReDoc: `/redoc`

You can also use descriptions and examples in your endpoint definitions.

---

## 🔟 How do you test FastAPI applications?

Using `TestClient`:

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

---

## ✅ Summary

- Use **Pydantic** for data validation
- Use **Depends** for dependency injection
- Use `async def` for async endpoints
- Docs are auto-generated with Swagger
- Use `TestClient` for testing

