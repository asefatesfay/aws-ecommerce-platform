# Sliding Window Maximum

**Difficulty:** Hard
**Pattern:** Monotonic Deque
**LeetCode:** #239

## Problem Statement

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

## Examples

### Example 1
**Input:** `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
**Output:** `[3,3,5,5,6,7]`

### Example 2
**Input:** `nums = [1]`, `k = 1`
**Output:** `[1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

## Hints

> 💡 **Hint 1:** A naive approach checks all k elements per window — O(nk). Use a monotonic deque for O(n).

> 💡 **Hint 2:** Maintain a decreasing deque of indices. When adding index i: remove from the back all indices j where nums[j] <= nums[i] (they can never be the max while i is in the window). Remove from the front if the front index is outside the window.

> 💡 **Hint 3:** The front of the deque is always the index of the maximum in the current window. Record it when the window is full (i >= k-1).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(k)

Monotonic decreasing deque of indices. Each element is added and removed at most once. Front always holds the current window maximum.
