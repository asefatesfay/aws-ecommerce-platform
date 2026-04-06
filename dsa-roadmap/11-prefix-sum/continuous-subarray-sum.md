# Continuous Subarray Sum

**Difficulty:** Medium
**Pattern:** Prefix Sum + Hash Map (Modulo)
**LeetCode:** #523

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a good subarray or `false` otherwise. A good subarray is a subarray where its length is at least two, and the sum of the elements of the subarray is a multiple of `k`.

## Examples

### Example 1
**Input:** `nums = [23, 2, 4, 6, 7]`, `k = 6`
**Output:** `true`
**Explanation:** [2, 4] is a subarray of length 2 with sum 6, which is a multiple of 6.

### Example 2
**Input:** `nums = [23, 2, 6, 4, 7]`, `k = 6`
**Output:** `true`
**Explanation:** [23,2,6,4,7] has sum 42 = 7×6.

### Example 3
**Input:** `nums = [23, 2, 6, 4, 7]`, `k = 13`
**Output:** `false`

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Similar to "Subarray Sums Divisible by K". A subarray sum is a multiple of k iff the prefix sums at both ends have the same remainder mod k.

> 💡 **Hint 2:** Store the first occurrence of each remainder in a HashMap. When you see the same remainder again, check if the subarray length is at least 2.

> 💡 **Hint 3:** Initialize the map with `{0: -1}` (remainder 0 at index -1, representing the empty prefix). If `current_remainder` is in the map and `i - map[remainder] >= 2`, return true.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Running prefix sum mod k. Store first occurrence of each remainder. When a remainder repeats with gap ≥ 2, return true.
