# Remove All Adjacent Duplicates In String

**Difficulty:** Easy
**Pattern:** Stack
**LeetCode:** #1047

## Problem Statement

You are given a string `s` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them. We repeatedly make duplicate removals on `s` until we no longer can. Return the final string after all such duplicate removals have been made.

## Examples

### Example 1
**Input:** `s = "abbaca"`
**Output:** `"ca"`
**Explanation:** "abbaca" → "aaca" → "ca".

### Example 2
**Input:** `s = "azxxzy"`
**Output:** `"ay"`

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** Use a stack. Process characters one by one.

> 💡 **Hint 2:** If the current character equals the top of the stack, they form a duplicate pair — pop the top. Otherwise, push the current character.

> 💡 **Hint 3:** The stack at the end contains the result string (read from bottom to top).

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Stack: push characters, pop when the top matches the current character. Join the stack for the result.
