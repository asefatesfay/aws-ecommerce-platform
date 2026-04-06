# 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers + Sorting
**LeetCode:** #15

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1
**Input:** `nums = [-1, 0, 1, 2, -1, -4]`
**Output:** `[[-1,-1,2],[-1,0,1]]`

### Example 2
**Input:** `nums = [0, 1, 1]`
**Output:** `[]`

### Example 3
**Input:** `nums = [0, 0, 0]`
**Output:** `[[0,0,0]]`

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Sort the array first. This enables two-pointer and easy duplicate skipping.

> 💡 **Hint 2:** Fix the first element with an outer loop (index i). For the remaining subarray, use two pointers to find pairs that sum to `-nums[i]`.

> 💡 **Hint 3:** Skip duplicates: if `nums[i] == nums[i-1]`, skip (same first element). After finding a valid triplet, skip duplicate values for both left and right pointers before continuing.

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(1) extra (output not counted)

Sort, then for each element as the first of the triplet, use two pointers on the remaining sorted subarray to find pairs summing to the negation. Skip duplicates at each level.
