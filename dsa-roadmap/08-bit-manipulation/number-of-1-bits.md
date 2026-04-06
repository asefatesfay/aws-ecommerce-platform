# Number of 1 Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**LeetCode:** #191

## Problem Statement

Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).

## Examples

### Example 1
**Input:** `n = 11` (binary: `00000000000000000000000000001011`)
**Output:** `3`
**Explanation:** Three bits are set.

### Example 2
**Input:** `n = 128` (binary: `00000000000000000000000010000000`)
**Output:** `1`

### Example 3
**Input:** `n = 2147483645` (binary: `01111111111111111111111111111101`)
**Output:** `30`

## Constraints
- `1 <= n <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Check each bit one at a time using `n & 1` to test the lowest bit, then right-shift n.

> 💡 **Hint 2:** A more elegant approach: `n & (n-1)` clears the lowest set bit. Count how many times you can do this before n becomes 0.

> 💡 **Hint 3:** Brian Kernighan's algorithm: repeatedly do `n = n & (n-1)` and count iterations. This runs in O(number of set bits) rather than O(32).

## Approach

**Time Complexity:** O(1) — at most 32 iterations
**Space Complexity:** O(1)

Brian Kernighan's algorithm: repeatedly clear the lowest set bit with `n &= (n-1)` and count how many times until n = 0.
