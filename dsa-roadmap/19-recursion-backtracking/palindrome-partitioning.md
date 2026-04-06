# Palindrome Partitioning

**Difficulty:** Medium
**Pattern:** Backtracking + DP
**LeetCode:** #131

## Problem Statement

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

## Examples

### Example 1
**Input:** `s = "aab"`
**Output:** `[["a","a","b"],["aa","b"]]`

### Example 2
**Input:** `s = "a"`
**Output:** `[["a"]]`

## Constraints
- `1 <= s.length <= 16`
- `s` consists of only lowercase English letters

## Hints

> 💡 **Hint 1:** Backtracking: at each position, try all substrings starting here. If the substring is a palindrome, add it to the current partition and recurse.

> 💡 **Hint 2:** When you reach the end of the string, add the current partition to results.

> 💡 **Hint 3:** Precompute a 2D boolean table `is_palindrome[i][j]` to check palindromes in O(1) during backtracking.

## Approach

**Time Complexity:** O(n × 2^n)
**Space Complexity:** O(n²) for palindrome table

Backtracking with palindrome precomputation. Try all prefixes at each position; recurse on the suffix when the prefix is a palindrome.

## Python Implementation

```python
def partition(s):
	result = []
	path = []

	def is_palindrome(left, right):
		while left < right:
			if s[left] != s[right]:
				return False
			left += 1
			right -= 1
		return True

	def backtrack(start):
		if start == len(s):
			result.append(path[:])
			return

		for end in range(start, len(s)):
			if not is_palindrome(start, end):
				continue
			path.append(s[start:end + 1])
			backtrack(end + 1)
			path.pop()

	backtrack(0)
	return result
```

## Step-by-Step Example

**Input:** `s = "aab"`

1. Start at index `0`. Prefix `"a"` is a palindrome, so choose it.
2. Start at index `1`. Prefix `"a"` is a palindrome, so choose it.
3. Start at index `2`. Prefix `"b"` is a palindrome, so record `["a", "a", "b"]`.
4. Backtrack to index `0`. Prefix `"aa"` is a palindrome, so choose it.
5. Remaining suffix is `"b"`, so record `["aa", "b"]`.

**Output:** `[["a", "a", "b"], ["aa", "b"]]`

## Flow Diagram

```mermaid
flowchart TD
	A[start index] --> B{start == len(s)?}
	B -- Yes --> C[record partition]
	B -- No --> D[try every end position]
	D --> E{substring is palindrome?}
	E -- No --> D
	E -- Yes --> F[append substring]
	F --> G[recurse from end + 1]
	G --> H[pop substring]
	H --> D
```

## Edge Cases

- Single-character substrings are always palindromes.
- A string like `"abc"` only partitions into single letters.
- Precomputing palindromes can speed up repeated checks on longer strings.
