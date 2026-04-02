
# Liskov Substitution Principle (LSP) in Python

The **Liskov Substitution Principle (LSP)** is the **"L"** in **SOLID** principles. It states:

> **Subtypes must be substitutable for their base types without altering the correctness of the program.**
> **Objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program**

In simple terms, if `S` is a subclass of `T`, then objects of type `T` should be replaceable with objects of type `S` **without breaking the program**.

---

## ❌ Bad Example: Violating LSP

```python
class Bird:
    def fly(self):
        print("Flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
```

🎯 **Problem**: Ostrich is a Bird, but it violates the expectation that all Birds can fly.

---

## ✅ Good Example: Following LSP

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class Sparrow(Bird):
    def move(self):
        print("Flying")

class Ostrich(Bird):
    def move(self):
        print("Running")
```

### ✅ Usage

```python
def make_bird_move(bird: Bird):
    bird.move()

make_bird_move(Sparrow())  # Output: Flying
make_bird_move(Ostrich())  # Output: Running
```

✅ Now `Ostrich` and `Sparrow` both follow the expected `move()` behavior of `Bird`.

---

## 📌 Real-World Use Case: Snowflake Loader

Suppose you have different Snowflake loaders. All should follow the same interface, and substituting one for another should not break the pipeline.

```python
class BaseLoader(ABC):
    @abstractmethod
    def load(self, file_path):
        pass

class CSVLoader(BaseLoader):
    def load(self, file_path):
        print("Loading CSV into Snowflake")

class JSONLoader(BaseLoader):
    def load(self, file_path):
        print("Loading JSON into Snowflake")

def run_loader(loader: BaseLoader, path: str):
    loader.load(path)

run_loader(CSVLoader(), "file.csv")
run_loader(JSONLoader(), "file.json")
```

Each loader can be **substituted** without affecting the pipeline logic — this is LSP in action.

---
