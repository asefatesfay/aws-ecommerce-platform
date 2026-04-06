# Longest Palindrome

**Difficulty:** Easy
**Pattern:** Hash Map / Counting
**LeetCode:** #409

## Problem Statement

Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters. Letters are case sensitive, so "Aa" is not considered a palindrome.

## Examples

### Example 1
**Input:** `s = "abccccdd"`
**Output:** `7`
**Explanation:** One longest palindrome is "dccaccd" with length 7. Use all pairs: cc(×2), dd(×1), and one 'a' in the middle.

### Example 2
**Input:** `s = "a"`
**Output:** `1`

## Constraints
- `1 <= s.length <= 2000`
- `s` consists of lowercase and/or uppercase English letters

## Hints

> 💡 **Hint 1:** A palindrome uses pairs of characters (one on each side) plus optionally one character in the middle.

> 💡 **Hint 2:** Count the frequency of each character. For each character, you can use floor(freq/2) * 2 characters in pairs.

> 💡 **Hint 3:** If any character has an odd frequency, you can place one of them in the center of the palindrome. Add 1 to the total if this is the case.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 52 distinct characters)

Count character frequencies. Sum up all even-count contributions (freq // 2 * 2). If any character has an odd count, add 1 for the center character.
