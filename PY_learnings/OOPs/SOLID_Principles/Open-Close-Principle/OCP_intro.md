
# Open/Closed Principle (OCP) in Python

The **Open/Closed Principle (OCP)** is the **"O"** in **SOLID** principles. It states:

> **Software entities (classes, modules, functions) should be open for extension but closed for modification.**

## 🧠 What It Means

- You **shouldn't have to change existing code** to add new features.
- Instead, you **extend** behavior through **inheritance**, **composition**, or **polymorphism**.

---

## ❌ Bad Example: Violating OCP

```python
class DiscountCalculator:
    def calculate(self, customer_type, amount):
        if customer_type == "regular":
            return amount * 0.95
        elif customer_type == "vip":
            return amount * 0.90
        elif customer_type == "employee":
            return amount * 0.85
        else:
            return amount
```
🎯 **Problem**: Every time a new customer type is added, you must **modify** this class.

---

## ✅ Good Example: OCP Compliant with Python (Using Strategy Pattern)

```python
from abc import ABC, abstractmethod

# Define base strategy
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

# Define individual strategies
class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.95

class VipCustomerDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.90

class EmployeeDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.85

# Main calculator, open for extension, closed for modification
class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate(self, amount):
        return self.strategy.apply_discount(amount)
```

### ✅ Usage Example

```python
amount = 1000

vip_discount = DiscountCalculator(VipCustomerDiscount())
print(vip_discount.calculate(amount))  # Output: 900.0

employee_discount = DiscountCalculator(EmployeeDiscount())
print(employee_discount.calculate(amount))  # Output: 850.0
```

---

## 📌 Real-World Use Case: ETL Logging

You could use the Open/Closed Principle to support multiple logging strategies:

- File Logger
- Database Logger
- Snowflake Logger

Each logger implements the same interface, but no changes are made to the main ETL logic — you just **plug in** the logger you need.

---
