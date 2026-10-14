# Binary Tree DFS Pattern in Python

# 📚 Concept: Binary Tree DFS Pattern

## What is DFS?

**Depth-First Search (DFS)** is a tree traversal algorithm that starts at the root and explores as far as possible along each branch before backtracking. It uses **recursion** or an explicit **stack** to traverse the tree.

DFS explores three common traversal orders in binary trees:
- **Preorder**: Visit the current node → Traverse left subtree → Traverse right subtree
- **Inorder**: Traverse left subtree → Visit current node → Traverse right subtree
- **Postorder**: Traverse left subtree → Traverse right subtree → Visit current node

---

## Why Use DFS?

DFS is used in binary tree problems for several key reasons:

- 🔁 **Recursive nature** of trees makes DFS a natural fit
- 🧠 **Keeps track of path/state** during traversal (e.g., sum, depth, list of values)
- 📌 **Efficient for problems** involving complete tree exploration
- ⚙️ Easy to implement using recursion or a manual stack

---

## When to Use DFS?

Use DFS when solving binary tree problems that involve:

- ✅ Finding all paths from root to leaf
- ✅ Searching for a target value or condition in the tree
- ✅ Calculating properties like depth, height, diameter, or sum
- ✅ Transforming or modifying the tree based on node values
- ✅ Recursively combining results from left and right subtrees

---

## How is DFS Implemented?

The simplest way to implement DFS in binary trees is using recursion. You visit the current node, then recursively call DFS on the left and right children.

```python
def dfs(node):
    if not node:
        return

    # Do something with node.val
    dfs(node.left)
    dfs(node.right)


The **Depth-First Search (DFS)** pattern is commonly used in binary tree problems. DFS explores as far as possible along each branch before backtracking, typically using recursion or an explicit stack.

## 🔧 DFS Variants
- **Preorder Traversal** (Node ➝ Left ➝ Right)
- **Inorder Traversal** (Left ➝ Node ➝ Right)
- **Postorder Traversal** (Left ➝ Right ➝ Node)

DFS is helpful when you want to:
- Visit all nodes in a specific order
- Solve problems involving recursive substructure (e.g., path sum, subtree search, etc.)
- Work with tree paths and depth-related logic

---

## ✅ Example: DFS Template (Recursive)
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    if not node:
        return

    # Do something with node.val
    print(node.val)

    dfs(node.left)   # Go left
    dfs(node.right)  # Go right

📘 Problem 1: Path Sum
Problem: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values equals the sum.

def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))


📘 Problem 2: Binary Tree Maximum Path Sum
Problem: Find the path in a binary tree that has the maximum sum.

def max_path_sum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)

        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val

    dfs(root)
    return max_sum

💡 Tips
Use DFS when you want to explore all paths or need to consider combinations.

Keep track of the state you need across recursive calls (e.g., path, depth, max value).

Use nonlocal or class variables to store results across recursion.

🚀 Practice Resources
LeetCode DFS Problems

GeeksforGeeks DFS in Binary Tree

Binary Tree Traversals Visualization

