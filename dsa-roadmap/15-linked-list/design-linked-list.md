# Design Linked List

**Difficulty:** Medium
**Pattern:** Linked List Design
**LeetCode:** #707

## Problem Statement

Design your implementation of the linked list. You can choose to use a singly or doubly linked list. Implement the `MyLinkedList` class:
- `MyLinkedList()` Initializes the object.
- `int get(int index)` Get the value of the `index`th node. Return `-1` if invalid.
- `void addAtHead(int val)` Add a node of value `val` before the first element.
- `void addAtTail(int val)` Append a node of value `val` as the last element.
- `void addAtIndex(int index, int val)` Add before the `index`th node. If index equals length, append. If index > length, do nothing.
- `void deleteAtIndex(int index)` Delete the `index`th node if valid.

## Examples

### Example 1
**Input:** `["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]` with args `[[],[1],[3],[1,2],[1],[1],[1]]`
**Output:** `[null,null,null,null,2,null,3]`

## Constraints
- `0 <= index, val <= 1000`
- At most `2000` calls to the methods

## Hints

> 💡 **Hint 1:** Use a dummy head node to simplify all operations (no special case for head insertion/deletion).

> 💡 **Hint 2:** Maintain a `size` counter. For `get` and `deleteAtIndex`, validate the index against size. For `addAtIndex`, traverse to the predecessor node.

> 💡 **Hint 3:** For a doubly linked list, also maintain a dummy tail for O(1) tail operations.

## Approach

**Time Complexity:** O(n) for index-based operations, O(1) for head/tail
**Space Complexity:** O(n)

Singly linked list with dummy head and size counter. Traverse to the predecessor for index-based operations.
