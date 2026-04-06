# Replace Words

**Difficulty:** Medium
**Pattern:** Trie
**LeetCode:** #648

## Problem Statement
Given a dictionary of roots and a sentence, replace all successors (words) in the sentence with the shortest root that forms a prefix of the successor. If a successor has multiple roots, replace with the shortest one.

## Examples

### Example 1
**Input:** `dictionary = ["cat","bat","rat"]`, `sentence = "the cattle was rattled by the battery"`
**Output:** `"the cat was rat by the bat"`

### Example 2
**Input:** `dictionary = ["a","b","c"]`, `sentence = "aadsfasf absbs bbab cadsfafs"`
**Output:** `"a a b c"`

## Constraints
- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- Sentence has 1–10⁶ characters

## Hints

> 💡 **Hint 1:** Build a Trie from all roots in the dictionary.

> 💡 **Hint 2:** For each word in the sentence, traverse the Trie character by character. The moment you hit a node marked as `is_end`, that's the shortest root — use it.

> 💡 **Hint 3:** If you reach the end of the Trie path without finding a root, keep the original word.

## Approach
**Time Complexity:** O(total characters in dictionary + sentence)
**Space Complexity:** O(total characters in dictionary)

Insert all roots into a Trie. For each sentence word, find the shortest matching root by traversing the Trie until `is_end` is found.
