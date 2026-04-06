# Hamming Distance

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**LeetCode:** #461

## Problem Statement

The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers `x` and `y`, return the Hamming distance between them.

## Examples

### Example 1
**Input:** `x = 1`, `y = 4`
**Output:** `2`
**Explanation:** 1 = 0001, 4 = 0100. Two bit positions differ.

### Example 2
**Input:** `x = 3`, `y = 1`
**Output:** `1`
**Explanation:** 3 = 011, 1 = 001. One bit position differs.

## Constraints
- `0 <= x, y <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** XOR of two numbers gives a 1 in every bit position where the two numbers differ.

> 💡 **Hint 2:** So `x ^ y` has 1s exactly at the positions where x and y differ. The Hamming distance is the number of 1 bits in `x ^ y`.

> 💡 **Hint 3:** Count the set bits in `x ^ y` using any popcount method (Brian Kernighan's, built-in, or bit-by-bit).

## Approach

**Time Complexity:** O(1) — at most 32 bits
**Space Complexity:** O(1)

Compute `x ^ y`, then count the number of set bits in the result.
