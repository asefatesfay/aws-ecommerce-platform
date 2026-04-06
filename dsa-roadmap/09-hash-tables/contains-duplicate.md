# Contains Duplicate

**Difficulty:** Easy
**Pattern:** Hash Set
**LeetCode:** #217

## Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Examples

### Example 1
**Input:** `nums = [1, 2, 3, 1]`
**Output:** `true`

### Example 2
**Input:** `nums = [1, 2, 3, 4]`
**Output:** `false`

### Example 3
**Input:** `nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`
**Output:** `true`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** You need to detect if any element has been seen before. What data structure gives O(1) membership testing?

> 💡 **Hint 2:** Use a HashSet. For each element, check if it's already in the set. If yes, return true. If no, add it to the set.

> 💡 **Hint 3:** Alternatively, sort the array and check adjacent elements. But that's O(n log n) — the HashSet approach is O(n).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Add elements to a HashSet one by one. Return true as soon as a duplicate is found (element already in set). Return false if the loop completes.
