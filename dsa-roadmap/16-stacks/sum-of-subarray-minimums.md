# Sum of Subarray Minimums

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #907

## Problem Statement

Given an array of integers `arr`, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer modulo `10^9 + 7`.

## Examples

### Example 1
**Input:** `arr = [3,1,2,4]`
**Output:** `17`
**Explanation:** Subarrays: [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2, [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1. Sum=17.

### Example 2
**Input:** `arr = [11,81,94,43,3]`
**Output:** `444`

## Constraints
- `1 <= arr.length <= 3 * 10^4`
- `1 <= arr[i] <= 3 * 10^4`

## Hints

> 💡 **Hint 1:** For each element, find how many subarrays have it as the minimum. This equals (number of subarrays where it's the leftmost minimum) × (number of subarrays where it's the rightmost minimum).

> 💡 **Hint 2:** For each element arr[i], find `left[i]` = distance to the previous smaller element, and `right[i]` = distance to the next smaller-or-equal element. Use monotonic stacks.

> 💡 **Hint 3:** The contribution of arr[i] is `arr[i] * left[i] * right[i]`. Sum all contributions.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Two monotonic stack passes to find left and right boundaries for each element as minimum. Contribution = value × left_count × right_count.
