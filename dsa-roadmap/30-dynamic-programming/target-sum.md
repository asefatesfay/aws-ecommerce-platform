# Target Sum

**Difficulty:** Medium
**Pattern:** 0/1 Knapsack DP
**LeetCode:** #494

## Problem Statement
You are given an integer array `nums` and an integer `target`.

You can assign a `+` or `-` sign before each number and then sum all values. Return the number of different expressions that evaluate to `target`.

## Examples

### Example 1
**Input:** `nums = [1,1,1,1,1]`, `target = 3`
**Output:** `5`

### Example 2
**Input:** `nums = [1]`, `target = 1`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `sum(nums) <= 1000`
- `-1000 <= target <= 1000`

## DP Breakdown
Convert sign assignment to subset counting:
- Let subset `P` be numbers with `+`, subset `N` with `-`.
- `sum(P) - sum(N) = target`
- `sum(P) + sum(N) = total`
- So `sum(P) = (total + target) / 2`

Now count subsets with sum `S = (total + target) / 2`.

- **State:** `dp[s]` = number of ways to make sum `s`
- **Transition:** for each `num`, iterate `s` from `S` down to `num`:
  `dp[s] += dp[s - num]`

## Hints
- If `total + target` is odd or negative, answer is `0`.
- Use reverse iteration for 0/1 knapsack counting.
- Initialize `dp[0] = 1`.

## Approach
**Time Complexity:** O(N * S)
**Space Complexity:** O(S)

Compute subset count with 1D knapsack DP.