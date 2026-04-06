# Find the Kth Largest Integer in the Array

**Difficulty:** Medium
**Pattern:** Sorting with Custom Comparator
**LeetCode:** #1985

## Problem Statement

You are given an array of strings `nums` and an integer `k`. Each string in `nums` represents an integer without leading zeros. Return the string that represents the `k`th largest integer in `nums`. Note: Duplicate numbers should be counted distinctly. For example, if `nums` is `["1","2","2"]`, `"2"` is the first largest integer, `"2"` is the second-largest integer, and `"1"` is the third-largest integer.

## Examples

### Example 1
**Input:** `nums = ["3","6","7","10"]`, `k = 4`
**Output:** `"3"`

### Example 2
**Input:** `nums = ["2","21","12","1"]`, `k = 3`
**Output:** `"2"`

### Example 3
**Input:** `nums = ["0","0"]`, `k = 2`
**Output:** `"0"`

## Constraints
- `1 <= k <= nums.length <= 10^4`
- `1 <= nums[i].length <= 100`
- `nums[i]` consists of only digits
- `nums[i]` will not have any leading zeros

## Hints

> 💡 **Hint 1:** You can't compare strings directly as numbers (lexicographic order doesn't match numeric order for different lengths).

> 💡 **Hint 2:** Custom comparator: first compare by length (longer = larger), then lexicographically for equal lengths.

> 💡 **Hint 3:** Sort with this comparator in descending order and return the kth element (index k-1).

## Approach

**Time Complexity:** O(n log n × L) where L is max string length
**Space Complexity:** O(1)

Sort with custom comparator: longer strings are larger; equal-length strings compare lexicographically. Return kth element.
