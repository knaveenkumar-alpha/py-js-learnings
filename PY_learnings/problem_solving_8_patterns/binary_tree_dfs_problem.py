# Binary Tree DFS Example: Find All Root-to-Leaf Paths That Sum to Target

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem: Given a binary tree and a target sum, return all root-to-leaf paths where the sum of the node values equals the target.

def path_sum(root, target_sum):
    result = []

    def dfs(node, current_path, current_sum):
        if not node:
            return

        # Add current node to the path
        current_path.append(node.val)
        current_sum += node.val

        # Check if it's a leaf node and path sum matches target
        if not node.left and not node.right and current_sum == target_sum:
            result.append(list(current_path))
        else:
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)

        # Backtrack
        current_path.pop()

    dfs(root, [], 0)
    return result

# ------------------
# Example Tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \      \
#   7    2      1

# Target Sum: 22
# Expected Output: [[5, 4, 11, 2], [5, 8, 4, 5]]

# Create example tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Run and print results
paths = path_sum(root, 22)
print("Paths with sum 22:", paths)

"""
Explanation:
- We perform DFS traversal, maintaining a current path and sum.
- When we reach a leaf node, we check if the accumulated sum equals the target.
- If yes, we save the path. We use backtracking to remove the last node after recursion.
- This is a classic DFS + backtracking pattern for binary trees.
"""
