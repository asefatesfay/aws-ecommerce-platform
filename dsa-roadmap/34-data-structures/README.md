# Data Structures — Python Implementations

Complete, runnable Python implementations of all major data structures with explanations, examples, and LeetCode problems.

---

## Table of Contents

| # | Data Structure | Key Operations | Best For |
|---|---|---|---|
| 1 | [Singly Linked List](./01-singly-linked-list.md) | append O(N), prepend O(1), delete O(N) | Sequential access, reversals |
| 2 | [Doubly Linked List](./02-doubly-linked-list.md) | all O(1) with node reference | LRU Cache, browser history |
| 3 | [Stack](./03-stack.md) | push/pop/peek O(1) | Parentheses, undo, DFS |
| 4 | [Queue](./04-queue.md) | enqueue/dequeue O(1) | BFS, task scheduling |
| 5 | [Deque](./05-deque.md) | push/pop both ends O(1) | Sliding window, palindrome |
| 6 | [Circular Buffer](./06-circular-buffer.md) | enqueue/dequeue O(1), fixed size | Streaming, OS buffers |
| 7 | [Binary Tree](./07-binary-tree.md) | traversals O(N) | Hierarchical data |
| 8 | [Binary Search Tree](./08-bst.md) | search/insert/delete O(log N) avg | Sorted data, range queries |
| 9 | [Min/Max Heap](./09-heap.md) | push/pop O(log N), peek O(1) | Priority queues, Top K |
| 10 | [Trie](./10-trie.md) | insert/search O(L) | Autocomplete, prefix search |
| 11 | [Hash Map](./11-hashmap.md) | get/put/delete O(1) avg | Frequency counting, caching |
| 12 | [Graph](./12-graph.md) | DFS/BFS O(V+E) | Networks, paths, dependencies |
| 13 | [Union-Find](./13-union-find.md) | find/union O(α(N)) | Connected components, MST |
| 14 | [LRU Cache](./14-lru-cache.md) | get/put O(1) | Caching with eviction |
| 15 | [Segment Tree](./15-segment-tree.md) | query/update O(log N) | Range queries with updates |
| 16 | [Fenwick Tree (BIT)](./16-fenwick-tree.md) | query/update O(log N) | Prefix sums with updates |
| 17 | [Monotonic Stack](./17-monotonic-stack.md) | push/pop O(1) amortized | Next greater/smaller element |
| 18 | [Monotonic Queue](./18-monotonic-queue.md) | push/pop O(1) amortized | Sliding window max/min |
| 19 | [Skip List](./19-skip-list.md) | search/insert/delete O(log N) avg | Sorted sets (Redis) |
| 20 | [Bloom Filter](./20-bloom-filter.md) | add/contains O(k) | Membership with false positives |
| 21 | [Sparse Table](./21-sparse-table.md) | query O(1), build O(N log N) | Static range min/max |
| 22 | [Circular Linked List](./22-circular-linked-list.md) | traverse O(N) | Round-robin, Josephus |
| 23 | [AVL Tree](./23-avl-tree.md) | insert/delete/search O(log N) worst | Read-heavy sorted data |
| 24 | [Red-Black Tree](./24-red-black-tree.md) | insert/delete/search O(log N) worst | Write-heavy sorted data |
| 25 | [Interval Tree](./25-interval-tree.md) | insert O(log N), overlap O(log N+k) | Calendar, scheduling |
| 26 | [Suffix Array](./26-suffix-array.md) | build O(N log N), query O(M log N) | String matching, LRS |
| 27 | [Treap](./27-treap.md) | all O(log N) expected | Competitive programming |
| 28 | [B-Tree](./28-b-tree.md) | all O(log_t N) | Database indexes |
| 29 | [Persistent Segment Tree](./29-persistent-segment-tree.md) | O(log N) per version | Historical range queries |
| 30 | [Disjoint Set with Rollback](./30-disjoint-set-with-rollback.md) | find/union O(log N), rollback O(1) | Dynamic connectivity |

---

## Quick Reference: Which DS to Use?

| Problem Type | Data Structure |
|---|---|
| "Find next greater element" | Monotonic Stack |
| "Sliding window max/min" | Monotonic Queue (Deque) |
| "Top K elements" | Min/Max Heap |
| "Prefix sum with updates" | Fenwick Tree |
| "Range query, static data" | Sparse Table |
| "Range query with updates" | Segment Tree |
| "Autocomplete / prefix search" | Trie |
| "Connected components" | Union-Find |
| "Shortest path (unweighted)" | BFS (Graph) |
| "Shortest path (weighted)" | Dijkstra (Graph + Heap) |
| "LRU eviction" | Doubly Linked List + Hash Map |
| "Frequency counting" | Hash Map |
| "Sorted order + O(log N) ops" | BST / Skip List |
| "Membership check, space-efficient" | Bloom Filter |
| "Fixed-size buffer, wrap-around" | Circular Buffer |
| "Undo/redo, DFS, parentheses" | Stack |
| "BFS, task queue" | Queue |
| "Hierarchical data" | Tree |

---

## Files

Each data structure has its own file with:
- Explanation and intuition
- Visual example
- Full Python implementation
- Complexity analysis
- LeetCode problems it solves
