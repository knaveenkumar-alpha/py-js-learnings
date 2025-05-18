## Single Responsibility Principle(SRP):
'''
The Single Responsibility Principle states that, A class should have only one reason to change, 
meaning it should only have one responsibility or one Job. In SOLID Principle 'S' is a Single Reponsible
principle.
'''

class Report:
    def __init__(self, data):
        self.data = data
    
    def generate_report(self):
        return f"Report Data: {self.data}"
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f_data:
            f_data.write(self.generate_report())


"""
#### Problem:
The Report class has two responsibilities.
1. Generating report content.
2. Saving it to a file.
This results in our code being highly coupled and makes it harder to understand, maintain, and test.
The Report class has two responsibilities.
"""
## With Single Responsibility Principle

class Report:
    def __init__(self, data):
        self.data = data
    
    def generate_report(self):
        return f"Report Data: {self.data}"


class ReportSaver:
    def save_to_file(self, report:Report, filename:str):
        with open(filename, 'w') as fdata:
            fdata.write(report.generate_report())


""" 
Why should we do:
1. Easier to maintain
2. Easier to test each part independently
3. Fewer bugs when requirements changes. 
"""

class Order:
    def __init__(self):
        self.items = []
        self.quatities = []
        self.prices = []
        self.status = "open"
    
    def add_item(self, name:str, quatity:int, price:float) -> None:
        self.items.append(name)
        self.quatities.append(quatity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for quantity, price in zip(self.quatities, self.prices):
            total += quantity * price
        return total
    
    def pay(self, payment_type:str, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
order.pay("debit", "0372846")

""" 
This code violates the SRP because it is both responsible for managing the order 
and the payment. This results in our code being highly coupled and makes it harder
to understand, maintain, and test.
"""

## Let’s refactor this code to adhere to the SRP.

class Order:
    def __init__(self):
        self.items = []
        self.quatities = []
        self.prices = []
        self.status = "open"
    
    def add_item(self, name:str, quantity:int, price:float) -> None:
        self.items.append(name)
        self.quatities.append(quantity)
        self.prices.append(price)


class PaymentProcessor:
    def pay(self, order:Order, security_code:str):
        print("Processing payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()

order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

processor = PaymentProcessor()
processor.pay(order, "0372846")
print(order.status)
