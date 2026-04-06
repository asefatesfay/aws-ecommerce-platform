# Ransom Note

**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting
**LeetCode:** #383

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise. Each letter in `magazine` can only be used once in `ransomNote`.

## Examples

### Example 1
**Input:** `ransomNote = "a"`, `magazine = "b"`
**Output:** `false`

### Example 2
**Input:** `ransomNote = "aa"`, `magazine = "ab"`
**Output:** `false`

### Example 3
**Input:** `ransomNote = "aa"`, `magazine = "aab"`
**Output:** `true`

## Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** Count the frequency of each character in `magazine`. These are the available "resources".

> 💡 **Hint 2:** For each character in `ransomNote`, check if it's available (count > 0) and decrement the count.

> 💡 **Hint 3:** If at any point a required character has count 0, return false. If you process all of ransomNote successfully, return true.

## Approach

**Time Complexity:** O(m + n) where m, n are the lengths of the two strings
**Space Complexity:** O(1) (26 lowercase letters)

Count character frequencies in magazine. Scan ransomNote, decrementing counts. Return false if any count goes below 0.
