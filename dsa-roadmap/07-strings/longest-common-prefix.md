# Longest Common Prefix

**Difficulty:** Easy
**Pattern:** String Comparison
**LeetCode:** #14

## Problem Statement

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

## Examples

### Example 1
**Input:** `strs = ["flower","flow","flight"]`
**Output:** `"fl"`

### Example 2
**Input:** `strs = ["dog","racecar","car"]`
**Output:** `""`
**Explanation:** There is no common prefix among the input strings.

## Constraints
- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters

## Hints

> 💡 **Hint 1:** The common prefix can be at most as long as the shortest string. Start with the first string as the candidate prefix.

> 💡 **Hint 2:** Compare the candidate prefix against each subsequent string. Shorten the prefix whenever it doesn't match the start of the current string.

> 💡 **Hint 3:** Keep trimming the last character of the prefix until it matches, or until the prefix is empty. Return whatever remains.

## Approach

**Time Complexity:** O(S) where S is the total number of characters across all strings
**Space Complexity:** O(1)

Use the first string as the initial prefix. For each subsequent string, shrink the prefix from the right until it matches the beginning of that string. Return the final prefix.
