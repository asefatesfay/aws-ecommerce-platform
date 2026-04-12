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

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| Implement Trie (#208) | Medium | Basic trie |
| Design Add and Search Words (#211) | Medium | Trie + DFS for wildcards |
| Search Suggestions System (#1268) | Medium | Trie or binary search |
| Replace Words (#648) | Medium | Trie for shortest root |
| Word Search II (#212) | Hard | Trie + DFS backtracking |
| Longest Word in Dictionary (#720) | Medium | Trie BFS |
| Maximum XOR of Two Numbers (#421) | Medium | Binary trie |
| Palindrome Pairs (#336) | Hard | Reverse trie |
| Stream of Characters (#1032) | Hard | Trie on reversed words |
| Concatenated Words (#472) | Hard | Trie + DP |
