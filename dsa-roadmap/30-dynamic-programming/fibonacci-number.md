# Fibonacci Number

**Difficulty:** Easy
**Pattern:** 1D DP / Fibonacci
**LeetCode:** #509

## Problem Statement
The Fibonacci numbers are defined as:
- `F(0) = 0`
- `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)` for `n > 1`

Given `n`, return `F(n)`.

## Examples

### Example 1
**Input:** `n = 2`
**Output:** `1`

### Example 2
**Input:** `n = 3`
**Output:** `2`

### Example 3
**Input:** `n = 4`
**Output:** `3`

## Constraints
- `0 <= n <= 30`

## DP Breakdown
- **State:** `dp[i]` = Fibonacci value at index `i`
- **Transition:** `dp[i] = dp[i - 1] + dp[i - 2]`
- **Base cases:** `dp[0] = 0`, `dp[1] = 1`
- **Iteration order:** left to right from `2` to `n`

## Hints
- A recursive solution repeats many calls.
- Build from small `i` to larger `i`.
- Keep only last two values to get O(1) space.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Track only two previous values (`a`, `b`) and update until `n`.