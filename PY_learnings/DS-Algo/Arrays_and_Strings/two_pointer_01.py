# leetcode Move Zeroes
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Two Pointers:
Container With Most Water
3Sum
Valid Palindrome
Merge Sorted Arrays

"""
def movezeroes(nums):
    left = 0  # Pointer for the position to place the next non-zero element
    right = 0  # Pointer to traverse the array
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums

# Example usage:
nums = [0, 1, 0, 3, 12]
print(movezeroes(nums))  # Output: [1, 3, 12, 0, 0]


# Time Complexity: O(n)
# Space Complexity: O(1)
nums = [0, 0, 1]
print(movezeroes(nums))  # Output: [1, 0, 0]
nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
print(movezeroes(nums))  # Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
nums = [0]
print(movezeroes(nums))  # Output: [0]


