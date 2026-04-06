# First Bad Version

**Difficulty:** Easy
**Pattern:** Binary Search
**LeetCode:** #278

## Problem Statement

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad. Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Examples

### Example 1
**Input:** `n = 5`, `bad = 4`
**Output:** `4`
**Explanation:** isBadVersion(3) = false, isBadVersion(5) = true, isBadVersion(4) = true → first bad is 4.

### Example 2
**Input:** `n = 1`, `bad = 1`
**Output:** `1`

## Constraints
- `1 <= bad <= n <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** Binary search for the first true in a sequence of false...false...true...true.

> 💡 **Hint 2:** If isBadVersion(mid) is true, the first bad version is at mid or earlier (right = mid). If false, it's after mid (left = mid + 1).

> 💡 **Hint 3:** Continue until left == right. That's the first bad version.

## Approach

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

Binary search for the leftmost true value. When mid is bad, search left half including mid. When mid is good, search right half.
