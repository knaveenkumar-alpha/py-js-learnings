"""
In Python, a lambda function is an anonymous function (i.e., a function without a name) defined using 
the lambda keyword. It can take any number of arguments, but can only have a single expression.

Syntax: lambda arguments: expression

Arguments: Inputs to the function, just like a regular function.
Expression: The logic of the function, which is evaluated and returned.

"""
# example 1 for single arg
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# exmaple for multiple args
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

# example using map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# example using filter()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

# example using reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)  # Output: 15


"""
Key Features of Lambda Functions:
=================================
Anonymous: Lambda functions do not require a name, unlike regular functions defined with def.

Concise: They can only contain a single expression, making them useful for short, simple operations.
Useful with functions like map(), filter(), and reduce(): They are often used in these higher-order 
functions for concise in-line operations.

Lambda functions are particularly helpful when you need a small function for a short period of time 
and don't want to define a full-fledged function using def.
"""

"""
Conclusion:
===========

Memory Perspective: Lambda functions are lightweight and consume slightly less memory because they 
don’t require a name or internal state. They are ideal when a simple, one-time-use function is needed.

Execution Perspective: There’s no significant performance advantage of lambda functions over regular 
functions in terms of execution speed. Their primary benefit is readability and convenience for short, 
concise operations.
"""