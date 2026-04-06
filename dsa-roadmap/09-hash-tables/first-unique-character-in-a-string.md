# First Unique Character in a String

**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting
**LeetCode:** #387

## Problem Statement

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Examples

### Example 1
**Input:** `s = "leetcode"`
**Output:** `0`
**Explanation:** 'l' appears once and is the first such character.

### Example 2
**Input:** `s = "loveleetcode"`
**Output:** `2`
**Explanation:** 'v' at index 2 is the first character that appears only once.

### Example 3
**Input:** `s = "aabb"`
**Output:** `-1`

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters

## Hints

> 💡 **Hint 1:** Two passes: first count the frequency of each character, then find the first character with frequency 1.

> 💡 **Hint 2:** Use a 26-element array (or HashMap) for frequencies. First pass: count all. Second pass: scan left to right and return the index of the first character with count 1.

> 💡 **Hint 3:** The second pass must go left to right (not iterate the map) to preserve the "first" requirement.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (26 characters)

Two-pass: count frequencies, then scan left to right returning the first index where the character's frequency is 1.
