# Subsets

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #78

## Problem Statement

Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

## Examples

### Example 1
**Input:** `nums = [1,2,3]`
**Output:** `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

### Example 2
**Input:** `nums = [0]`
**Output:** `[[],[0]]`

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique

## Hints

> 💡 **Hint 1:** For each element, you have two choices: include it or exclude it. This gives 2^n subsets.

> 💡 **Hint 2:** Backtracking: at each step, add the current subset to results, then try adding each remaining element.

> 💡 **Hint 3:** Use a start index to avoid revisiting elements. For each call, iterate from start to end, add nums[i], recurse with start=i+1, then remove nums[i].

## Approach

**Time Complexity:** O(n × 2^n)
**Space Complexity:** O(n) recursion depth

Backtracking with a start index. Add current state to results at every call (not just leaf nodes). Iterate forward to avoid duplicates.
