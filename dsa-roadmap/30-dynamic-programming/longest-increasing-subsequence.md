# Longest Increasing Subsequence

**Difficulty:** Medium
**Pattern:** LIS DP / Binary Search
**LeetCode:** #300

## Problem Statement
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

## Examples

### Example 1
**Input:** `nums = [10,9,2,5,3,7,101,18]`
**Output:** `4`
**Explanation:** [2,3,7,101]

### Example 2
**Input:** `nums = [0,1,0,3,2,3]`
**Output:** `4`

## Constraints
- `1 <= nums.length <= 2500`
- `-10⁴ <= nums[i] <= 10⁴`

## Hints

> 💡 **Hint 1:** O(N²) DP: `dp[i]` = length of LIS ending at index i. For each i, check all j < i where `nums[j] < nums[i]`.

> 💡 **Hint 2:** O(N log N) approach: maintain a `tails` array where `tails[i]` is the smallest tail element of all increasing subsequences of length i+1.

> 💡 **Hint 3:** For each number, binary search in `tails` to find where to place it. If it's larger than all, append. Otherwise replace the first element ≥ it.

## Approach
**Time Complexity:** O(N log N) with patience sorting
**Space Complexity:** O(N)

Maintain a `tails` array. Binary search to find the correct position for each element. Length of `tails` at the end is the answer.
