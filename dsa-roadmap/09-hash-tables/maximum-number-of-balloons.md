# Maximum Number of Balloons

**Difficulty:** Easy
**Pattern:** Hash Map / Frequency Counting
**LeetCode:** #1189

## Problem Statement

Given a string `text`, you want to use the characters of `text` to form as many instances of the word `"balloon"` as possible. You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

## Examples

### Example 1
**Input:** `text = "nlaebolko"`
**Output:** `1`

### Example 2
**Input:** `text = "loonbalxballpoon"`
**Output:** `2`

### Example 3
**Input:** `text = "leetcode"`
**Output:** `0`

## Constraints
- `1 <= text.length <= 10^4`
- `text` consists of lower case English letters only

## Hints

> 💡 **Hint 1:** Count the frequency of each character in `text`. The word "balloon" needs: b×1, a×1, l×2, o×2, n×1.

> 💡 **Hint 2:** For each required character, compute how many complete "balloon"s that character allows: `freq[c] // required[c]`.

> 💡 **Hint 3:** The answer is the minimum across all required characters. Note that 'l' and 'o' each appear twice in "balloon", so divide their counts by 2.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (fixed 26-character alphabet)

Count character frequencies, then compute `min(freq['b'], freq['a'], freq['l']//2, freq['o']//2, freq['n'])`.
