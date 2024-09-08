"""
1. Bubble Sort: Bubble sort repeatedly steps through the list/array, compares adjacent elements, and swaps them
if they are in the wrong order. This process is repeated until the list is sorted.
Time Complexity: 
Best case:  O(n) when the list is already sorted.
Average case: O(n^2)
Worst case: O(n^2)
Space complexity: O(1) (in place sort)
"""
# Bubble sort:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # flag to check if any swapping happened in this iteration
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # if no elements were swapped, the list is already sorted
        if not swapped:
            break


numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
# [11, 12, 22, 25, 34, 64, 90]
print("Sorted list using Bubble Sort:", numbers)
# ==========================================================================================
"""
2. Selection Sort: Selection sort divides the list into two parts: sorted and unsorted.
It repeatedly selects the smallest (or Largest, depending on sorting order) element from
the unsorted part and moves it to the end of the sorted part.

Time complexity:
Best case: O(n^2)
Average case: O(n^2)
Worst case: O(n^2)
"""
# Selection Sort:


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


ls = [64, 25, 12, 22, 11]
selection_sort(ls)
print("Sorted list using Selection Sort:", ls)  # [11, 12, 22, 25, 64]
# ==========================================================================================
"""
3. Insertion Sort: Insertion Sort builds the final sorted array one item at a time. It picks each element and inserts
it into its correct position in the already sorted portion of the array.

Time Complexity:
Best case: O(n) (when the list is already sorted)
Average case: O(n^2)
Worst Case: O(n^2)

Space Complexity: O(1) (in-place Sort)
"""
# Insertion Sort:


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key


# Example usage
num = [12, 11, 13, 5, 6]
insertion_sort(num)
print("Sorted list using Insertion Sort:", num)  # [5, 6, 11, 12, 13]

"""
4. Merge sort: Merge Sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts
each half and the merges the sorted halves back together.

Time Complexity:
Best Case: O(nlogn)
Average case: O(nlogn)
Worst case: O(nlogn)

Space Complexity: O(n) (Due to auxiliary space required for merging)
"""
# Merge Sort:


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    first = merge_sort(arr[mid:])
    last = merge_sort(arr[:mid])
    i = j = 0
    res = []
    while i < len(first) and j < len(last):
        if first[i] <= last[j]:
            res.append(first[i])
            i += 1
        else:
            res.append(last[j])
            j += 1
    res.extend(first[i:])
    res.extend(last[j:])
    return res


# With Merge sort the time complexity for best case O(nlog2n) n*logn base 2
# https://www.w3schools.com/dsa/dsa_timecomplexity_mergesort.php

# Example usage
nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print("Sorted list using Merge Sort:", nums)  # [3, 9, 10, 27, 38, 43, 82]

"""
5. Quick Sort: Quick sort is another divide-and-conquer algorithm that selects a 'pivot' element from the array
and partitions the other elements into two sub-arrays, according to whether they are less than or greater the pivot.

Time Complexity:
Best case: O(nlogn)
Average case: O(nlogn)
Worst case: O(n^2) (when the smallest or largest element is always chosen as the pivot)

Space Complexity: O(logn) (due to recursive calls)
"""

ls = [37, 25, 43, 3]
res = merge_sort(ls)
print(res)

# Quick sort


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# With Quick sort the time complexity for best case O(nlogn) and worst case O(n^2)
# https://www.w3schools.com/dsa/dsa_timecomplexity_quicksort.php
arr = [35, 29, 10, 43]
res = quick_sort(arr)
print(res)

"""
6. Heap Sort: Heap sort uses a binary heap data structure to manage the data. It first builds
a max-heap and then repeatedly extracts the maximum element, maintaining  the heap property 
until all elements are sorted.

Time Complexity:
Best case: O(nlogn)
Average case: O(nlogn)
Worst case: O(n logn)

Space Complexity: O(1) (in-place sort)
"""


"""
Summary of Sorting Techniques:
-----------------------------------------------------------------------------------------
| Sorting Algorithm	 Best Case	Average Case	Worst Case	Space Complexity	Stability|
-----------------------------------------------------------------------------------------
| Bubble Sort	     O(n)	     O(n²)	         O(n²)	      O(1)	             Yes     |
-----------------------------------------------------------------------------------------
| Selection Sort	 O(n²)	     O(n²)	         O(n²)	      O(1)	             No      |
-----------------------------------------------------------------------------------------
| Insertion Sort	 O(n)	     O(n²)	         O(n²)	      O(1)	             Yes     |
-----------------------------------------------------------------------------------------
| Merge Sort	     O(n log n)	 O(n log n)	     O(n log n)	  O(n)	             Yes     |
-----------------------------------------------------------------------------------------
| Quick Sort	     O(n log n)	 O(n log n)	     O(n²)	      O(log n)	         No      |
-----------------------------------------------------------------------------------------
| Heap Sort	         O(n log n)	 O(n log n)	     O(n log n)	  O(1)	             No      |
-----------------------------------------------------------------------------------------

Conclusion:
----------
These examples provide a basic understanding of how different sorting algorithms work, 
their implementations in Python, and their time and space complexities. Choosing the right 
sorting algorithm depends on the specific requirements, such as stability, space limitations, 
and the expected size and distribution of the data.
"""
