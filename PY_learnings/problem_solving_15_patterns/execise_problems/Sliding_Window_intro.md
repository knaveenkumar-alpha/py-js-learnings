# Sliding Window Pattern

## Overview
Sliding Window is an optimization technique that **avoids redundant computations** by maintaining a window over the dataset. It is commonly used in:

- **Finding subarrays with a given sum**
- **Maximum/minimum values in a subarray**
- **Finding the longest/shortest subarray satisfying a condition**
- **Efficient computation over contiguous sequences**

## Types of Sliding Window
### 1️⃣ Fixed-Size Sliding Window
- The window size is **constant** (e.g., `k`).
- Used when processing a fixed number of elements at a time.

### 2️⃣ Variable-Size Sliding Window
- The window **expands or shrinks** dynamically based on conditions.
- Used when the problem requires a **flexible** subarray size.

## Complexity Analysis
- **Time Complexity:** `O(n)` in most cases.
- **Space Complexity:** `O(1)` as only a few variables are maintained.

## Applications
✔️ Strings and Arrays Processing
✔️ Real-time Data Streams (e.g., Rate Limiting in APIs)
✔️ Maximum/Minimum in Subarrays
✔️ Sliding Averages, Moving Window Computations

## Example Code
### Fixed-Size Sliding Window (Maximum Sum of K Consecutive Elements)
```python
# O(n) Sliding Window Approach
def max_sum_sliding_window(arr, k):
    max_sum = float('-inf')
    window_sum = sum(arr[:k])
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_sliding_window(arr, k))  # Output: 9
```

### Variable-Size Sliding Window (Smallest Subarray with Sum ≥ S)
```python
# O(n) Variable Window Approach
def min_subarray_length(arr, S):
    min_length = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum >= S:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

arr = [2, 3, 1, 2, 4, 3]
S = 7
print(min_subarray_length(arr, S))  # Output: 2
```

## 🔥 Key Takeaways
- **Sliding Window avoids redundant computations** by maintaining a moving window.
- **Fixed-size Window** is used when the subarray size is **constant**.
- **Variable-size Window** is used when the subarray size **depends on conditions**.
- **Optimized for O(n) time complexity**, making it highly efficient.

This technique is **widely used** in real-world applications, including **network monitoring, time-series analysis, and data streaming processing**.