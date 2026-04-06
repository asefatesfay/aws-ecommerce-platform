# Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Pattern:** Two Pointers (Opposite Ends)
**LeetCode:** #167

## Problem Statement

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2. The tests are generated such that there is exactly one solution. You may not use the same element twice. Your solution must use only constant extra space.

## Examples

### Example 1
**Input:** `numbers = [2, 7, 11, 15]`, `target = 9`
**Output:** `[1, 2]`
**Explanation:** 2 + 7 = 9. Indices 1 and 2 (1-indexed).

### Example 2
**Input:** `numbers = [2, 3, 4]`, `target = 6`
**Output:** `[1, 3]`

### Example 3
**Input:** `numbers = [-1, 0]`, `target = -1`
**Output:** `[1, 2]`

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- Exactly one solution exists

## Hints

> 💡 **Hint 1:** The array is sorted — use this property. A HashMap would work but uses O(n) space. Can you do O(1)?

> 💡 **Hint 2:** Place one pointer at the start and one at the end. Compute their sum.

> 💡 **Hint 3:** If sum == target, return the indices. If sum < target, move left pointer right (need larger sum). If sum > target, move right pointer left (need smaller sum).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers from both ends. Adjust based on whether the current sum is too small or too large. Guaranteed to find the solution.
