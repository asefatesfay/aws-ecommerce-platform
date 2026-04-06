# Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy
**Pattern:** Divide and Conquer / Tree Construction
**LeetCode:** #108

## Problem Statement

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree. A height-balanced binary tree is one where the depth of the two subtrees of every node never differs by more than one.

## Examples

### Example 1
**Input:** `nums = [-10,-3,0,5,9]`
**Output:** `[0,-3,9,-10,null,5]`
**Explanation:** Root is 0 (middle). Left subtree from [-10,-3], right from [5,9].

### Example 2
**Input:** `nums = [1,3]`
**Output:** `[3,1]` or `[1,null,3]`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in strictly increasing order

## Hints

> 💡 **Hint 1:** To keep the tree height-balanced, always pick the middle element of the current subarray as the root. This ensures equal-sized left and right subtrees.

> 💡 **Hint 2:** Recursively build: `mid = (left + right) // 2`, create a node with `nums[mid]`, then recurse on `nums[left..mid-1]` for the left subtree and `nums[mid+1..right]` for the right.

> 💡 **Hint 3:** The base case is when `left > right` — return null. This naturally handles empty subarrays.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(log n) for the recursion stack

Divide and conquer: always pick the midpoint as root, recursively build left subtree from the left half and right subtree from the right half.
