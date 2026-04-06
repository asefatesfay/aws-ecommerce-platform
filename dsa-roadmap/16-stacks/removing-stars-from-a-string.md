# Removing Stars From a String

**Difficulty:** Medium
**Pattern:** Stack
**LeetCode:** #2390

## Problem Statement

You are given a string `s`, which contains stars `*`. In one operation, you can choose a star in `s`, remove the closest non-star character to its left, as well as remove the star itself. Return the string after all stars have been removed.

## Examples

### Example 1
**Input:** `s = "leet**cod*e"`
**Output:** `"lecoe"`
**Explanation:** Remove 't' and first '*', then 'e' and second '*', then 'd' and third '*'.

### Example 2
**Input:** `s = "erase*****"`
**Output:** `""`

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters and stars `*`
- The operation above can always be performed on the input

## Hints

> 💡 **Hint 1:** Use a stack. Process characters left to right.

> 💡 **Hint 2:** When you see a regular character, push it. When you see a `*`, pop the top character (the closest non-star to the left).

> 💡 **Hint 3:** The stack at the end contains the result (read from bottom to top).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack: push letters, pop on `*`. Join the stack for the result.
