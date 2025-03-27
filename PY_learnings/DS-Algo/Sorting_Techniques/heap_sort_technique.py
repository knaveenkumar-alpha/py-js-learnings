"""
Heapify:
========
    Heapify is the process of converting a binary tree into a heap. It ensures that the tree satisfies the heap
    property, where each parent node is greater than or equal to its child nodes(For a Max Heap)

Heap Sort:
==========
    Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure. It works by building
    a max heap from the input data, then repeatedly extracting the maximum element from the heap and rebuilding the
    heap until all elements are sorted.

Priority Queue:
===============
    A Priority Queue is an abstract data type similar to a regular queue, but each element has a priority associated
    with it. Elements with higher priority are dequeued before elements with lower priority.

"""

def heapify(arr, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[root] < arr[left]:
        root = left
    if right < n and arr[root] < arr[right]:
        root = right
    if root != i:
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, n, root)


def heap_sort(ls):
    n = len(ls)
    for i in range(n//2 - 1, -1, -1):
        heapify(ls, n, i)

    for j in range(n-1, 0, -1):
        ls[j], ls[0] = ls[0], ls[j]
        heapify(ls, j, 0)
    return ls

ls = [12, 11, 13, 5, 6, 7]
print(f"Array: {ls}")
arr = heap_sort(ls)
print("Sorted array is:", arr)


