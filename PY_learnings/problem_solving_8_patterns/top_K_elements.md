# Top K Elements Pattern in Python (Without Built-ins like heapq or Counter)

The **Top K Elements** pattern can also be implemented manually using a **heapify** approach without relying on Python built-ins like `heapq` or `collections.Counter`.

## 🔧 Common Use Cases
- Top K frequent elements
- Kth largest/smallest number
- Sort characters by frequency
- Top K numbers in a stream

---

## ✅ Manual Techniques

### 1. **Manual Min-Heap Implementation**
```python
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def find_k_largest(nums, k):
    heap = nums[:k]
    build_min_heap(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heap[0] = num
            heapify(heap, k, 0)
    return heap


def top_k_frequent(nums, k):
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    items = list(freq_map.items())[:k]
    build_min_heap(items)

    for item in list(freq_map.items())[k:]:
        if item[1] > items[0][1]:
            items[0] = item
            heapify(items, k, 0)

    return [item[0] for item in items]


💡 Tips
Manual heapify gives more control but requires more code.
Best when built-in libraries are restricted.
Good for understanding heap behavior from scratch.
Practice problems: Leetcode 347, 215, 703, 451

📘 Example Problem: Kth Largest Element

def find_kth_largest(nums, k):
    top_k = find_k_largest(nums, k)
    return min(top_k)
This version returns the Kth largest number using a manually implemented heap.

