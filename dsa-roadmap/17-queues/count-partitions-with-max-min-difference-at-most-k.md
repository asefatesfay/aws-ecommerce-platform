# Count Partitions With Max-Min Difference at Most K

**Difficulty:** Medium
**Pattern:** Monotonic Deque / DP
**LeetCode:** #3117

## Problem Statement

You are given an integer array `nums` and a non-negative integer `k`. Return the number of partitions of `nums` into one or more contiguous subarrays such that the difference between the maximum and minimum values in each subarray is at most `k`. Since the answer may be large, return it modulo `10^9 + 7`.

## Examples

### Example 1
**Input:** `nums = [3,6,1,2,5]`, `k = 2`
**Output:** `4`

### Example 2
**Input:** `nums = [1,2,3,4]`, `k = 1`
**Output:** `2`

## Constraints
- `2 <= nums.length <= 5 * 10^4`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Hints

> 💡 **Hint 1:** DP: `dp[i]` = number of valid partitions of nums[0..i-1]. For each i, find all valid last subarrays ending at i.

> 💡 **Hint 2:** A subarray [j, i] is valid if max(nums[j..i]) - min(nums[j..i]) ≤ k. Use two monotonic deques to efficiently track max and min as j varies.

> 💡 **Hint 3:** For each i, find the leftmost j where the subarray [j, i] is valid. Sum dp[j-1] through dp[i-1] using a prefix sum of dp values.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

DP with two monotonic deques for range max/min. Prefix sum of dp values for efficient range sum queries.
