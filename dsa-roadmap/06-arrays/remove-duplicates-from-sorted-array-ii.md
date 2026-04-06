# Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #80

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. Return the number of elements `k` in the modified array. The first `k` elements should hold the result.

## Examples

### Example 1
**Input:** `nums = [1, 1, 1, 2, 2, 3]`
**Output:** `5`, `nums = [1, 1, 2, 2, 3, _]`
**Explanation:** Each element appears at most twice. 1 appears twice, 2 appears twice, 3 appears once.

### Example 2
**Input:** `nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]`
**Output:** `7`, `nums = [0, 0, 1, 1, 2, 3, 3, _, _]`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** This is a generalization of "Remove Duplicates I". Instead of allowing 1 occurrence, you allow 2. Think about how to adapt the write pointer logic.

> 💡 **Hint 2:** Use a write pointer `k` starting at 2 (the first two elements are always valid). For each element at index i ≥ 2, compare it with the element at position `k-2` (two positions behind the write pointer).

> 💡 **Hint 3:** If `nums[i] != nums[k-2]`, the current element is safe to include (it can't be a third duplicate). Write it to position `k` and advance `k`. This works because the array is sorted.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Start the write pointer at 2. For each element from index 2 onward, if it differs from the element two positions behind the write pointer, write it and advance the pointer. The key insight: in a sorted array, if `nums[i] == nums[k-2]`, then `nums[i]` would be at least the third occurrence of that value.
