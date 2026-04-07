# Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable)
**LeetCode:** #3

## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

### Example 1
**Input:** `s = "abcabcbb"`
**Output:** `3`
**Explanation:** "abc" is the longest substring without repeating characters.

### Example 2
**Input:** `s = "bbbbb"`
**Output:** `1`

### Example 3
**Input:** `s = "pwwkew"`
**Output:** `3`
**Explanation:** "wke" is the answer.

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces

## Hints

> 💡 **Hint 1:** Use a sliding window. Expand the right pointer. When a duplicate is found, shrink from the left.

> 💡 **Hint 2:** Use a HashSet to track characters in the current window. When s[right] is already in the set, remove s[left] from the set and advance left.

> 💡 **Hint 3:** Alternatively, use a HashMap storing the last seen index of each character. When a duplicate is found, jump left directly to max(left, last_seen[char] + 1).

---

## 🔴 Approach 1: Brute Force (All Substrings)

**Mental Model:** Check every possible substring and verify it has no repeating characters. Track the longest.

**Time Complexity:** O(n³)
**Space Complexity:** O(min(n, alphabet_size))

### Why the Brute Force Works

```python
def length_of_longest_substring_brute(s):
    """
    Generate all substrings and check if each has no duplicates.
    Time: O(n³) — O(n²) substrings × O(n) to check duplicates
    Space: O(k) — storing one substring at a time
    """
    max_length = 0
    n = len(s)
    
    # Try all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            
            # Check if this substring has no repeating characters
            if len(substring) == len(set(substring)):
                max_length = max(max_length, len(substring))
    
    return max_length
```

### Tracing Brute Force: `"abcabcbb"`

```
i=0:
  [0:1] = "a": len 1 == set 1 ✓, max_length = 1
  [0:2] = "ab": len 2 == set 2 ✓, max_length = 2
  [0:3] = "abc": len 3 == set 3 ✓, max_length = 3
  [0:4] = "abca": len 4 != set 3 ✗ (duplicate 'a')
  [0:5] = "abcab": len 5 != set 3 ✗ (duplicates)
  ... (all remaining have duplicates)

i=1:
  [1:2] = "b": len 1 == set 1 ✓, max_length = 3
  [1:3] = "bc": len 2 == set 2 ✓, max_length = 3
  [1:4] = "bca": len 3 == set 3 ✓, max_length = 3
  [1:5] = "bcab": len 4 != set 3 ✗
  ... (checking all remaining)

... continue for all i ...

Result: 3 (substrings "abc", "bca", "cab", "bc", etc.)
```

**Problem with brute force:** For n=50,000, we have O(n²) = 2.5 billion substrings to check. Plus O(n) character verification for each = O(n³) total. Infeasible.

---

## 🟢 Approach 2: Optimal (Sliding Window with Hash Set)

**Mental Model:** Maintain a window of characters with no repeats. Expand right when you can, shrink left when a duplicate appears.

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, alphabet_size))

### Why the Optimal Approach Works

Each character is visited **at most twice**: once by the right pointer (expansion) and once by the left pointer (shrinking). So total operations are O(2n) = O(n).

```python
def length_of_longest_substring(s):
    """
    Sliding window with HashSet.
    Expand right, shrink left when duplicate appears.
    Time: O(n) — each char visited by left and right at most once
    Space: O(k) — storing at most k unique chars in window
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If char already in window, shrink from left until it's gone
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add new character
        char_set.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### Tracing Optimal: `"abcabcbb"`

```
Index:  0 1 2 3 4 5 6 7
Char:   a b c a b c b b

Initial: char_set = {}, left = 0, max_length = 0

right=0, char='a':
  'a' in set? No
  char_set.add('a') → {'a'}
  length = 0 - 0 + 1 = 1, max_length = 1

right=1, char='b':
  'b' in set? No
  char_set.add('b') → {'a', 'b'}
  length = 1 - 0 + 1 = 2, max_length = 2

