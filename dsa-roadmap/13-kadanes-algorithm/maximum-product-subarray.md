# Maximum Product Subarray

**Difficulty:** Medium
**Pattern:** Kadane's (Product Variant)
**LeetCode:** #152

## Problem Statement

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

## Examples

### Example 1
**Input:** `nums = [2, 3, -2, 4]`
**Output:** `6`
**Explanation:** [2,3] has product 6.

### Example 2
**Input:** `nums = [-2, 0, -1]`
**Output:** `0`
**Explanation:** The result cannot be 2 because [-2,-1] is not a subarray.

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer

## Hints

> 💡 **Hint 1:** Unlike sum, product has a complication: a large negative number can become the maximum if multiplied by another negative. You need to track both the maximum and minimum product ending at each position.

> 💡 **Hint 2:** At each position, the new max is `max(nums[i], max_prev * nums[i], min_prev * nums[i])`. The new min is `min(nums[i], max_prev * nums[i], min_prev * nums[i])`.

> 💡 **Hint 3:** Track both `max_prod` and `min_prod` at each step. Update the global maximum with `max_prod`. When you see a 0, both reset to 0 (or the current element).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track both maximum and minimum product ending at each position. The minimum can become the maximum when multiplied by a negative number. Update global max at each step.
