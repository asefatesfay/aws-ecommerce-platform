# 4Sum

**Difficulty:** Medium
**Pattern:** Two Pointers + Sorting
**LeetCode:** #18

## Problem Statement

Given an array `nums` of `n` integers and an integer `target`, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that `a, b, c, d` are distinct indices and `nums[a] + nums[b] + nums[c] + nums[d] == target`.

## Examples

### Example 1
**Input:** `nums = [1, 0, -1, 0, -2, 2]`, `target = 0`
**Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### Example 2
**Input:** `nums = [2, 2, 2, 2, 2]`, `target = 8`
**Output:** `[[2,2,2,2]]`

## Constraints
- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Hints

> 💡 **Hint 1:** This is a generalization of 3Sum. Sort the array and use two nested loops to fix the first two elements, then use two pointers for the remaining two.

> 💡 **Hint 2:** Outer loop fixes index i, inner loop fixes index j (j > i). Two pointers left = j+1, right = n-1 find pairs summing to `target - nums[i] - nums[j]`.

> 💡 **Hint 3:** Skip duplicates at all three levels: for i, for j, and for the two-pointer step. Be careful with overflow when computing sums (use long/int64).

## Approach

**Time Complexity:** O(n³)
**Space Complexity:** O(1) extra

Sort, then two nested loops fixing the first two elements, with two pointers for the last two. Skip duplicates at each level to avoid duplicate quadruplets.
