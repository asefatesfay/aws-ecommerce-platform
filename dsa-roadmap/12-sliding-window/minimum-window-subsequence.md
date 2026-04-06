# Minimum Window Subsequence

**Difficulty:** Hard
**Pattern:** Sliding Window / Two Pointers
**LeetCode:** #727

## Problem Statement

Given strings `s1` and `s2`, return the minimum contiguous substring window of `s1` that contains `s2` as a subsequence. If there is no such window in `s1` that covers all characters in `s2`, return the empty string `""`. If there are multiple answers, return the one with the left-most starting index.

## Examples

### Example 1
**Input:** `s1 = "abcdebdde"`, `s2 = "bde"`
**Output:** `"bcde"`
**Explanation:** "bcde" is the shortest window containing "bde" as a subsequence.

### Example 2
**Input:** `s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"`, `s2 = "u"`
**Output:** `""`

## Constraints
- `1 <= s1.length <= 2 * 10^4`
- `1 <= s2.length <= 100`
- `s1` and `s2` consist of lowercase English letters

## Hints

> 💡 **Hint 1:** This is different from "Minimum Window Substring" — here s2 must appear as a subsequence (order matters, but gaps are allowed), not as a set of characters.

> 💡 **Hint 2:** For each starting position in s1, greedily match s2 as a subsequence going right. When s2 is fully matched, you have a valid window ending at some position.

> 💡 **Hint 3:** To minimize the window, after finding the right end, scan backward from the right end to find the leftmost valid start. Track the minimum length window found.

## Approach

**Time Complexity:** O(|s1| × |s2|)
**Space Complexity:** O(1)

Two-pointer forward scan to find a valid window (match s2 as subsequence), then backward scan to tighten the left boundary. Repeat from each new starting position.
