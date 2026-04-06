# BST / Ordered Set

A Binary Search Tree (BST) maintains the invariant: all values in the left subtree are less than the root, and all values in the right subtree are greater. This gives O(log n) search, insert, and delete for balanced trees. An ordered set (like `SortedList` in Python or `TreeSet` in Java) provides the same guarantees with a self-balancing BST under the hood.

## BST Core Properties

- **Inorder traversal** produces sorted output — exploit this constantly
- **Search:** Go left if target < node, right if target > node
- **Insert:** Follow search path until you find a null slot
- **Delete:** Three cases — leaf (just remove), one child (replace with child), two children (replace with inorder successor)

## Key Patterns

### Inorder for Sorted Access
Any problem asking for "kth smallest", "minimum difference", or "sorted output" from a BST → inorder traversal.

### Bounds Propagation
For validation or range queries, pass `(min_bound, max_bound)` down through the tree. Each node must satisfy its bounds.

### Predecessor / Successor
In a BST, the inorder predecessor of a node is the rightmost node in its left subtree. The inorder successor is the leftmost node in its right subtree.

### Ordered Set Applications
When you need a dynamic sorted collection with O(log n) insert/delete/search and O(log n) rank queries, use an ordered set (balanced BST). Common use cases:
- Sliding window with sorted order
- Finding the closest value to a target
- Range queries on a dynamic set

## When to Recognize This Pattern

- Problem involves a BST and asks for sorted/ordered output → inorder traversal
- "Find kth smallest/largest" in a BST → inorder with counter
- "Validate BST" → bounds propagation DFS
- "Find closest value" → BST search, track closest during traversal
- "Interval scheduling with conflicts" → ordered set for efficient overlap detection
- "Stock prices" or "event scheduling" with dynamic insertions → ordered set

## Common Techniques

- **Augmented BST:** Store subtree size at each node for O(log n) rank queries
- **Morris traversal:** O(1) space inorder traversal
- **Lazy deletion:** Mark nodes as deleted instead of restructuring
- **Coordinate compression:** Map values to ranks before building BST

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Search in a Binary Search Tree](./search-in-a-binary-search-tree.md) | Easy |
| [Closest Binary Search Tree Value](./closest-binary-search-tree-value.md) | Easy |
| [Two Sum IV - Input is a BST](./two-sum-iv-input-is-a-bst.md) | Easy |
| [Range Sum of BST](./range-sum-of-bst.md) | Easy |
| [Trim a Binary Search Tree](./trim-a-binary-search-tree.md) | Medium |
| [Insert into a Binary Search Tree](./insert-into-a-binary-search-tree.md) | Medium |
| [Delete Node in a BST](./delete-node-in-a-bst.md) | Medium |
| [Recover Binary Search Tree](./recover-binary-search-tree.md) | Medium |
| [Inorder Successor in BST](./inorder-successor-in-bst.md) | Medium |
| [Lowest Common Ancestor of a Binary Search Tree](./lowest-common-ancestor-of-a-binary-search-tree.md) | Medium |
| [Construct BST from Preorder Traversal](./construct-bst-from-preorder-traversal.md) | Medium |
| [Convert BST to Sorted Doubly Linked List](./convert-bst-to-sorted-doubly-linked-list.md) | Medium |
| [Largest BST Subtree](./largest-bst-subtree.md) | Medium |
| [My Calendar I](./my-calendar-i.md) | Medium |
| [My Calendar II](./my-calendar-ii.md) | Medium |
| [Stock Price Fluctuation](./stock-price-fluctuation.md) | Medium |
