# Longest Valid Parentheses

**Difficulty:** Hard
**Pattern:** Stack / DP
**LeetCode:** #32

## Problem Statement

Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

## Examples

### Example 1
**Input:** `s = "(()"`
**Output:** `2`
**Explanation:** The longest valid parentheses substring is `"()"`.

### Example 2
**Input:** `s = ")()())"`
**Output:** `4`
**Explanation:** The longest valid parentheses substring is `"()()"`.

### Example 3
**Input:** `s = ""`
**Output:** `0`

## Constraints
- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('` or `')'`

## Hints

> 💡 **Hint 1:** Use a stack of indices. Initialize with -1 as a base.

> 💡 **Hint 2:** For `(`, push its index. For `)`, pop the top. If the stack is empty after popping, push the current index as the new base. If not empty, the current valid length is `current_index - stack.top`.

> 💡 **Hint 3:** Track the maximum valid length seen. The stack always has the index of the last unmatched character as its bottom.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack of indices with -1 as base. For each `)`, pop and compute length if stack is non-empty, or reset base if empty. Track maximum.
