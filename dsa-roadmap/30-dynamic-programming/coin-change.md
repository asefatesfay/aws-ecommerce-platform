# Coin Change

**Difficulty:** Medium
**Pattern:** Unbounded Knapsack DP
**LeetCode:** #322

## Problem Statement
Given coins of different denominations and a total `amount`, return the fewest number of coins needed to make up that amount. Return -1 if it's not possible.

## Examples

### Example 1
**Input:** `coins = [1,2,5]`, `amount = 11`
**Output:** `3`
**Explanation:** 5 + 5 + 1 = 11

### Example 2
**Input:** `coins = [2]`, `amount = 3`
**Output:** `-1`

## Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2³¹ - 1`
- `0 <= amount <= 10⁴`

## Hints

> 💡 **Hint 1:** `dp[i]` = minimum coins to make amount `i`. Initialize `dp[0] = 0`, all others = infinity.

> 💡 **Hint 2:** For each amount from 1 to target, try each coin: `dp[i] = min(dp[i], dp[i - coin] + 1)` if `i >= coin`.

> 💡 **Hint 3:** If `dp[amount]` is still infinity, return -1.

## Approach
**Time Complexity:** O(amount × coins.length)
**Space Complexity:** O(amount)

Bottom-up DP: build up from amount 0. For each amount, try all coins and take the minimum.
