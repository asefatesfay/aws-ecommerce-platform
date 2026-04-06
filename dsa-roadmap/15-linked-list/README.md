# Linked List

Linked lists are linear data structures where each node points to the next. Unlike arrays, they don't support O(1) random access, but they support O(1) insertion/deletion at known positions.

## Key Concepts

- **Singly linked list:** Each node has `val` and `next`.
- **Doubly linked list:** Each node has `val`, `next`, and `prev`.
- **Dummy/sentinel node:** A fake head node simplifies edge cases (empty list, operations on the head).
- **Fast/slow pointers:** Two pointers at different speeds — classic for cycle detection, finding the middle, and kth-from-end.

## Common Patterns

### Dummy Head
Create a dummy node before the real head. Simplifies code when the head might change or be deleted.

### Fast/Slow Pointers
- Middle of list: slow moves 1 step, fast moves 2 steps. When fast reaches end, slow is at middle.
- Cycle detection: if fast and slow ever meet, there's a cycle.
- kth from end: advance fast k steps, then move both until fast reaches end.

### Reversal
Iterative: maintain `prev`, `curr`, `next`. Recursive: reverse the rest, then fix the current node's pointer.

### Merge
Two-pointer merge of sorted lists. Use a dummy head to simplify.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Intersection of Two Linked Lists](./intersection-of-two-linked-lists.md) | Easy |
| [Remove Duplicates from Sorted List](./remove-duplicates-from-sorted-list.md) | Easy |
| [Design Linked List](./design-linked-list.md) | Medium |
| [Remove Nth Node From End of List](./remove-nth-node-from-end-of-list.md) | Medium |
| [Remove Duplicates from Sorted List II](./remove-duplicates-from-sorted-list-ii.md) | Medium |
| [Swap Nodes in Pairs](./swap-nodes-in-pairs.md) | Medium |
| [Copy List with Random Pointer](./copy-list-with-random-pointer.md) | Medium |
| [Partition List](./partition-list.md) | Medium |
| [Rotate List](./rotate-list.md) | Medium |
| [Add Two Numbers](./add-two-numbers.md) | Medium |
| [Flatten a Multilevel Doubly Linked List](./flatten-a-multilevel-doubly-linked-list.md) | Medium |
| [Delete the Middle Node of a Linked List](./delete-the-middle-node-of-a-linked-list.md) | Medium |
| [Odd Even Linked List](./odd-even-linked-list.md) | Medium |
| [Reorder List](./reorder-list.md) | Medium |
| [Add Two Numbers II](./add-two-numbers-ii.md) | Medium |
| [Delete Node in a Linked List](./delete-node-in-a-linked-list.md) | Medium |
| [Insert into a Sorted Circular Linked List](./insert-into-a-sorted-circular-linked-list.md) | Medium |
| [Merge In Between Linked Lists](./merge-in-between-linked-lists.md) | Medium |
| [Palindrome Linked List](./palindrome-linked-list.md) | Easy |
| [Reverse Linked List](./reverse-linked-list.md) | Easy |
| [Reverse Linked List II](./reverse-linked-list-ii.md) | Medium |
| [Reverse Nodes in k-Group](./reverse-nodes-in-k-group.md) | Hard |
| [Middle of the Linked List](./middle-of-the-linked-list.md) | Easy |
| [Happy Number](./happy-number.md) | Easy |
| [Linked List Cycle II](./linked-list-cycle-ii.md) | Medium |
