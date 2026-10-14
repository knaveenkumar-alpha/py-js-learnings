"""
Sliding Window Pattern

This pattern involves maintaining a window of elements and adjusting its size based on certain conditions. It is commonly used to solve problems related to arrays and strings where we need to find a subarray or substring that meets specific criteria.
problem:
- Maximum Sum Subarray of Size K
Given an array of integers and an integer k, find the maximum sum of a subarray of size k.
array = [1, 3, 2, 4, 1, 2] target sum = 6
"""
array = [1, 3, 2, 4, 1, 2]
target_sum = 6


def longest_subarray(array, target_sum):
    """
    Find the length of the longest subarray with a sum less than or equal to target_sum.

    Args:
        array (_type_): A list of integers.
        target_sum (_type_): The target sum.

    Returns:
        _type_: The length of the longest subarray.
    """
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(array)):
        current_sum += array[right]

        # Shrink the window from the left if the current sum exceeds target_sum
        while current_sum > target_sum and left <= right:
            current_sum -= array[left]
            left += 1

        # Update max_length if the current window is valid
        max_length = max(max_length, right - left + 1)

    return max_length

# Time Complexity: O(n) - Each element is visited at most once.
# Space Complexity: O(1) - Only a constant amount of space is used.

# Run the function and print the result
result = longest_subarray(array, target_sum)
print(f"Length of the longest subarray with sum <= {target_sum}: {result}")



