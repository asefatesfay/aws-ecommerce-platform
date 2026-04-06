# Sum of Two Integers

**Difficulty:** Medium
**Pattern:** Bit Manipulation
**LeetCode:** #371

## Problem Statement

Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

## Examples

### Example 1
**Input:** `a = 1`, `b = 2`
**Output:** `3`

### Example 2
**Input:** `a = 2`, `b = 3`
**Output:** `5`

## Constraints
- `-1000 <= a, b <= 1000`

## Hints

> 💡 **Hint 1:** Think about how addition works at the bit level. When you add two bits: 0+0=0, 0+1=1, 1+0=1, 1+1=0 with carry 1. The sum without carry is XOR; the carry is AND shifted left.

> 💡 **Hint 2:** Compute `sum = a ^ b` (bits that don't produce a carry) and `carry = (a & b) << 1` (bits that produce a carry, shifted to the next position).

> 💡 **Hint 3:** Repeat with `a = sum` and `b = carry` until carry is 0. The final `a` is the answer. In Python, handle the 32-bit mask to avoid infinite loops with negative numbers.

## Approach

**Time Complexity:** O(1) — at most 32 iterations
**Space Complexity:** O(1)

Iteratively compute XOR (sum without carry) and AND shifted left (carry), using the carry as the new addend, until carry is 0.
