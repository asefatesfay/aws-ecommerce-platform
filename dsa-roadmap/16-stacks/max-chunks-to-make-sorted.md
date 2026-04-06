# Max Chunks To Make Sorted

**Difficulty:** Medium
**Pattern:** Stack / Greedy
**LeetCode:** #769

## Problem Statement

You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`. We split `arr` into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array. Return the largest number of chunks we can make to sort the array.

## Examples

### Example 1
**Input:** `arr = [4,3,2,1,0]`
**Output:** `1`
**Explanation:** Splitting into any chunk other than the whole array will not give a sorted result.

### Example 2
**Input:** `arr = [1,0,2,3,4]`
**Output:** `4`
**Explanation:** Split into [1,0],[2],[3],[4]. Sort each: [0,1],[2],[3],[4].

## Constraints
- `n == arr.length`
- `1 <= n <= 10`
- `0 <= arr[i] < n`
- All the elements of `arr` are unique

## Hints

> 💡 **Hint 1:** A chunk can be sorted independently if all elements in it are in the right "zone" — the maximum element in the chunk equals the chunk's last index.

> 💡 **Hint 2:** Scan left to right, tracking the running maximum. When `max_so_far == current_index`, we can make a cut here.

> 💡 **Hint 3:** Count the number of valid cut points.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track running maximum. When max equals current index, increment chunk count. The running max equals the index means all elements in this prefix belong to this prefix's sorted positions.
