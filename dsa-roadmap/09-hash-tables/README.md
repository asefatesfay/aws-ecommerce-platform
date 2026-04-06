# Hash Tables

Hash tables (HashMaps and HashSets) provide O(1) average-case insert, lookup, and delete. They're the go-to data structure when you need fast membership testing or key-value association.

## Key Concepts

- **HashMap:** Maps keys to values. Use when you need to associate data with a key.
- **HashSet:** Stores unique keys. Use when you only need membership testing.
- **Collision handling:** Chaining (linked lists at each bucket) or open addressing. Affects worst-case performance.
- **Load factor:** When too many elements fill the table, it resizes (rehashing). Amortized O(1) operations.

## When to Use Hash Tables

- "Find if X exists" → HashSet
- "Count occurrences of X" → HashMap
- "Group elements by property" → HashMap with list values
- "Two-sum style: find complement" → HashMap
- "Detect duplicates" → HashSet

## Common Patterns

### Frequency Counting
Build a frequency map, then query it. Useful for anagram detection, majority element, etc.

### Complement Lookup
For two-sum: store seen values in a set. For each new value, check if its complement is already in the set.

### Grouping
Use a canonical form as the key. For anagrams: sorted string as key. For shifted strings: difference pattern as key.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Design HashMap](./design-hashmap.md) | Easy |
| [Maximum Number of Balloons](./maximum-number-of-balloons.md) | Easy |
| [Number of Good Pairs](./number-of-good-pairs.md) | Easy |
| [Ransom Note](./ransom-note.md) | Easy |
| [First Unique Character in a String](./first-unique-character-in-a-string.md) | Easy |
| [Find All Numbers Disappeared in an Array](./find-all-numbers-disappeared-in-an-array.md) | Easy |
| [Contains Duplicate](./contains-duplicate.md) | Easy |
| [Contains Duplicate II](./contains-duplicate-ii.md) | Easy |
| [Intersection of Two Arrays II](./intersection-of-two-arrays-ii.md) | Easy |
| [Isomorphic Strings](./isomorphic-strings.md) | Easy |
| [Word Pattern](./word-pattern.md) | Easy |
| [Group Anagrams](./group-anagrams.md) | Medium |
| [Group Shifted Strings](./group-shifted-strings.md) | Medium |
| [Encode and Decode TinyURL](./encode-and-decode-tinyurl.md) | Medium |
| [Reorganize String](./reorganize-string.md) | Medium |
| [Longest Consecutive Sequence](./longest-consecutive-sequence.md) | Medium |
| [Number of Matching Subsequences](./number-of-matching-subsequences.md) | Medium |
| [Number of Good Ways to Split a String](./number-of-good-ways-to-split-a-string.md) | Medium |
| [Split Array into Consecutive Subsequences](./split-array-into-consecutive-subsequences.md) | Medium |
| [Minimum Deletions to Make Character Frequencies Unique](./minimum-deletions-to-make-character-frequencies-unique.md) | Medium |
