"""
Recursion:
----------
def: Any function which calls itself is called Recursive. A recursive method solves a problem by calling a copy of itself to work
on a smaller problem. This is called the recursion step. The recursion step can result in many more such recursive calls.  
It is important to ensure that the recursion terminates. Each time the function calls itself with a slightly simpler version 
of the original problem. The sequence of smaller problems must eventually converge on the base case. 

Backtracking:
-------------
def: Backtracking is an improvement of the brute force approach. It systematically searches for a solution to a problem among all 
available options. In backtracking, we start with one possible option out of many available options and try to solve the problem 
if we are able to solve the problem with the selected move then we will print the solution else we will backtrack and select some 
other option and try to solve it. If none if the options work out, we will claim that there is no solution for the problem.

Here are some tech lead interview questions on recursion and backtracking, along with explanations:

### 1. **Explain how recursion works and give an example where it is an appropriate solution.**
   - **Answer**: Recursion is a technique where a function calls itself to solve smaller instances of the same problem. 
       It is appropriate for problems that can be divided into smaller subproblems, like calculating factorials, Fibonacci sequences, 
       or traversing tree structures.
   - **Example Question**: "Can you write a recursive function to calculate the nth Fibonacci number?"
   - **Follow-up**: "How would you optimize this function to avoid redundant calculations?" (Hint: Discuss memoization or dynamic 
       programming.)

### 2. **Describe a problem where backtracking is the best approach and explain why.**
   - **Answer**: Backtracking is suitable for problems where you need to explore all possible solutions, such as puzzles, combinatorial 
       problems, or constraint satisfaction problems like the N-Queens or Sudoku.
   - **Example Question**: "How would you solve the N-Queens problem using backtracking? Can you explain the base case and the recursive 
       step?"
   - **Follow-up**: "What are the time and space complexities of your solution? How could you optimize it?"

### 3. **What are the trade-offs of using recursion versus iteration?**
   - **Answer**: Recursion can lead to simpler, more readable code but can also result in higher memory usage due to the call stack. 
       Iteration is more memory-efficient but may be less intuitive for problems naturally expressed recursively.
   - **Example Question**: "Can you convert a recursive solution to an iterative one? For example, the factorial function?"
   - **Follow-up**: "What challenges did you face when converting the code?"

### 4. **Discuss how you would handle stack overflow issues in a recursive function.**
   - **Answer**: Stack overflow can occur if a recursive function has too many calls. To handle this, one could:
     - Optimize the recursion to reduce depth (e.g., using tail recursion).
     - Convert the recursive solution to an iterative one.
     - Increase the stack size (though this is often not recommended).
   - **Example Question**: "Given a deep binary tree, how would you avoid a stack overflow when performing a depth-first search?"

### 5. **How would you debug a recursive function that isn’t working as expected?**
   - **Answer**: Debugging a recursive function involves checking the base case, ensuring the recursive calls reduce the problem size, 
       and using print statements or a debugger to trace the call stack.
   - **Example Question**: "If your recursive function to solve a maze isn't finding the correct path, what steps would you take to 
       identify the issue?"
   - **Follow-up**: "Can you discuss how recursion depth and base cases could affect the correctness of your solution?"

### 6. **Design a solution for the subset sum problem using backtracking.**
   - **Answer**: Use backtracking to explore all subsets of the given set and check if their sum equals the target.
   - **Example Question**: "How would you modify your backtracking algorithm to handle cases where subsets can include duplicate elements?"
   - **Follow-up**: "How would you improve the efficiency of this backtracking solution?"

### 7. **Can you discuss the difference between divide and conquer and backtracking techniques?**
   - **Answer**: Divide and conquer splits a problem into independent subproblems, solves them recursively, and combines their results. 
       Backtracking, on the other hand, builds a solution incrementally and abandons solutions that don't satisfy constraints.
   - **Example Question**: "Can you provide examples where divide and conquer is more suitable than backtracking and vice versa?"
   - **Follow-up**: "What are the typical time complexities for problems solved using these techniques?"

### 8. **Explain the concept of memoization in recursion. When would you use it?**
   - **Answer**: Memoization is an optimization technique where you store the results of expensive function calls and reuse them when 
       the same inputs occur again, reducing the number of recursive calls.
   - **Example Question**: "How would you implement memoization for a recursive Fibonacci function?"
   - **Follow-up**: "What are the advantages and disadvantages of using memoization?"

These questions are designed to probe your understanding of recursion and backtracking, as well as your ability to apply these techniques 
effectively in real-world scenarios. Be ready to discuss your thought process, optimizations, and potential trade-offs for each solution.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6)) # output 8

# Memoization 
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(fibonacci_memo(6))

# Iterative Factorial Conversion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
    
    
def fact_itr(n):
    res = 1
    for i in range(2, n+1):
        res += i
    return res

# Subset Sum Problem Using Backtracking
def subset_sum(arr, target):
    result = []
    def backtrack(start, current_sum, path):
        if current_sum == target:
            result.append(list(path))
            return
        for i in range(start, len(arr)):
            if current_sum + arr[i] <= target:
                path.append(arr[i])
                backtrack(i + 1, current_sum + arr[i], path)
                path.pop()

    arr.sort()
    backtrack(0, 0, [])
    return result

# Example usage
arr = [3, 34, 4, 12, 5, 2]
target = 9
print(subset_sum(arr, target))  # Output: [[3, 4, 2], [5, 4]]





