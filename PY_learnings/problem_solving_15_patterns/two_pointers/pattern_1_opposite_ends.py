"""
Two sum II: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
array = [-3,1,4,6,9,11] target = 10
"""

# array = [-3, 1, 4, 6, 9, 11]
# target = 10
array = [3,2,4]
target = 6

def two_sum_sorted(array, target):
    """
    Find indices of two numbers in a sorted array that add up to the target.

    Args:
        array (_type_): A sorted list of integers.
        target (_type_): The target sum.

    Returns:
        _type_: A list containing the indices of the two numbers, or an empty list if not found.
    """
    left, right = 0, len(array) - 1

    while left <= right:
        total = array[left] + array[right]

        if total == target:
            return [left, right]  # found the pair
        elif total < target:
            left += 1   # sum too small --> move left pointer to up(right)
        else:
            right -= 1  # sum too large --> move right pointer to down(left)
    return []

# Time Complexity: O(n) - Each element is visited at most once.
# Space Complexity: O(1) - Only a constant amount of space is used.

# Run the function and print the result
result = two_sum_sorted(array, target)
print(result)

"""
if the array is not sorted, we can use a hash map to store the indices of the elements and check for the complement of 
each element in the hash map. This approach has a time complexity of O(n) and space complexity of O(n).

"""

def two_sum_unsorted(array, target):
    """
    Find indices of two numbers in an unsorted array that add up to the target.

    Args:
        array (_type_): An unsorted list of integers.
        target (_type_): The target sum.
    Returns:
        _type_: A list containing the indices of the two numbers, or an empty list if not found.
    """
    seen = {}  # Dictionary to store the indices of elements
    for index, num in enumerate(array):
        complement = target - num
        if complement in seen:
            return [seen[complement], index]  # found the pair
        seen[num] = index  # store the index of the current number
    return []  # no pair found

# Time Complexity: O(n) - Each element is visited at most once.
# Space Complexity: O(n) - The hash map may store up to n elements.

# Run the function and print the result
result_unsorted = two_sum_unsorted(array, target)
print("Indices of two numbers in unsorted array:", result_unsorted)
