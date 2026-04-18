# Dummy Nodes — Do You Actually Need Them?

Short answer: no, you don't need them. But once you understand why they exist,
you'll choose to use them because they make your code simpler, not harder.

---

## What Is a Dummy Node?

A dummy node (also called a sentinel node) is a fake node you create at the
start of your algorithm. It has no meaningful value — it just sits before the
real head of the list.

```
Without dummy:   [1] → [2] → [3] → None
                  ↑
                 head

With dummy:   [0] → [1] → [2] → [3] → None
               ↑     ↑
             dummy   head (real data starts here)
```

You never return the dummy. You return `dummy.next` — the real head.

---

## The Problem Dummy Nodes Solve

The root issue: **the head node is special**.

When you delete, insert, or modify nodes, you need a reference to the node
BEFORE the one you're working on. But the head has no node before it — so
every algorithm needs a special case for it.

### Example: Remove all nodes with value 1

```
Input:  [1] → [1] → [2] → [3] → None,  val=1
Output: [2] → [3] → None
```

**Without dummy — you need a special case for the head:**

```python
def remove_elements_no_dummy(head, val):
    # Special case: skip all leading nodes that match
    while head and head.val == val:
        head = head.next          # ← special case for head

    # Now handle the rest
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

**With dummy — one uniform loop, no special case:**

```python
def remove_elements_with_dummy(head, val):
    dummy = ListNode(0, head)     # dummy sits before head
    curr = dummy                  # start from dummy, not head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next   # same operation every time
        else:
            curr = curr.next
    return dummy.next             # dummy.next is the real head
```

The dummy makes the head just another node. No special case needed.

---

## Side-by-Side: With vs Without Dummy

Let's trace both through the same example to see the difference concretely.

```
Input:  [1] → [1] → [2] → [3],  val=1
```

### Without Dummy

```
Step 1: head=[1], head.val==1 → head = head.next = [1]
Step 2: head=[1], head.val==1 → head = head.next = [2]
Step 3: head=[2], head.val≠1 → stop special case loop

curr=[2]
Step 4: curr.next=[3], curr.next.val≠1 → curr=[3]
Step 5: curr.next=None → stop

return head=[2]  ✓

Two separate loops. Easy to get wrong — what if you forget the first loop?
```

### With Dummy

```
dummy=[0] → [1] → [1] → [2] → [3]
curr=dummy

Step 1: curr.next=[1], val==1 → curr.next = curr.next.next = [1]
        dummy=[0] → [1] → [2] → [3]

Step 2: curr.next=[1], val==1 → curr.next = curr.next.next = [2]
        dummy=[0] → [2] → [3]

Step 3: curr.next=[2], val≠1 → curr=[2]

Step 4: curr.next=[3], val≠1 → curr=[3]

Step 5: curr.next=None → stop

return dummy.next=[2]  ✓

One loop. Same operation every iteration.
```

---

## The Three Cases Where Dummy Nodes Help

### Case 1: Deleting the head

```
Without dummy:
  if head.val == target:
      return head.next    ← special case

With dummy:
  curr = dummy
  while curr.next:
      if curr.next.val == target:
          curr.next = curr.next.next   ← same as any other deletion
```

### Case 2: Inserting before the head

```
Without dummy:
  new_node.next = head
  return new_node         ← must return new head

With dummy:
  new_node.next = dummy.next
  dummy.next = new_node
  return dummy.next       ← always return dummy.next, no special case
```

### Case 3: Building a new list (merge, partition, etc.)

```
Without dummy:
  result_head = None
  if first_node:
      result_head = first_node
      curr = result_head
  # ... then append more nodes

With dummy:
  dummy = ListNode(0)
  curr = dummy
  # ... just keep doing curr.next = new_node; curr = curr.next
  return dummy.next
```

---

## When You DON'T Need a Dummy Node

Dummy nodes are only useful when you might need to modify the head.
If you're just reading or the head is guaranteed to stay, skip it.

```python
# No dummy needed — just reading values
def sum_list(head):
    total = 0
    curr = head
    while curr:
        total += curr.val
        curr = curr.next
    return total

# No dummy needed — head never changes
def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev   # prev is the new head, no dummy needed

# No dummy needed — slow/fast pointer problems
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

---

## Dummy Node Decision Guide

```
Ask yourself: "Could the head node be deleted or replaced?"

YES → use a dummy node
  - Remove elements by value
  - Remove nth from end (if n == length, head gets deleted)
  - Merge two lists (result head is unknown until first comparison)
  - Partition list
  - Any problem where you return a potentially different head

NO → skip the dummy
  - Reverse a list (head changes but you track it with prev)
  - Find middle (just reading)
  - Detect cycle (just reading)
  - Any traversal-only problem
```

---

## The Dummy Node Pattern in Code

Every dummy node usage follows the same template:

```python
def some_operation(head):
    dummy = ListNode(0)   # create dummy
    dummy.next = head     # attach to real list
    curr = dummy          # start traversal from dummy

    while curr.next:      # loop condition uses curr.next, not curr
        # ... do work using curr.next (the real current node)
        curr = curr.next

    return dummy.next     # always return dummy.next
```

The key: `curr` always points to the node BEFORE the one you're examining.
`curr.next` is the node you're actually working with.

---

## Concrete Example: Remove Nth From End

This is a good example because without a dummy, you need a special case
when n equals the length of the list (deleting the head).

```
Input: [1] → [2] → [3] → [4] → [5],  n=5
Output: [2] → [3] → [4] → [5]   (head gets deleted!)
```

### Without Dummy — needs special case

```python
def remove_nth_no_dummy(head, n):
    # Count length
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    # Special case: deleting the head
    if n == length:
        return head.next    ← special case

    # Normal case: find the node before target
    curr = head
    for _ in range(length - n - 1):
        curr = curr.next
    curr.next = curr.next.next
    return head
```

### With Dummy — no special case

```python
def remove_nth_with_dummy(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy

    # Advance fast n+1 steps
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast is None
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete — works even if slow is dummy (deleting head)
    slow.next = slow.next.next
    return dummy.next
```

Trace for n=5 (deleting head):
```
dummy → [1] → [2] → [3] → [4] → [5] → None

Advance fast 6 steps: fast = None (went past the end)

while fast: → skip (fast is already None)

slow = dummy
slow.next = slow.next.next
dummy.next = [2]   ← head deleted ✓

return dummy.next = [2] ✓
```

---

## Summary

| | Without Dummy | With Dummy |
|--|--------------|------------|
| Head deletion | Special case needed | Handled uniformly |
| Head insertion | Must return new head explicitly | Always return dummy.next |
| Code length | Longer (extra if/while) | Shorter |
| Bug surface | More edge cases | Fewer edge cases |
| Conceptual overhead | Lower (no extra node) | Slightly higher initially |
| Recommended for | Simple traversals | Any modification problem |

The dummy node trades one concept (the extra node) for eliminating multiple
special cases. Once you internalize "dummy sits before head, I always return
dummy.next", it actually makes problems easier to think about — not harder.
