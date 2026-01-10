Great! Let’s move forward with **Day 4** and **Day 5** of your DSA Week 1 plan — focused on **reversing arrays** and understanding **array search/insert/delete techniques**. Each day is structured to fit within your 1-hour study time, with **layman explanations + Python examples + exercises**.

---

## 📅 **Week 1 – Day 4: Reverse an Array (Two-Pointer Method)**

---

### 🧠 **Goal for Today**

* Understand the **two-pointer technique**
* Reverse an array **without using extra space**
* Build a base for solving more advanced problems later

---

### 🔸 What is the Two-Pointer Technique?

> Imagine two friends standing at **opposite ends of a line** of people. They walk towards each other and swap items until they meet.

📌 In arrays:

* Use **two indices** (start and end)
* Swap values and move pointers inward

---

### 🔹 Reversing Array Using Two Pointers

```python
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap
        arr[left], arr[right] = arr[right], arr[left]
        # Move pointers
        left += 1
        right -= 1

    return arr

# Example
nums = [1, 2, 3, 4, 5]
print(reverse_array(nums))  # Output: [5, 4, 3, 2, 1]
```

🧠 Time Complexity: **O(n)**
🧠 Space Complexity: **O(1)** (no extra list used)

---

### 🔍 Why Not Use Python's Built-in `[::-1]`?

```python
arr[::-1]  # One-liner, yes! But...
```

* ✅ It’s easy
* ❌ But it **creates a new list**, so not space-efficient for interviews

---

### 🧪 Mini Practice Tasks

1. Reverse `[10, 20, 30, 40]` using a loop
2. Write your own `reverse_array()` function
3. Try it with an empty list and a list of 1 element
4. Bonus: Modify it to return **new list** without changing the original

---

## ✅ Recap: Day 4 Key Points

| Concept       | Value                   |
| ------------- | ----------------------- |
| Method        | Two-pointer technique   |
| Complexity    | Time: O(n), Space: O(1) |
| Why important | Common in 100+ problems |

---

## 📅 **Week 1 – Day 5: Searching, Inserting, Deleting in Arrays**

---

### 🧠 **Goal for Today**

* Practice how to **search**, **insert**, and **delete** values from arrays **manually** (not using built-in methods)

---

### 🔸 1. **Linear Search** (Find an element)

> Go through each item one-by-one until you find your target.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([1, 2, 3, 4], 3))  # Output: 2
```

🧠 Time Complexity: **O(n)**
🧠 Space: O(1)

---

### 🔸 2. **Insert at Specific Index** (Manual)

```python
def insert_at_index(arr, index, value):
    arr.append(0)  # Add dummy to increase length
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]  # Shift right
    arr[index] = value
    return arr

print(insert_at_index([1, 2, 3], 1, 99))  # [1, 99, 2, 3]
```

🧠 Time: O(n) — elements must be shifted

---

### 🔸 3. **Delete by Index**

```python
def delete_at_index(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]  # Shift left
    arr.pop()  # Remove last extra copy
    return arr

print(delete_at_index([1, 2, 3, 4], 2))  # [1, 2, 4]
```

---

### 🧪 Mini Practice Tasks

1. Write a function to find if an element exists in list
2. Insert 77 at index 3 in `[10, 20, 30, 40, 50]`
3. Delete the item at index 2
4. Try insert/delete on edge cases (start, end, empty list)

---

## ✅ Recap: Day 5 Key Points

| Operation | Method Used           | Time Complexity |
| --------- | --------------------- | --------------- |
| Search    | Linear Search         | O(n)            |
| Insert    | Manual shift & insert | O(n)            |
| Delete    | Manual shift & pop    | O(n)            |

---

## 🏁 **End of Week 1 Preview**

You're now equipped with:

* Time/space analysis
* List fundamentals
* Array traversal
* In-place reversal
* Manual insert/delete/search

---

Would you like me to prepare a **Weekend Revision Plan (Sat & Sun, 2 hours each)** for reviewing these 5 days + solving real problems?
