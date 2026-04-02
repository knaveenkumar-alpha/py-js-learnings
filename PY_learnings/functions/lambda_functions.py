""""
Lambda Function in Python:
=========================
- A lambda function is an anonymous (unnamed) function defined using the lambda keyword. It is typically used for short,
one-liner functions. It can take multiple arguments but contains a single expression.

Use cases of Lambda function:
============================
1. A small throwaway function is needed for a short duration. 
2. Used with functions like map(), filter(), and reduce() to perform operations without defining full function. 

Limitations:
===========
1. Cannot contain multiple expressions or statements. 
2. Harder to debug due to their anonymous nature. 
3. Should only be used for simple, short-term operations. 
"""
import random as rd

ls = [rd.randint(1, 10) for _ in range(15)]
print(ls)
print(f"Using Lambda function with map(): {list(map(lambda x: x**2, ls))}")
print(f"Using Lambda function with filter(): {list(filter(lambda x: x%2==0, ls))}")


"""
Difference:
==========
map()    ==> transforms each element in an iterable.
filter() ==> selects elements based on a condition.
reduce() ==> combines elements to produce a single result.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5]
# Filter even numbers, square them, and find their product
result = reduce(lambda x, y: x * y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # Output: 16 (4 squared = 16)

""" 
Can map() and filter() work with multiple iterables?
===================================================
map() can take multiple iterables and applies the given function to corresponding elements from each:
result = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
print(result)  # Output: [5, 7, 9]
filter() only works with a single iterable because it evaluates a condition on each item of the iterable.
"""
