Absolutely! Here’s your **Week 1 – Day 3** of the DSA study plan — focused on **Arrays** (Traversal, Insertion, and Deletion) using Python, explained in **layman terms** and tailored for **1 hour** of study.

---

## 📅 **Week 1 – Day 3: Arrays – Traversal, Insertion & Deletion**

---

### 🧠 **Goal for Today**

* Understand what arrays are in coding.
* Learn how to access, insert, and delete elements.
* Practice basic operations using Python lists.

---

## 🔸 What is an Array? (Layman Explanation)

> Imagine a **row of mailboxes**, each with a number on it and a value inside.
> An **array** is just like that: a group of **data items stored side-by-side**, and you can access any item by its **position (index)**.

📌 In Python, arrays are implemented using **lists**.

```python
arr = [10, 20, 30, 40, 50]
```

* `arr[0]` → 10
* `arr[1]` → 20
* `arr[4]` → 50

---

## 🔹 1. Traversal of an Array

> “Visiting” each element one by one.

```python
arr = [10, 20, 30, 40, 50]

# Using for loop
for num in arr:
    print(num)

# Using index
for i in range(len(arr)):
    print(f"Element at index {i} is {arr[i]}")
```

🧠 Time Complexity: **O(n)** (We touch each element once)

---

## 🔹 2. Insertion in an Array

### ➤ Insert at the end:

```python
arr = [10, 20, 30]
arr.append(40)
print(arr)  # [10, 20, 30, 40]
```

### ➤ Insert at a specific index:

```python
arr.insert(1, 15)  # Insert 15 at index 1
print(arr)  # [10, 15, 20, 30, 40]
```

🧠 Time Complexity:

* At end → **O(1)**
* At middle/start → **O(n)** (Because elements must shift)

---

## 🔹 3. Deletion in an Array

### ➤ Delete by value:

```python
arr.remove(20)  # Removes first occurrence of 20
print(arr)
```

### ➤ Delete by index:

```python
arr.pop(2)  # Removes element at index 2
print(arr)
```

### ➤ Delete last item:

```python
arr.pop()  # Removes last item
print(arr)
```

🧠 Time Complexity:

* `pop()` → **O(1)** (last element)
* `pop(i)` or `remove(val)` → **O(n)** (shifts needed)

---

## 🔸 4. Array Interview Tip

Most basic DSA problems (like finding max/min, reversing, summing elements) start with **traversing the array**. Always **master this first**.

---

## 🧪 Mini Practice Problems (30 mins)

1. **Print elements of a list**

   ```python
   arr = [5, 10, 15, 20]
   ```

2. **Insert a number at index 2**

3. **Remove a number by value**

4. **Find the largest number in the list**

5. **Write a function to reverse an array**

   * Input: `[1, 2, 3]`
   * Output: `[3, 2, 1]`

---

## 🔄 Optional Challenge (for Weekend Practice)

> Write a Python function that takes a list and a target number, and inserts the number **after the middle element**.

---

## 🧠 Summary

| Operation | Python Method                         | Time Complexity |
| --------- | ------------------------------------- | --------------- |
| Traverse  | `for item in arr`                     | O(n)            |
| Insert    | `arr.append(x)` or `arr.insert(i, x)` | O(1) or O(n)    |
| Delete    | `arr.pop()` or `arr.remove(x)`        | O(1) or O(n)    |

---

Would you like me to prepare **Day 4: Reverse an Array – with two-pointer technique and Python practice** tomorrow in the same style?
