# Find Smallest Letter Greater Than Target

**Difficulty:** Easy
**Pattern:** Binary Search
**LeetCode:** #744

## Problem Statement

You are given an array of characters `letters` that is sorted in non-decreasing order, and a character `target`. There are at least two different characters in `letters`. Return the smallest character in `letters` that is lexicographically greater than `target`. If such a character does not exist, return the first character in `letters`.

## Examples

### Example 1
**Input:** `letters = ['c','f','j']`, `target = 'a'`
**Output:** `'c'`

### Example 2
**Input:** `letters = ['c','f','j']`, `target = 'c'`
**Output:** `'f'`

### Example 3
**Input:** `letters = ['x','x','y','y']`, `target = 'z'`
**Output:** `'x'`
**Explanation:** No letter greater than 'z', wrap around to first.

## Constraints
- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter
- `letters` is sorted in non-decreasing order
- `letters` contains at least two different characters
- `target` is a lowercase English letter

## Hints

> 💡 **Hint 1:** Binary search for the first letter strictly greater than target.

> 💡 **Hint 2:** If letters[mid] <= target, search right (left = mid + 1). Otherwise, search left (right = mid).

> 💡 **Hint 3:** If left == letters.length (no letter greater than target), return letters[0] (wrap around).

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search for the leftmost letter > target. Wrap around if none found.
