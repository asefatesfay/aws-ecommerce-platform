# Singly Linked List

## What is it?
A linear data structure where each node contains a value and a pointer to the next node. Unlike arrays, nodes are not stored contiguously in memory — each node can be anywhere.

## Visual Example
```
head
 |
[1] → [2] → [3] → [4] → None

Append(5):
[1] → [2] → [3] → [4] → [5] → None

Delete(3):
[1] → [2] → [4] → [5] → None

Reverse:
[5] → [4] → [2] → [1] → None
```

## Implementation

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        """Add to end — O(N)"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def prepend(self, val):
        """Add to front — O(1)"""
        self.head = Node(val, self.head)
        self.size += 1

    def delete(self, val):
        """Delete first occurrence — O(N)"""
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next

    def search(self, val):
        """Find node — O(N)"""
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None

    def reverse(self):
        """Reverse in-place — O(N)"""
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def get_middle(self):
        """Find middle node using slow/fast pointers — O(N)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def has_cycle(self):
        """Detect cycle using Floyd's algorithm — O(N)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def to_list(self):
        result, curr = [], self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join(map(str, self.to_list())) + " -> None"
```

## Example Usage
```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
print(ll)          # 0 -> 1 -> 2 -> 3 -> None

ll.delete(2)
print(ll)          # 0 -> 1 -> 3 -> None

ll.reverse()
print(ll)          # 3 -> 1 -> 0 -> None

print(ll.get_middle().val)  # 1
```

## When to Use
- When you need O(1) insertions/deletions at known positions
- Implementing stacks, queues, LRU cache
- When size is unknown and dynamic

## LeetCode Problems

| Problem | Difficulty | Technique |
|---------|-----------|-----------|
| Reverse Linked List (#206) | Easy | Iterative/recursive reversal |
| Middle of the Linked List (#876) | Easy | Slow/fast pointers |
| Linked List Cycle (#141) | Easy | Floyd's cycle detection |
| Linked List Cycle II (#142) | Medium | Floyd's + find entry |
| Remove Nth Node From End (#19) | Medium | Two pointers, gap of N |
| Merge Two Sorted Lists (#21) | Easy | Merge with dummy head |
| Palindrome Linked List (#234) | Easy | Reverse second half |
| Reorder List (#143) | Medium | Find middle + reverse + merge |
| Add Two Numbers (#2) | Medium | Digit-by-digit addition |
| Copy List with Random Pointer (#138) | Medium | Hash map or interleaving |
| Reverse Nodes in k-Group (#25) | Hard | Reverse in chunks |
