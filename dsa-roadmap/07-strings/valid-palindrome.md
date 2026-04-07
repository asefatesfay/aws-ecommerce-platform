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

---

## 🔴 Approach 1: Brute Force (Build, Clean, Compare)

**Mental Model:** Clean the string first, then check if it reads the same forwards and backwards.

1. Remove all non-alphanumeric characters and convert to lowercase
2. Check if the cleaned string equals its reverse

**Time Complexity:** O(n)
**Space Complexity:** O(n) — building the cleaned string

### Why the Brute Force Works

```python
def is_palindrome_brute(s):
    """
    1. Clean the string (remove non-alphanumeric, lowercase)
    2. Compare with its reverse
    Time: O(n) — one pass to clean, one pass to reverse-compare
    Space: O(n) — storing cleaned string
    """
    # Step 1: Build a cleaned string
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    
    # Step 2: Check if it's a palindrome
    return cleaned == cleaned[::-1]
```

### Tracing Brute Force: `"A man, a plan, a canal: Panama"`

```
Step 1: Clean the string
  A man, a plan, a canal: Panama
  ↓ remove non-alphanumeric, lowercase
  amanaplanacanalpanama

Step 2: Compare with reverse
  cleaned = "amanaplanacanalpanama"
  reversed = "amanaplanacanalpanama"
  cleaned == reversed? YES ✓

Result: true (palindrome) ✓
```

**Why this works:** A palindrome reads the same forwards and backwards. So the simplest approach is to literally check if `cleaned == reversed(cleaned)`.

**Problem with brute force:** We use O(n) extra space to store the cleaned string. Also, reversing creates another copy. For very large strings, this is wasteful.

---

## 🟢 Approach 2: Optimal (Two Pointers, No Extra Space)

**Mental Model:** Use two pointers starting from both ends and walk inward. Skip non-alphanumeric characters on-the-fly. Compare characters case-insensitively.

**Time Complexity:** O(n)
**Space Complexity:** O(1) — only two pointer variables

### Why the Optimal Approach Works

Instead of building a cleaned string, we compare the original string in-place:
- Loop condition: `left < right` (stop when pointers meet)
- Skip non-alphanumeric characters by advancing pointers
- Compare `s[left]` and `s[right]` in lowercase
- If any mismatch, return `false` immediately

```python
def is_palindrome(s):
    """
    Two pointers from both ends, skipping non-alphanumeric.
    Compare case-insensitively.
    Time: O(n) — single pass over both ends
    Space: O(1) — only pointer variables
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from the left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### Tracing Optimal: `"A man, a plan, a canal: Panama"`

```
String indices: 0=A, 1=space, 2=m, 3=a, 4=n, 5=,, ...
Let me use the cleaned version for clarity:
actual: "A man, a plan, a canal: Panama"
clean:  "amanaplanacanalpanama"

left=0, right=30 (last index of original string)
But for visibility, I'll number the cleaned version: 0-20 (21 chars)

left=0 ('a'), right=20 ('a'):
  left is alphanumeric: 'a'
  right is alphanumeric: 'a'
  Compare: 'a' == 'a'? ✓
  left=1, right=19

left=1 ('m'), right=19 ('m'):
  Compare: 'm' == 'm'? ✓
  left=2, right=18

left=2 ('a'), right=18 ('a'):
  Compare: 'a' == 'a'? ✓
  left=3, right=17

left=3 ('n'), right=17 ('n'):
  Compare: 'n' == 'n'? ✓
  left=4, right=16

left=4 ('a'), right=16 ('a'):
  Compare: 'a' == 'a'? ✓
  left=5, right=15

left=5 ('p'), right=15 ('p'):
  Compare: 'p' == 'p'? ✓
  left=6, right=14

left=6 ('l'), right=14 ('l'):
  Compare: 'l' == 'l'? ✓
  left=7, right=13

left=7 ('a'), right=13 ('a'):
  Compare: 'a' == 'a'? ✓
  left=8, right=12

left=8 ('n'), right=12 ('n'):
  Compare: 'n' == 'n'? ✓
  left=9, right=11

left=9 ('a'), right=11 ('a'):
  Compare: 'a' == 'a'? ✓
  left=10, right=10

Loop exits (left == right, which means we've checked all pairs)

Result: true (palindrome) ✓
```

### Key Difference: What "Skip Non-Alphanumeric" Does

```
Input: "0P"  (with a special character in between)
       "0!P"

Two pointers start at indices 0 and 2:
left=0, right=2

Iteration 1:
  s[left=0] = '0' → alphanumeric, don't skip
  s[right=2] = 'P' → alphanumeric, don't skip
  Compare: '0'.lower() vs 'P'.lower() → '0' vs 'p' → NOT equal ✗
  Return false

But if input is "0P" with no special char:
left=0, right=1
  s[left=0] = '0' → alphanumeric
  s[right=1] = 'P' → alphanumeric
  Compare: '0' vs 'p' → still not equal ✗
  (The special character is irrelevant; the logic skips it automatically)
```

---

## Comparison: Brute Force vs Optimal

| Aspect | Brute Force | Optimal |
|--------|-----------|---------|
| **Time Complexity** | O(n) | O(n) |
| **Space Complexity** | **O(n)** | **O(1)** |
| **Extra String Built** | Yes (cleaned string) | No |
| **Reverse Operation** | Yes (reversed string) | No |
| **For large strings** | More memory usage | **Better for memory-constrained systems** |
| **Interview Viability** | Acceptable | **Preferred — demonstrates optimization** |

**Why optimal wins:** Both are O(n) time, but optimal uses no extra space. This demonstrates understanding of space optimization through clever pointer manipulation.

---

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

