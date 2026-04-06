# Copy List with Random Pointer

**Difficulty:** Medium
**Pattern:** Linked List / Hash Map
**LeetCode:** #138

## Problem Statement

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`. Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. Return the head of the copied linked list.

## Examples

### Example 1
**Input:** `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
**Output:** `[[7,null],[13,0],[11,4],[10,2],[1,0]]`

## Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list

## Hints

> 💡 **Hint 1:** Use a HashMap mapping original nodes to their copies. First pass: create all new nodes. Second pass: set next and random pointers using the map.

> 💡 **Hint 2:** Two-pass with HashMap: pass 1 creates copies, pass 2 wires up pointers.

> 💡 **Hint 3:** O(1) space approach: interleave copies with originals (insert copy after each original), set random pointers, then separate the two lists.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n) with HashMap, O(1) with interleaving trick

HashMap approach: two passes — create nodes, then wire pointers. Interleaving approach: insert copies inline, set randoms, then split.
