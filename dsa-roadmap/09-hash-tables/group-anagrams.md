# Group Anagrams

**Difficulty:** Medium
**Pattern:** Hash Map / Canonical Form
**LeetCode:** #49

## Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

## Examples

### Example 1
**Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`
**Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

### Example 2
**Input:** `strs = [""]`
**Output:** `[[""]]`

### Example 3
**Input:** `strs = ["a"]`
**Output:** `[["a"]]`

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** Anagrams have the same characters in different orders. You need a canonical form that all anagrams share.

> 💡 **Hint 2:** Sorting each string gives a canonical key: "eat", "tea", "ate" all sort to "aet". Use this sorted string as the HashMap key.

> 💡 **Hint 3:** Alternatively, use a tuple of 26 character counts as the key (avoids sorting). Group strings by their key and return the groups.

## Approach

**Time Complexity:** O(n × k log k) where k is the max string length
**Space Complexity:** O(n × k)

Use a HashMap where the key is the sorted version of each string. Append each string to its group. Return all groups.
