# Search Insert Position

**Difficulty:** Easy
**Pattern:** Binary Search
**LeetCode:** #35

## Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

## Examples

### Example 1
**Input:** `nums = [1,3,5,6]`, `target = 5`
**Output:** `2`

### Example 2
**Input:** `nums = [1,3,5,6]`, `target = 2`
**Output:** `1`

### Example 3
**Input:** `nums = [1,3,5,6]`, `target = 7`
**Output:** `4`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains distinct values sorted in ascending order
- `-10^4 <= target <= 10^4`

## Hints

> 💡 **Hint 1:** Standard binary search, but instead of returning -1 when not found, return the left pointer.

> 💡 **Hint 2:** When the loop ends (left > right), `left` is the insertion position.

> 💡 **Hint 3:** This is equivalent to finding the leftmost position where nums[i] >= target.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search: return mid if found, otherwise return left (the insertion point).
