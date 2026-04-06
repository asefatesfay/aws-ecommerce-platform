# Maximum Absolute Sum of Any Subarray

**Difficulty:** Medium
**Pattern:** Kadane's Algorithm
**LeetCode:** #1749

## Problem Statement

You are given an integer array `nums`. The absolute sum of a subarray `[nums_l, nums_{l+1}, ..., nums_r-1, nums_r]` is `abs(nums_l + nums_{l+1} + ... + nums_r-1 + nums_r)`. Return the maximum absolute sum of any (possibly empty) subarray of `nums`.

## Examples

### Example 1
**Input:** `nums = [1, -3, 2, 3, -4]`
**Output:** `5`
**Explanation:** [2,3] has sum 5, absolute value 5.

### Example 2
**Input:** `nums = [2, -5, 1, -4, 3, -2]`
**Output:** `8`
**Explanation:** [-5,1,-4] has sum -8, absolute value 8.

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** The maximum absolute sum is either the maximum subarray sum or the absolute value of the minimum subarray sum.

> 💡 **Hint 2:** Run Kadane's algorithm twice: once to find the maximum subarray sum, once to find the minimum subarray sum.

> 💡 **Hint 3:** Return `max(max_sum, abs(min_sum))`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Run Kadane's for both maximum and minimum subarray sums. Return the maximum of the two absolute values.
