# Jump Game VI

**Difficulty:** Medium
**Pattern:** Monotonic Deque / DP
**LeetCode:** #1696

## Problem Statement

You are given a 0-indexed integer array `nums` and an integer `k`. You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going out of the bounds of the array. You want to reach the last index of the array (index `n - 1`). Your score is the sum of all `nums[j]` for each index `j` you visited in the array. Return the maximum score you can get.

## Examples

### Example 1
**Input:** `nums = [1,-1,-2,4,-7,3]`, `k = 2`
**Output:** `7`
**Explanation:** Jump to indices 0,3,5: 1+4+3=7.

### Example 2
**Input:** `nums = [10,-5,-2,4,0,3]`, `k = 3`
**Output:** `17`

## Constraints
- `1 <= nums.length, k <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** DP: `dp[i]` = maximum score to reach index i. `dp[i] = nums[i] + max(dp[i-k], ..., dp[i-1])`.

> 💡 **Hint 2:** The naive DP is O(nk). Use a monotonic deque to maintain the maximum of the last k dp values in O(1).

> 💡 **Hint 3:** Maintain a decreasing deque of (dp_value, index) pairs. Remove from front when index is out of the k-window. Remove from back when the new dp value is larger.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

DP with monotonic deque to efficiently query the maximum dp value in the last k positions.
