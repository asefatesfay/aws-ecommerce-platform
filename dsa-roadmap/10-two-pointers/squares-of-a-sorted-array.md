# Squares of a Sorted Array

**Difficulty:** Easy
**Pattern:** Two Pointers (Opposite Ends)
**LeetCode:** #977

## Problem Statement

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Examples

### Example 1
**Input:** `nums = [-4, -1, 0, 3, 10]`
**Output:** `[0, 1, 9, 16, 100]`

### Example 2
**Input:** `nums = [-7, -3, 2, 3, 11]`
**Output:** `[4, 9, 9, 49, 121]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order

## Hints

> 💡 **Hint 1:** Squaring removes the sign, so the largest squares come from either end of the sorted array (most negative or most positive values).

> 💡 **Hint 2:** Use two pointers at both ends. Compare the absolute values (or squares) at each pointer. The larger square goes into the result array from the back.

> 💡 **Hint 3:** Fill the result array from right to left. At each step, place the larger of the two end squares at the current position, then advance the corresponding pointer inward.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) for the output

Two pointers from both ends, filling the result array from right to left with the larger square at each step.
