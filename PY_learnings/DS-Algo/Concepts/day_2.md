Absolutely! Here's your **DSA Study Plan – Week 1, Day 2** — crafted to fit into your **1-hour daily study window**, with **layman-style explanations and Python code**.

---

## 📅 **Week 1 – Day 2: Python Essentials for DSA**

---

### 🧠 **Goal for Today**

Before jumping into data structures like arrays and linked lists, you must master **basic Python tools** that are commonly used in solving DSA problems.

Today’s focus:

* Lists & List operations
* Loops (for & while)
* Conditionals (if-else)
* Functions
* Input/Output for coding challenges

---

## 🔹 1. Lists in Python (aka Arrays)

> Think of a list like a train with boxes — each box has something (numbers, words, etc.).

```python
# Create a list
arr = [10, 20, 30, 40, 50]

# Access elements
print(arr[0])     # 10
print(arr[-1])    # 50 (last element)

# Update
arr[1] = 25       # arr becomes [10, 25, 30, 40, 50]

# Add (append)
arr.append(60)    # [10, 25, 30, 40, 50, 60]

# Remove
arr.pop()         # removes last → [10, 25, 30, 40, 50]

# Length
print(len(arr))   # 5
```

---

## 🔹 2. Loops in Python

### 🔸 For Loop – go through each item

```python
for num in arr:
    print(num)
```

### 🔸 While Loop – repeat until a condition fails

```python
i = 0
while i < len(arr):
    print(arr[i])
    i += 1
```

---

## 🔹 3. Conditional Statements (if-else)

> Decision-making tools in code.

```python
x = 10
if x > 5:
    print("Greater than 5")
else:
    print("5 or less")
```

---

## 🔹 4. Functions – Reusable code blocks

```python
def greet(name):
    print("Hello", name)

greet("Naveen")  # Output: Hello Naveen
```

**With return value:**

```python
def add(a, b):
    return a + b

print(add(3, 4))  # Output: 7
```

---

## 🔹 5. Taking Input (used in coding tests)

### Single input:

```python
n = int(input("Enter a number: "))
```

### Space-separated input as list:

```python
arr = list(map(int, input("Enter numbers: ").split()))
# Example input: 10 20 30
# Output: [10, 20, 30]
```

---

## 📝 **Mini Practice Tasks (Total: 20–30 mins)**

Try writing these small Python programs:

1. Print all elements of a list using a loop
2. Find the sum of all numbers in a list
3. Check if a number is even or odd using a function
4. Take a list of `n` numbers as input and print them in reverse order

---

## 🔄 **Wrap-Up (5–10 mins)**

* Write down **what you understood** today in your own words.
* Reflect on where you use these Python basics in real life (loops = daily routines, functions = reusable habits).

---

### 🧠 Summary of What You Learned Today:

| Concept      | Why It's Important for DSA         |
| ------------ | ---------------------------------- |
| Lists        | Foundation of arrays, stacks, etc. |
| Loops        | Used to traverse/modify data       |
| Conditionals | Logic-building in algorithms       |
| Functions    | Break problems into small parts    |
| Input        | Needed for coding contests         |

---

Would you like me to prepare **Day 3: Arrays – Traversal, Insert, Delete** next, with easy steps and Python examples?
