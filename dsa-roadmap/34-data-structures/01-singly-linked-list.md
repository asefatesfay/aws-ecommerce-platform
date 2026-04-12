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

---

### 1. Reverse Linked List — #206 (Easy)

**Problem**: Given the head of a singly linked list, reverse the list and return the reversed list's head.

```
Input:  1 → 2 → 3 → 4 → 5 → None
Output: 5 → 4 → 3 → 2 → 1 → None

Input:  1 → 2 → None
Output: 2 → 1 → None

Input:  None
Output: None
```

**Constraints**: 0 to 5000 nodes, values -5000 to 5000.

**Hints**:
1. Use three pointers: `prev=None`, `curr=head`, `nxt`
2. Each step: save `nxt = curr.next`, point `curr.next = prev`, advance both
3. When `curr` is None, `prev` is the new head

---

### 2. Middle of the Linked List — #876 (Easy)

**Problem**: Given the head of a singly linked list, return the middle node. If two middle nodes exist, return the second one.

```
Input:  1 → 2 → 3 → 4 → 5
Output: node with value 3  (middle of 5 nodes)

Input:  1 → 2 → 3 → 4 → 5 → 6
Output: node with value 4  (second middle of 6 nodes)
```

**Hints**:
1. Use slow/fast pointers: slow moves 1 step, fast moves 2 steps
2. When fast reaches the end, slow is at the middle
3. For even-length lists, slow lands on the second middle naturally

---

### 3. Linked List Cycle — #141 (Easy)

**Problem**: Given the head of a linked list, determine if the list has a cycle. Return `true` if there is a cycle, `false` otherwise.

```
Input:  3 → 2 → 0 → -4 → (back to node 2)
Output: true

Input:  1 → 2 → (back to node 1)
Output: true

Input:  1 → None
Output: false
```

**Hints**:
1. Floyd's algorithm: slow moves 1 step, fast moves 2 steps
2. If they ever meet, there's a cycle
3. If fast reaches None, no cycle

---

### 4. Linked List Cycle II — #142 (Medium)

**Problem**: Given the head of a linked list, return the node where the cycle begins. If no cycle, return `null`.

```
Input:  3 → 2 → 0 → -4 → (back to node 2)
Output: node with value 2  (cycle starts here)

Input:  1 → 2 → (back to node 1)
Output: node with value 1

Input:  1 → None
Output: null
```

**Hints**:
1. First detect the cycle using Floyd's (slow/fast pointers)
2. When they meet, reset one pointer to head
3. Move both one step at a time — they meet at the cycle entry

---

### 5. Remove Nth Node From End of List — #19 (Medium)

**Problem**: Given the head of a linked list, remove the nth node from the end and return the head.

```
Input:  1 → 2 → 3 → 4 → 5,  n = 2
Output: 1 → 2 → 3 → 5        (removed 4, which is 2nd from end)

Input:  1,  n = 1
Output: None

Input:  1 → 2,  n = 1
Output: 1
```

**Hints**:
1. Use two pointers with a gap of n between them
2. Advance the fast pointer n steps first
3. Then move both until fast reaches the end — slow is just before the target

---

### 6. Merge Two Sorted Lists — #21 (Easy)

**Problem**: Merge two sorted linked lists and return the merged list (also sorted).

```
Input:  list1 = 1 → 2 → 4,  list2 = 1 → 3 → 4
Output: 1 → 1 → 2 → 3 → 4 → 4

Input:  list1 = None,  list2 = None
Output: None

Input:  list1 = None,  list2 = 0
Output: 0
```

**Hints**:
1. Use a dummy head node to simplify edge cases
2. Compare the current nodes of both lists, attach the smaller one
3. When one list is exhausted, attach the rest of the other

---

### 7. Palindrome Linked List — #234 (Easy)

**Problem**: Given the head of a singly linked list, return `true` if it is a palindrome.

```
Input:  1 → 2 → 2 → 1
Output: true

Input:  1 → 2
Output: false

Input:  1 → 2 → 3 → 2 → 1
Output: true
```

**Hints**:
1. Find the middle using slow/fast pointers
2. Reverse the second half of the list
3. Compare the first half with the reversed second half node by node

---

### 8. Reorder List — #143 (Medium)

**Problem**: Given the head of a singly linked list `L0 → L1 → ... → Ln`, reorder it to `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`. Modify in-place.

```
Input:  1 → 2 → 3 → 4
Output: 1 → 4 → 2 → 3

Input:  1 → 2 → 3 → 4 → 5
Output: 1 → 5 → 2 → 4 → 3
```

**Hints**:
1. Find the middle of the list
2. Reverse the second half
3. Merge the two halves by alternating nodes

---

### 9. Add Two Numbers — #2 (Medium)

**Problem**: Two non-empty linked lists represent two non-negative integers stored in reverse order (each node contains a single digit). Add the two numbers and return the sum as a linked list.

```
Input:  l1 = 2 → 4 → 3,  l2 = 5 → 6 → 4
        (represents 342 + 465)
Output: 7 → 0 → 8
        (represents 807)

Input:  l1 = 0,  l2 = 0
Output: 0

Input:  l1 = 9 → 9 → 9 → 9 → 9 → 9 → 9
        l2 = 9 → 9 → 9 → 9
Output: 8 → 9 → 9 → 9 → 0 → 0 → 0 → 1
```

**Hints**:
1. Traverse both lists simultaneously, tracking a carry
2. `digit = (l1.val + l2.val + carry) % 10`, `carry = (sum) // 10`
3. Continue until both lists are exhausted AND carry is 0

---

### 10. Copy List with Random Pointer — #138 (Medium)

**Problem**: A linked list where each node has a `next` and a `random` pointer (which can point to any node or null). Return a deep copy of the list.

```
Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]
        (each pair is [val, random_index])
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        (deep copy — new nodes, same structure)
```

**Hints**:
1. First pass: create a hash map `{original_node → copy_node}`
2. Second pass: set `copy.next` and `copy.random` using the map
3. Alternative O(1) space: interleave copies between originals, then separate

---

### 11. Reverse Nodes in k-Group — #25 (Hard)

**Problem**: Given the head of a linked list, reverse the nodes of the list k at a time and return the modified list. If the number of nodes is not a multiple of k, leave the remaining nodes as-is.

```
Input:  1 → 2 → 3 → 4 → 5,  k = 2
Output: 2 → 1 → 4 → 3 → 5

Input:  1 → 2 → 3 → 4 → 5,  k = 3
Output: 3 → 2 → 1 → 4 → 5

Input:  1 → 2 → 3 → 4 → 5,  k = 1
Output: 1 → 2 → 3 → 4 → 5
```

**Hints**:
1. Check if there are at least k nodes remaining before reversing
2. Reverse k nodes, then recursively handle the rest
3. Connect the reversed group to the result of the recursive call
