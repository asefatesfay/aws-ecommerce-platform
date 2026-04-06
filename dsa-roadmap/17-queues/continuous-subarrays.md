# Continuous Subarrays

**Difficulty:** Medium
**Pattern:** Monotonic Deque / Sliding Window
**LeetCode:** #2762

## Problem Statement

You are given a 0-indexed integer array `nums`. A subarray of `nums` is called continuous if for any two elements `nums[i]` and `nums[j]` in the subarray, `|nums[i] - nums[j]| <= 2`. Return the total number of continuous subarrays.

## Examples

### Example 1
**Input:** `nums = [5,4,2,4]`
**Output:** `8`
**Explanation:** Continuous subarrays of size 1: [5],[4],[2],[4] = 4. Size 2: [5,4],[4,2],[2,4] = 3. Size 3: [4,2,4] = 1. Total = 8.

### Example 2
**Input:** `nums = [1,2,3]`
**Output:** `6`

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** A subarray is valid if max - min ≤ 2. Use two monotonic deques (one for max, one for min) with a sliding window.

> 💡 **Hint 2:** Variable window: expand right, shrink left when max - min > 2. For each valid right endpoint, all subarrays ending there with left in [left, right] are valid.

> 💡 **Hint 3:** Add `right - left + 1` to the count for each valid window position.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Two monotonic deques for max and min. Variable sliding window. Count valid subarrays ending at each right endpoint.