right=2, char='c':
  'c' in set? No
  char_set.add('c') → {'a', 'b', 'c'}
  length = 2 - 0 + 1 = 3, max_length = 3

right=3, char='a':
  'a' in set? Yes ✓
  While loop:
    Remove s[left=0]='a' → {'b', 'c'}
    left = 1
  char_set.add('a') → {'b', 'c', 'a'}
  length = 3 - 1 + 1 = 3, max_length = 3

right=4, char='b':
  'b' in set? Yes ✓
  While loop:
    Remove s[left=1]='b' → {'c', 'a'}
    left = 2
  char_set.add('b') → {'c', 'a', 'b'}
  length = 4 - 2 + 1 = 3, max_length = 3

right=5, char='c':
  'c' in set? Yes ✓
  While loop:
    Remove s[left=2]='c' → {'a', 'b'}
    left = 3
  char_set.add('c') → {'a', 'b', 'c'}
  length = 5 - 3 + 1 = 3, max_length = 3

right=6, char='b':
  'b' in set? Yes ✓
  While loop:
    Remove s[left=3]='a' → {'b', 'c'}
    left = 4
    'b' still in set? Yes ✓
    Remove s[left=4]='b' → {'c'}
    left = 5
  char_set.add('b') → {'c', 'b'}
  length = 6 - 5 + 1 = 2, max_length = 3

right=7, char='b':
  'b' in set? Yes ✓
  While loop:
    Remove s[left=5]='c' → {'b'}
    left = 6
    'b' still in set? Yes ✓
    Remove s[left=6]='b' → {}
    left = 7
  char_set.add('b') → {'b'}
  length = 7 - 7 + 1 = 1, max_length = 3

Result: 3 ✓ (substring "abc", "bca", or "cab")
```

### Visual: The Sliding Window in Action

```
String: "abcabcbb"

Step 1: Expand to "abc"
  [abc]abcbb
   ↑   ↑
  left right
  Window = "abc" (3 unique) ✓

Step 2: Hit duplicate 'a' at right=3, shrink left
  a[bca]bcbb
    ↑  ↑
  left right
  Window = "bca" (3 unique) ✓

Step 3: Hit duplicate 'b' at right=4, shrink left
  ab[cab]cbb
     ↑  ↑
  left right
  (Need to shrink further for next duplicate)

Step 4: Hit duplicate 'c' at right=5, shrink left
  abc[abc]bb
       ↑  ↑
  left right
  (Keep shrinking as duplicates appear)

... continues until end ...

Maximum window size = 3
```

---

## Approach 3: HashMap Optimization (Single Pass, No While Loop)

Instead of a HashSet with a while loop, use a HashMap to store the **last seen index** of each character. Jump left directly.

```python
def length_of_longest_substring_hashmap(s):
    """
    HashMap stores last index of each character.
    When duplicate found, jump left directly.
    Time: O(n) — single pass, no inner loop
    Space: O(k) — storing char -> index map
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Jump left to after the last occurrence of this char
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

This avoids the while loop entirely by computing the exact new left position in O(1).

---

## Comparison: All Approaches

| Aspect | Brute Force | Hash Set Window | Hash Map Window |
|--------|-----------|-----------------|-----------------|
| **Time Complexity** | **O(n³)** | O(n) | O(n) |
| **Space Complexity** | O(k) | O(k) | O(k) |
| **For n=1000** | **~1B ops (slow)** | ~1K ops ✓ | ~1K ops ✓ |
| **For n=50,000** | **Too slow** | ~50K ops ✓ | ~50K ops ✓ |
| **Algorithm** | Check all substrings | Expand/shrink with set | Expand/jump with map |
| **Implementation** | Simple | Clear two-pointer logic | Slightly more complex |

**Why optimal wins:** Sliding window converts O(n³) brute force into O(n) elegant solution by recognizing that each character is visited at most twice.

---

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(min(n, alphabet_size))

Variable window with a HashSet or HashMap. Expand right; when a duplicate is encountered, shrink left until the duplicate is removed. Track maximum window size.

## Python Implementation

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```
