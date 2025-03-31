"""
Merge Sort:
===========
    Merge sort is a divide-and-conquer algorithm that splits an array into two halves, 
    recursively sorts each half, and then merges the sorted halves to produce the final 
    sorted array. It's known for its efficiency and stable sorting.
Merge sort works by:
====================
1. Dividing the unsorted list into two approximately equal halves.
2. Recursively sorting each half.
3. Merging the two sorted halves to produce the sorted list.
"""

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2
    first = merge_sort(arr[:mid])
    last = merge_sort(arr[mid:])
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


# Example usage
nums = [38, 27, 3, 3, 9, 50, 82, -10, 2]
print(f"Before Merge Sort list: {nums}")
sorted_nums = merge_sort(nums)
print("Sorted list using Merge Sort:", sorted_nums)
