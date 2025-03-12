""" 
1. What are the SOLID Principles?
Answer:
SOLID is an acronym for a set of design principles aimed at writing clean, maintainable, and 
scalable code in object-oriented programming.

The principles are:

S: Single Responsibility Principle (SRP)
O: Open/Closed Principle (OCP)
L: Liskov Substitution Principle (LSP)
I: Interface Segregation Principle (ISP)
D: Dependency Inversion Principle (DIP)

"""

"""
2. Can you explain the Single Responsibility Principle (SRP)?
Answer:
A class should have only one reason to change, meaning it should have a single responsibility.
"""
# Example:
class ReportGenerator:
    def generate_report(self, data):
        print("Generating report...")

class ReportSaver:
    def save_to_file(self, report, filename):
        print(f'Saving report to {filename}...')

# Responsibilities are split between generating and saving the report. 

"""
3.What is the Open/Closed Principle (OCP)?
Answer:
Code should be Open for extension but closed for modification. This means you can add new 
functionality without altering existing code.
"""
# Example:
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass


class PercentageDiscount(Discount):
    def calculate(self, price):
        return price * 0.9


class FlatDiscount(Discount):
    def calculate(self, price):
        return price - 50

# You can add new discount classes without modifying existing ones. 

""" 
4. What is the Liskov Substitution Principle (LSP)?
Answer:
It states that a subclass should be substitutable for its parent class without altering the behavior
or correctness of the program.  

"""
class Bird:
    def move(self):
        print("Moving...")

class FlyingBird(Bird):
    def fly(self):
        print("Flying high!")

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird):
    def move(self):
        print("Running on the ground!")

# Usage
sparrow = Sparrow()
sparrow.fly()  # Output: Flying high!

ostrich = Ostrich()
ostrich.move()  # Output: Running on the ground!


""" 
5. What is the interface Segregation Principle (ISP)?
Answer:
Classes should not be forced to implement interfaces they don't use. 
"""
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
        print("Working...")

    def eat(self):
        print("Eating...")

class Robot(Workable):
    def work(self):
        print("Robot is working.")

""" 
6. What is the Dependency Inversion Principle (DIP):
Answer:
High-level modules should not depend on low-level modules. Both should depend on abstractions. 

"""
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}...")

class PaymentService:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def process(self, amount):
        self.processor.process_payment(amount)

# Dependency Injection
processor = CreditCardProcessor()
service = PaymentService(processor)
service.process(100)

""" 
7. Why are SOLID Principles important?
Answer:
1. Encourages reusable and scalable code. 
2. Improves code readability and maintainability. 
3. Reduces code rigidity, fragility, and unnecessary dependencies. 

"""
