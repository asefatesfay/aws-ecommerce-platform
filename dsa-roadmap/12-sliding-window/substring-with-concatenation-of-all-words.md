# Substring with Concatenation of All Words

**Difficulty:** Hard
**Pattern:** Sliding Window (Fixed) + Frequency Map
**LeetCode:** #30

## Problem Statement

You are given a string `s` and an array of strings `words`. All the strings of `words` are of the same length. A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated. Return an array of the starting indices of all the concatenated substrings in `s`. You can return the answer in any order.

## Examples

### Example 1
**Input:** `s = "barfoothefoobarman"`, `words = ["foo","bar"]`
**Output:** `[0, 9]`
**Explanation:** "barfoo" starts at 0, "foobar" starts at 9.

### Example 2
**Input:** `s = "wordgoodgoodgoodbestword"`, `words = ["word","good","best","word"]`
**Output:** `[]`

## Constraints
- `1 <= s.length <= 10^4`
- `1 <= words.length <= 5000`
- `1 <= words[i].length <= 30`
- `s` and `words[i]` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** The window size is fixed: `len(words) * len(words[0])`. Slide a window of this size across s.

> 💡 **Hint 2:** For each window, split it into chunks of word length and check if the frequency map of chunks matches the frequency map of words.

> 💡 **Hint 3:** For efficiency, run len(words[0]) separate sliding window passes (one for each starting offset 0, 1, ..., word_len-1). Within each pass, use a sliding window over word-sized chunks.

## Approach

**Time Complexity:** O(n × word_len)
**Space Complexity:** O(total words length)

Run word_len separate sliding window passes. Each pass uses a word-frequency sliding window to find valid starting positions.
