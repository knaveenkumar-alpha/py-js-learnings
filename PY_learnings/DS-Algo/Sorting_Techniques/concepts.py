"""
What is Sorting?
----------------
Sorting is the process of arranging data in a specific order, usually in ascending or descending order. Sorting is essential in computer 
science because it helps organize data efficiently, enabling faster searches, better data analysis, and improving the performance of other 
algorithms like searching and merging.

Why is Sorting Necessary?
-------------------------
Sorting is used for several reasons:
1. Improved Data Retrieval: Sorted data allows for faster searching (e.g., using binary search).
2. Organizing Data: Sorted lists are easier to read, understand, and process.
3. Algorithm Optimization: Sorting is a fundamental operation that helps other algorithms perform better, such as searching and merging 
   in divide-and-conquer strategies.
4. Efficient Data Processing: Sorting can reduce the complexity of algorithms that depend on ordered data.

Common Sorting Techniques:
There are many sorting algorithms, each with different use cases. Here are some of the most commonly used sorting techniques
with Python code examples.
1. Bubble sort 2. Selection sort 3. Insertion sort 4. Merge sort 5. Quick sort 6. Heap sort

"""
"""
1. Bubble Sort:
Bubble Sort is one of the simplest sorting algorithms. It repeatedly steps through the list, compares adjacent elements, and swaps them 
if they are in the wrong order.

Time Complexity:
----------------
Best: O(n)
Worst and Average: O(n^2)

Space Complexity: O(1)

Use Case: Bubble Sort is rarely used in practice due to its inefficiency, but it's good for educational purposes and small datasets.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)
print("=======================================================================================")
##################################################################################################################################

"""
2. Selection Sort:
-----------------
It divides the array into two parts; a sorted and an unsorted part. It repeatedly selects the minimum element from
the unsorted part and swaps it with the first element of the unsorted part.

Time Complexity:
----------------
Best, Worst, and Average: O(n^2)
Space Complexity: O(1)

Use Case: Selection Sort is simple and performs well on small arrays but is inefficient for large datasets.

"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

ls =  [64, 25, 12, 22, 11]
selection_sort(ls)
print("Sorted array is:", ls)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")




