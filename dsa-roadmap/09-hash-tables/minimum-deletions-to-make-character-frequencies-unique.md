# Minimum Deletions to Make Character Frequencies Unique

**Difficulty:** Medium
**Pattern:** Hash Map / Greedy
**LeetCode:** #1647

## Problem Statement

A string `s` is called good if there are no two different characters in `s` that have the same frequency. Given a string `s`, return the minimum number of characters you need to delete to make `s` good.

## Examples

### Example 1
**Input:** `s = "aab"`
**Output:** `0`
**Explanation:** 'a' appears 2 times, 'b' appears 1 time. All frequencies are unique.

### Example 2
**Input:** `s = "aaabbbcc"`
**Output:** `2`
**Explanation:** Delete one 'b' and one 'c' to get frequencies {3,2,1} or {3,1,1} — wait, need all unique. Delete 2 to get {3,2,1}.

### Example 3
**Input:** `s = "ceabaacb"`
**Output:** `2`

## Constraints
- `1 <= s.length <= 10^5`
- `s` contains only lowercase English letters

## Hints

> 💡 **Hint 1:** Count character frequencies. The problem reduces to: given a multiset of frequencies, make all values unique with minimum decrements.

> 💡 **Hint 2:** Sort frequencies in descending order. For each frequency, if it's already taken, reduce it by 1 (one deletion) and try again. If it reaches 0, stop.

> 💡 **Hint 3:** Use a set to track used frequencies. For each frequency, keep decrementing until you find an unused value or reach 0. Count total decrements.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (26 characters)

Count frequencies, sort descending. Use a set of used frequencies. For each frequency, decrement until it's unique or zero, counting deletions.
