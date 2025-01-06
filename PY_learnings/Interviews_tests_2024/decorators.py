"""
Decorator:
----------
def:
In Python, a decorator is a function that takes another function as argument and extends its behavior 
without explicitly modifying it. Decorators are commonly used to add additional functionality to functions, 
such as logging, timing, or checking preconditions.

Basic Structure of a Decorator
A decorator typically takes a function, adds some code (before or after the original function is executed),
and returns a new function.

Example of a Simple Decorator
Let’s create a decorator that logs the execution time of a function.

"""
import time

# Define the decorator function
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record end time
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper  # Return the wrapped function

# Use the decorator on a function
@timer_decorator
def slow_function():
    print("Function is running...")
    time.sleep(2)  # Simulate a slow function

# Call the decorated function
slow_function()


# Another Example: Decorator with Arguments
# Here’s an example of a decorator that accepts arguments to control its behavior.

def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(times=3)
def greet(name):
    print(f"Hello, {name}!")

# Call the decorated function
greet("Naveen Kumar")


