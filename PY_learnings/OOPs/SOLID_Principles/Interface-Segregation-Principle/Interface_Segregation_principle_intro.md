# Interface Segregation Principle (ISP) in Python

The **Interface Segregation Principle (ISP)** is the "I" in SOLID principles. It states:

> **Clients should not be forced to depend on interfaces they do not use.**

---

## ❌ Bad Example: Violating ISP

```python
class Worker:
    def work(self):
        pass

    def eat(self):
        pass

class Human(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")
```

🎯 **Problem**: `Robot` is forced to implement an `eat` method it doesn't need.

---

## ✅ Good Example: ISP Compliant

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class Robot(Workable):
    def work(self):
        print("Robot working")
```

✅ Now, classes implement **only the interfaces they need**.

---

## ✅ Usage Example

```python
def perform_work(entity: Workable):
    entity.work()

def take_lunch_break(entity: Eatable):
    entity.eat()

human = Human()
robot = Robot()

perform_work(human)  # Human working
perform_work(robot)  # Robot working
take_lunch_break(human)  # Human eating
# take_lunch_break(robot)  # ❌ This would raise an error
```

---

By segregating interfaces, we avoid forcing classes to implement unused behaviors — keeping our design clean and robust.

