# Intersection of Two Arrays II

**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting
**LeetCode:** #350

## Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

## Examples

### Example 1
**Input:** `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`
**Output:** `[2, 2]`

### Example 2
**Input:** `nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]`
**Output:** `[4, 9]`

## Constraints
- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

## Hints

> 💡 **Hint 1:** Count the frequency of each element in the smaller array using a HashMap.

> 💡 **Hint 2:** Iterate through the larger array. For each element, if it exists in the frequency map with count > 0, add it to the result and decrement the count.

> 💡 **Hint 3:** Follow-up: if arrays are sorted, use two pointers instead of a HashMap for O(1) space.

## Approach

**Time Complexity:** O(m + n)
**Space Complexity:** O(min(m, n))

Count frequencies of the smaller array. Scan the larger array, adding elements to the result when they appear in the frequency map (decrementing count each time).
