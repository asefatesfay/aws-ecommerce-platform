# Best Time to Buy and Sell Stock IV

**Difficulty:** Hard
**Pattern:** State Machine DP
**LeetCode:** #188

## Problem Statement
You are given an integer `k` and an array `prices` where `prices[i]` is the stock price on day `i`.

Find the maximum profit with at most `k` transactions.

## Examples

### Example 1
**Input:** `k = 2`, `prices = [2,4,1]`
**Output:** `2`

### Example 2
**Input:** `k = 2`, `prices = [3,2,6,5,0,3]`
**Output:** `7`

## Constraints
- `1 <= k <= 100`
- `1 <= prices.length <= 1000`
- `0 <= prices[i] <= 1000`

## DP Breakdown
Let `buy[t]` and `sell[t]` represent best profit after processing current day with transaction count `t`:
- `buy[t] = max(buy[t], sell[t - 1] - price)`
- `sell[t] = max(sell[t], buy[t] + price)`
for `t = 1..k`.

Optimization: if `k >= n/2`, this becomes unlimited transactions (sum of all positive differences).

## Hints
- Use arrays of size `k + 1`.
- Update transaction states in order carefully.
- Shortcut to greedy when `k` is large.

## Approach
**Time Complexity:** O(N * K)
**Space Complexity:** O(K)

Use transaction-stage DP with rolling arrays for buy/sell states.