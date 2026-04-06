# House Robber

**Difficulty:** Medium
**Pattern:** 1D DP
**LeetCode:** #198

## Problem Statement
You are a robber planning to rob houses along a street. Adjacent houses have security systems — you cannot rob two adjacent houses. Given `nums[i]` = money in house i, return the maximum amount you can rob.

## Examples

### Example 1
**Input:** `nums = [1,2,3,1]`
**Output:** `4`
**Explanation:** Rob house 1 (1) + house 3 (3) = 4.

### Example 2
**Input:** `nums = [2,7,9,3,1]`
**Output:** `12`
**Explanation:** Rob house 1 (2) + house 3 (9) + house 5 (1) = 12.

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Hints

> 💡 **Hint 1:** At each house, you decide: rob it (can't rob previous) or skip it (keep previous max).

> 💡 **Hint 2:** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` — either skip house i or rob it plus the best from two houses back.

> 💡 **Hint 3:** Only need two variables — optimize to O(1) space.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Track `prev2` (best up to i-2) and `prev1` (best up to i-1). At each step: `curr = max(prev1, prev2 + nums[i])`.
