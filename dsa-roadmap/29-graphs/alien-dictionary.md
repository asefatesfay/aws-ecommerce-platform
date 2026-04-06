# Alien Dictionary

**Difficulty:** Hard
**Pattern:** Topological Sort
**LeetCode:** #269

## Problem Statement
Given a sorted list of words from an alien language, derive the order of letters in that language. Return any valid ordering, or "" if invalid (cycle or contradiction).

## Examples

### Example 1
**Input:** `words = ["wrt","wrf","er","ett","rftt"]`
**Output:** `"wertf"`

### Example 2
**Input:** `words = ["z","x"]`
**Output:** `"zx"`

### Example 3
**Input:** `words = ["z","x","z"]`
**Output:** `""` (cycle: z → x → z)

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- Only lowercase English letters

## Hints

> 💡 **Hint 1:** Compare adjacent words to extract ordering constraints. The first differing character gives `char1 → char2` (char1 comes before char2).

> 💡 **Hint 2:** Build a directed graph from these constraints. Run topological sort (Kahn's BFS).

> 💡 **Hint 3:** Edge case: if `word1` is a prefix of `word2` but appears after it (e.g., ["abc","ab"]), return "" immediately.

## Approach
**Time Complexity:** O(C) where C = total characters in all words
**Space Complexity:** O(1) — at most 26 nodes

Extract ordering from adjacent word comparisons, build graph, topological sort. Cycle = invalid ordering.
