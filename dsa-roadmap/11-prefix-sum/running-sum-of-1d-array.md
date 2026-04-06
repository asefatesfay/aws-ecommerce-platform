# Running Sum of 1d Array

**Difficulty:** Easy
**Pattern:** Prefix Sum
**LeetCode:** #1480

## Problem Statement

Given an array `nums`, return the running sum of `nums`. The running sum of an array is defined as `runningSum[i] = sum(nums[0]...nums[i])`.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 4]`
**Output:** `[1, 3, 6, 10]`

### Example 2
**Input:** `nums = [1, 1, 1, 1, 1]`
**Output:** `[1, 2, 3, 4, 5]`

### Example 3
**Input:** `nums = [3, 1, 2, 10, 1]`
**Output:** `[3, 4, 6, 16, 17]`

## Constraints
- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Hints

> 💡 **Hint 1:** This is the definition of a prefix sum array.

> 💡 **Hint 2:** You can build it in-place: for each index i > 0, set `nums[i] += nums[i-1]`.

> 💡 **Hint 3:** Or build a new array where each element is the sum of all previous elements plus the current one.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) if in-place, O(n) for new array

Single pass: each element becomes the sum of itself and all previous elements.
