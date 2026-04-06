# Sort Colors

**Difficulty:** Medium
**Pattern:** Dutch National Flag / Three Pointers
**LeetCode:** #75

## Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.

## Examples

### Example 1
**Input:** `nums = [2,0,2,1,1,0]`
**Output:** `[0,0,1,1,2,2]`

### Example 2
**Input:** `nums = [2,0,1]`
**Output:** `[0,1,2]`

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`

## Hints

> 💡 **Hint 1:** Two-pass: count 0s, 1s, 2s, then fill. But can you do it in one pass?

> 💡 **Hint 2:** Dutch National Flag algorithm: three pointers — `low` (boundary of 0s), `mid` (current element), `high` (boundary of 2s).

> 💡 **Hint 3:** If nums[mid] == 0: swap with nums[low], advance both low and mid. If nums[mid] == 2: swap with nums[high], decrement high (don't advance mid — the swapped element needs checking). If nums[mid] == 1: advance mid.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Dutch National Flag: three-pointer single pass. Partition into three sections in one scan.
