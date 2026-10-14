"""
1. Class with __init__ and Instance Methods. Create Object and Get Methods
How do you create a class in Python with an __init__ method and instance methods? Show how to create 
an object and call the instance methods.
eg:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# Create an object
person = Person("John", 30)

# Call the instance method
print(person.greet())

2. Lambda Function to Show Even Numbers Using filter Function
How can you use a lambda function with the filter function to get even numbers from a list?

code:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6, 8, 10]

3. Different Models in Django
Q: What are the different types of models in Django?
In Django, all models are Python classes that represent database tables. However, there are some specific 
types of models:

Regular models: The default Django model that maps to a single database table.
Abstract base models: These models do not create a database table but can be inherited by other models 
                      to reuse fields and methods.
Multi-table inheritance models: Allow inheritance between models with each model corresponding to its own 
                                table.
Proxy models: These do not create new database tables but allow you to add extra methods or modify behavior
              of an existing model.

4. Advantages and Disadvantages of Django
Q: What are the advantages and disadvantages of using Django?
Advantages:

Batteries-included: Django provides built-in features like authentication, admin interface, and ORM.
Security: Django has built-in protection against common security vulnerabilities (e.g., SQL injection, 
cross-site scripting).
Scalability: Django is designed to handle high-traffic websites.
Community Support: A large, active community with extensive documentation and third-party packages.
Disadvantages:

Monolithic: Django follows a monolithic architecture which may be too rigid for certain projects.
Learning curve: Django’s "magic" can be overwhelming for beginners.
Performance overhead: While Django is suitable for most applications, it may have performance limitations 
for extremely high-performance systems compared to lightweight frameworks like Flask.

5. Flask vs Django
Q: How does Flask differ from Django?
Architecture: Flask is lightweight and follows a micro-framework architecture. Django is a full-stack 
              framework with "batteries-included".
Flexibility: Flask provides more flexibility by allowing developers to choose their tools, while Django 
             provides a structured framework.
Use case: Flask is ideal for small applications or microservices, while Django is suitable for large, 
          complex projects that require an admin panel and built-in features.
Community: Django has a larger community and more built-in features, while Flask provides more minimalism
           and control.

6. SQL Injection Attacks
Q: What is an SQL injection attack?
SQL injection is a code injection technique that allows an attacker to execute arbitrary SQL queries on a 
database. It occurs when user input is improperly sanitized and injected into a SQL query, giving the 
attacker the ability to manipulate the query and potentially extract sensitive data or modify the database.

7. How to Resolve Performance Issues in Django
Q: What steps can be taken to resolve performance issues in Django?

Database optimization: Use database indexing, denormalization, and query optimization.
Caching: Implement caching using Django’s cache framework with services like Redis or Memcached.
Lazy loading: Avoid loading unnecessary data by using lazy evaluation techniques 
             (e.g., select_related, prefetch_related for ORM queries).
Use async: For high-concurrency tasks, Django 3.1+ supports asynchronous views.
Load balancing: Scale the application using load balancers and horizontally distribute traffic.
Compression: Compress static files (CSS/JS) and use Gzip for HTTP responses.

8. How Django Is Loosely Coupled
Q: How does Django ensure loose coupling between components?
Django follows the principle of loose coupling by:

MTV Architecture: The models, templates, and views in Django are independent and can be modified or 
replaced without affecting the others.
Reusable apps: Django encourages modular and reusable apps that can function independently across projects.
Middleware: Django's middleware stack allows each layer to operate independently, providing flexibility in 
adding or removing layers without disrupting the entire system.

9. Proxy Model in Django
Q: What is a proxy model in Django?
A proxy model in Django is a subclass of an existing model that allows you to change the behavior of the 
model without modifying its fields or creating a new database table. You can add custom methods or change 
the default ordering, but the proxy model shares the same database table as the original model.
Example:
class BaseModel(models.Model):
    name = models.CharField(max_length=100)

class BaseModelProxy(BaseModel):
    class Meta:
        proxy = True
        ordering = ['name']

10. Python Multi-threading Disadvantages
Q: What are the disadvantages of Python multi-threading?

Global Interpreter Lock (GIL): In CPython, the GIL prevents multiple native threads from executing 
                               Python bytecodes at once, meaning Python threads are not true parallel 
                               execution threads in CPU-bound tasks.
Complexity: Managing thread synchronization (e.g., using locks) can add complexity and lead to issues 
            like deadlocks.
Inefficiency for CPU-bound tasks: Due to GIL, multi-threading is inefficient for CPU-bound operations, 
                                  and multi-processing is preferred for these cases.
Debugging challenges: Multi-threaded applications are harder to debug due to potential race conditions, 
                      deadlocks, and unpredictable behavior.


"""