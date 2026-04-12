# Trie (Prefix Tree)

## What is it?
A tree where each node represents a character. The path from root to a node spells a prefix. All words sharing a prefix share the same path. Optimized for prefix-based string operations.

## Visual Example
```
Insert: "cat", "car", "card", "care", "bat"

         root
        /    \
       c      b
       |      |
       a      a
      / \     |
     t   r    t
         |
         d,e  ← is_end for "card" and "care"

Search "car":  root→c→a→r  (is_end=False → not a word, but prefix exists)
Search "card": root→c→a→r→d (is_end=True → word exists!)
StartsWith "ca": root→c→a  (exists → True)
StartsWith "ba": root→b→a  (exists → True)
StartsWith "be": root→b→e  (e not in b's children → False)
```

## Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False  # marks end of a complete word
        self.count = 0       # words passing through this node

class Trie:
    """
    Prefix tree with insert, search, startsWith, delete, autocomplete.
    All operations O(L) where L = word length.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert word — O(L)"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def search(self, word):
        """Returns True if exact word exists — O(L)"""
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        """Returns True if any word starts with prefix — O(L)"""
        return self._traverse(prefix) is not None

    def _traverse(self, s):
        """Walk trie following string s, return final node or None"""
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def delete(self, word):
        """Remove word from trie — O(L)"""
        def _delete(node, word, depth):
            if depth == len(word):
                if node.is_end:
                    node.is_end = False
                return len(node.children) == 0
            ch = word[depth]
            if ch not in node.children:
                return False
            should_delete = _delete(node.children[ch], word, depth + 1)
            if should_delete:
                del node.children[ch]
                return len(node.children) == 0 and not node.is_end
            return False
        _delete(self.root, word, 0)

    def autocomplete(self, prefix, limit=10):
        """Return up to limit words with given prefix — O(P + N)"""
        node = self._traverse(prefix)
        if not node:
            return []
        results = []
        def dfs(n, path):
            if len(results) >= limit:
                return
            if n.is_end:
                results.append(prefix + path)
            for ch in sorted(n.children):
                dfs(n.children[ch], path + ch)
        dfs(node, "")
        return results

    def count_words_with_prefix(self, prefix):
        """Count words starting with prefix — O(L)"""
        node = self._traverse(prefix)
        return node.count if node else 0
```

## Example Usage
```python
trie = Trie()
for word in ["cat", "car", "card", "care", "bat"]:
    trie.insert(word)

print(trie.search("car"))        # False (not a complete word)
print(trie.search("card"))       # True
print(trie.starts_with("ca"))    # True
print(trie.starts_with("be"))    # False
print(trie.autocomplete("ca"))   # ['car', 'card', 'care', 'cat']
print(trie.count_words_with_prefix("car"))  # 3 (car, card, care)

trie.delete("card")
print(trie.search("card"))       # False
print(trie.search("care"))       # True (unaffected)
```

## When to Use
- Autocomplete / search suggestions
- Spell checking
- IP routing (longest prefix match)
- Word games (Boggle, Scrabble)
- Finding words with common prefixes

## LeetCode Problems

---

### 1. Implement Trie — #208 (Medium)

**Problem**: Implement a trie with `insert(word)`, `search(word)` (returns true if exact word exists), and `startsWith(prefix)` (returns true if any word starts with prefix).

```
Input:
["Trie","insert","search","search","startsWith","insert","search"]
[[],   ["apple"],["apple"],["app"], ["app"],     ["app"],  ["app"]]

Output: [null, null, true, false, true, null, true]

Trace:
insert("apple")
search("apple")    → true
search("app")      → false  (not a complete word)
startsWith("app")  → true   (prefix exists)
insert("app")
search("app")      → true   (now it's a complete word)
```

**Hints**:
1. Each node has a `children` dict and an `is_end` flag
2. `insert`: walk the trie, creating nodes as needed, set `is_end=True` at the last character
3. `search`: walk the trie, return `node.is_end` at the end; `startsWith`: return `node is not None`

---

### 2. Design Add and Search Words Data Structure — #211 (Medium)

**Problem**: Design a data structure supporting `addWord(word)` and `search(word)` where `word` may contain `.` as a wildcard matching any single letter.

```
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],              ["bad"],  ["dad"],  ["mad"],  ["pad"], ["bad"], [".ad"], ["b.."]]

Output: [null, null, null, null, false, true, true, true]

Trace:
addWord("bad"), addWord("dad"), addWord("mad")
search("pad")  → false
search("bad")  → true
search(".ad")  → true  (matches "bad", "dad", "mad")
search("b..")  → true  (matches "bad")
```

**Hints**:
1. Build a trie for `addWord`
2. For `search`, when you hit a `.`, recursively try all children
3. DFS with backtracking for wildcard matching

---

### 3. Search Suggestions System — #1268 (Medium)

**Problem**: Given a list of products and a search word, return a list of up to 3 product suggestions after each character is typed. Suggestions must start with the typed prefix and be lexicographically sorted.

```
Input:  products=["mobile","mouse","moneypot","monitor","mousepad"], searchWord="mouse"
Output: [
  ["mobile","moneypot","monitor"],  (after "m")
  ["mobile","moneypot","monitor"],  (after "mo")
  ["mouse","mousepad"],             (after "mou")
  ["mouse","mousepad"],             (after "mous")
  ["mouse","mousepad"]              (after "mouse")
]
```

**Hints**:
1. Sort products first (ensures lexicographic order)
2. Insert all products into a trie
3. For each prefix, do DFS from the prefix node and collect up to 3 words
4. Simpler alternative: binary search on the sorted list for each prefix

---

### 4. Word Search II — #212 (Hard)

**Problem**: Given an `m x n` board of characters and a list of words, return all words that can be found in the board. Words can be constructed from sequentially adjacent cells (horizontally or vertically), and each cell can only be used once per word.

```
Input:
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```

**Hints**:
1. Build a trie from all words
2. DFS from every cell; at each step, check if the current path is a trie prefix
3. Mark cells as visited during DFS, unmark on backtrack
4. When `is_end=True` in the trie, add the word to results

---

### 5. Replace Words — #648 (Medium)

**Problem**: Given a dictionary of root words and a sentence, replace each word in the sentence with its shortest root from the dictionary. If no root exists, keep the original word.

```
Input:  dictionary=["cat","bat","rat"], sentence="the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Input:  dictionary=["a","b","c"], sentence="aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```

**Hints**:
1. Insert all roots into a trie
2. For each word in the sentence, traverse the trie character by character
3. Return the root as soon as you hit an `is_end` node; otherwise return the full word

---

### 6. Maximum XOR of Two Numbers in an Array — #421 (Medium)

**Problem**: Given an integer array, find the maximum XOR of any two elements.

```
Input:  [3, 10, 5, 25, 2, 8]
Output: 28
Explanation: 5 XOR 25 = 28

Input:  [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
Output: 127
```

**Hints**:
1. Build a binary trie (bit by bit from MSB to LSB)
2. For each number, greedily try to find a complement bit at each level
3. If the opposite bit exists in the trie, take it (maximizes XOR); otherwise take the same bit
