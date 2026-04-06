# Shortest Unsorted Continuous Subarray

**Difficulty:** Medium
**Pattern:** Stack / Two Pointers
**LeetCode:** #581

## Problem Statement

Given an integer array `nums`, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order. Return the shortest such subarray and output its length.

## Examples

### Example 1
**Input:** `nums = [2,6,4,8,10,9,15]`
**Output:** `5`
**Explanation:** Sort [6,4,8,10,9] to get the whole array sorted.

### Example 2
**Input:** `nums = [1,2,3,4]`
**Output:** `0`

### Example 3
**Input:** `nums = [1]`
**Output:** `0`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Find the leftmost element that is out of order (greater than the minimum of the suffix). Find the rightmost element that is out of order (less than the maximum of the prefix).

> 💡 **Hint 2:** Scan left to right tracking the running maximum. When nums[i] < running_max, i is a candidate for the right boundary.

> 💡 **Hint 3:** Scan right to left tracking the running minimum. When nums[i] > running_min, i is a candidate for the left boundary. The answer is right - left + 1.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two passes: find the rightmost position where the element is less than the running max (left to right), and the leftmost position where the element is greater than the running min (right to left).
