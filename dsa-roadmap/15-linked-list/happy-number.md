# Happy Number

**Difficulty:** Easy
**Pattern:** Fast/Slow Pointers (Cycle Detection)
**LeetCode:** #202

## Problem Statement

Write an algorithm to determine if a number `n` is happy. A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy. Return `true` if `n` is a happy number, and `false` if not.

## Examples

### Example 1
**Input:** `n = 19`
**Output:** `true`
**Explanation:** 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1.

### Example 2
**Input:** `n = 2`
**Output:** `false`

## Constraints
- `1 <= n <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** The sequence either reaches 1 (happy) or enters a cycle (not happy). This is a cycle detection problem.

> 💡 **Hint 2:** Use fast/slow pointers on the sequence. Slow computes one step, fast computes two steps. If they meet at 1, it's happy. If they meet elsewhere, there's a cycle.

> 💡 **Hint 3:** Alternatively, use a HashSet to detect if a number has been seen before. If you see 1, return true. If you see a repeat, return false.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1) with fast/slow, O(log n) with HashSet

Fast/slow pointers on the digit-square-sum sequence. If fast reaches 1, return true. If fast and slow meet (not at 1), return false.
