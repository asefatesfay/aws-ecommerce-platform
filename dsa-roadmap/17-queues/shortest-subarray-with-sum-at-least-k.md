# Shortest Subarray with Sum at Least K

**Difficulty:** Hard
**Pattern:** Monotonic Deque + Prefix Sum
**LeetCode:** #862

## Problem Statement

Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.

## Examples

### Example 1
**Input:** `nums = [1]`, `k = 1`
**Output:** `1`

### Example 2
**Input:** `nums = [1,2]`, `k = 4`
**Output:** `-1`

### Example 3
**Input:** `nums = [2,-1,2]`, `k = 3`
**Output:** `3`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`
- `1 <= k <= 10^9`

## Hints

> 💡 **Hint 1:** Build a prefix sum array. The sum of subarray [l, r] = prefix[r+1] - prefix[l]. You want the shortest [l, r] where this is ≥ k.

> 💡 **Hint 2:** Use a monotonic increasing deque of prefix sum indices. For each new prefix sum index r, pop from the front while `prefix[r] - prefix[front] >= k` — these are valid subarrays, and we want the shortest.

> 💡 **Hint 3:** After checking the front, remove from the back any indices with prefix sum ≥ current prefix sum (they can never give a shorter valid subarray).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Prefix sum + monotonic increasing deque. For each right endpoint, find the leftmost valid left endpoint using the deque.
