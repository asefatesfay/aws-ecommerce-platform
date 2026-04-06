# Longest Turbulent Subarray

**Difficulty:** Medium
**Pattern:** Kadane's / Sliding Window
**LeetCode:** #978

## Problem Statement

Given an integer array `arr`, return the length of a maximum size turbulent subarray of `arr`. A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray. Formally, a subarray `arr[i..j]` is turbulent if for each `i <= k < j`: `arr[k] > arr[k+1]` when k is odd, and `arr[k] < arr[k+1]` when k is even. Or vice versa.

## Examples

### Example 1
**Input:** `arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]`
**Output:** `5`
**Explanation:** [4,2,10,7,8] is turbulent: 4>2<10>7<8.

### Example 2
**Input:** `arr = [4, 8, 12, 16]`
**Output:** `2`

### Example 3
**Input:** `arr = [100]`
**Output:** `1`

## Constraints
- `1 <= arr.length <= 4 * 10^4`
- `0 <= arr[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Use a Kadane's-style approach. Track the length of the current turbulent subarray ending at each position.

> 💡 **Hint 2:** At each position i, check if the comparison sign between arr[i-1] and arr[i] is opposite to the sign between arr[i-2] and arr[i-1]. If yes, extend the current subarray. If no (or equal), reset.

> 💡 **Hint 3:** Track the current length and the maximum length. Reset to 1 (or 2 if the current pair is strictly increasing/decreasing) when the turbulent property breaks.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass tracking current turbulent length. Extend when the comparison sign alternates; reset when it doesn't or when elements are equal.
