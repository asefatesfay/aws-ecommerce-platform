# Reverse Words in a String

**Difficulty:** Medium
**Pattern:** String Manipulation / Two Pointers
**LeetCode:** #151

## Problem Statement

Given an input string `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. Return a string of the words in reverse order concatenated by a single space. Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words.

## Examples

### Example 1
**Input:** `s = "the sky is blue"`
**Output:** `"blue is sky the"`

### Example 2
**Input:** `s = "  hello world  "`
**Output:** `"world hello"`
**Explanation:** Leading and trailing spaces are removed.

### Example 3
**Input:** `s = "a good   example"`
**Output:** `"example good a"`
**Explanation:** Multiple spaces between words are reduced to one.

## Constraints
- `1 <= s.length <= 10^4`
- `s` contains English letters, digits, and spaces
- There is at least one word in `s`

## Hints

> 💡 **Hint 1:** The easy approach: split by spaces, filter empty strings, reverse the list, join with single space.

> 💡 **Hint 2:** For an in-place O(1) space approach (treating the string as a char array): first reverse the entire string, then reverse each individual word.

> 💡 **Hint 3:** After reversing the whole string, scan for word boundaries and reverse each word in place. This gives the correct word order with reversed characters fixed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) for the output (O(1) extra with in-place approach on char array)

Split, filter, reverse, join — or use the two-reversal trick on a character array: reverse all, then reverse each word individually.

## Python Implementation

```python
def reverse_words(s):
	return " ".join(s.split()[::-1])
```

## Typical Interview Use Cases

- Tokenization plus normalization of extra spaces
- Reordering words rather than characters
- Comparison point between Python built-ins and in-place char-array approaches

