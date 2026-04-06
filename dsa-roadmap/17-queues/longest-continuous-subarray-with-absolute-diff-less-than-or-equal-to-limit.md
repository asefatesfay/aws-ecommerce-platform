# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

**Difficulty:** Medium
**Pattern:** Monotonic Deque / Sliding Window
**LeetCode:** #1438

## Problem Statement

Given an array of integers `nums` and an integer `limit`, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to `limit`.

## Examples

### Example 1
**Input:** `nums = [8,2,4,7]`, `limit = 4`
**Output:** `2`
**Explanation:** [2,4] has max diff 2 ≤ 4.

### Example 2
**Input:** `nums = [10,1,2,4,7,2]`, `limit = 5`
**Output:** `4`
**Explanation:** [2,4,7,2] has max diff 5 ≤ 5.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Hints

> 💡 **Hint 1:** The condition is `max(window) - min(window) <= limit`. Use two monotonic deques: one for max, one for min.

> 💡 **Hint 2:** Maintain a decreasing deque for max and an increasing deque for min. The window is valid when `max_deque.front - min_deque.front <= limit`.

> 💡 **Hint 3:** Variable sliding window: expand right, shrink left when invalid. Track maximum window size.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Two monotonic deques (max and min) with a variable sliding window. Shrink when max - min > limit.
