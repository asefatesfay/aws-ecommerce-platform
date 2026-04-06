# House Robber II

**Difficulty:** Medium
**Pattern:** 1D DP / Circular Array
**LeetCode:** #213

## Problem Statement
You are a robber planning to rob houses in a circle. Adjacent houses have alarms, and the first and last house are also adjacent.

Given `nums[i]` as money in house `i`, return the maximum amount you can rob without robbing two adjacent houses.

## Examples

### Example 1
**Input:** `nums = [2,3,2]`
**Output:** `3`

### Example 2
**Input:** `nums = [1,2,3,1]`
**Output:** `4`

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## DP Breakdown
- In a circle, you cannot take both first and last house.
- Split into two linear robberies:
  - rob range `[0..n-2]`
  - rob range `[1..n-1]`
- **Answer:** `max(robLinear(0..n-2), robLinear(1..n-1))`

## Hints
- Reuse the House Robber I helper for linear arrays.
- Handle `n == 1` as a special case.
- Linear transition: `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Compute best non-adjacent sum twice on two ranges, then take max.