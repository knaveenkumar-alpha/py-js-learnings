
# Dependency Inversion Principle (DIP) in Python

The **Dependency Inversion Principle (DIP)** is the "D" in SOLID principles. It states:

> **High-level modules should not depend on low-level modules. Both should depend on abstractions.**

---

## ✅ Key Ideas:
- High-level code (business logic) shouldn't rely directly on low-level implementations.
- Instead, both should depend on interfaces or abstract classes.
- This allows for flexibility, easy swapping of implementations, and better testing.

---

## ❌ Bad Example: Violates DIP

```python
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class DataFetcher:
    def __init__(self):
        self.db = MySQLDatabase()  # Tight coupling to MySQL

    def fetch(self):
        self.db.connect()
```

🎯 Problem: `DataFetcher` is tightly coupled to `MySQLDatabase`.

---

## ✅ Good Example: DIP Compliant

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

class SnowflakeDatabase(Database):
    def connect(self):
        print("Connected to Snowflake")

class DataFetcher:
    def __init__(self, db: Database):
        self.db = db  # Depends on abstraction

    def fetch(self):
        self.db.connect()
```

✅ Now `DataFetcher` works with any `Database` implementation: MySQL, Snowflake, etc.

---

## 🧪 Usage Example

```python
mysql = MySQLDatabase()
snowflake = SnowflakeDatabase()

fetcher1 = DataFetcher(mysql)
fetcher2 = DataFetcher(snowflake)

fetcher1.fetch()  # Output: Connected to MySQL
fetcher2.fetch()  # Output: Connected to Snowflake
```

---

By applying DIP, your code becomes more modular, testable, and open to extension with minimal changes.
