# Min Cost Climbing Stairs

**Difficulty:** Easy
**Pattern:** 1D DP
**LeetCode:** #746

## Problem Statement
You are given an integer array `cost` where `cost[i]` is the cost of step `i` on a staircase. Once you pay the cost, you can climb either one or two steps.

You can start from step `0` or step `1`. Return the minimum cost to reach the top (one step beyond the last index).

## Examples

### Example 1
**Input:** `cost = [10,15,20]`
**Output:** `15`

### Example 2
**Input:** `cost = [1,100,1,1,1,100,1,1,100,1]`
**Output:** `6`

## Constraints
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## DP Breakdown
- **State:** `dp[i]` = minimum cost to reach step `i`
- **Transition:** `dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])`
- **Base cases:** `dp[0] = cost[0]`, `dp[1] = cost[1]`
- **Answer:** `min(dp[n - 1], dp[n - 2])`

## Hints
- Think in terms of minimum cost to arrive at each step.
- From step `i`, previous step must be `i-1` or `i-2`.
- You only need last two DP values.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Iterate once while storing best costs for the previous two steps.