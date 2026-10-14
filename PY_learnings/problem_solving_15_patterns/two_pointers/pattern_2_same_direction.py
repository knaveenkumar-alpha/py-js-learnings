"""
This module contains implementations of the two pointers method, 
a common technique used in solving problems related to arrays and strings.
The two pointers method involves using two indices to traverse the data 
structure, allowing for efficient solutions to various problems such as 
finding pairs, triplets, or subarrays that meet certain criteria.

problem-solving patterns:
1. Two Pointers - Opposite Ends: This pattern involves using two pointers that start at
2. Two Pointers - Same Direction: This pattern involves using two pointers that move in the same direction, often used for problems involving subarrays or substrings.
3. Two Pointers - Fast and Slow: This pattern involves using one pointer that moves faster than the other, often used for problems involving cycles or linked lists.

example problems:
- Remove Duplicates from Sorted Array
- Move Zeroes
- Valid Palindrome
"""
"""Remove Duplicates from Sorted Array in place: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
array = [1,1,2,2,3,4,4] slow builds unique prefix, fast scans through the array
"""

array = [1, 1, 2, 2, 3, 4, 4]

def remove_duplicates(array):
    """
    Remove duplicates from a sorted array in place.

    Args:
        array (_type_): A sorted list of integers.
    Returns:
        _type_: The new length of the array after removing duplicates.
    """
    if not array:
        return 0

    slow = 0  # Pointer for the position of the last unique element

    for fast in range(1, len(array)):
        if array[fast] != array[slow]:
            slow += 1
            array[slow] = array[fast]  # Move unique element to the front

    return slow + 1  # New length is slow index + 1

# Time Complexity: O(n) - Each element is visited at most once.
# Space Complexity: O(1) - Only a constant amount of space is used.

# Run the function and print the result
new_length = remove_duplicates(array)
print("New length after removing duplicates:", new_length)
print("Array after removing duplicates:", array[:new_length])
