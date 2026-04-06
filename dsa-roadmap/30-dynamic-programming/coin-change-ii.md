# Coin Change II

**Difficulty:** Medium
**Pattern:** Unbounded Knapsack DP
**LeetCode:** #518

## Problem Statement
Given an integer `amount` and an array `coins`, return the number of combinations that make up that amount.

You have infinite copies of each coin. Two combinations are considered the same if they use the same counts of coins (order does not matter).

## Examples

### Example 1
**Input:** `amount = 5`, `coins = [1,2,5]`
**Output:** `4`
**Explanation:** `5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`

### Example 2
**Input:** `amount = 3`, `coins = [2]`
**Output:** `0`

## Constraints
- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- `0 <= amount <= 5000`

## DP Breakdown
- **State:** `dp[a]` = number of ways to make amount `a`
- **Base case:** `dp[0] = 1`
- **Transition:** for each `coin`, for `a` from `coin` to `amount`:
  `dp[a] += dp[a - coin]`

Coin-first iteration prevents counting permutations multiple times.

## Hints
- This is counting combinations, not minimum coins.
- Iterate coins in outer loop.
- `dp[0] = 1` means one way to make zero amount: choose nothing.

## Approach
**Time Complexity:** O(amount * coins.length)
**Space Complexity:** O(amount)

1D unbounded knapsack counting DP.