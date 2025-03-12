""" 
In Python, data types are categorized as mutable or immutable based on whether their value can be modified after they are created.

Mutable Data Types:
===================
These data types allow changes to their content without changing their identity (memory location).
ex: List, Dict, Set, and Bytearry. 

Immutable Data Types:
====================
These data types do not allow modifications. Any change results in the creation of a new object.
ex: String, Tuple, Integer, Float, Boolean, and Bytes. 
"""
# List
my_list = [1, 2, 3]
print(my_list, id(my_list))
my_list[0] = 0  # Modifies the first element
print(my_list, id(my_list))  # Output: [0, 2, 3]

# Dict
my_dict = {'a': 1, 'b': 2}
print(my_dict, id(my_dict))
my_dict['a'] = 10  # Updates the value for key 'a'
print(my_dict, id(my_dict))  # Output: {'a': 10, 'b': 2}

# Set
my_set = {1, 2, 3}
print(my_set, id(my_set))
my_set.add(4)  # Adds an element
print(my_set, id(my_set))  # Output: {1, 2, 3, 4}

print("=================================================")

# String
my_string = "hello"
print(my_string, id(my_string))
my_string = my_string + " world"  # Creates a new string object
print(my_string, id(my_string))  # Output: "hello world"

# tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 0  # Raises a TypeError since tuples are immutable

#Integer
a = 10
print(a, id(a))
a = a + 1  # Creates a new integer object
print(a, id(a))  # Output: 11


