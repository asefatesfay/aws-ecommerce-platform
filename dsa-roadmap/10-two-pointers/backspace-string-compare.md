# Backspace String Compare

**Difficulty:** Easy
**Pattern:** Two Pointers (from Back)
**LeetCode:** #844

## Problem Statement

Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character. Note that after backspacing an empty text, the text will continue empty.

## Examples

### Example 1
**Input:** `s = "ab#c"`, `t = "ad#c"`
**Output:** `true`
**Explanation:** Both become "ac".

### Example 2
**Input:** `s = "ab##"`, `t = "c#d#"`
**Output:** `true`
**Explanation:** Both become "".

### Example 3
**Input:** `s = "a#c"`, `t = "b"`
**Output:** `false`

## Constraints
- `1 <= s.length, t.length <= 200`
- `s` and `t` only contain lowercase letters and `'#'` characters

## Hints

> 💡 **Hint 1:** The easy approach: simulate with a stack, build the final strings, compare. O(n) time, O(n) space.

> 💡 **Hint 2:** For O(1) space, process both strings from right to left simultaneously. Track how many backspaces are "pending" for each string.

> 💡 **Hint 3:** For each string, skip characters that are cancelled by pending backspaces. When both strings have a valid character to compare, compare them. If one runs out before the other, they're not equal.

## Approach

**Time Complexity:** O(n + m)
**Space Complexity:** O(1)

Two pointers from the back of each string. Maintain a backspace count for each. Skip characters consumed by backspaces. Compare the next valid characters from each string.
