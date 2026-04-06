# Jump Game

**Difficulty:** Medium
**Pattern:** Greedy
**LeetCode:** #55

## Problem Statement
Given an integer array `nums` where `nums[i]` is the maximum jump length from index `i`, return true if you can reach the last index starting from index 0.

## Examples

### Example 1
**Input:** `nums = [2,3,1,1,4]`
**Output:** `true`
**Explanation:** Jump 1 step from 0 to 1, then 3 steps to the last index.

### Example 2
**Input:** `nums = [3,2,1,0,4]`
**Output:** `false`
**Explanation:** You always reach index 3 with value 0, can't go further.

## Constraints
- `1 <= nums.length <= 10⁴`
- `0 <= nums[i] <= 10⁵`

## Hints

> 💡 **Hint 1:** Track the maximum index you can reach so far (`max_reach`). At each index `i`, if `i > max_reach`, you're stuck.

> 💡 **Hint 2:** Update `max_reach = max(max_reach, i + nums[i])` at each step.

> 💡 **Hint 3:** If you finish the loop without getting stuck, return true.

## Approach
**Time Complexity:** O(N)
**Space Complexity:** O(1)

Single pass: track the farthest reachable index. If current index exceeds it, return false. If we reach the end, return true.
