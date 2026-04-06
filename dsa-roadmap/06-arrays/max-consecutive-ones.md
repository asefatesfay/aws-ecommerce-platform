# Max Consecutive Ones

**Difficulty:** Easy
**Pattern:** Array / Counting
**LeetCode:** #485

## Problem Statement

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

## Examples

### Example 1
**Input:** `nums = [1, 1, 0, 1, 1, 1]`
**Output:** `3`
**Explanation:** The last three elements are all 1s, giving a run of 3.

### Example 2
**Input:** `nums = [1, 0, 1, 1, 0, 1]`
**Output:** `2`

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

## Hints

> 💡 **Hint 1:** Scan through the array, keeping a running count of the current streak of 1s.

> 💡 **Hint 2:** When you see a 1, increment the current count. When you see a 0, reset the current count to 0.

> 💡 **Hint 3:** At each step, update a global maximum with the current count. Return the maximum at the end.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Single pass: maintain a current count and a maximum count. Increment current on 1, reset to 0 on 0, and update maximum at each step.
