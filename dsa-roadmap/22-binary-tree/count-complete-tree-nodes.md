# Count Complete Tree Nodes

**Difficulty:** Easy
**Pattern:** Binary Search / Tree Properties
**LeetCode:** #222

## Problem Statement

Given the root of a complete binary tree, return the number of the nodes in the tree. In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.

Design an algorithm that runs in less than O(n) time complexity.

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5,6]`
**Output:** `6`

### Example 2
**Input:** `root = []`
**Output:** `0`

## Constraints
- The number of nodes in the tree is in the range `[0, 5 * 10^4]`
- `0 <= Node.val <= 5 * 10^4`
- The tree is guaranteed to be complete

## Hints

> 💡 **Hint 1:** A naive O(n) traversal works but misses the point. Exploit the "complete" property: compute the left height and right height. If they're equal, the left subtree is a perfect binary tree with `2^h - 1` nodes.

> 💡 **Hint 2:** Compute `left_height` by going left repeatedly, and `right_height` by going right repeatedly. If equal, left subtree is perfect: return `2^left_height - 1 + 1 + count(right)`. If not equal, right subtree is perfect one level shorter.

> 💡 **Hint 3:** Each recursive call reduces the problem by half (you only recurse into one subtree), giving O(log^2 n) time — O(log n) levels, each computing height in O(log n).

## Approach

**Time Complexity:** O(log^2 n)
**Space Complexity:** O(log n) for the recursion stack

Compare left-path height vs right-path height. If equal, left subtree is perfect (count = 2^h - 1); recurse only into right. Otherwise, right subtree is perfect one level shorter; recurse only into left.
