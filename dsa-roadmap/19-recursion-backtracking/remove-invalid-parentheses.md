# Remove Invalid Parentheses

**Difficulty:** Hard
**Pattern:** BFS / Backtracking
**LeetCode:** #301

## Problem Statement

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid. Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

## Examples

### Example 1
**Input:** `s = "()())()"`
**Output:** `["(())()","()()()"]`

### Example 2
**Input:** `s = "(a)())()"`
**Output:** `["(a())()","(a)()()"]`

### Example 3
**Input:** `s = ")("`
**Output:** `[""]`

## Constraints
- `1 <= s.length <= 25`
- `s` consists of lowercase English letters and parentheses `'('` and `')'`
- There will be at most `20` parentheses in `s`

## Hints

> 💡 **Hint 1:** BFS approach: start with the original string. Generate all strings with one character removed. Check validity. If any are valid, those are the answers (minimum removals = 1).

> 💡 **Hint 2:** If none are valid at level 1, try level 2 (remove 2 characters), etc. Use a HashSet to avoid duplicates.

> 💡 **Hint 3:** Validity check: scan left to right, count open brackets. If count goes negative, invalid. At end, count must be 0.

## Approach

**Time Complexity:** O(n × 2^n)
**Space Complexity:** O(n × 2^n)

BFS level by level (each level removes one more character). Stop at the first level that produces valid strings.
