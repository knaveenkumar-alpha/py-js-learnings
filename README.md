# Software Engineering Interview Preparation Roadmap

A 12-week roadmap for preparing for software engineering interviews through Python and JavaScript practice, data structures and algorithms, system design, and mock interviews.

## How to use this roadmap

- Aim for **1–2 focused hours per day**, adjusting the pace as needed.
- Implement core concepts in both Python and JavaScript where practical.
- Solve problems by explaining your approach, complexity, and edge cases—not just reaching an answer.
- Keep notes and revisit topics that feel difficult.
- Treat the schedule as a guide: spend additional time on weak areas.

## Table of Contents

- [Weekly Roadmap](#weekly-roadmap)
- [Language Topics](#language-topics)
- [System Design Framework](#system-design-framework)
- [Interview Practice Routine](#interview-practice-routine)
- [Progress Tracker](#progress-tracker)

---

## Weekly Roadmap

### Weeks 1–2: Programming Fundamentals, Complexity, and Linked Lists

**Goals:** Strengthen problem-solving fundamentals and become comfortable analyzing time and space complexity.

**Study and practice:**
- Review arrays, strings, hash maps, sets, and basic recursion.
- Learn Big O notation and compare common operations.
- Implement singly and doubly linked lists.
- Practice insertion, deletion, reversal, cycle detection, and merging.
- Review sorting: merge sort, quicksort, heap sort, and built-in sorting behavior.

**Python focus:**
- Lists, tuples, dictionaries, and sets
- Slicing, comprehensions, and built-in functions
- References, mutability, and function arguments

**JavaScript focus:**
- Arrays, objects, `Map`, and `Set`
- `let`, `const`, scope, and equality
- Array methods, callbacks, and basic debugging

**Practice problems:** Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle, Intersection of Two Linked Lists, Sort an Array.

---

### Weeks 3–4: Stacks, Queues, and Language Fundamentals

**Goals:** Use stacks and queues confidently and understand the features of each language that commonly arise in interviews.

**Study and practice:**
- Implement stacks, queues, and priority queues.
- Practice monotonic stacks and sliding-window techniques.
- Review iteration, recursion, exceptions, and writing testable functions.

**Python focus:**
- Iterators and generators
- Decorators and closures
- Classes, properties, and dunder methods
- `collections.deque` and `heapq`

**JavaScript focus:**
- Functions, closures, and arrow functions
- Promises, `async`/`await`, and error handling
- Prototypes and classes
- Node.js modules and package basics

**Practice problems:** Valid Parentheses, Min Stack, Daily Temperatures, Evaluate Reverse Polish Notation, Sliding Window Maximum.

---

### Weeks 5–6: Trees, Heaps, and Graph Fundamentals

**Goals:** Choose appropriate traversal strategies and solve common tree and graph problems.

**Study and practice:**
- Implement binary trees and binary search trees.
- Practice preorder, inorder, postorder, and level-order traversal.
- Learn heaps and priority-queue use cases.
- Represent graphs with adjacency lists and matrices.
- Practice BFS, DFS, connected components, and cycle detection.

**Python focus:** `deque`, recursion limits, and heap-based algorithms.  
**JavaScript focus:** Queue implementation choices, object/map-based graph representations, and recursive traversal.

**Practice problems:** Binary Tree Level Order Traversal, Maximum Depth of Binary Tree, Lowest Common Ancestor, Number of Islands, Clone Graph, Course Schedule.

---

### Weeks 7–8: Shortest Paths, Dynamic Programming, and Advanced Techniques

**Goals:** Recognize when a problem needs graph algorithms, dynamic programming, or a more efficient search strategy.

**Study and practice:**
- Implement Dijkstra’s algorithm, topological sort, and union-find.
- Understand dynamic programming through states, transitions, base cases, and memoization.
- Practice one-dimensional and two-dimensional DP.
- Review backtracking, binary search, and greedy strategies.

**Python focus:** Memoization with dictionaries or `functools`, and efficient heap usage.  
**JavaScript focus:** Memoization with `Map`, array initialization, and avoiding accidental shared references.

**Practice problems:** Network Delay Time, Coin Change, Climbing Stairs, House Robber, Longest Increasing Subsequence, Word Break.

---

### Weeks 9–10: System Design and Practical Engineering

**Goals:** Structure design discussions clearly and explain trade-offs.

**Study and practice:**
- Requirements: clarify users, features, constraints, and success metrics.
- Capacity estimation: traffic, storage, bandwidth, and growth.
- Components: APIs, databases, caches, queues, and object storage.
- Scalability: load balancing, replication, partitioning, and sharding.
- Reliability: retries, timeouts, idempotency, monitoring, and disaster recovery.
- Data choices: SQL versus NoSQL, indexing, consistency, and transactions.
- Practice designing a URL shortener, notification service, news feed, or file-storage service.

**Design discussion checklist:**
1. Clarify functional and non-functional requirements.
2. Estimate scale and identify important constraints.
3. Sketch the high-level architecture and request flow.
4. Define APIs and data models.
5. Identify bottlenecks and failure cases.
6. Explain trade-offs and possible future improvements.

---

### Weeks 11–12: Projects, Revision, and Mock Interviews

**Goals:** Consolidate knowledge and practice communicating under interview conditions.

**Study and practice:**
- Revisit weak topics and redo selected problems without notes.
- Complete or polish a small project using Python or JavaScript.
- Write tests and document setup, design decisions, and trade-offs.
- Practice coding interviews with a timer and explain your reasoning aloud.
- Conduct system design and behavioral mock interviews.
- Review mistakes and create a short final revision sheet.

**Suggested project ideas:**
- Python: REST API, command-line task tracker, or data-processing tool.
- JavaScript: API-backed web app, real-time dashboard, or Node.js service.
- For either language, include input validation, error handling, tests, and a clear README.

---

## Language Topics

### Python checklist

- [ ] Core data types, collections, and complexity
- [ ] Functions, scope, exceptions, and modules
- [ ] Iterators, generators, and comprehensions
- [ ] Classes, inheritance, and properties
- [ ] Testing and debugging
- [ ] Common standard-library tools such as `collections`, `heapq`, and `itertools`

### JavaScript checklist

- [ ] Types, coercion, scope, and equality
- [ ] Arrays, objects, `Map`, and `Set`
- [ ] Functions, closures, and prototypes
- [ ] Promises and `async`/`await`
- [ ] Modules, Node.js basics, and error handling
- [ ] Testing and debugging

---

## System Design Framework

For each design problem, write down:

- **Requirements:** What must the system do? What quality attributes matter?
- **Scale:** What are the expected users, requests, and data volumes?
- **Interfaces:** What APIs or events connect the components?
- **Storage:** What data is stored, and how is it queried?
- **Architecture:** How do requests and data flow through the system?
- **Trade-offs:** What changes with higher scale, stricter consistency, or lower latency?
- **Operations:** How are errors, security, monitoring, and recovery handled?

Start with the simplest design that satisfies the requirements, then evolve it to address specific bottlenecks.

---

## Interview Practice Routine

For each coding problem:

1. Restate the problem and clarify assumptions.
2. Work through a small example and edge cases.
3. Describe a straightforward solution, then improve it if needed.
4. Explain the algorithm before coding.
5. Test normal, boundary, and invalid inputs.
6. State time and space complexity.
7. Review what could be improved after solving it.

For behavioral interviews, prepare concise examples using the **Situation, Task, Action, Result** structure.

---

## Progress Tracker

Copy this checklist for each study week:

- [ ] Review the week’s concepts.
- [ ] Implement at least one core technique.
- [ ] Solve practice problems and record mistakes.
- [ ] Explain one solution aloud.
- [ ] Revisit a topic from an earlier week.
- [ ] Update notes or a project.

## Final Reminder

Consistency matters more than following the schedule perfectly. Focus on understanding, implementation, clear communication, and learning from mistakes.