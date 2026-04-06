# Remove Duplicates from Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #26

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements `k`. The first `k` elements of `nums` should hold the unique elements in order.

## Examples

### Example 1
**Input:** `nums = [1, 1, 2]`
**Output:** `2`, `nums = [1, 2, _]`
**Explanation:** Two unique elements: 1 and 2.

### Example 2
**Input:** `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
**Output:** `5`, `nums = [0, 1, 2, 3, 4, _, _, _, _, _]`
**Explanation:** Five unique elements: 0, 1, 2, 3, 4.

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Since the array is sorted, all duplicates of a value are adjacent. You only need to keep the first occurrence of each value.

> 💡 **Hint 2:** Use a write pointer `k` starting at 1 (the first element is always unique). Scan from index 1; whenever `nums[i] != nums[i-1]`, it's a new unique value — write it to position `k`.

> 💡 **Hint 3:** The condition `nums[i] != nums[k-1]` (comparing with the last written value) is equivalent and slightly cleaner. Advance `k` each time you write.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Use a write pointer starting at 1. Scan from index 1; whenever the current element differs from the previous element (or from the last written element), copy it to the write position and advance the write pointer.
