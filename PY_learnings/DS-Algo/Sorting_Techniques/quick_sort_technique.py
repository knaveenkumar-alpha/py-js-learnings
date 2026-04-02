"""
Quick Sort:
==========
    Quick Sort is a divide-and-conquer algorithm that works by selecting
    a pivot element from the array and partitioning the array into two 
    sub arrays, according to whether they are less than or greater than
    the pivot. The sub-array are then sorted recursively.

    Quick sort works by:
    ====================
    1. Choosing a pivot: An element from the array.
    2. Partitioning: Rearranging the array so that elements less than the pivot come before it, and elements greater than the pivot come after it.
    3. Recursively sorting: Applying the same process to the sub-arrays formed by partitioning.
"""

def quick_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)