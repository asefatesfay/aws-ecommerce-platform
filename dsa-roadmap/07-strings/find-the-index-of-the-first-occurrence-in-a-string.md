# Find the Index of the First Occurrence in a String

**Difficulty:** Easy
**Pattern:** String Matching
**LeetCode:** #28

## Problem Statement

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Examples

### Example 1
**Input:** `haystack = "sadbutsad"`, `needle = "sad"`
**Output:** `0`
**Explanation:** "sad" occurs at index 0 and 6. The first occurrence is at index 0.

### Example 2
**Input:** `haystack = "leetcode"`, `needle = "leeto"`
**Output:** `-1`
**Explanation:** "leeto" does not occur in "leetcode".

## Constraints
- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English letters

## Hints

> 💡 **Hint 1:** The brute force approach: for each starting position in haystack, check if needle matches starting there. This is O(n*m).

> 💡 **Hint 2:** For each index i in haystack (from 0 to len(haystack) - len(needle)), check if haystack[i:i+len(needle)] == needle.

> 💡 **Hint 3:** For an O(n+m) solution, look into the KMP (Knuth-Morris-Pratt) algorithm, which uses a failure function to avoid redundant comparisons. For interviews, the brute force or built-in find() is usually acceptable.

## Approach

**Time Complexity:** O(n*m) brute force, O(n+m) with KMP
**Space Complexity:** O(1) brute force, O(m) with KMP

Brute force: slide a window of size len(needle) across haystack and compare. For optimal solution, KMP preprocesses the needle to build a failure function that allows skipping redundant comparisons.

## Python Implementation

```python
def str_str(haystack, needle):
	if needle == "":
		return 0

	m = len(needle)
	for i in range(len(haystack) - m + 1):
		if haystack[i : i + m] == needle:
			return i
	return -1
```

## Typical Interview Use Cases

- Substring search baseline before KMP or Rabin-Karp follow-ups
- Sliding fixed-length window comparison
- Distinguishing brute-force and linear-time string matching

