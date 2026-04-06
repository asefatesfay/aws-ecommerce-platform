# Count Subarrays With Fixed Bounds

**Difficulty:** Hard
**Pattern:** Two Pointers / Sliding Window
**LeetCode:** #2444

## Problem Statement

You are given an integer array `nums` and two integers `minK` and `maxK`. A fixed-bound subarray of `nums` is a subarray that satisfies the following conditions:
- The minimum value in the subarray is equal to `minK`.
- The maximum value in the subarray is equal to `maxK`.

Return the number of fixed-bound subarrays.

## Examples

### Example 1
**Input:** `nums = [1, 3, 5, 2, 7, 5]`, `minK = 1`, `maxK = 5`
**Output:** `2`
**Explanation:** Fixed-bound subarrays are [1,3,5] and [1,3,5,2].

### Example 2
**Input:** `nums = [1, 1, 1, 1]`, `minK = 1`, `maxK = 1`
**Output:** `10`

## Constraints
- `2 <= nums.length <= 10^5`
- `1 <= nums[i], minK, maxK <= 10^6`

## Hints

> 💡 **Hint 1:** Any element outside [minK, maxK] breaks a valid subarray. Track the last "bad" index (element out of range).

> 💡 **Hint 2:** Track the last position where minK was seen (`last_min`) and the last position where maxK was seen (`last_max`). A valid subarray ending at index i must contain both.

> 💡 **Hint 3:** For each index i, the number of valid subarrays ending at i is `max(0, min(last_min, last_max) - last_bad)`. Sum this across all i.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass tracking three positions: last bad index, last minK index, last maxK index. For each position, count valid subarrays ending there using the formula above.
