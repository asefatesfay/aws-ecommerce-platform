# 24. Tries (Prefix Trees)

## Overview
A Trie (prefix tree) is a tree data structure where each node represents a character. It's optimized for prefix-based string operations — insert, search, and startsWith all run in O(L) where L is the word length.

## Key Concepts
- Each node has up to 26 children (for lowercase English letters)
- `is_end` flag marks complete words
- Root node is empty; path from root to a node spells a prefix

## When to Use
- Autocomplete / search suggestions
- Spell checking
- IP routing (longest prefix match)
- Word games (Boggle, Scrabble)
- Finding words with common prefixes

## Common Techniques
- **Standard Trie**: insert + search + startsWith
- **Trie + DFS**: word search, wildcard matching
- **Trie + Bitmask**: XOR maximization problems
- **Compressed Trie**: merge single-child nodes

## Problems
| Problem | Difficulty |
|---------|-----------|
| Implement Trie | Medium |
| Design Add and Search Words | Medium |
| Search Suggestions System | Medium |
| Longest Word in Dictionary | Medium |
| Replace Words | Medium |
| Maximum XOR of Two Numbers | Medium |
| Word Search II | Hard |
| Palindrome Pairs | Hard |
