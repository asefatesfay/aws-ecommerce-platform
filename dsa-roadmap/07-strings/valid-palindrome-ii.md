# Valid Palindrome II

**Difficulty:** Easy
**Pattern:** Two Pointers / Greedy
**LeetCode:** #680

## Problem Statement

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

## Examples

### Example 1
**Input:** `s = "aba"`
**Output:** `true`

### Example 2
**Input:** `s = "abca"`
**Output:** `true`
**Explanation:** Delete 'c' or 'b' to get "aba" or "aca", both palindromes.

### Example 3
**Input:** `s = "abc"`
**Output:** `false`

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** Start with the standard two-pointer palindrome check. When do you need to use your "one deletion"?

> 💡 **Hint 2:** Use two pointers from both ends. When you find a mismatch at positions i and j, you have two choices: skip s[i] (check if s[i+1..j] is a palindrome) or skip s[j] (check if s[i..j-1] is a palindrome).

> 💡 **Hint 3:** If either of those substrings is a palindrome, return true. If neither is, return false. You only get one deletion, so you only need to check these two cases at the first mismatch.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two-pointer scan; on the first mismatch, check if either s[i+1..j] or s[i..j-1] is a palindrome using a helper function. Return true if either check passes.

## Python Implementation

```python
def valid_palindrome(s):
	def is_pal(i, j):
		while i < j:
			if s[i] != s[j]:
				return False
			i += 1
			j -= 1
		return True

	left, right = 0, len(s) - 1
	while left < right:
		if s[left] != s[right]:
			return is_pal(left + 1, right) or is_pal(left, right - 1)
		left += 1
		right -= 1

	return True
```

## Typical Interview Use Cases

- One allowed modification or deletion in a near-palindrome
- Branching only at the first mismatch to keep O(n)
- Strong example of helper-function decomposition with indices

