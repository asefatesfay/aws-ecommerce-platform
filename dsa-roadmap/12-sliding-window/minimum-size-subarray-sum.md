# Minimum Size Subarray Sum

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #209

## Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

## Examples

### Example 1
**Input:** `target = 7`, `nums = [2, 3, 1, 2, 4, 3]`
**Output:** `2`
**Explanation:** [4,3] has sum 7 and length 2.

### Example 2
**Input:** `target = 4`, `nums = [1, 4, 4]`
**Output:** `1`

### Example 3
**Input:** `target = 11`, `nums = [1, 1, 1, 1, 1, 1, 1, 1]`
**Output:** `0`

## Constraints
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Hints

> 💡 **Hint 1:** Use a variable sliding window. Expand the right pointer to increase the sum. When the sum meets the target, try to shrink from the left.

> 💡 **Hint 2:** When `current_sum >= target`, record the window length and shrink from the left (subtract nums[left], advance left). Keep shrinking as long as the sum remains ≥ target.

> 💡 **Hint 3:** Track the minimum window length seen. Initialize to infinity; return 0 if it never changed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Variable window: expand right to grow sum, shrink left when sum ≥ target. Track minimum window length when constraint is satisfied.
