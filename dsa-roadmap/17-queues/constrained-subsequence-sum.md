# Constrained Subsequence Sum

**Difficulty:** Hard
**Pattern:** Monotonic Deque / DP
**LeetCode:** #1425

## Problem Statement

Given an integer array `nums` and a positive integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, `nums[i]` and `nums[j]`, where `i < j`, it holds that `j - i <= k`. A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

## Examples

### Example 1
**Input:** `nums = [10,2,-10,5,20]`, `k = 2`
**Output:** `37`
**Explanation:** [10,2,5,20].

### Example 2
**Input:** `nums = [-1,-2,-3]`, `k = 1`
**Output:** `-1`

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** DP: `dp[i]` = maximum subsequence sum ending at index i. `dp[i] = nums[i] + max(0, max(dp[i-k], ..., dp[i-1]))`.

> 💡 **Hint 2:** Use a monotonic decreasing deque to efficiently query the maximum dp value in the last k positions.

> 💡 **Hint 3:** The `max(0, ...)` handles the case where it's better to start a new subsequence at i rather than extending a negative one.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

DP with monotonic decreasing deque for O(1) range maximum queries over the last k dp values.
