# Frequency of the Most Frequent Element

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable) + Sorting
**LeetCode:** #1838

## Problem Statement

The frequency of an element is the number of times it occurs in an array. You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`. Return the maximum possible frequency of an element after performing at most `k` operations.

## Examples

### Example 1
**Input:** `nums = [1, 2, 4]`, `k = 5`
**Output:** `3`
**Explanation:** Increment 1 twice and 2 once to get [3,3,4] — wait, increment to make all equal to 4: 1→4 (3 ops), 2→4 (2 ops). Total 5 ops. Frequency of 4 = 3.

### Example 2
**Input:** `nums = [1, 4, 8, 13]`, `k = 5`
**Output:** `2`

### Example 3
**Input:** `nums = [3, 9, 6]`, `k = 2`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Hints

> 💡 **Hint 1:** Sort the array. To make multiple elements equal to some target, it's cheapest to make them all equal to the largest element in the group (you can only increment, not decrement).

> 💡 **Hint 2:** Use a sliding window on the sorted array. The target value is always nums[right] (the largest in the window). The cost to make all elements in [left, right] equal to nums[right] is `nums[right] * window_size - window_sum`.

> 💡 **Hint 3:** If cost > k, shrink from the left. Track the maximum window size where cost ≤ k.

## Approach

**Time Complexity:** O(n log n) for sorting
**Space Complexity:** O(1)

Sort, then variable window. Cost to equalize window to nums[right] = nums[right] * size - sum. Shrink when cost > k. Track maximum window size.
