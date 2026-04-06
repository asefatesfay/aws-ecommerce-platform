# Maximum Subarray Sum with One Deletion

**Difficulty:** Medium
**Pattern:** Kadane's with State / DP
**LeetCode:** #1186

## Problem Statement

Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum is maximized.

## Examples

### Example 1
**Input:** `arr = [1, -2, 0, 3]`
**Output:** `4`
**Explanation:** Delete -2 to get [1,0,3] with sum 4.

### Example 2
**Input:** `arr = [1, -2, -2, 3]`
**Output:** `3`
**Explanation:** Just take [3].

### Example 3
**Input:** `arr = [-1, -1, -1, -1]`
**Output:** `-1`
**Explanation:** Must keep at least one element.

## Constraints
- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

## Hints

> 💡 **Hint 1:** Use DP with two states: `no_del[i]` = max subarray sum ending at i with no deletion, `one_del[i]` = max subarray sum ending at i with exactly one deletion.

> 💡 **Hint 2:** Transitions: `no_del[i] = max(arr[i], no_del[i-1] + arr[i])`. `one_del[i] = max(no_del[i-1], one_del[i-1] + arr[i])` — either delete arr[i] (take no_del[i-1]) or extend a subarray that already had a deletion.

> 💡 **Hint 3:** Answer is max over all i of max(no_del[i], one_del[i]).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two-state Kadane's: track max subarray sum ending here with 0 deletions and with 1 deletion. Transition between states at each step.
