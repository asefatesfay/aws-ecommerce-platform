# Perfect Squares

**Difficulty:** Medium
**Pattern:** Unbounded Knapsack DP
**LeetCode:** #279

## Problem Statement
Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A perfect square is an integer that is the square of an integer, such as `1, 4, 9, 16`.

## Examples

### Example 1
**Input:** `n = 12`
**Output:** `3`
**Explanation:** `12 = 4 + 4 + 4`

### Example 2
**Input:** `n = 13`
**Output:** `2`
**Explanation:** `13 = 4 + 9`

## Constraints
- `1 <= n <= 10^4`

## DP Breakdown
- **State:** `dp[i]` = minimum number of perfect squares to make sum `i`
- **Base case:** `dp[0] = 0`
- **Transition:**
  `dp[i] = min(dp[i], dp[i - sq] + 1)` for every square `sq <= i`

This is unbounded knapsack because each square can be reused.

## Hints
- Precompute all perfect squares up to `n`.
- Initialize DP with a large value.
- Build answers from `1` to `n`.

## Approach
**Time Complexity:** O(n * sqrt(n))
**Space Complexity:** O(n)

Try every square for each target sum and keep the minimum count.