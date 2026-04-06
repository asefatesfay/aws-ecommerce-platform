# Maximum Number of Vowels in a Substring of Given Length

**Difficulty:** Medium
**Pattern:** Sliding Window (Fixed)
**LeetCode:** #1456

## Problem Statement

Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`. Vowel letters in English are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Examples

### Example 1
**Input:** `s = "abciiidef"`, `k = 3`
**Output:** `3`
**Explanation:** "iii" has 3 vowels.

### Example 2
**Input:** `s = "aeiou"`, `k = 2`
**Output:** `2`

### Example 3
**Input:** `s = "leetcode"`, `k = 3`
**Output:** `2`
**Explanation:** "lee", "eet", "etc" — max 2 vowels.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters
- `1 <= k <= s.length`

## Hints

> 💡 **Hint 1:** Count vowels in the first k characters. This is your initial window count.

> 💡 **Hint 2:** Slide the window: if the outgoing character is a vowel, decrement count. If the incoming character is a vowel, increment count.

> 💡 **Hint 3:** Track the maximum count seen across all windows.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Fixed window of size k. Maintain a running vowel count, updating as the window slides. Track the maximum.
