# Reverse String

**Difficulty:** Easy
**Pattern:** Two Pointers
**LeetCode:** #344

## Problem Statement

Write a function that reverses a string. The input string is given as an array of characters `s`. You must do this by modifying the input array in-place with O(1) extra memory.

## Examples

### Example 1
**Input:** `s = ['h','e','l','l','o']`
**Output:** `['o','l','l','e','h']`

### Example 2
**Input:** `s = ['H','a','n','n','a','h']`
**Output:** `['h','a','n','n','a','H']`

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is a printable ASCII character

## Hints

> 💡 **Hint 1:** Use two pointers — one at the start and one at the end of the array.

> 💡 **Hint 2:** Swap the characters at the two pointers, then move the left pointer right and the right pointer left.

> 💡 **Hint 3:** Continue until the two pointers meet in the middle. The array is now reversed.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Two pointers starting at both ends, swapping and moving inward until they meet.

### Visual Example: Pointer Movements

```
Input: ['h', 'e', 'l', 'l', 'o']

Step 0: left=0, right=4
  ['h', 'e', 'l', 'l', 'o']
   ↑                      ↑
  Swap 'h' and 'o' → ['o', 'e', 'l', 'l', 'h']

Step 1: left=1, right=3
  ['o', 'e', 'l', 'l', 'h']
        ↑           ↑
  Swap 'e' and 'l' → ['o', 'l', 'l', 'e', 'h']

Step 2: left=2, right=2
  ['o', 'l', 'l', 'e', 'h']
           ↑
  Pointers meet - stop

Final: ['o', 'l', 'l', 'e', 'h'] ✓
```

## Python Implementation

```python
def reverse_string(s):
	left, right = 0, len(s) - 1
	while left < right:
		s[left], s[right] = s[right], s[left]
		left += 1
		right -= 1
```

## Typical Interview Use Cases

- Basic in-place two-pointer reversal
- Warm-up for palindrome and array reversal questions
- Character-array mutation under O(1) space constraints

