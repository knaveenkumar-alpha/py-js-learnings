
# Python Design Patterns Explained

## 🏭 1. Factory Pattern

**Definition**:  
The Factory Pattern provides a way to create objects without specifying the exact class of object that will be created. It uses a factory method to create objects in a superclass but allows subclasses to alter the type of objects that will be created.

**Use Case**:  
When you need to create objects without knowing the exact class or when the object creation logic is complex.

**Example**:
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal")
```

---

## 🔂 2. Singleton Pattern

**Definition**:  
The Singleton Pattern ensures that a class has only one instance and provides a global access point to that instance.

**Use Case**:  
Used for resources like configuration, logging, thread pool, etc., where a single point of access is needed.

**Example**:
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## 🎛️ 3. Facade Pattern

**Definition**:  
The Facade Pattern provides a simplified interface to a complex subsystem. It decouples the client from the subsystem.

**Use Case**:  
When you want to provide a simplified interface to a complex set of classes.

**Example**:
```python
class CPU:
    def freeze(self): print("CPU Freeze")
    def jump(self): print("CPU Jump to boot sector")
    def execute(self): print("CPU Execute")

class Memory:
    def load(self): print("Memory Load boot program")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()

    def start(self):
        self.cpu.freeze()
        self.memory.load()
        self.cpu.jump()
        self.cpu.execute()
```

---

## 🔌 4. Adapter Pattern

**Definition**:  
The Adapter Pattern allows incompatible interfaces to work together. It wraps an existing class with a new interface.

**Use Case**:  
When you want to use a class but its interface does not match your needs.

**Example**:
```python
class EuropeanSocket:
    def voltage(self): return 230

class Adapter(EuropeanSocket):
    def power_110v(self): return f"Converted to {self.voltage() / 2}V for US device"
```

---

## 👀 5. Observer Pattern

**Definition**:  
The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified automatically.

**Use Case**:  
Useful in event-driven systems, GUI toolkits, real-time notifications.

**Example**:
```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

class Observer:
    def update(self, message):
        print(f"Received message: {message}")
```
