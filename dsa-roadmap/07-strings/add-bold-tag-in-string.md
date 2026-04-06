# Add Bold Tag in String

**Difficulty:** Medium
**Pattern:** String / Interval Merging
**LeetCode:** #616

## Problem Statement

You are given a string `s` and an array of strings `words`. You should add a closed pair of bold tags `<b>` and `</b>` to wrap the substrings in `s` that exist in `words`. If two such substrings overlap, you should wrap them together with only one pair of bold tags. If two substrings wrapped by bold tags are consecutive, you should combine them.

Return `s` after adding the bold tags.

## Examples

### Example 1
**Input:** `s = "abcxyz123"`, `words = ["abc","123"]`
**Output:** `"<b>abc</b>xyz<b>123</b>"`

### Example 2
**Input:** `s = "aaabbb"`, `words = ["aa","b"]`
**Output:** `"<b>aaabbb</b>"`
**Explanation:** "aa" matches at index 0 and 1. "b" matches at index 3, 4, 5. These overlap/are adjacent, so one bold tag wraps all.

## Constraints
- `1 <= s.length <= 1000`
- `0 <= words.length <= 100`
- `1 <= words[i].length <= 1000`
- `words[i]` and `s` consist of English letters and digits

## Hints

> 💡 **Hint 1:** Create a boolean array `bold` of length n, where `bold[i]` is true if character `s[i]` should be bolded.

> 💡 **Hint 2:** For each word in `words`, find all occurrences in `s`. For each occurrence starting at index i with length L, mark `bold[i..i+L-1]` as true.

> 💡 **Hint 3:** Build the result by scanning the bold array. When transitioning from non-bold to bold, insert `<b>`. When transitioning from bold to non-bold, insert `</b>`.

## Approach

**Time Complexity:** O(n × m × k) where n = len(s), m = number of words, k = average word length
**Space Complexity:** O(n)

Mark bold positions using a boolean array, then build the result string by inserting tags at bold/non-bold transitions.

## Python Implementation

```python
def add_bold_tag(s, words):
	bold = [False] * len(s)

	for i in range(len(s)):
		for word in words:
			if s.startswith(word, i):
				for j in range(i, i + len(word)):
					bold[j] = True

	parts = []
	for i, ch in enumerate(s):
		if bold[i] and (i == 0 or not bold[i - 1]):
			parts.append("<b>")
		parts.append(ch)
		if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
			parts.append("</b>")

	return "".join(parts)
```

## Typical Interview Use Cases

- Interval marking followed by formatted output construction
- Merging overlapping or adjacent highlighted regions
- Good bridge between strings and interval-style thinking

