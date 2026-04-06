# String Compression

**Difficulty:** Medium
**Pattern:** Two Pointers (Read/Write)
**LeetCode:** #443

## Problem Statement

Given an array of characters `chars`, compress it using the following algorithm: Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`, if the group's length is 1, append the character to `s`. Otherwise, append the character followed by the group's length. The compressed string `s` should not be returned separately, but instead, be stored in the input character array `chars`. After you are done modifying the input array, return the new length of the array. You must write an algorithm that uses only constant extra space.

## Examples

### Example 1
**Input:** `chars = ['a','a','b','b','c','c','c']`
**Output:** `6`, `chars = ['a','2','b','2','c','3']`

### Example 2
**Input:** `chars = ['a']`
**Output:** `1`

### Example 3
**Input:** `chars = ['a','b','b','b','b','b','b','b','b','b','b','b','b']`
**Output:** `4`, `chars = ['a','b','1','2']`

## Constraints
- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol

## Hints

> 💡 **Hint 1:** Use a read pointer to scan groups and a write pointer to write the compressed output in-place.

> 💡 **Hint 2:** For each group of identical characters, write the character at the write pointer, then write the count (if > 1) digit by digit.

> 💡 **Hint 3:** The count may be multi-digit (e.g., 12 → '1','2'). Write each digit separately. The write pointer is always ≤ read pointer, so in-place is safe.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Read pointer scans groups, write pointer writes compressed output in-place. For each group, write the character and (if count > 1) each digit of the count.
