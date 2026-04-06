# Count Binary Substrings

**Difficulty:** Easy
**Pattern:** Two Pointers / Grouping
**LeetCode:** #696

## Problem Statement

Given a binary string `s`, return the number of non-empty substrings that have the same number of `0`s and `1`s, and all the `0`s and all the `1`s in these substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.

## Examples

### Example 1
**Input:** `s = "00110011"`
**Output:** `6`
**Explanation:** "0011", "01", "1100", "10", "0011", "01" — 6 substrings.

### Example 2
**Input:** `s = "10101"`
**Output:** `4`
**Explanation:** "10", "01", "10", "01".

## Constraints
- `1 <= s.length <= 3 * 10^4`
- `s[i]` is either `'0'` or `'1'`

## Hints

> 💡 **Hint 1:** Group consecutive identical characters. For "00110011", groups are [2,2,2,2] (two 0s, two 1s, two 0s, two 1s).

> 💡 **Hint 2:** Between adjacent groups of sizes a and b, the number of valid substrings is `min(a, b)`. For example, groups of 2 and 2 give min(2,2) = 2 valid substrings.

> 💡 **Hint 3:** Compute group sizes, then sum `min(groups[i], groups[i+1])` for all adjacent pairs.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) for groups, or O(1) with a two-variable rolling approach

Compute run-length groups, then sum min of adjacent group sizes. Alternatively, track current and previous group sizes with two variables.
