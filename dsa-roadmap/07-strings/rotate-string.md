# Rotate String

**Difficulty:** Easy
**Pattern:** String Manipulation
**LeetCode:** #796

## Problem Statement

Given two strings `s` and `goal`, return `true` if and only if `s` can become `goal` after some number of shifts on `s`. A shift on `s` consists of moving the leftmost character of `s` to the rightmost position.

## Examples

### Example 1
**Input:** `s = "abcde"`, `goal = "cdeab"`
**Output:** `true`
**Explanation:** Shift "abcde" twice: "bcdea" → "cdeab".

### Example 2
**Input:** `s = "abcde"`, `goal = "abced"`
**Output:** `false`

## Constraints
- `1 <= s.length, goal.length <= 100`
- `s` and `goal` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** If you concatenate `s` with itself (s + s), all possible rotations of `s` appear as substrings of this doubled string.

> 💡 **Hint 2:** Check if `goal` is a substring of `s + s`. Also verify that `len(s) == len(goal)`.

> 💡 **Hint 3:** This reduces to a substring search problem, which can be solved with built-in string methods.

## Approach

**Time Complexity:** O(n²) with naive substring search, O(n) with KMP
**Space Complexity:** O(n)

Concatenate s with itself and check if goal appears as a substring. Also verify equal lengths.
