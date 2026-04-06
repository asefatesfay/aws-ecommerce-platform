# Maximum Width Ramp

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**LeetCode:** #962

## Problem Statement

A ramp in an integer array `nums` is a pair `(i, j)` for which `i < j` and `nums[i] <= nums[j]`. The width of such a ramp is `j - i`. Given an integer array `nums`, return the maximum width of a ramp in `nums`. If there is no ramp in `nums`, return `0`.

## Examples

### Example 1
**Input:** `nums = [6,0,8,2,1,5]`
**Output:** `4`
**Explanation:** Ramp (1,5): nums[1]=0 ≤ nums[5]=5, width=4.

### Example 2
**Input:** `nums = [9,8,1,0,1,9,4,0,4,1]`
**Output:** `7`

## Constraints
- `2 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 5 * 10^4`

## Hints

> 💡 **Hint 1:** Build a decreasing stack of indices from left to right (only push if nums[i] < current stack top's value). These are the candidates for the left end of the ramp.

> 💡 **Hint 2:** Scan from right to left. For each j, pop indices from the stack while nums[stack.top] <= nums[j]. The width is j - stack.top.

> 💡 **Hint 3:** Track the maximum width. The right-to-left scan ensures we find the maximum j for each candidate i.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Build decreasing stack of left candidates. Scan right to left, popping and computing widths. Track maximum.
