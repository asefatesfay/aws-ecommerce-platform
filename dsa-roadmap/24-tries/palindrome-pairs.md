# Palindrome Pairs

**Difficulty:** Hard
**Pattern:** Trie / Hash Map
**LeetCode:** #336

## Problem Statement
Given a list of unique strings `words`, return all pairs `[i, j]` such that `words[i] + words[j]` is a palindrome.

## Examples

### Example 1
**Input:** `words = ["abcd","dcba","lls","s","sssll"]`
**Output:** `[[0,1],[1,0],[3,2],[2,4]]`
**Explanation:** "abcddcba", "dcbaabcd", "slls", "llssssll" are all palindromes.

### Example 2
**Input:** `words = ["bat","tab","cat"]`
**Output:** `[[0,1],[1,0]]`

## Constraints
- `1 <= words.length <= 5000`
- `0 <= words[i].length <= 300`
- Only lowercase English letters

## Hints

> 💡 **Hint 1:** For each word, consider splitting it into two parts: `prefix` and `suffix`. If `prefix` is a palindrome and the reverse of `suffix` exists in the list, then `reverse(suffix) + word` is a palindrome pair.

> 💡 **Hint 2:** Similarly, if `suffix` is a palindrome and the reverse of `prefix` exists, then `word + reverse(prefix)` is a palindrome pair.

> 💡 **Hint 3:** Use a hash map for O(1) reverse lookups. Handle the empty string case separately (any palindrome word paired with "").

## Approach
**Time Complexity:** O(N × L²) where L = max word length
**Space Complexity:** O(N × L)

Build a reverse-word hash map. For each word, try all splits and check if the other part's reverse exists in the map.
