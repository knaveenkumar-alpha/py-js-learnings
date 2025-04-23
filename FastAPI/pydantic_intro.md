
# 🧩 Pydantic in Python and FastAPI

Pydantic is a **data validation** and **settings management** library using **Python type annotations**.

---

## ✅ Why use Pydantic?

- Automatic **type validation & conversion**
- Built-in **error reporting**
- **Serialization** and **deserialization** (e.g., JSON ↔ Python)
- **Data modeling** for request/response in FastAPI

---

## 🧱 Basic Example: Defining a Model

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
```

Usage:

```python
input_data = {"id": "1", "name": "Alice", "email": "alice@example.com"}
user = User(**input_data)
print(user)
```

---

## 🧪 Validation Example

```python
from pydantic import ValidationError

try:
    user = User(id="abc", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e.json())
```

---

## 🚀 Pydantic in FastAPI

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

---

## 🔁 Serialization

```python
item = Item(name="Keyboard", price=49.99)
print(item.dict())
print(item.json())
```

---

## 🔐 Advanced Concepts

### Field Validation

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=1, le=100)
```

### Custom Validators

```python
from pydantic import validator

class User(BaseModel):
    name: str
    email: str

    @validator("email")
    def validate_email(cls, v):
        if "@example.com" not in v:
            raise ValueError("Email must be from example.com domain")
        return v
```

---

## 🧱 Nested Models

```python
class Address(BaseModel):
    city: str
    zip: str

class Customer(BaseModel):
    name: str
    address: Address

data = {
    "name": "Jane",
    "address": {"city": "NYC", "zip": "10001"}
}

customer = Customer(**data)
```

---

## 📦 Summary Table

| Feature               | Description                                      |
|-----------------------|--------------------------------------------------|
| `BaseModel`           | Base class for all models                        |
| `Field(...)`          | Add constraints, metadata                        |
| `validator()`         | Custom validation for fields                     |
| `.dict()` / `.json()` | Serialize model to dict/JSON                     |
| `ValidationError`     | Exception raised for invalid data                |
| Nested Models         | Compose complex data structures                  |
