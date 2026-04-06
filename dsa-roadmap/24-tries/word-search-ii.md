# Word Search II

**Difficulty:** Hard
**Pattern:** Trie + DFS Backtracking
**LeetCode:** #212

## Problem Statement
Given an `m × n` board of characters and a list of strings `words`, return all words on the board. A word can be constructed from letters of sequentially adjacent cells (horizontally or vertically). The same cell may not be used more than once in a word.

## Examples

### Example 1
**Input:** `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`, `words = ["oath","pea","eat","rain"]`
**Output:** `["eat","oath"]`

### Example 2
**Input:** `board = [["a","b"],["c","d"]]`, `words = ["abcb"]`
**Output:** `[]`

## Constraints
- `m, n` in range `[1, 12]`
- `words.length` up to 3×10⁴
- Each word length 1–10

## Hints

> 💡 **Hint 1:** Build a Trie from all words first. Then DFS from each cell — at each step, check if the current path exists in the Trie.

> 💡 **Hint 2:** During DFS, mark cells as visited (e.g., replace with `#`) to avoid reuse, then restore after backtracking.

> 💡 **Hint 3:** When you reach a Trie node with `is_end = true`, add the word to results and set `is_end = false` to avoid duplicates. Prune Trie nodes with no children to speed up search.

## Approach
**Time Complexity:** O(M × N × 4 × 3^(L-1)) where L = max word length
**Space Complexity:** O(total characters in all words)

Build a Trie from all words, then DFS from every cell. Use the Trie to prune paths that can't lead to any word.
