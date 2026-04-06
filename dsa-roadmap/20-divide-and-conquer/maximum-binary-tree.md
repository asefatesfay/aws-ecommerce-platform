# Maximum Binary Tree

**Difficulty:** Medium
**Pattern:** Divide and Conquer
**LeetCode:** #654

## Problem Statement

You are given an integer array `nums` with no duplicates. A maximum binary tree can be built recursively from `nums` using the following algorithm: Create a root node whose value is the maximum value in `nums`. Recursively build the left subtree on the subarray prefix to the left of the maximum value. Recursively build the right subtree on the subarray suffix to the right of the maximum value. Return the maximum binary tree built from `nums`.

## Examples

### Example 1
**Input:** `nums = [3,2,1,6,0,5]`
**Output:** `[6,3,5,null,2,0,null,null,1]`
**Explanation:** Root is 6 (max). Left subtree from [3,2,1], right from [0,5].

### Example 2
**Input:** `nums = [3,2,1]`
**Output:** `[3,null,2,null,1]`

## Constraints
- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- All integers in `nums` are unique

## Hints

> 💡 **Hint 1:** Find the index of the maximum element in the current subarray. That element becomes the root.

> 💡 **Hint 2:** Recursively build the left subtree from nums[left..max_idx-1] and the right subtree from nums[max_idx+1..right].

> 💡 **Hint 3:** Base case: empty subarray returns null.

## Approach

**Time Complexity:** O(n²) average, O(n log n) with segment tree
**Space Complexity:** O(n) recursion depth

Divide and conquer: find max, create root, recurse on left and right subarrays.
