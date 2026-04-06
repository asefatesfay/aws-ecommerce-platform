# Contains Duplicate II

**Difficulty:** Easy
**Pattern:** Hash Map / Sliding Window
**LeetCode:** #219

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 1]`, `k = 3`
**Output:** `true`
**Explanation:** nums[0] == nums[3] and |0-3| = 3 ≤ 3.

### Example 2
**Input:** `nums = [1, 0, 1, 1]`, `k = 1`
**Output:** `true`

### Example 3
**Input:** `nums = [1, 2, 3, 1, 2, 3]`, `k = 2`
**Output:** `false`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Hints

> 💡 **Hint 1:** For each element, you need to know if the same value appeared within the last k positions.

> 💡 **Hint 2:** Use a HashMap that maps each value to its most recent index. When you see a value again, check if the index difference is ≤ k.

> 💡 **Hint 3:** Always update the map with the current index (even if a duplicate was found), so future checks use the most recent occurrence.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, k))

HashMap from value to most recent index. For each element, check if it's in the map and the index difference is ≤ k. Update the map with the current index.
