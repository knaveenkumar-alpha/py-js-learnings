"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

example 2:
Input: height = [1,1]
Output: 1
"""

def maxArea(height):
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        max_area = max(min(height[left], height[right]) * (right - left), max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


ls = [1,8,6,2,5,4,8,3,7]
print(maxArea(ls))