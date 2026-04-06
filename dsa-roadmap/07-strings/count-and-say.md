# Count and Say

**Difficulty:** Medium
**Pattern:** String Simulation / Run-Length Encoding
**LeetCode:** #38

## Problem Statement

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- `countAndSay(1) = "1"`
- `countAndSay(n)` is the run-length encoding of `countAndSay(n - 1)`

Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters with the character followed by the count of repetitions.

Given a positive integer `n`, return the `n`th element of the count-and-say sequence.

## Examples

### Example 1
**Input:** `n = 1`
**Output:** `"1"`

### Example 2
**Input:** `n = 4`
**Output:** `"1211"`
**Explanation:**
- countAndSay(1) = "1"
- countAndSay(2) = RLE of "1" = "11" (one 1)
- countAndSay(3) = RLE of "11" = "21" (two 1s)
- countAndSay(4) = RLE of "21" = "1211" (one 2, one 1)

## Constraints
- `1 <= n <= 30`

## Hints

> 💡 **Hint 1:** Build the sequence iteratively. Start with "1" and apply the run-length encoding transformation n-1 times.

> 💡 **Hint 2:** To apply RLE to a string: scan through it, counting consecutive identical characters. When the character changes (or you reach the end), append the count and the character to the result.

> 💡 **Hint 3:** Use a pointer and a count variable. When `s[i] != s[i-1]`, emit the count and character, then reset the count.

## Approach

**Time Complexity:** O(2^n) in the worst case (sequence length can double each step)
**Space Complexity:** O(2^n)

Iteratively apply run-length encoding n-1 times, starting from "1". Each iteration scans the current string and builds the next by counting consecutive identical characters.
