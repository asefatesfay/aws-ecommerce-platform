# Slow & Fast Pointers — Complete Guide

The slow/fast pointer pattern (also called Floyd's Tortoise and Hare) uses
two pointers moving at different speeds through a sequence. The speed ratio
creates useful mathematical relationships.

---

## The Core Idea

```
slow moves 1 step at a time
fast moves 2 steps at a time

After k iterations:
  slow is at position k
  fast is at position 2k

This 2:1 ratio is what makes all the problems below work.
```

---

## Even-Length List — Which Middle?

Before anything else, let's settle the even-length question.

```
List: [1] → [2] → [3] → [4]
       0      1      2      3   (0-indexed positions)

There is no single middle. You get to choose which one you want
by picking the right loop condition.
```

### Variant A — Second Middle (position n/2, 0-indexed)

```
while fast and fast.next:

Start: slow=[1], fast=[1]

Step 1: slow=[2], fast=[3]
        Check: fast=[3] ✓, fast.next=[4] ✓ → continue

Step 2: slow=[3], fast=None
        (fast was [3], fast.next=[4], fast.next.next=None → fast becomes None)
        Check: fast=None → STOP

slow = [3]  ← second middle
```

### Variant B — First Middle (position (n-1)/2, 0-indexed)

```
while fast.next and fast.next.next:

Start: slow=[1], fast=[1]

Step 1: fast.next=[2] ✓, fast.next.next=[3] ✓ → continue
        slow=[2], fast=[3]

Step 2: fast.next=[4] ✓, fast.next.next=None → STOP

slow = [2]  ← first middle
```

### Summary Table

```
List: [1, 2, 3, 4]

Condition                    | slow stops at | Use when
─────────────────────────────────────────────────────────────────
while fast and fast.next     | [3] (2nd mid) | LeetCode #876, cycle detection
while fast.next and          | [2] (1st mid) | Palindrome check, reorder list
  fast.next.next             |               | (need to split list in half)
```

```
List: [1, 2, 3, 4, 5]  (odd — both variants give the same result)

Condition                    | slow stops at
─────────────────────────────────────────────
while fast and fast.next     | [3]
while fast.next and          | [3]
  fast.next.next             |
```

---

## Problem 1 — Find Middle of Linked List #876 (Easy)

```
Input:  [1] → [2] → [3] → [4] → [5]
Output: node [3]

Input:  [1] → [2] → [3] → [4]
Output: node [3]  (second middle)
```

### Brute Force

```python
def find_middle_brute(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    return nodes[len(nodes) // 2]
# O(n) time, O(n) space — stores all nodes
```

### Optimal — Slow/Fast

```
[1] → [2] → [3] → [4] → [5]

     slow  fast
Step 0: [1]   [1]
Step 1: [2]   [3]
Step 2: [3]   [5]   fast.next=None → stop

slow = [3] ✓

[1] → [2] → [3] → [4]

     slow  fast
Step 0: [1]   [1]
Step 1: [2]   [3]
Step 2: [3]   None  fast.next=[4], fast.next.next=None → fast=None → stop

slow = [3] ✓ (second middle)
```

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

| | Time | Space |
|--|------|-------|
| Brute force | O(n) | O(n) |
| Slow/fast | O(n) | O(1) |

---

## Problem 2 — Linked List Cycle #141 (Easy)

```
Input:  [3] → [2] → [0] → [-4] → (back to [2])
Output: True

Input:  [1] → [2] → None
Output: False
```

### Brute Force — Hash Set

```python
def has_cycle_brute(head):
    seen = set()
    curr = head
    while curr:
        if id(curr) in seen:
            return True
        seen.add(id(curr))
        curr = curr.next
    return False
# O(n) time, O(n) space
```

### Optimal — Floyd's Detection

```
Intuition: if there's a cycle, fast will eventually lap slow.
Think of two runners on a circular track — the faster one always catches up.

No cycle: fast reaches None → return False
Cycle:    fast laps slow → they meet → return True

[3] → [2] → [0] → [-4]
              ↑_________↓  (cycle: -4 points back to 0)

     slow  fast
Step 0: [3]   [3]
Step 1: [2]   [0]
Step 2: [0]   [2]   (fast: -4 → 0 → 2... wait let me retrace)

Let me index: 3=A, 2=B, 0=C, -4=D, cycle back to B

     slow  fast
Step 0: A    A
Step 1: B    C     (slow: A→B, fast: A→B→C)
Step 2: C    B     (slow: B→C, fast: C→D→B)
Step 3: D    D     (slow: C→D, fast: B→C→D)
slow == fast → CYCLE DETECTED ✓
```

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

| | Time | Space |
|--|------|-------|
| Hash set | O(n) | O(n) |
| Floyd's | O(n) | O(1) |

---

## Problem 3 — Find Cycle Entry Point #142 (Medium)

```
Input:  [3] → [2] → [0] → [-4] → (back to [2])
Output: node [2]  (where the cycle begins)
```

### Why Phase 2 Works (the math)

```
Let:
  F = distance from head to cycle entry
  C = cycle length
  k = distance from entry to meeting point (inside cycle)

When slow and fast meet:
  slow traveled:  F + k
  fast traveled:  F + k + C  (fast did one extra full loop)

Since fast = 2 × slow:
  F + k + C = 2(F + k)
  C = F + k
  F = C - k

So: distance from head to entry (F)
  = distance from meeting point to entry going forward (C - k)

Reset slow to head. Keep fast at meeting point.
Both move 1 step at a time.
They meet exactly at the cycle entry. ✓
```

```
Visual with F=1, C=4, k=1:

head → [A] → [B] → [C] → [D]
                ↑_____________↓
              entry

Phase 1: slow and fast meet at [C] (k=1 step past entry [B])

Phase 2:
  slow starts at head [A]
  fast stays at [C]

  Step 1: slow=[B], fast=[D]
  Step 2: slow=[B]? No...

Let me use the actual example:
  head=[3], entry=[2], cycle=[2]→[0]→[-4]→[2]
  F=1 (head to entry: 3→2)
  C=3 (cycle length: 2→0→-4→2)
  k=2 (meeting point is 2 steps past entry)

  Phase 1 meeting point: [-4]

  Phase 2:
    slow=[3] (head), fast=[-4]
    Step 1: slow=[2], fast=[2]  ← MEET at entry ✓
```

```python
def detect_cycle(head):
    slow = fast = head

    # Phase 1: find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # no cycle

    # Phase 2: find entry
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

| | Time | Space |
|--|------|-------|
| Hash set | O(n) | O(n) |
| Floyd's two-phase | O(n) | O(1) |

---

## Problem 4 — Palindrome Linked List #234 (Easy)

```
Input:  [1] → [2] → [2] → [1]
Output: True

Input:  [1] → [2] → [3] → [2] → [1]
Output: True

Input:  [1] → [2]
Output: False
```

### Brute Force — Collect Values

```python
def is_palindrome_brute(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    return vals == vals[::-1]
# O(n) time, O(n) space
```

### Optimal — Find Middle + Reverse Second Half

```
This combines slow/fast (find middle) with reversal.

Step 1: Find the first middle using while fast.next and fast.next.next
        (we want first middle so second half starts right after it)

Step 2: Reverse the second half

Step 3: Compare first half with reversed second half

[1] → [2] → [2] → [1]

Step 1: Find first middle
  slow  fast
  [1]   [1]
  [2]   [3]? No, list is [1]→[2]→[2]→[1]

  slow  fast
  [1]   [1]
  Step: fast.next=[2] ✓, fast.next.next=[2] ✓ → move
  [2]   [2(3rd)]
  Step: fast.next=[1] ✓, fast.next.next=None → STOP
  slow = [2] (first middle, index 1)

Step 2: Reverse from slow.next = [2] → [1]
  Reversed: [1] → [2]

Step 3: Compare
  First half:          [1] → [2] → ...
  Reversed second half:[1] → [2] → ...
  Match ✓ → palindrome

[1] → [2] → [3] → [2] → [1]

Step 1: Find first middle
  slow  fast
  [1]   [1]
  [2]   [3]   (fast.next=[2], fast.next.next=[1] ✓ → move)
  [3]   [1]   (fast.next=None → STOP)
  slow = [3] (true middle for odd list)

Step 2: Reverse from slow.next = [2] → [1]
  Reversed: [1] → [2]

Step 3: Compare
  First half:          [1] → [2] → [3]
  Reversed second half:[1] → [2]
  Compare until second half exhausted: 1==1 ✓, 2==2 ✓ → palindrome ✓
```

```python
def is_palindrome(head):
    # Step 1: find first middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    prev, curr = None, slow.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # prev = head of reversed second half

    # Step 3: compare
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

| | Time | Space |
|--|------|-------|
| Collect values | O(n) | O(n) |
| Find middle + reverse | O(n) | O(1) |

---

## Problem 5 — Remove Nth Node From End #19 (Medium)

```
Input:  [1] → [2] → [3] → [4] → [5],  n=2
Output: [1] → [2] → [3] → [5]
```

This uses a **gap** variant: fast is n steps ahead of slow.
When fast reaches None, slow is just before the target.

### Brute Force — Two Passes

```python
def remove_nth_brute(head, n):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    dummy = ListNode(0, head)
    curr = dummy
    for _ in range(length - n):
        curr = curr.next
    curr.next = curr.next.next
    return dummy.next
```

### Optimal — Gap Pointer

```
Advance fast n+1 steps ahead of slow (starting from dummy).
When fast=None, slow is just before the nth-from-end node.

[dummy] → [1] → [2] → [3] → [4] → [5] → None,  n=2

Step 1: Advance fast n+1=3 steps from dummy
  fast: dummy → [1] → [2] → [3]

  slow=[dummy], fast=[3]
  Gap = 3 nodes between them

Step 2: Move both until fast=None
  slow=[1], fast=[4]
  slow=[2], fast=[5]
  slow=[3], fast=None → STOP

  slow=[3] is just before [4] (the 2nd from end)

Step 3: slow.next = slow.next.next
  [3].next = [5]
  Result: [1] → [2] → [3] → [5] ✓
```

```
Why n+1 steps (not n)?
  We want slow to stop BEFORE the target, not AT the target.
  If we advance n steps, slow stops AT the target (can't delete it without prev).
  If we advance n+1 steps, slow stops one node before the target.
```

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy

    # Advance fast n+1 steps
    for _ in range(n + 1):
        fast = fast.next

    # Move both until fast is None
    while fast:
        slow = slow.next
        fast = fast.next

    # Delete the target
    slow.next = slow.next.next
    return dummy.next
```

| | Time | Space |
|--|------|-------|
| Two passes | O(n) | O(1) |
| Gap pointer | O(n) | O(1) |

---

## Problem 6 — Happy Number #202 (Easy) — Slow/Fast on Numbers

```
Input:  n=19
Output: True

19 → 1²+9² = 82
82 → 8²+2² = 68
68 → 6²+8² = 100
100 → 1²+0²+0² = 1  ← reached 1, it's happy!

Input:  n=2
Output: False  (enters a cycle that never reaches 1)
```

This is slow/fast applied to a **number sequence**, not a linked list.
The sequence either reaches 1 (happy) or enters a cycle (not happy).

### Brute Force — Hash Set

```python
def is_happy_brute(n):
    def next_num(x):
        return sum(int(d)**2 for d in str(x))

    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = next_num(n)
    return True
# O(log n) per step, O(log n) space for the set
```

### Optimal — Slow/Fast on the Sequence

```
Treat the sequence as a linked list where each "node" is a number
and "next" is the sum-of-squares function.

If the sequence cycles, fast will lap slow (just like cycle detection).
If it reaches 1, fast gets there first.

n=4 (not happy):
  Sequence: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...
                                                           ↑ cycle!

  slow  fast
  4     4
  16    37    (slow: 4→16, fast: 4→16→37)
  37    89    (slow: 16→37, fast: 37→58→89)
  58    42    (slow: 37→58, fast: 89→145→42)
  89    4     (slow: 58→89, fast: 42→20→4)
  145   37    (slow: 89→145, fast: 4→16→37)
  42    89    (slow: 145→42, fast: 37→58→89)
  20    42    (slow: 42→20, fast: 89→145→42)
  4     4     ← slow == fast → CYCLE → not happy
```

```python
def is_happy(n):
    def next_num(x):
        total = 0
        while x:
            x, digit = divmod(x, 10)
            total += digit * digit
        return total

    slow = n
    fast = next_num(n)

    while fast != 1 and slow != fast:
        slow = next_num(slow)
        fast = next_num(next_num(fast))

    return fast == 1
```

| | Time | Space |
|--|------|-------|
| Hash set | O(log n) | O(log n) |
| Slow/fast | O(log n) | O(1) |

---

## Problem 7 — Find Duplicate Number #287 (Medium)

```
Input:  [1, 3, 4, 2, 2]
Output: 2

Input:  [3, 1, 3, 4, 2]
Output: 3

Constraints: n+1 integers, each in [1,n], exactly one duplicate.
Must use O(1) space and not modify the array.
```

### Brute Force — Sort or Set

```python
def find_duplicate_brute(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
# O(n) time, O(n) space — violates O(1) space constraint
```

### Optimal — Treat Array as Linked List

```
Key insight: treat each value as a "next pointer".
  index 0 → nums[0] → nums[nums[0]] → ...

This creates a linked list where the duplicate value creates a cycle
(two indices point to the same next value = two nodes with the same "next").

[1, 3, 4, 2, 2]
 0  1  2  3  4

"Linked list":
  0 → nums[0]=1 → nums[1]=3 → nums[3]=2 → nums[2]=4 → nums[4]=2 → nums[2]=4 → ...
                                            ↑_________________________________↑
                                            cycle! entry = 2

Phase 1: Find meeting point (Floyd's cycle detection)
  slow = nums[0] = 1
  fast = nums[nums[0]] = nums[1] = 3

  slow  fast
  1     3
  3     2     (slow: nums[1]=3, fast: nums[nums[3]]=nums[2]=4... wait)

Let me retrace carefully:
  slow = nums[slow]
  fast = nums[nums[fast]]

  Start: slow=0, fast=0 (start at index 0)

  Step 1: slow=nums[0]=1, fast=nums[nums[0]]=nums[1]=3
  Step 2: slow=nums[1]=3, fast=nums[nums[3]]=nums[2]=4
  Step 3: slow=nums[3]=2, fast=nums[nums[4]]=nums[2]=4
  Step 4: slow=nums[2]=4, fast=nums[nums[4]]=nums[2]=4
  slow==fast=4 → meeting point

Phase 2: Find cycle entry (= duplicate)
  Reset slow=0, keep fast=4

  Step 1: slow=nums[0]=1, fast=nums[4]=2
  Step 2: slow=nums[1]=3, fast=nums[2]=4
  Step 3: slow=nums[3]=2, fast=nums[4]=2
  slow==fast=2 → duplicate is 2 ✓
```

```python
def find_duplicate(nums):
    # Phase 1: find meeting point
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find cycle entry = duplicate
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```

| | Time | Space |
|--|------|-------|
| Hash set | O(n) | O(n) |
| Floyd's on array | O(n) | O(1) |

---

## Summary — When to Use Which Variant

```
PROBLEM TYPE                    VARIANT                 CONDITION
────────────────────────────────────────────────────────────────────────
Find middle (2nd middle)        slow+1, fast+2          while fast and fast.next
Find middle (1st middle)        slow+1, fast+2          while fast.next and fast.next.next
Detect cycle                    slow+1, fast+2          while fast and fast.next
Find cycle entry                Phase 1 + Phase 2       same as detect cycle
Remove nth from end             gap of n+1              advance fast n+1 first
Palindrome check                1st middle + reverse    while fast.next and fast.next.next
Happy number / number cycle     slow+1, fast+2          while fast != 1 and slow != fast
Find duplicate (array as list)  slow+1, fast+2          same as cycle detection
```

```
SPEED RATIO CHEAT SHEET:

slow moves 1 step → position after k steps: k
fast moves 2 steps → position after k steps: 2k

When fast laps slow in a cycle of length C:
  2k - k = C  →  k = C
  They meet after C steps (one full cycle for slow)

When fast is n steps ahead:
  fast reaches end when slow is n steps from end
  → slow is at the (length - n)th node
```
