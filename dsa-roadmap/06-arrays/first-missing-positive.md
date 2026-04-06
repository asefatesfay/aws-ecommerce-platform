# First Missing Positive

**Difficulty:** Hard
**Pattern:** Index as Identity / Cyclic Sort
**LeetCode:** #41

## Problem Statement

Given an unsorted integer array `nums`, return the smallest missing positive integer. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

## Examples

### Example 1
**Input:** `nums = [1, 2, 0]`
**Output:** `3`

### Example 2
**Input:** `nums = [3, 4, -1, 1]`
**Output:** `2`

### Example 3
**Input:** `nums = [7, 8, 9, 11, 12]`
**Output:** `1`

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** The answer must be in the range [1, n+1] where n is the array length. Why? Because with n elements, the worst case is [1, 2, ..., n], making the answer n+1.

> 💡 **Hint 2:** Use the array itself as a hash map. The value x (if 1 ≤ x ≤ n) should be at index x-1. Rearrange elements to their "correct" positions by swapping.

> 💡 **Hint 3:** After rearranging, scan the array. The first index i where nums[i] != i+1 means i+1 is the missing positive. If all positions are correct, return n+1.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Cyclic sort: for each element, if it's in range [1, n] and not already at its correct position (index value-1), swap it to its correct position. After sorting, the first index where the value doesn't match is the answer.
