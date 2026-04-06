# Word Ladder

**Difficulty:** Hard
**Pattern:** BFS (Shortest Path)
**LeetCode:** #127

## Problem Statement
Given `beginWord`, `endWord`, and a `wordList`, find the length of the shortest transformation sequence from `beginWord` to `endWord` where each step changes exactly one letter and each intermediate word must be in `wordList`. Return 0 if no such sequence exists.

## Examples

### Example 1
**Input:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`
**Output:** `5`
**Explanation:** "hit" → "hot" → "dot" → "dog" → "cog"

### Example 2
**Input:** `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log"]`
**Output:** `0`

## Constraints
- `1 <= beginWord.length <= 10`
- `endWord.length == beginWord.length`
- `1 <= wordList.length <= 5000`

## Hints

> 💡 **Hint 1:** Model as a graph where words are nodes and edges connect words differing by one letter. BFS finds the shortest path.

> 💡 **Hint 2:** For each word in the queue, try replacing each character with 'a'-'z'. If the result is in the word set, add it to the queue.

> 💡 **Hint 3:** Use a set for O(1) lookup. Remove words from the set when visited to avoid cycles.

## Approach
**Time Complexity:** O(M² × N) where M = word length, N = wordList size
**Space Complexity:** O(M² × N)

BFS from beginWord. At each level, generate all one-letter variations and check if they're in the word set. Return level count when endWord is reached.
