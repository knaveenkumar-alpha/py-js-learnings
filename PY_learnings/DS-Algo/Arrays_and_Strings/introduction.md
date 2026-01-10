# **Array: Complete DSA Concept with Python**

## **What is an Array?**

An **array** is a **contiguous block of memory** that stores elements of the **same data type** in sequential order. Each element can be accessed directly using an **index**.

### **Key Characteristics:**
- **Fixed size** (in most languages, but dynamic in Python lists)
- **Contiguous memory allocation**
- **Random access** via indices (O(1) time)
- **Homogeneous elements** (same data type)

## **1. Array vs Python List**

**Python doesn't have built-in arrays** - it has **lists** which are more flexible. But we can use:
- `list` (dynamic array)
- `array` module (for primitive types)
- `numpy` arrays (for numerical computing)

```python
# Python List (Dynamic Array)
python_list = [1, 2, 3, 'hello', True]  # Can hold different types

# Array Module (Fixed type)
from array import array
int_array = array('i', [1, 2, 3, 4])  # 'i' for signed integers
float_array = array('f', [1.0, 2.0, 3.0])  # 'f' for floats

# NumPy Array (For numerical computing)
import numpy as np
numpy_array = np.array([1, 2, 3, 4], dtype=np.int32)
```

## **2. Memory Representation**

### **How arrays are stored in memory:**
```
Index:   0     1     2     3     4
Value:  10    20    30    40    50
Memory: 1000  1004  1008  1012  1016  (addresses for int, 4 bytes each)
```

Each element is stored at:  
`Base Address + (index × element_size)`

## **3. Types of Arrays**

### **A. One-Dimensional Array**
```python
# Declaration and initialization
arr = [10, 20, 30, 40, 50]

# Access
print(arr[2])  # 30
print(arr[-1]) # 50 (last element in Python)

# Traversal
for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")

for element in arr:
    print(element)
```

### **B. Multi-Dimensional Arrays**
#### **2D Array (Matrix)**
```python
# 3x3 Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, column 2
print(matrix[1][2])  # 6

# Traversal
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()

# Using numpy for better multi-dimensional arrays
import numpy as np
np_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_matrix.shape)  # (3, 3)
```

#### **3D Array**
```python
# 2x3x4 3D array
array_3d = [
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
]

print(array_3d[1][2][3])  # 24
```

## **4. Basic Operations with Time Complexity**

| Operation | Time Complexity | Python Example |
|-----------|----------------|----------------|
| Access | O(1) | `arr[3]` |
| Search (unsorted) | O(n) | `value in arr` |
| Search (sorted) | O(log n) | Binary search |
| Insert at end | O(1)* | `arr.append(10)` |
| Insert at beginning | O(n) | `arr.insert(0, 10)` |
| Delete from end | O(1) | `arr.pop()` |
| Delete from beginning | O(n) | `arr.pop(0)` |
| Update | O(1) | `arr[2] = 100` |

*Python lists have amortized O(1) for append

## **5. Complete Implementation of Array Operations**

```python
class Array:
    def __init__(self, capacity=10):
        """Initialize array with fixed capacity"""
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def __len__(self):
        """Return current size of array"""
        return self.size
    
    def __getitem__(self, index):
        """Get element at index"""
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")
    
    def __setitem__(self, index, value):
        """Set element at index"""
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")
    
    def append(self, value):
        """Add element at the end"""
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Insert element at specific index"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size == self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        
        self.data[index] = value
        self.size += 1
    
    def remove(self, index):
        """Remove element at index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]
        
        self.size -= 1
        return self.data[self.size]  # Return removed element
    
    def _resize(self):
        """Double the capacity when array is full"""
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
    
    def search(self, value):
        """Linear search for value"""
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1
    
    def reverse(self):
        """Reverse the array in-place"""
        left, right = 0, self.size - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1
    
    def __str__(self):
        """String representation"""
        return str(self.data[:self.size])

# Example usage
arr = Array(5)
arr.append(10)
arr.append(20)
arr.append(30)
arr.insert(1, 15)
print(arr)  # [10, 15, 20, 30]
print(arr[2])  # 20
arr[2] = 25
print(arr)  # [10, 15, 25, 30]
arr.remove(1)
print(arr)  # [10, 25, 30]
```

## **6. Common Array Algorithms**

### **A. Sorting Algorithms**
```python
def bubble_sort(arr):
    """Bubble Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    """Selection Sort - O(n²)"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Insertion Sort - O(n²)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    """Merge Sort - O(n log n)"""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        
        # Merge
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """Quick Sort - O(n log n) average, O(n²) worst"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)
```

### **B. Searching Algorithms**
```python
def linear_search(arr, target):
    """O(n) - works on any array"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """O(log n) - requires sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left, right):
    """Recursive binary search"""
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

## **7. Important Array Concepts**

### **A. Dynamic Array (How Python List works)**
Python lists are **dynamic arrays** that automatically resize when needed.

```python
import sys

