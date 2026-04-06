# Reverse Bits

**Difficulty:** Easy
**Pattern:** Bit Manipulation
**LeetCode:** #190

## Problem Statement

Reverse bits of a given 32-bit unsigned integer.

## Examples

### Example 1
**Input:** `n = 00000010100101000001111010011100` (binary)
**Output:** `964176192` = `00111001011110000010100101000000` (binary)

### Example 2
**Input:** `n = 11111111111111111111111111111101` (binary)
**Output:** `3221225471` = `10111111111111111111111111111111` (binary)

## Constraints
- The input must be a binary string of length 32

## Hints

> 💡 **Hint 1:** Process the input bit by bit. Extract the lowest bit of n, place it in the correct position of the result, then shift n right.

> 💡 **Hint 2:** For each of 32 iterations: shift result left by 1, OR in the lowest bit of n (`n & 1`), then shift n right by 1.

> 💡 **Hint 3:** After 32 iterations, result holds the reversed bits. Be careful with unsigned right shift in languages like Java (use `>>>` not `>>`).

## Approach

**Time Complexity:** O(1) — exactly 32 iterations
**Space Complexity:** O(1)

Iterate 32 times: each iteration shifts the result left, appends the current lowest bit of n, and shifts n right. After 32 iterations, result contains the reversed bits.
