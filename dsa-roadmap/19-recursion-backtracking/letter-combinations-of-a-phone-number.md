# Letter Combinations of a Phone Number

**Difficulty:** Medium
**Pattern:** Backtracking
**LeetCode:** #17

## Problem Statement

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below: 2→abc, 3→def, 4→ghi, 5→jkl, 6→mno, 7→pqrs, 8→tuv, 9→wxyz.

## Examples

### Example 1
**Input:** `digits = "23"`
**Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

### Example 2
**Input:** `digits = ""`
**Output:** `[]`

### Example 3
**Input:** `digits = "2"`
**Output:** `["a","b","c"]`

## Constraints
- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`

## Hints

> 💡 **Hint 1:** Use a phone mapping dictionary. Backtrack through each digit.

> 💡 **Hint 2:** At each position, try all letters mapped to the current digit. Recurse to the next digit.

> 💡 **Hint 3:** When the current combination has length equal to digits length, add to results.

## Approach

**Time Complexity:** O(4^n × n) where n is digits length
**Space Complexity:** O(n)

Backtracking: for each digit, try all its mapped letters. Collect when combination is complete.
