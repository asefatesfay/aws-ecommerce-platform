# Circular Linked List

## What is it?
A linked list where the **last node's `next` pointer points back to the head** (singly circular) or the head's `prev` points to the tail (doubly circular). There is no `None` at the end — the list forms a loop.

## Visual Example
```
Singly Circular:
head
 |
[1] → [2] → [3] → [4] → (back to [1])
 ↑___________________________________|

Doubly Circular:
[1] ⇄ [2] ⇄ [3] ⇄ [4]
 ↑_________________________↓
(head.prev = tail, tail.next = head)

Traversal from head:
1 → 2 → 3 → 4 → 1 → 2 → ... (infinite loop if not careful!)
Stop condition: curr.next == head
```

## Key Difference from Regular Linked List
```
Regular:  [1] → [2] → [3] → None
Circular: [1] → [2] → [3] → [1]  (wraps around)

Use case: Round-robin scheduling
  Process 1 → Process 2 → Process 3 → Process 1 → ...
  Each process gets a time slice, then moves to next.
```

## Implementation

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CircularLinkedList:
    """
    Singly circular linked list.
    The tail's next points back to head.
    
    Example:
        cll = CircularLinkedList()
        cll.append(1)
        cll.append(2)
        cll.append(3)
        # Structure: 1 → 2 → 3 → (back to 1)
        cll.to_list()  # [1, 2, 3]
        cll.rotate(1)  # [2, 3, 1]
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        """Add to end — O(N) without tail pointer"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # points to itself
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
        self.size += 1

    def prepend(self, val):
        """Add to front — O(N) to update tail"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            curr.next = new_node
            self.head = new_node
        self.size += 1

    def delete(self, val):
        """Delete first occurrence — O(N)"""
        if not self.head:
            return False
        if self.head.val == val:
            if self.size == 1:
                self.head = None
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            return True
        curr = self.head
        while curr.next != self.head:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.size -= 1
                return True
            curr = curr.next
        return False

    def rotate(self, k):
        """
        Rotate list by k positions (move head forward k steps).
        rotate(1): [1,2,3] → [2,3,1]
        O(N)
        """
        if not self.head or k == 0:
            return
        k = k % self.size
        if k == 0:
            return
        curr = self.head
        for _ in range(k - 1):
            curr = curr.next
        self.head = curr.next

    def josephus(self, k):
        """
        Josephus problem: n people in circle, every k-th person eliminated.
        Returns the value of the last remaining person.
        O(N * k) simulation.
        
        Example: josephus(k=3) with [1,2,3,4,5]
          Eliminate: 3, 1, 5, 2 → Survivor: 4
        """
        if not self.head:
            return None
        curr = self.head
        while self.size > 1:
            # Move k-1 steps forward
            for _ in range(k - 1):
                curr = curr.next
            # Delete curr
            val_to_delete = curr.val
            next_node = curr.next
            self.delete(val_to_delete)
            curr = next_node if self.head else None
        return self.head.val if self.head else None

    def to_list(self):
        """Convert to Python list — O(N)"""
        if not self.head:
            return []
        result = [self.head.val]
        curr = self.head.next
        while curr != self.head:
            result.append(curr.val)
            curr = curr.next
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        lst = self.to_list()
        if not lst:
            return "Empty"
        return " → ".join(map(str, lst)) + f" → (back to {lst[0]})"
```

## Example Usage
```python
cll = CircularLinkedList()
for v in [1, 2, 3, 4, 5]:
    cll.append(v)

print(cll)           # 1 → 2 → 3 → 4 → 5 → (back to 1)
print(cll.to_list()) # [1, 2, 3, 4, 5]

cll.rotate(2)
print(cll.to_list()) # [3, 4, 5, 1, 2]

cll.delete(4)
print(cll.to_list()) # [3, 5, 1, 2]

# Josephus problem
cll2 = CircularLinkedList()
for v in [1, 2, 3, 4, 5]:
    cll2.append(v)
print(cll2.josephus(3))  # 4 (survivor when every 3rd is eliminated)

# Mathematical solution for Josephus (O(N), no list needed)
def josephus_math(n, k):
    """Find 0-indexed position of survivor — O(N)"""
    pos = 0
    for i in range(2, n + 1):
        pos = (pos + k) % i
    return pos + 1  # convert to 1-indexed

print(josephus_math(5, 3))  # 4
```

## When to Use
- **Round-robin scheduling**: OS process scheduling, network token ring
- **Circular buffer simulation**: when you need wrap-around behavior
- **Josephus problem**: classic elimination problem
- **Music playlist**: loop through songs continuously
- **Multiplayer games**: turn-based games cycling through players

## LeetCode Problems

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| Find the Winner of the Circular Game (#1823) | Medium | Josephus problem |
| Insert into a Sorted Circular Linked List (#708) | Medium | Direct circular LL |
| Design Circular Queue (#622) | Medium | Circular structure |
| Design Circular Deque (#641) | Medium | Circular structure |
| Linked List Cycle (#141) | Easy | Detect cycle (Floyd's) |
| Linked List Cycle II (#142) | Medium | Find cycle entry |
