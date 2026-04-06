# One Edit Distance

**Difficulty:** Medium
**Pattern:** String Comparison / Two Pointers
**LeetCode:** #161

## Problem Statement

Given two strings `s` and `t`, return `true` if they are both one edit distance apart, otherwise return `false`. An edit is one of the following:
- Insert a character into `s`
- Delete a character from `s`
- Replace a character in `s`

## Examples

### Example 1
**Input:** `s = "ab"`, `t = "acb"`
**Output:** `true`
**Explanation:** Insert 'c' between 'a' and 'b' in s.

### Example 2
**Input:** `s = ""`, `t = ""`
**Output:** `false`
**Explanation:** They are 0 edits apart, not 1.

### Example 3
**Input:** `s = "cab"`, `t = "ad"`
**Output:** `false`
**Explanation:** More than one edit needed.

## Constraints
- `0 <= s.length, t.length <= 10^4`
- `s` and `t` consist of lowercase English letters, digits, and/or spaces

## Hints

> 💡 **Hint 1:** The length difference between s and t must be 0 or 1 for one edit to be possible. If |len(s) - len(t)| > 1, return false immediately.

> 💡 **Hint 2:** Ensure s is the shorter string (swap if needed). Scan both strings simultaneously. Find the first position where they differ.

> 💡 **Hint 3:** At the first mismatch: if lengths are equal, skip one character in both (replace) and check if the rest matches. If lengths differ by 1, skip one character in the longer string (insert/delete) and check if the rest matches. If no mismatch found, return true only if lengths differ by exactly 1.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Find the first differing position. Based on whether lengths are equal or differ by 1, check if the remaining suffixes match after making the appropriate single edit.

## Python Implementation

```python
def is_one_edit_distance(s, t):
	m, n = len(s), len(t)
	if abs(m - n) > 1:
		return False

	if m > n:
		return is_one_edit_distance(t, s)

	for i in range(m):
		if s[i] != t[i]:
			if m == n:
				return s[i + 1 :] == t[i + 1 :]
			return s[i:] == t[i + 1 :]

	return m + 1 == n
```

## Typical Interview Use Cases

- Single edit validation across insert, delete, and replace cases
- Length-based case splitting to simplify logic
- Common neighbor problem to edit distance and typo detection

