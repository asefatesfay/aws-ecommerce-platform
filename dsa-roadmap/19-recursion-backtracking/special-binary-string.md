# Special Binary String

**Difficulty:** Hard
**Pattern:** Recursion / Divide and Conquer
**LeetCode:** #761

## Problem Statement

Special binary strings are binary strings with the following two properties: The number of `0`'s is equal to the number of `1`'s. Every prefix of the binary string has at least as many `1`'s as `0`'s. You are given a special binary string `s`. A move consists of choosing two consecutive, non-empty, special substrings of `s`, and swapping them. Return the lexicographically largest resulting string possible after any number of moves.

## Examples

### Example 1
**Input:** `s = "11011000"`
**Output:** `"11100100"`

### Example 2
**Input:** `s = "10"`
**Output:** `"10"`

## Constraints
- `1 <= s.length <= 50`
- `s[i]` is either `'0'` or `'1'`
- `s` is a special binary string

## Hints

> 💡 **Hint 1:** A special binary string has the form `1 + inner + 0` where inner is also a special binary string (or empty).

> 💡 **Hint 2:** Recursively find all top-level special substrings. Sort them in descending order (lexicographically largest first). Concatenate.

> 💡 **Hint 3:** For each top-level special substring `1X0`, recursively solve the inner part X to get the best inner arrangement.

## Approach

**Time Complexity:** O(n² log n)
**Space Complexity:** O(n)

Recursive: find top-level special substrings, recursively optimize each, sort descending, concatenate.
