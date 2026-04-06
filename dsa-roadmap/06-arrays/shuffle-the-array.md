# Shuffle the Array

**Difficulty:** Easy
**Pattern:** Array Manipulation
**LeetCode:** #1470

## Problem Statement

Given an array `nums` consisting of `2n` elements in the form `[x1, x2, ..., xn, y1, y2, ..., yn]`, return the array in the form `[x1, y1, x2, y2, ..., xn, yn]`.

## Examples

### Example 1
**Input:** `nums = [2, 5, 1, 3, 4, 7]`, `n = 3`
**Output:** `[2, 3, 5, 4, 1, 7]`
**Explanation:** x1=2, x2=5, x3=1 and y1=3, y2=4, y3=7. Interleaved: [2,3,5,4,1,7].

### Example 2
**Input:** `nums = [1, 2, 3, 4, 4, 3, 2, 1]`, `n = 4`
**Output:** `[1, 4, 2, 3, 3, 2, 4, 1]`

## Constraints
- `1 <= n <= 500`
- `nums.length == 2n`
- `1 <= nums[i] <= 10^3`

## Hints

> 💡 **Hint 1:** The first half of the array contains the x values (indices 0 to n-1) and the second half contains the y values (indices n to 2n-1).

> 💡 **Hint 2:** For position i in the result, you need x[i] = nums[i] and y[i] = nums[n+i]. Build the result by alternating between these two sources.

> 💡 **Hint 3:** Iterate i from 0 to n-1 and for each i, append nums[i] then nums[n+i] to the result array.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Create a result array of size 2n. For each index i from 0 to n-1, place nums[i] at result[2*i] and nums[n+i] at result[2*i+1].
