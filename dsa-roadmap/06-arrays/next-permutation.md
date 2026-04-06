# Next Permutation

**Difficulty:** Medium
**Pattern:** Array Manipulation
**LeetCode:** #31

## Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order. The next permutation of an array of integers is the next lexicographically greater permutation of its integer. If no such arrangement is possible (the array is in descending order), rearrange it as the lowest possible order (ascending order).

The replacement must be in place and use only constant extra memory.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3]`
**Output:** `[1, 3, 2]`

### Example 2
**Input:** `nums = [3, 2, 1]`
**Output:** `[1, 2, 3]`
**Explanation:** Already the largest permutation, so wrap around to smallest.

### Example 3
**Input:** `nums = [1, 1, 5]`
**Output:** `[1, 5, 1]`

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Hints

> 💡 **Hint 1:** To find the next permutation, you need to make the smallest possible increase. Scan from right to left to find the first element that is smaller than its right neighbor — this is the "pivot".

> 💡 **Hint 2:** Once you find the pivot at index i, find the smallest element to its right that is still larger than nums[i]. Swap them. Now the suffix (everything after index i) is in descending order.

> 💡 **Hint 3:** Reverse the suffix after index i to make it ascending (the smallest possible arrangement for that suffix). This gives the next permutation.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Three steps: (1) find the rightmost "dip" (index i where nums[i] < nums[i+1]), (2) find the smallest element to the right of i that is greater than nums[i] and swap them, (3) reverse the suffix starting at i+1 to get the smallest arrangement.
