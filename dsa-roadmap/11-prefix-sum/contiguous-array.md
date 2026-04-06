# Contiguous Array

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map
**LeetCode:** #525

## Problem Statement

Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

## Examples

### Example 1
**Input:** `nums = [0, 1]`
**Output:** `2`
**Explanation:** [0, 1] has equal 0s and 1s.

### Example 2
**Input:** `nums = [0, 1, 0]`
**Output:** `2`
**Explanation:** [0, 1] or [1, 0].

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

## Hints

> 💡 **Hint 1:** Transform the problem: replace 0s with -1s. Now "equal number of 0s and 1s" becomes "subarray sum equals 0".

> 💡 **Hint 2:** Use a prefix sum. A subarray from l to r has sum 0 iff `prefix[r] == prefix[l-1]`. You want the longest such subarray.

> 💡 **Hint 3:** Use a HashMap storing the first occurrence of each prefix sum. When you see the same prefix sum again, the subarray between those indices has sum 0. Track the maximum length.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Replace 0→-1. Running prefix sum with a HashMap storing first occurrence of each sum. When a sum repeats, compute the subarray length and update the maximum.
