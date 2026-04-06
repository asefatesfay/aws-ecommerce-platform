# 132 Pattern

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #456

## Problem Statement

Given an array of `n` integers `nums`, a 132 pattern is a subsequence of three integers `nums[i]`, `nums[j]`, `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`. Return `true` if there is a 132 pattern in `nums`, otherwise, return `false`.

## Examples

### Example 1
**Input:** `nums = [1,2,3,4]`
**Output:** `false`

### Example 2
**Input:** `nums = [3,1,4,2]`
**Output:** `true`
**Explanation:** 1 < 2 < 4 (indices 1, 3, 2).

### Example 3
**Input:** `nums = [-1,3,2,0]`
**Output:** `true`

## Constraints
- `n == nums.length`
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** Scan from right to left. Use a monotonic stack to track potential "3" values (nums[j]). Track the best "2" value (nums[k]) seen so far.

> 💡 **Hint 2:** Maintain a decreasing stack. When you pop an element (because the current is larger), that popped element becomes the best candidate for "2" (nums[k]).

> 💡 **Hint 3:** If the current element (potential "1") is less than the best "2" candidate, you've found a 132 pattern.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Scan right to left with a monotonic decreasing stack. Track the maximum "2" value (third element in 132). Return true when a "1" smaller than "2" is found.
