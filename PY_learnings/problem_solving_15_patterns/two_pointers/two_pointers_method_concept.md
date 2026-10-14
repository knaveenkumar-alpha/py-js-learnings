
TWO POINTERS METHOD
====================

This module contains implementations of the two pointers method, a common technique used in solving problems related to arrays 
and strings. The two pointers method involves using two indices to traverse the data structure, allowing for efficient solutions
to various problems such as finding pairs, triplets, or subarrays that meet certain criteria.

The Mental Model -- How to THINK about Two Pointers
----------------------------------------------------
- The core idea is simple: instead of using a nested loop (O(n2)), place two index markers on the array and move them smartly toward each other (or in the same direction) to find your answer in O(n)

When to recognize it in an interview:
1. The array/string is sorted (or can be sorted)
2. You're asked about pairs, triplets, or subarrays
3. You see words like: "find two numbers that..", "longest/shortest sub-array where...", "palindrome check"
4. Brute force is O(n2) and interviewer hints at doing better

The 3 patterns to memorize:

| **Pattern**   | **Pointers Start**| **Move Condition** | **Use Case** |
|---------------|-------------------|--------------------|--------------|
| Opposite ends | left=0, right=end | Converge inward    | Pair sum, palindrome|
| Same direction | Both at 0 | Fast moves,slow follows | Duplicates, cycles detection |
| Sliding window | Both at 0 | Right expands, left shrinks | Subarray/substring problems |

## The Memory Trick -- "SORT --> SQUEEZE"
--------------------------------------------
when you see a problem, ask these 2 questions in order
1. Is the array SORTED (or can I sort it)? --> Two pointers likely works
2. Am I SQUEEZING toward a target?
  - From both ends? --> Pattern 1 (Opposite ends)
  - One chasing the other? --> Pattern 2 (Same direction)
  - A window expanding/shrinking? --> Pattern 3 (Sliding Window)

## How to Spot Each Pattern in an Interview?

Pattern 1 trigger words: "pair that sums to", "palindrome", "container with most water", "sorted array"

Pattern 2 trigger words: "remove duplicates in-place", "move zeros", "slow/fast pointer", "linked list cycle"

Pattern 3 trigger words: "longest subarray/substring", "minimum window", "at most K distinct", "subarray sum equals"

## ⚡ Common Mistakes to Avoid

1. `Forgetting` while left < right — without this, left and right can cross and give wrong answers
2. `Moving the wrong pointer` — always move toward making the condition valid again
3. `Sliding window`: use while not if — sometimes you need to shrink multiple times before the window is valid again
4. `Not handling empty arrays` — always add the base check first






