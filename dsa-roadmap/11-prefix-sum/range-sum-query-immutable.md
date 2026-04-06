# Range Sum Query - Immutable

**Difficulty:** Easy
**Pattern:** Prefix Sum
**LeetCode:** #303

## Problem Statement

Given an integer array `nums`, handle multiple queries of the following type: calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive.

## Examples

### Example 1
**Input:** `["NumArray","sumRange","sumRange","sumRange"]` with `[[-2,0,3,-5,2,-1],[0,2],[2,5],[0,5]]`
**Output:** `[null,1,-1,-3]`
**Explanation:** sumRange(0,2) = -2+0+3 = 1. sumRange(2,5) = 3-5+2-1 = -1. sumRange(0,5) = -2+0+3-5+2-1 = -3.

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- At most `10^4` calls to `sumRange`

## Hints

> 💡 **Hint 1:** Computing the sum from scratch for each query is O(n) per query. With many queries, this is too slow.

> 💡 **Hint 2:** Precompute a prefix sum array where `prefix[i]` = sum of nums[0..i-1] (with prefix[0] = 0 as a sentinel).

> 💡 **Hint 3:** Then `sumRange(left, right) = prefix[right+1] - prefix[left]`. Each query is O(1) after O(n) preprocessing.

## Approach

**Time Complexity:** O(n) preprocessing, O(1) per query
**Space Complexity:** O(n)

Build prefix sum array in constructor. Answer each query with a single subtraction.
