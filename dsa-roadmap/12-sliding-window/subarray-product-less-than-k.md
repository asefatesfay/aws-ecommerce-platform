# Subarray Product Less Than K

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #713

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

## Examples

### Example 1
**Input:** `nums = [10, 5, 2, 6]`, `k = 100`
**Output:** `8`
**Explanation:** Subarrays with product < 100: [10],[5],[2],[6],[10,5],[5,2],[2,6],[5,2,6]. Note [10,5,2] = 100, not strictly less.

### Example 2
**Input:** `nums = [1, 2, 3]`, `k = 0`
**Output:** `0`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Hints

> 💡 **Hint 1:** Variable sliding window. Track the product of the current window. Expand right; when product ≥ k, shrink from the left.

> 💡 **Hint 2:** When the window [left, right] has product < k, how many valid subarrays end at `right`? All subarrays ending at `right` with left endpoint in [left, right] are valid — that's `right - left + 1` subarrays.

> 💡 **Hint 3:** Add `right - left + 1` to the count at each step (after ensuring the window is valid). This counts all new subarrays ending at `right`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Variable window tracking product. When product < k, add (right - left + 1) to count (all subarrays ending at right with valid product). Shrink when product ≥ k.
