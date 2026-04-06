# Text Justification

**Difficulty:** Hard
**Pattern:** String Simulation / Greedy
**LeetCode:** #68

## Problem Statement

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified. Pack as many words as you can in each line. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the extra spaces go to the left slots. The last line should be left-justified with no extra space between words.

## Examples

### Example 1
**Input:** `words = ["This","is","an","example","of","text","justification."]`, `maxWidth = 16`
**Output:**
```
"This    is    an"
"example  of text"
"justification.  "
```

### Example 2
**Input:** `words = ["What","must","be","acknowledgment","shall","be"]`, `maxWidth = 16`
**Output:**
```
"What   must   be"
"acknowledgment  "
"shall be        "
```

## Constraints
- `1 <= words.length <= 300`
- `1 <= words[i].length <= 20`
- `words[i]` consists of only English letters and symbols
- `1 <= maxWidth <= 100`
- `words[i].length <= maxWidth`

## Hints

> 💡 **Hint 1:** First, greedily determine which words go on each line. Pack words left to right until adding the next word would exceed maxWidth (accounting for at least one space between words).

> 💡 **Hint 2:** For each line (except the last), calculate the total spaces needed and distribute them evenly. If spaces don't divide evenly, the first (spaces % gaps) slots get one extra space.

> 💡 **Hint 3:** Handle special cases: (1) a line with only one word — pad with spaces on the right, (2) the last line — left-justify with single spaces between words and pad the right.

## Approach

**Time Complexity:** O(n × maxWidth)
**Space Complexity:** O(maxWidth) per line

Greedy line packing, then for each line compute the space distribution. The tricky part is the edge cases: single-word lines and the last line both use left-justification.
