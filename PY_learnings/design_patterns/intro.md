### Design Patterns -- Easy to remember Definitions
## Factory Pattern:
    Def: A class that creates objects for you, so you don't use `new` directly. You ask the factory 'give me a product/object'
    --> it decides which concrete class to give you.
    One-liner: Don't call `new` yourself --> ask the factory for the right object.

**Example**:
```python
from abc import ABC, abstractmethod

class Payment:
    @abstractmethod
    def pay(self):
        ...

class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} via UPI"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} via Card"

class PaymentFactory:
    @staticmethod
    def create(method):
        if method == "upi":
            return UPIPayment()
        elif method == "card":
            return CardPayment()
        raise ValueError("Unknown animal")


p = PaymentFactory.create("upi")
p.pay(500)

```

## Singleton Pattern
    def: A class that allows only one instance of itself to exist, and provides a single global access point to it.
    Analogy: A country has only one President at a time. Everyone accesses the same person through the same office.
    One-liner: Only one instance. Everyone shares it.

**Example**:
```python

class Database:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Connecting to DB...")
        return cls._instance


a = Database()
b = Database()

print(a is b)  # true
```

## Facade Pattern
    def: A single simple interface that hides the complexity of a whole subsystem(many classes working together)
    analogy: like pressing a power button --> one call triggers a whole sequence of complex operations hidden behind the facades.
    one-liner: One simple front door that hides a complex system.

**Example**:
```python
class CPU:
    def freeze(self): 
        return "CPU: freeze"
    
    def jump(self):
        return "CPU: jump to boot address"

class Memory:
    def load(self):
        return f"Memory: loading OS"

class HardDrive:
    def read(self):
        return "HardDrive: reading data"

class Computer:
    def __init__(self):
        self.cpu, self.ram, self.hdd = CPU(), Memory(), HardDrive()
    
    def start(self):
        self.cpu.freeze()
        self.ram.load()
        self.hdd.read()
        self.cpu.jump()
    
```

## Adapter Pattern
    def: Converts the interface of one class into another interface the client expects --> making incompatible classes work together.
    analogy: A travel adapter for your phone charger. The wall socket(US plug) doesn't match your device (EU plug) --> the adapter bridge them.
    one-liner: A translator/plug-converter between two incompatible interfaces.

**Example**:
```python
class LegacyPrinter:
    def print_old_format(self, text):
        return f"[OLD] format {text}"

class ModernPrinter:
    def printing(self, text):
        return f"Printing {text}"

class PrinterAdapter(ModernPrinter):
    def __init__(self, legacy):
        self.legacy = legacy

    def printing(self, text):
        self.legacy.print_old_format(text)

adapter = PrinterAdapter(LegacyPrinter())
adapter.print("Hello!")

## Like a phone charger travel adapter --same electricity, different plug shape. Client talks to the new interface only.
```

## Observer Pattern
    def: One-to-many dependency --when one object changes state, all its dependents are automatically notified.
    analogy: YouTube subscribe button. One channel (subject) publishes; thousands of subscribers (observers) get notified instantly.
    one-liner: One changes --> many get notified automatically.

```python

class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def upload(self, video):
        print(f"📹 Uploaded: {video}")
        for user in self.subscribers:     # notify ALL observers
            user.update(video)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, video):
        print(f"🔔 {self.name} got notified: {video}")

channel = YouTubeChannel()
channel.subscribe(Subscriber("Tara"))
channel.subscribe(Subscriber("Sara"))

channel.upload("Python Tutorial")
# 📹 Uploaded: Python Tutorial
# 🔔 Tara got notified: Python Tutorial
# 🔔 Sara got notified: Python Tutorial

## Subject maintains a list of observers and pushes updates to all of them. Real use: event systems, pub-sub, UI listeners.
```

## Decorator pattern
    def: Adds new behavior to object dynamically at runtime by wrapping it, without modifying its class. Wrappers stack like layers.
    one-liner: Wrap an object to add features layer by layer

```python

# Base component
def plain_coffee():
    return "Coffee"

# Decorators WRAP the function and ADD behavior
def add_milk(func):
    def wrapper():
        return func() + " + Milk"
    return wrapper

def add_sugar(func):
    def wrapper():
        return func() + " + Sugar"
    return wrapper

@add_sugar        # applied bottom-up
@add_milk
def order():
    return plain_coffee()

print(order())    # Coffee + Milk + Sugar

## Each decorator wraps and extends without touching the original --> like layers of toppings on coffee. Python's @decorator syntax IS is the pattern

```

## Strategy + Dependency Injection


```python
from abc import ABC, abstractmethod

# STRATEGIES — interchangeable algorithms
class RouteStrategy(ABC):
    @abstractmethod
    def route(self, a, b): ...

class FastestRoute(RouteStrategy):
    def route(self, a, b): return f"Fastest: {a} → {b}"

class ShortestRoute(RouteStrategy):
    def route(self, a, b): return f"Shortest: {a} → {b}"

# Context — strategy is INJECTED (DI), not created inside
class Navigator:
    def __init__(self, strategy: RouteStrategy):   # <-- Dependency Injection
        self.strategy = strategy

    def navigate(self, a, b):
        return self.strategy.route(a, b)

# Swap strategies at runtime!
nav = Navigator(FastestRoute())
print(nav.navigate("Home", "Office"))   # Fastest: Home → Office

nav.strategy = ShortestRoute()          # swapped, no code change!
print(nav.navigate("Home", "Office"))   # Shortest: Home → Office

```

| Pattern     | Keyword  | Remember as                      |
| ----------- | -------- | -------------------------------- |
| Factory     | Create   | "Who makes it? The factory."     |
| Singleton   | One      | "Only one exists."               |
| Facade      | Simplify | "One door, hidden mess."         |
| Adapter     | Convert  | "Plug converter."                |
| Observer    | Notify   | "Subscribe & notify."            |
| Decorator   | Wrap     | "Coffee toppings."               |
| Strategy/DI | Swap     | "Plug in behavior from outside." |

**Bonus tip:** Decorator and Adapter both wrap objects — the difference is why: Adapter changes the interface; Decorator adds behavior.


| Pattern     | Say this ONE sentence                                                  |
| ----------- | ---------------------------------------------------------------------- |
| Factory     | "Centralizes object creation, client says *what*, not *how*."          |
| Singleton   | "One instance ever — checked in `__new__`."                            |
| Facade      | "One simple method hiding a complex subsystem."                        |
| Adapter     | "Converts an old interface into the expected one."                     |
| Observer    | "Subject notifies all registered observers automatically."             |
| Decorator   | "Wraps an object to add behavior — Python `@` syntax is built on it."  |
| Strategy/DI | "Inject interchangeable algorithms — swap at runtime, no code change." |


**Pro tip for interviews:** when they ask "give an example," always mention a real-world use: 
Factory → payment gateways,
Singleton → DB connection,
Observer → pub-sub/Kafka,
Decorator → @login_required,
Strategy → sorting (e.g., Python's key= parameter). That shows you understand why, not just what.


