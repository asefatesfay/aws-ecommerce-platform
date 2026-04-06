# Contains Duplicate III

**Difficulty:** Hard
**Pattern:** Bucket Sort / Sorted Set
**LeetCode:** #220

## Problem Statement

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`. Find a pair of indices `(i, j)` such that `i != j`, `abs(i - j) <= indexDiff`, and `abs(nums[i] - nums[j]) <= valueDiff`. Return `true` if such a pair exists or `false` otherwise.

## Examples

### Example 1
**Input:** `nums = [1,2,3,1]`, `indexDiff = 3`, `valueDiff = 0`
**Output:** `true`

### Example 2
**Input:** `nums = [1,5,9,1,5,9]`, `indexDiff = 2`, `valueDiff = 3`
**Output:** `false`

## Constraints
- `2 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `1 <= indexDiff <= nums.length`
- `0 <= valueDiff <= 10^9`

## Hints

> 💡 **Hint 1:** Use a sliding window of size indexDiff. Within the window, check if any two values are within valueDiff of each other.

> 💡 **Hint 2:** Bucket approach: assign each number to a bucket of size valueDiff+1. Two numbers in the same bucket are within valueDiff. Check adjacent buckets too.

> 💡 **Hint 3:** Maintain a HashMap of buckets for the current window. For each new element, check its bucket and adjacent buckets. Remove the element that falls out of the window.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, indexDiff))

Bucket sort with sliding window. Each bucket has size valueDiff+1. Check same and adjacent buckets for valid pairs.
