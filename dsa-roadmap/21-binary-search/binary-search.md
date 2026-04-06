# Binary Search

**Difficulty:** Easy
**Pattern:** Binary Search
**LeetCode:** #704

## Problem Statement

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`. You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1
**Input:** `nums = [-1,0,3,5,9,12]`, `target = 9`
**Output:** `4`

### Example 2
**Input:** `nums = [-1,0,3,5,9,12]`, `target = 2`
**Output:** `-1`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique
- `nums` is sorted in ascending order

## Hints

> 💡 **Hint 1:** Maintain left and right boundaries. Compute mid = (left + right) // 2.

> 💡 **Hint 2:** If nums[mid] == target, return mid. If nums[mid] < target, search right half (left = mid + 1). If nums[mid] > target, search left half (right = mid - 1).

> 💡 **Hint 3:** Continue while left <= right. Return -1 if not found.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Standard binary search: halve the search space at each step based on comparison with mid.
