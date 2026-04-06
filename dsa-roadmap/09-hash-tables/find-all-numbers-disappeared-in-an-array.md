# Find All Numbers Disappeared in an Array

**Difficulty:** Easy
**Pattern:** Hash Map / Index Marking
**LeetCode:** #448

## Problem Statement

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

## Examples

### Example 1
**Input:** `nums = [4, 3, 2, 7, 8, 2, 3, 1]`
**Output:** `[5, 6]`

### Example 2
**Input:** `nums = [1, 1]`
**Output:** `[2]`

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

## Hints

> 💡 **Hint 1:** A HashSet approach works: add all elements to a set, then check which numbers 1..n are missing. But can you do it with O(1) extra space?

> 💡 **Hint 2:** Use the array itself as a marker. For each value v in the array, mark index v-1 as "visited" by negating the value there.

> 💡 **Hint 3:** After marking, scan the array. Any index i where nums[i] is still positive means i+1 was never visited — it's a missing number.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) extra (output doesn't count)

Mark visited indices by negating values. After processing, indices with positive values correspond to missing numbers.
