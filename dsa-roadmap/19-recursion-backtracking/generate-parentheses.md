# Generate Parentheses

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #22

## Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

### Example 1
**Input:** `n = 3`
**Output:** `["((()))","(()())","(())()","()(())","()()()"]`

### Example 2
**Input:** `n = 1`
**Output:** `["()"]`

## Constraints
- `1 <= n <= 8`

## Hints

> 💡 **Hint 1:** Track the count of open and close parentheses used so far.

> 💡 **Hint 2:** You can add `(` if open < n. You can add `)` if close < open (there's an unmatched open bracket).

> 💡 **Hint 3:** When the string has length 2n, add it to results. This naturally generates only valid combinations.

## Approach

**Time Complexity:** O(4^n / √n) — the nth Catalan number
**Space Complexity:** O(n) recursion depth

Backtracking with open/close counters. Add `(` when open < n, add `)` when close < open. Collect when length == 2n.
