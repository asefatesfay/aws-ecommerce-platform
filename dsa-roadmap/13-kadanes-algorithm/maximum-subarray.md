# Maximum Subarray

**Difficulty:** Medium
**Pattern:** Kadane's Algorithm
**LeetCode:** #53

## Problem Statement

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

## Examples

### Example 1
**Input:** `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Output:** `6`
**Explanation:** [4,-1,2,1] has the largest sum = 6.

### Example 2
**Input:** `nums = [1]`
**Output:** `1`

### Example 3
**Input:** `nums = [5, 4, -1, 7, 8]`
**Output:** `23`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** At each position, you have two choices: start a new subarray here, or extend the current subarray. Which is better?

> 💡 **Hint 2:** If the current running sum is negative, it's always better to start fresh at the current element. A negative prefix only hurts the total.

> 💡 **Hint 3:** Track `current_sum = max(nums[i], current_sum + nums[i])` and `max_sum = max(max_sum, current_sum)`. This is Kadane's algorithm.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Kadane's: maintain a running sum that resets to the current element when it would be negative. Track the global maximum.
