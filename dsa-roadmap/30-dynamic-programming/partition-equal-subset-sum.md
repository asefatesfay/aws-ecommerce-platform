# Partition Equal Subset Sum

**Difficulty:** Medium
**Pattern:** 0/1 Knapsack DP
**LeetCode:** #416

## Problem Statement
Given a non-empty integer array `nums`, determine if it can be partitioned into two subsets with equal sum.

## Examples

### Example 1
**Input:** `nums = [1,5,11,5]`
**Output:** `true`
**Explanation:** [1,5,5] and [11]

### Example 2
**Input:** `nums = [1,2,3,5]`
**Output:** `false`

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Hints

> 💡 **Hint 1:** If total sum is odd, return false immediately. Otherwise, find if any subset sums to `total/2`.

> 💡 **Hint 2:** `dp[j]` = true if sum `j` is achievable. For each number, update dp backwards: `dp[j] = dp[j] or dp[j - num]`.

> 💡 **Hint 3:** Process backwards to avoid using the same element twice (0/1 knapsack pattern).

## Approach
**Time Complexity:** O(N × sum/2)
**Space Complexity:** O(sum/2)

0/1 knapsack: can we achieve exactly `total/2`? Use 1D boolean DP, iterate backwards for each number.
