# Modified Binary Search Pattern

## Introduction
Modified Binary Search is an extension of the classic Binary Search algorithm that allows solving a variety of problems beyond just finding an element in a sorted array. By tweaking the search conditions, this technique helps in solving problems like:

- Finding the first or last occurrence of an element
- Searching in a rotated sorted array
- Finding an element’s position in an infinite sorted array
- Searching in nearly sorted arrays

## Key Concept
Binary Search operates on a sorted collection by repeatedly dividing the search space into two halves. The modified versions tweak the conditions to fit different problem statements.

**Time Complexity:** O(log n) in most cases.

---

## Example Problems

### 1. Find First and Last Position of an Element
#### Problem Statement
Given a sorted array, find the first and last occurrence of a target element.

#### Implementation
```python
from typing import List

def find_first_last(nums: List[int], target: int) -> List[int]:
    def binary_search(left=True):
        low, high = 0, len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                if left:
                    high = mid - 1  # Move left
                else:
                    low = mid + 1   # Move right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index

    return [binary_search(left=True), binary_search(left=False)]

# Example Usage
nums = [5,7,7,8,8,10]
target = 8
print(find_first_last(nums, target))  # Output: [3, 4]
```

---

### 2. Search in a Rotated Sorted Array
#### Problem Statement
Given a rotated sorted array, find the index of a target element.

#### Implementation
```python
def search_rotated(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:  # Left side is sorted
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# Example Usage
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated(nums, target))  # Output: 4
```

---

### 3. Find Minimum in Rotated Sorted Array
#### Problem Statement
Find the minimum element in a rotated sorted array.

#### Implementation
```python
def find_min(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

# Example Usage
nums = [3,4,5,1,2]
print(find_min(nums))  # Output: 1
```

---

## Summary
- **Standard Binary Search:** O(log n) complexity to find an element in a sorted array.
- **Finding First/Last Position:** Modify search direction upon finding the target.
- **Rotated Sorted Array Search:** Adjust conditions to determine which half is sorted.
- **Finding Minimum in Rotated Array:** Use binary search to locate the smallest element.

These modifications make **Binary Search** applicable to a wide range of problems, improving efficiency significantly!

