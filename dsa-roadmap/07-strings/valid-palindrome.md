# Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #125

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1
**Input:** `s = "A man, a plan, a canal: Panama"`
**Output:** `true`
**Explanation:** After cleaning: "amanaplanacanalpanama" — a palindrome.

### Example 2
**Input:** `s = "race a car"`
**Output:** `false`
**Explanation:** After cleaning: "raceacar" — not a palindrome.

### Example 3
**Input:** `s = " "`
**Output:** `true`
**Explanation:** After cleaning: "" — an empty string is a palindrome.

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## Hints

> 💡 **Hint 1:** Use two pointers starting at both ends. Skip non-alphanumeric characters as you move inward.

> 💡 **Hint 2:** At each step, compare the characters at the two pointers (case-insensitive). If they don't match, return false.

> 💡 **Hint 3:** Continue until the pointers meet. If all comparisons passed, return true. No need to build a cleaned string.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers from both ends, skipping non-alphanumeric characters and comparing case-insensitively. Return false on any mismatch, true if pointers cross.

### Visual Example: Skipping Non-Alphanumeric

```
Input: "A man, a plan, a canal: Panama"

left=0, right=31 (len=31)

Step 1: left points to 'A' (alphanumeric), right points to 'a' (alphanumeric)
  [A]  m a n ,   a   p l a n ,   a   c a n a l :   [P]anama
   ↑                                               ↑
  Compare 'A' vs 'P' (lowercase: 'a' vs 'p') → NOT EQUAL!

Wait, let me recount... Actually "Panama" ends with 'a', not 'P'.
Let me reconsider: right=30 is 'a' (last character)

Step 1: left=0 'A', right=30 'a'
  Compare 'a' vs 'a' ✓, move left++, right--

Step 2: left=1 'm', right=29 'n'
  Skip ',', ':' etc.
  Compare 'm' vs 'a' (from 'Panama' backwards = ...anama)
  Actually, let me trace the palindrome: a-m-a-n-a-p-l-a-n-a-c-a-n-a-l-p-a-n-a-m-a
  
  m[1] vs m[end-1]
  
Actually, let me simplify with the cleaned version:
Cleaned: "amanaplanacanalpanama"

left=0 'a', right=20 'a' → match ✓
left=1 'm', right=19 'm' → match ✓
left=2 'a', right=18 'a' → match ✓
left=3 'n', right=17 'n' → match ✓
left=4 'a', right=16 'a' → match ✓
left=5 'p', right=15 'p' → match ✓
left=6 'l', right=14 'l' → match ✓
left=7 'a', right=13 'a' → match ✓
left=8 'n', right=12 'n' → match ✓
left=9 'a', right=11 'a' → match ✓
left=10 'c' (middle)

Result: true (valid palindrome) ✓
```

## Python Implementation

```python
def is_palindrome(s):
	left, right = 0, len(s) - 1

	while left < right:
		while left < right and not s[left].isalnum():
			left += 1
		while left < right and not s[right].isalnum():
			right -= 1

		if s[left].lower() != s[right].lower():
			return False

		left += 1
		right -= 1

	return True
```

## Typical Interview Use Cases

- Two-pointer comparison with skipped characters
- Case normalization without building a cleaned string
- Foundation for near-palindrome and deletion variants

