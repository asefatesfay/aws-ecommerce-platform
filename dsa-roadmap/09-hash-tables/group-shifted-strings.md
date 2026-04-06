# Group Shifted Strings

**Difficulty:** Medium
**Pattern:** Hash Map / Canonical Form
**LeetCode:** #249

## Problem Statement

We can shift a string by shifting each of its letters to its successive letter. For example, `"abc"` can be shifted to `"bcd"`. We can keep shifting, so `"abc"` can become `"xyz"` (wrapping around). Given an array of strings `strings`, group all strings that belong to the same shifting sequence. Return the answer in any order.

## Examples

### Example 1
**Input:** `strings = ["abc","bcd","acef","xyz","az","ba","a","z"]`
**Output:** `[["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]`

### Example 2
**Input:** `strings = ["a"]`
**Output:** `[["a"]]`

## Constraints
- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i]` consists of lowercase English letters

## Hints

> 💡 **Hint 1:** Two strings belong to the same shifting sequence if one can be shifted to become the other. What's a canonical form that captures this?

> 💡 **Hint 2:** Normalize each string by computing the differences between consecutive characters (modulo 26). This difference pattern is invariant under shifting.

> 💡 **Hint 3:** For "abc": differences are (1,1). For "bcd": differences are (1,1). For "az": differences are (25). For "ba": differences are (25). Use the difference tuple as the HashMap key.

## Approach

**Time Complexity:** O(n × k) where k is max string length
**Space Complexity:** O(n × k)

Compute a canonical key for each string as the tuple of consecutive character differences (mod 26). Group strings by this key.
