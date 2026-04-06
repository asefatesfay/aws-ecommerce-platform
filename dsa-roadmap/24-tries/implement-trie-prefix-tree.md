# Implement Trie (Prefix Tree)

**Difficulty:** Medium
**Pattern:** Trie Implementation
**LeetCode:** #208

## Problem Statement
Implement a trie with `insert`, `search`, and `startsWith` methods.
- `insert(word)` — inserts the string into the trie
- `search(word)` — returns true if the exact word exists
- `startsWith(prefix)` — returns true if any word starts with the prefix

## Examples

### Example 1
**Input:**
```
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
```
**Output:** `[null,null,true,false,true,null,true]`
**Explanation:** After inserting "apple", searching "apple" returns true, "app" returns false (not inserted yet), but startsWith("app") returns true.

## Constraints
- `1 <= word.length, prefix.length <= 2000`
- Only lowercase English letters
- At most 3×10⁴ calls total

## Hints

> 💡 **Hint 1:** Each node needs an array of 26 children (one per letter) and a boolean `is_end` flag.

> 💡 **Hint 2:** For `insert`, walk the trie character by character, creating nodes as needed. Set `is_end = true` at the last character.

> 💡 **Hint 3:** For `search`, walk the trie — if any character is missing return false. At the end, check `is_end`. For `startsWith`, same walk but don't check `is_end`.

## Approach
**Time Complexity:** O(L) per operation where L = word length
**Space Complexity:** O(N × 26) where N = total characters inserted

Use a TrieNode class with `children[26]` and `is_end`. All three operations traverse the trie one character at a time.
