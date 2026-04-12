# Doubly Linked List

## What is it?
A linked list where each node has pointers to both the **next** and **previous** nodes. This allows O(1) deletion of any node (given a reference to it) and O(1) insertion at both ends.

## Visual Example
```
None ← [1] ⇄ [2] ⇄ [3] ⇄ [4] → None
        ^head                ^tail

With sentinel nodes (simplifies edge cases):
[dummy_head] ⇄ [1] ⇄ [2] ⇄ [3] ⇄ [dummy_tail]

Insert after [2]:
[dummy_head] ⇄ [1] ⇄ [2] ⇄ [NEW] ⇄ [3] ⇄ [dummy_tail]

Remove [2]:
[dummy_head] ⇄ [1] ⇄ [3] ⇄ [dummy_tail]
(just update prev/next pointers — O(1) with node reference)
```

## Implementation

```python
class DNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None
        self.key = None  # used in LRU cache

class DoublyLinkedList:
    """
    Doubly linked list with sentinel head and tail.
    Sentinel nodes eliminate null checks for edge cases.
    """
    def __init__(self):
        self.head = DNode()  # dummy head (most recent end)
        self.tail = DNode()  # dummy tail (least recent end)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _insert_after(self, node, new_node):
        """Insert new_node immediately after node — O(1)"""
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.size += 1

    def _remove(self, node):
        """Remove node from list — O(1) given node reference"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

    def append_front(self, val):
        """Add to front (after dummy head) — O(1)"""
        self._insert_after(self.head, DNode(val))

    def append_back(self, val):
        """Add to back (before dummy tail) — O(1)"""
        self._insert_after(self.tail.prev, DNode(val))

    def pop_front(self):
        """Remove and return front value — O(1)"""
        if self.size == 0:
            raise IndexError("Empty list")
        return self._remove(self.head.next).val

    def pop_back(self):
        """Remove and return back value — O(1)"""
        if self.size == 0:
            raise IndexError("Empty list")
        return self._remove(self.tail.prev).val

    def move_to_front(self, node):
        """Move existing node to front — O(1)"""
        self._remove(node)
        self._insert_after(self.head, node)
        self.size += 1  # _remove decremented, re-increment

    def __len__(self):
        return self.size

    def to_list(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.val)
            curr = curr.next
        return result
```

## Example Usage
```python
dll = DoublyLinkedList()
dll.append_back(1)
dll.append_back(2)
dll.append_back(3)
dll.append_front(0)
print(dll.to_list())   # [0, 1, 2, 3]

dll.pop_front()
print(dll.to_list())   # [1, 2, 3]

dll.pop_back()
print(dll.to_list())   # [1, 2]
print(len(dll))        # 2
```

## When to Use
- LRU Cache (O(1) move-to-front + O(1) remove-from-back)
- Browser history (forward/backward navigation)
- Text editor cursor movement
- Any situation needing O(1) deletion with node reference

## LeetCode Problems

| Problem | Difficulty | How DLL Helps |
|---------|-----------|---------------|
| LRU Cache (#146) | Medium | O(1) move-to-front + eviction |
| LFU Cache (#460) | Hard | Frequency buckets with DLL |
| Design Linked List (#707) | Medium | Direct DLL implementation |
| Flatten a Multilevel Doubly Linked List (#430) | Medium | DLL traversal |
| All O`one Data Structure (#432) | Hard | DLL of frequency buckets |
| Design Browser History (#1472) | Medium | DLL for navigation |
