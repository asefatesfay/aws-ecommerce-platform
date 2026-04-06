# Climbing Stairs

**Difficulty:** Easy
**Pattern:** 1D DP / Fibonacci
**LeetCode:** #70

## Problem Statement
You're climbing a staircase with `n` steps. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

## Examples

### Example 1
**Input:** `n = 2`
**Output:** `2`
**Explanation:** 1+1, 2

### Example 2
**Input:** `n = 3`
**Output:** `3`
**Explanation:** 1+1+1, 1+2, 2+1

## Constraints
- `1 <= n <= 45`

## Hints

> 💡 **Hint 1:** To reach step n, you came from step n-1 (1 step) or step n-2 (2 steps). So `dp[n] = dp[n-1] + dp[n-2]`.

> 💡 **Hint 2:** Base cases: `dp[1] = 1`, `dp[2] = 2`. This is exactly the Fibonacci sequence.

> 💡 **Hint 3:** You only need the last two values — optimize to O(1) space.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Fibonacci recurrence: `ways(n) = ways(n-1) + ways(n-2)`. Track only the last two values.
