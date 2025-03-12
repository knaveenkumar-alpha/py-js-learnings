"""
Generator:
    A Generator in python is a special type of function that returns an iterator. Unlike a normal
    function, which returns a single value and terminates, a generator yields multiple
    values one at a time using the 'yield' Keyword.
    Generators are used to create iterators in memory-efficient way because they do not store
    the entire sequence in memory but generate values on demand.

Why Use Generators?
    Memory Efficiency – Since generators produce values on demand, they do not store the entire sequence 
        in memory.
    Lazy Evaluation – Generators do not compute all values at once; they compute the next value only when 
        requested.
    Improved Performance – Since generators avoid storing all values in memory, they work efficiently 
        for large datasets.
    Simplifies Code – Writing a generator is often easier than implementing an iterator class manually.

"""
gen_expr = (x**2 for x in range(10))
print(list(gen_expr))
# Instead of storing all values in memory, it yields values one at a time.

"""
Feature	         List	                               Generator
==================================================================================================
Memory Usage	 Stores all values in memory	       Generates values on demand (saves memory)
Performance	     Slower for large datasets	           Faster and more efficient
Syntax	         Uses []	                           Uses yield
Usage	         Useful when all values are needed	   Best for large or infinite sequences
==================================================================================================

✅ Generators are special functions that use yield instead of return.
✅ They generate values on demand, saving memory and improving performance.
✅ They are useful for working with large datasets, streams, and infinite sequences.
✅ They pause execution at yield, remembering their state for the next call.

"""

