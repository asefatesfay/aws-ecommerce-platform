# Find Pivot Index

**Difficulty:** Easy
**Pattern:** Prefix Sum
**LeetCode:** #724

## Problem Statement

Given an array of integers `nums`, calculate the pivot index of this array. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the right of the index. If the index is on the left edge of the array, then the left sum is 0. Return the leftmost pivot index. If no such index exists, return -1.

## Examples

### Example 1
**Input:** `nums = [1, 7, 3, 6, 5, 6]`
**Output:** `3`
**Explanation:** Left sum of index 3 = 1+7+3 = 11. Right sum = 5+6 = 11.

### Example 2
**Input:** `nums = [1, 2, 3]`
**Output:** `-1`

### Example 3
**Input:** `nums = [2, 1, -1]`
**Output:** `0`
**Explanation:** Left sum = 0, right sum = 1+(-1) = 0.

## Constraints
- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

## Hints

> 💡 **Hint 1:** Compute the total sum of the array. Then scan left to right, maintaining a running left sum.

> 💡 **Hint 2:** At each index i, the right sum = total - left_sum - nums[i]. Check if left_sum == right_sum.

> 💡 **Hint 3:** After checking, add nums[i] to left_sum and continue. No need for a prefix sum array — just two variables.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Compute total sum. Scan left to right with a running left sum. At each index, check if left_sum equals total - left_sum - nums[i].
