# Binary Search Tree Iterator

**Difficulty:** Medium
**Pattern:** BST Inorder Traversal / Iterator Design
**LeetCode:** #173

## Problem Statement

Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a BST. `BSTIterator(root)` initializes the object. `boolean hasNext()` returns true if there exists a next number in the traversal. `int next()` moves the pointer to the right, then returns the number at the pointer. You may assume `next()` calls will always be valid.

## Examples

### Example 1
**Input:** `["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]` with tree `[7,3,15,null,null,9,20]`
**Output:** `[null,3,7,true,9,true,15,true,20,false]`

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`
- `0 <= Node.val <= 10^6`
- At most `10^5` calls will be made to `hasNext` and `next`

## Hints

> 💡 **Hint 1:** The key constraint is O(h) space (not O(n)). Don't precompute the entire inorder traversal — that would use O(n) space.

> 💡 **Hint 2:** Use a stack. In the constructor, push all left-spine nodes (root, root.left, root.left.left, ...). `next()` pops the top node, records its value, then pushes the left spine of its right child.

> 💡 **Hint 3:** `hasNext()` simply returns `len(stack) > 0`. Each `next()` call is amortized O(1) — each node is pushed and popped exactly once across all calls.

## Approach

**Time Complexity:** O(1) amortized for next(), O(h) for constructor
**Space Complexity:** O(h) for the stack

Stack-based lazy inorder traversal: initialize with the left spine, then on each `next()` call pop the top, push the left spine of its right child.
