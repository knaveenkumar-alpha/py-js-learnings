"""
Definitions:
------------
Mapping Function:
=================
A map() function applies a given function to all items in an input list (or iterable) and returns a new 
list with the results. 
In this case, it’s used to double the even numbers.

Filter Function:
================
A filter() function filters elements from an iterable based on a function that returns either True or 
False for each element. 
Here, it’s used to filter out even numbers.

Reduce Function:
================
reduce() applies a binary function (e.g., sum, product) cumulatively to the items of an iterable, reducing 
it to a single value. 
In this case, it’s used to sum up all the doubled even numbers.

"""
"""
Mapping, filtering, and reducing a list of random integers.
"""
import random
from functools import reduce  # Correct import (no underscore required)

# Functions for filtering, mapping, and reducing
def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def double(n):
    """Double the input number."""
    return n * 2


def sum_all(a, b):
    """Return the sum of two numbers."""
    return a + b


# Generating a random list of integers
l = [random.randint(1, 50) for _ in range(10)]  # Changed 'i' to '_' to indicate it is unused

# Filtering even numbers, mapping to double them, and reducing to sum the results
evens = list(filter(is_even, l))  # Using named function for readability
doubles = list(map(double, evens))  # Using named function for readability
total_sum = reduce(sum_all, doubles) if doubles else 0  # Safeguard to avoid reduce() on empty list

# Printing results
print(f"Original list: {l}")
print(f"Even numbers: {evens}, Length: {len(evens)}")
print(f"Doubled even numbers: {doubles}, Length: {len(doubles)}")
print(f"Sum of doubled even numbers: {total_sum}")
