# Longest Nice Substring

**Difficulty:** Easy
**Pattern:** Divide and Conquer
**LeetCode:** #1763

## Problem Statement

A string `s` is nice if, for every letter of the alphabet that `s` contains, it appears both in uppercase and lowercase. For example, `"abABB"` is nice because `'A'` and `'a'` appear, and `'B'` and `'b'` appear. However, `"abA"` is not because `'b'` appears, but `'B'` does not. Given a string `s`, return the longest substring of `s` that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

## Examples

### Example 1
**Input:** `s = "YazaAay"`
**Output:** `"aAay"`
**Explanation:** "aAay" is nice because 'A'/'a' and 'Y'/'y' — wait, 'Y' is present but 'y' is not in "aAay". Actually "aAay" has a,A,y — 'Y' is not present. So it's nice.

### Example 2
**Input:** `s = "Bb"`
**Output:** `"Bb"`

### Example 3
**Input:** `s = "c"`
**Output:** `""`

## Constraints
- `1 <= s.length <= 100`
- `s` consists of uppercase and lowercase English letters

## Hints

> 💡 **Hint 1:** A character that appears in only one case (upper or lower) must be a split point — it can't be in any nice substring.

> 💡 **Hint 2:** Find any character that appears in only one case. Split the string at all occurrences of that character. Recursively find the longest nice substring in each part.

> 💡 **Hint 3:** Return the longest result among all parts. Base case: if no such character exists, the whole string is nice.

## Approach

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

Divide and conquer: find a "bad" character (only one case present), split at it, recurse on each part, return the longest nice result.
