# Top K Frequent Words

**Difficulty:** Medium
**Pattern:** Hash Map + Heap/Sort
**LeetCode:** #692

## Problem Statement

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings. Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

## Examples

### Example 1
**Input:** `words = ["i","love","leetcode","i","love","coding"]`, `k = 2`
**Output:** `["i","love"]`

### Example 2
**Input:** `words = ["the","day","is","sunny","the","the","the","sunny","is","is"]`, `k = 4`
**Output:** `["the","is","sunny","day"]`

## Constraints
- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters
- `k` is in the range `[1, the number of unique words[i]]`

## Hints

> 💡 **Hint 1:** Count word frequencies with a HashMap.

> 💡 **Hint 2:** Sort words by (-frequency, word) to get descending frequency and ascending lexicographic order for ties.

> 💡 **Hint 3:** Return the first k words. Alternatively, use a min-heap of size k with a custom comparator.

## Approach

**Time Complexity:** O(n log k) with heap, O(n log n) with sort
**Space Complexity:** O(n)

Count frequencies, then sort by (-freq, word) and take first k. Or use a min-heap of size k.
