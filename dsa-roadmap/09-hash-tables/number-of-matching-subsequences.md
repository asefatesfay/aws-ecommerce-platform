# Number of Matching Subsequences

**Difficulty:** Medium
**Pattern:** Hash Map / String Matching
**LeetCode:** #792

## Problem Statement

Given a string `s` and an array of strings `words`, return the number of `words[i]` that is a subsequence of `s`.

## Examples

### Example 1
**Input:** `s = "abcde"`, `words = ["a","bb","acd","ace"]`
**Output:** `3`
**Explanation:** "a", "acd", "ace" are subsequences of "abcde". "bb" is not.

### Example 2
**Input:** `s = "dsahjpjauf"`, `words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]`
**Output:** `2`

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 50`
- `s` and `words[i]` consist of only lowercase English letters

## Hints

> 💡 **Hint 1:** Checking each word independently with two pointers is O(|s| × |words|). Can you process all words simultaneously?

> 💡 **Hint 2:** Group words by their current "waiting character" — the next character each word needs to match. Use a HashMap from character to list of (word, pointer) pairs.

> 💡 **Hint 3:** Scan through s. For each character c, process all words waiting for c: advance their pointer. If a word is fully matched, increment the count. Otherwise, move it to the bucket for its next needed character.

## Approach

**Time Complexity:** O(|s| + total characters in words)
**Space Complexity:** O(total characters in words)

Bucket words by their next needed character. Scan s once, advancing all words waiting for the current character. Count words that complete matching.
