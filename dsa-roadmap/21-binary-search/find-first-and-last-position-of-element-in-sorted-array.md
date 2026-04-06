# Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search (Leftmost/Rightmost)
**LeetCode:** #34

## Problem Statement

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If `target` is not found in the array, return `[-1, -1]`. You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1
**Input:** `nums = [5,7,7,8,8,10]`, `target = 8`
**Output:** `[3,4]`

### Example 2
**Input:** `nums = [5,7,7,8,8,10]`, `target = 6`
**Output:** `[-1,-1]`

### Example 3
**Input:** `nums = []`, `target = 0`
**Output:** `[-1,-1]`

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing integer array
- `-10^9 <= target <= 10^9`

## Hints

> 💡 **Hint 1:** Run binary search twice: once to find the leftmost occurrence, once for the rightmost.

> 💡 **Hint 2:** For leftmost: when nums[mid] == target, don't stop — continue searching left (right = mid). For rightmost: when nums[mid] == target, continue searching right (left = mid + 1, then answer is left - 1).

> 💡 **Hint 3:** Alternatively, use `bisect_left` and `bisect_right` (Python) or implement equivalent logic.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Two binary searches: one for the leftmost position (lower bound), one for the rightmost (upper bound - 1).
