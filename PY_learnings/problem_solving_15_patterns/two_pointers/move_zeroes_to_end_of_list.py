"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

example1: 
input: [0,1,0,3,12]

output: [1,3,12,0,0]
"""

def moveZeroes(nums):
    # Initialize a pointer to track the position of the next non-zero element
    left = 0
    
    # Iterate through the array
    for right in range(len(nums)):
        # If the current element is not zero, swap it with the element at the left pointer
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

# Time Complexity: O(n) - Each element is visited at most once.
# Space Complexity: O(1) - Only a constant amount of space is used.

# Run the function and print the result
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print("Array after moving zeroes to the end:", result)