# Maximum Sum Circular Subarray

**Difficulty:** Medium
**Pattern:** Kadane's Algorithm (Circular Variant)
**LeetCode:** #918

## Problem Statement

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray of `nums`. A circular array means the end of the array connects to the beginning. A subarray may only include each element of the fixed buffer `nums` at most once.

## Examples

### Example 1
**Input:** `nums = [1, -2, 3, -2]`
**Output:** `3`
**Explanation:** [3] has sum 3.

### Example 2
**Input:** `nums = [5, -3, 5]`
**Output:** `10`
**Explanation:** [5,5] (wrapping around) has sum 10.

### Example 3
**Input:** `nums = [-3, -2, -3]`
**Output:** `-2`

## Constraints
- `n == nums.length`
- `1 <= n <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Hints

> 💡 **Hint 1:** There are two cases: the maximum subarray doesn't wrap around (standard Kadane's), or it does wrap around.

> 💡 **Hint 2:** If it wraps around, the subarray consists of a prefix and a suffix. Maximizing prefix + suffix = total sum - minimum middle subarray. Use Kadane's to find the minimum subarray sum.

> 💡 **Hint 3:** Answer = max(max_subarray_sum, total_sum - min_subarray_sum). Edge case: if all elements are negative, the circular answer would be total - total = 0, which is wrong. In that case, return the standard Kadane's result.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Run Kadane's for maximum subarray and minimum subarray. Answer is max(max_kadane, total - min_kadane), with the edge case that if all elements are negative, return max_kadane.
