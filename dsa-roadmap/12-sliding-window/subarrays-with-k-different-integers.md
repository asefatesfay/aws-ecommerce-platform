# Subarrays with K Different Integers

**Difficulty:** Hard
**Pattern:** Sliding Window — "At Most K" Trick
**LeetCode:** #992

## Problem Statement

Given an integer array `nums` and an integer `k`, return the number of good subarrays of `nums`. A good array is an array where the number of different integers in that array is exactly `k`.

## Examples

### Example 1
**Input:** `nums = [1, 2, 1, 2, 3]`, `k = 2`
**Output:** `7`
**Explanation:** Subarrays with exactly 2 different integers: [1,2],[2,1],[1,2],[2,3],[1,2,1],[2,1,2],[1,2,1,2].

### Example 2
**Input:** `nums = [1, 2, 1, 3, 4]`, `k = 3`
**Output:** `3`
**Explanation:** [1,2,1,3],[2,1,3],[1,3,4].

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i] <= nums.length`
- `1 <= k <= nums.length`

## Hints

> 💡 **Hint 1:** Counting subarrays with exactly k distinct values is hard directly. Use the "at most k" trick.

> 💡 **Hint 2:** `count(exactly k) = count(at most k) - count(at most k-1)`.

> 💡 **Hint 3:** For "at most k distinct", use a variable sliding window with a frequency map. When distinct count > k, shrink from the left. The number of valid subarrays ending at `right` is `right - left + 1`.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Implement "at most k distinct" as a sliding window helper. Call it twice (k and k-1) and subtract the results.