# Demonstrate dynamic array resizing
lst = []
for i in range(10):
    print(f"Length: {len(lst):2d}, Capacity: {sys.getsizeof(lst)} bytes")
    lst.append(i)
```

### **B. Circular Array**
```python
class CircularArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.head = 0
        self.size = 0
    
    def get(self, index):
        """Get element at index (considering circular nature)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.arr[(self.head + index) % self.capacity]
    
    def append(self, value):
        """Add to the end"""
        if self.size == self.capacity:
            self._resize()
        self.arr[(self.head + self.size) % self.capacity] = value
        self.size += 1
    
    def rotate(self, k):
        """Rotate array by k positions"""
        self.head = (self.head + k) % self.capacity
    
    def _resize(self):
        """Double capacity"""
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity
        
        for i in range(self.size):
            new_arr[i] = self.arr[(self.head + i) % self.capacity]
        
        self.arr = new_arr
        self.capacity = new_capacity
        self.head = 0
```

### **C. Sparse Arrays**
Arrays where most elements are zero/default.
```python
class SparseArray:
    """Efficient representation of sparse arrays"""
    def __init__(self, default_value=0):
        self.data = {}
        self.default = default_value
    
    def __setitem__(self, index, value):
        if value == self.default:
            if index in self.data:
                del self.data[index]
        else:
            self.data[index] = value
    
    def __getitem__(self, index):
        return self.data.get(index, self.default)
    
    def __len__(self):
        return max(self.data.keys()) + 1 if self.data else 0
```

## **8. Common Array Problems**

### **Problem 1: Find Maximum Subarray Sum (Kadane's Algorithm)**
```python
def max_subarray_sum(nums):
    """Kadane's Algorithm - O(n)"""
    max_so_far = nums[0]
    max_ending_here = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```

### **Problem 2: Dutch National Flag (Sort 0s, 1s, 2s)**
```python
def sort_colors(nums):
    """Three-way partitioning - O(n)"""
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# Example
print(sort_colors([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]
```

### **Problem 3: Rotate Array**
```python
def rotate_array(nums, k):
    """Rotate array to the right by k steps - O(n)"""
    n = len(nums)
    k = k % n
    
    # Reverse entire array
    nums.reverse()
    
    # Reverse first k elements
    nums[:k] = reversed(nums[:k])
    
    # Reverse remaining elements
    nums[k:] = reversed(nums[k:])
    
    return nums

# Example
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))  # [5, 6, 7, 1, 2, 3, 4]
```

### **Problem 4: Find Missing Number**
```python
def find_missing_number(nums):
    """Find missing number from 0 to n - O(n)"""
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# XOR method (better for overflow)
def find_missing_number_xor(nums):
    """Using XOR - O(n)"""
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Example
print(find_missing_number([3, 0, 1]))  # 2
```

## **9. Array Patterns to Recognize**

1. **Two Pointers**: When you need to process elements in pairs
2. **Sliding Window**: When dealing with subarrays/substrings
3. **Prefix Sum**: For range queries and subarray sums
4. **In-place Operations**: When O(1) space is required
5. **Cyclic Sort**: When array contains numbers in a range
6. **Fast & Slow Pointers**: For cycle detection

## **10. Advantages & Disadvantages**

### **Advantages:**
1. **Fast access** - O(1) random access
2. **Memory efficiency** - contiguous memory, no overhead
3. **Cache friendly** - spatial locality
4. **Simple implementation**

### **Disadvantages:**
1. **Fixed size** (in static arrays)
2. **Costly insertions/deletions** in middle - O(n)
3. **Memory wastage** if array is partially filled
4. **Need contiguous memory block**

## **11. When to Use Arrays**

✅ **Use Arrays When:**
- You know the size in advance
- Need random access frequently
- Memory efficiency is critical
- Working with multi-dimensional data
- Implementing other data structures (stack, queue, heap)

❌ **Avoid Arrays When:**
- Size changes frequently
- Frequent insertions/deletions in middle
- Need dynamic resizing
- Memory fragmentation is a concern

## **12. Real-world Applications**

1. **Database indexing** - B-trees use arrays
2. **Image processing** - pixels stored as 2D arrays
3. **Game development** - game boards, inventories
4. **Operating systems** - process tables, file systems
5. **Machine learning** - feature vectors, matrices
6. **Audio processing** - sound samples
7. **CPU caching** - cache lines are arrays

## **Practice Problems by Difficulty**

### **Beginner:**
1. Find largest element
2. Reverse an array
3. Find second largest element
4. Move zeros to end
5. Check if array is sorted

### **Intermediate:**
1. Maximum subarray sum (Kadane's)
2. Product of array except self
3. Find duplicate number
4. Container with most water
5. Merge intervals

### **Advanced:**
1. Trapping rain water
2. Find minimum in rotated sorted array
3. Median of two sorted arrays
4. Count inversions
5. Maximum product subarray

Arrays are the **building blocks** of most data structures. Mastering arrays is essential for understanding more complex structures like linked lists, trees, graphs, and hash tables!