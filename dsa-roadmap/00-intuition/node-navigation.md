# Node Navigation Intuition

The core mental block with linked lists, trees, and graphs is the same:
**you're holding a reference to a node, not the node itself.**

Think of a node as a box sitting somewhere in memory. You hold a sticky note
with the box's address. When you do `curr = curr.next`, you're not moving —
you're throwing away your old sticky note and writing a new one with the
address of the next box.

---

## Part 1 — Singly Linked List

### The Mental Model

```
Memory:
  [1 | addr:200] → [2 | addr:300] → [3 | addr:400] → [None]
   ^addr:100         ^addr:200         ^addr:300

head = sticky note saying "100"
curr = sticky note saying "100"  (you start here)

curr.next = sticky note saying "200"  (the next box's address)
```

Every operation is just: **read the address on your sticky note, go to that
box, do something, maybe update your sticky note.**

---

### Pattern 1: Simple Traversal

```
Goal: visit every node once.

[1] → [2] → [3] → None
 ↑
curr

Step 1: visit curr (value=1), then curr = curr.next
[1] → [2] → [3] → None
       ↑
      curr

Step 2: visit curr (value=2), then curr = curr.next
[1] → [2] → [3] → None
              ↑
             curr

Step 3: visit curr (value=3), then curr = curr.next → None
Stop when curr is None.
```

```python
def traverse(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next   # update sticky note to next box
```

**Key insight:** `curr = curr.next` does NOT move the node. It updates which
node you're currently looking at.

---

### Pattern 2: Reversal — The Classic Confusion Point

This is where most people get lost. The trick is you need **3 sticky notes**
because you're about to cut a connection and you can't lose the address of
what comes next.

```
Goal: reverse [1] → [2] → [3] → None
Result:        [3] → [2] → [1] → None

Before starting:
  prev = None   (nothing before the first node yet)
  curr = [1]    (start here)
  nxt  = ???    (will save curr.next before we cut it)
```

**The arrow `→` always means `.next` points to the right-hand node.**
After reversal, `[3].next = [2]`, `[2].next = [1]`, `[1].next = None`.

**Step by step — think of it as redirecting arrows:**

```
INITIAL STATE:
  prev = None
  curr = [1]
  List: [1] → [2] → [3] → None

─────────────────────────────────────────────────────
ITERATION 1  (curr = [1])

  STEP 1: Save nxt BEFORE cutting
    nxt = curr.next
    nxt = [2]

  STEP 2: Redirect curr.next to point at prev (None)
    curr.next = prev
    [1].next is now None
    List so far: None ← [1]   [2] → [3] → None
                              ↑
                             (nxt still holds this address)

  STEP 3: Advance prev to curr
    prev = [1]

  STEP 4: Advance curr to nxt
    curr = [2]

  State after iteration 1:
    prev = [1],  curr = [2]
    Reversed so far: [1] → None
    Remaining:       [2] → [3] → None

─────────────────────────────────────────────────────
ITERATION 2  (curr = [2])

  STEP 1: nxt = curr.next = [3]

  STEP 2: curr.next = prev
    [2].next is now [1]
    [2] → [1] → None

  STEP 3: prev = [2]
  STEP 4: curr = [3]

  State after iteration 2:
    prev = [2],  curr = [3]
    Reversed so far: [2] → [1] → None
    Remaining:       [3] → None

─────────────────────────────────────────────────────
ITERATION 3  (curr = [3])

  STEP 1: nxt = curr.next = None

  STEP 2: curr.next = prev
    [3].next is now [2]
    [3] → [2] → [1] → None

  STEP 3: prev = [3]
  STEP 4: curr = None  ← loop ends here

─────────────────────────────────────────────────────
RESULT:
  curr = None → loop exits
  prev = [3]  → this is the new head

  [3] → [2] → [1] → None  ✓
```

**Why the arrows look "backward" during the process:**

```
During iteration 1, after step 2:
  [1].next = None   (we just cut [1]'s connection to [2])
  nxt still points to [2]

So at that moment you have TWO separate chains:
  Chain A (reversed so far): [1] → None
  Chain B (not yet reversed): [2] → [3] → None

prev tracks the head of Chain A.
curr/nxt tracks the head of Chain B.
Each iteration moves one node from Chain B to the front of Chain A.
```

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next    # 1. save next (don't lose it!)
        curr.next = prev   # 2. redirect arrow backward
        prev = curr        # 3. advance prev
        curr = nxt         # 4. advance curr
    return prev            # prev is the new head
```

**The order matters:** always save `nxt` FIRST before you cut `curr.next`.
If you do `curr.next = prev` first, you've lost the address of the next node.

---

### Pattern 3: Slow/Fast Pointers

Two sticky notes moving at different speeds. Used for: finding middle,
detecting cycles, finding nth from end.

```
Find middle of [1]→[2]→[3]→[4]→[5]

slow moves 1 step, fast moves 2 steps.
When fast reaches the end, slow is at the middle.

Start:
  slow=[1], fast=[1]

Step 1:
  slow=[2], fast=[3]

Step 2:
  slow=[3], fast=[5]

Step 3:
  fast.next=None → stop. slow=[3] is the middle. ✓
```

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Why it works:** fast covers 2x the distance. When fast has traveled n steps,
slow has traveled n/2 steps — exactly the middle.

---

### Pattern 4: Dummy Head Node

When you need to insert/delete at the beginning, a dummy node eliminates
special cases.

```
Without dummy: deleting head requires special case
  if head.val == target: return head.next  ← special case

With dummy:
  dummy → [1] → [2] → [3] → None
  prev = dummy
  
  Now deletion is always: prev.next = prev.next.next
  No special case needed. Return dummy.next as the new head.
```

```python
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head
    while curr:
        if curr.val == val:
            prev.next = curr.next   # skip curr
        else:
            prev = curr             # advance prev only when not deleting
        curr = curr.next
    return dummy.next
```

---

## Part 2 — Doubly Linked List

Each node has TWO sticky notes: `prev` and `next`.

```
None ← [1] ⇄ [2] ⇄ [3] → None
        ↑prev  ↑next
```

### Insertion (after a given node)

```
Insert [NEW] after [2] in: [1] ⇄ [2] ⇄ [3]

Before:
  [2].next = [3]
  [3].prev = [2]

Step 1: Set NEW's pointers first (point into existing structure)
  new.prev = node        →  new.prev = [2]
  new.next = node.next   →  new.next = [3]

Step 2: Update neighbors to point to NEW
  node.next.prev = new   →  [3].prev = new
  node.next = new        →  [2].next = new

After: [1] ⇄ [2] ⇄ [NEW] ⇄ [3]
```

**Critical order:** Set the new node's pointers BEFORE updating neighbors.
If you do `node.next = new` first, you lose the reference to `[3]`.

```python
def insert_after(node, new_node):
    new_node.prev = node
    new_node.next = node.next
    if node.next:
        node.next.prev = new_node   # must do this BEFORE node.next = new_node
    node.next = new_node
```

### Deletion (of a given node)

```
Delete [2] from: [1] ⇄ [2] ⇄ [3]

Just bridge the gap — make [1] and [3] point to each other:
  node.prev.next = node.next   →  [1].next = [3]
  node.next.prev = node.prev   →  [3].prev = [1]

After: [1] ⇄ [3]
```

```python
def delete_node(node):
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev
```

**Why DLL deletion is O(1):** You have the node reference directly. No need
to traverse from the head to find the predecessor — `node.prev` gives it
instantly.

---

## Part 3 — Binary Trees

A tree node has two sticky notes: `left` and `right`. The key mental shift:
**recursion is just the function calling itself with a different sticky note.**

### The Call Stack Mental Model

```
Tree:
        1
       / \
      2   3
     / \
    4   5

inorder(1) calls:
  inorder(2) calls:
    inorder(4) calls:
      inorder(None) → return   ← base case
    print(4)
    inorder(None) → return
  print(2)
  inorder(5) calls:
    inorder(None) → return
    print(5)
    inorder(None) → return
print(1)
inorder(3) calls:
  ...
```

Think of each recursive call as "going deeper into the tree." The call stack
IS the path from root to current node.

### Pattern 1: DFS Traversals

```python
def inorder(node):       # Left → Root → Right
    if not node:
        return
    inorder(node.left)   # go left first
    print(node.val)      # visit root
    inorder(node.right)  # go right

def preorder(node):      # Root → Left → Right
    if not node:
        return
    print(node.val)      # visit root first
    preorder(node.left)
    preorder(node.right)

def postorder(node):     # Left → Right → Root
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)      # visit root last
```

**Intuition for when to use each:**
- Preorder: serialize a tree, copy a tree (process node before children)
- Inorder: get sorted values from BST (left < root < right)
- Postorder: delete a tree, compute subtree properties (need children first)

---

### Pattern 2: Return Values Up the Tree

This is the key to most tree problems. Each recursive call returns something
useful to its parent.

```
Problem: find height of tree

height(node):
  if node is None: return 0
  left_h  = height(node.left)   ← get height of left subtree
  right_h = height(node.right)  ← get height of right subtree
  return 1 + max(left_h, right_h)  ← return to parent

For tree:
        1
       / \
      2   3
     /
    4

height(4) = 1 + max(0,0) = 1
height(2) = 1 + max(1,0) = 2
height(3) = 1 + max(0,0) = 1
height(1) = 1 + max(2,1) = 3
```

```python
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
```

---

### Pattern 3: Global Variable for Cross-Subtree Problems

Some problems need information from BOTH subtrees at once (like diameter,
max path sum). Use a nonlocal variable to track the global answer.

```
Problem: diameter = longest path between any two nodes

For each node, the diameter THROUGH it = depth(left) + depth(right)

        1
       / \
      2   3
     / \
    4   5

At node 2: depth(left=4)=1, depth(right=5)=1 → diameter through 2 = 2
At node 1: depth(left=2)=2, depth(right=3)=1 → diameter through 1 = 3

Answer = max across all nodes = 3
```

```python
def diameter(root):
    best = [0]  # use list to allow mutation in nested function

    def depth(node):
        if not node:
            return 0
        left  = depth(node.left)
        right = depth(node.right)
        best[0] = max(best[0], left + right)  # update global answer
        return 1 + max(left, right)           # return depth to parent

    depth(root)
    return best[0]
```

**Why `best = [0]` instead of a variable?** Python closures can read outer
variables but can't reassign them without `nonlocal`. Using a list sidesteps
this. Alternatively: `nonlocal best`.

---

### Pattern 4: Passing State Down the Tree

Sometimes you need to pass information FROM parent TO children (top-down).

```
Problem: path sum — does any root-to-leaf path sum to target?

Pass the REMAINING sum down. At a leaf, check if remaining == leaf.val.

pathSum(node, remaining):
  if not node: return False
  remaining -= node.val
  if not node.left and not node.right:  ← leaf
    return remaining == 0
  return pathSum(node.left, remaining) or pathSum(node.right, remaining)
```

```python
def has_path_sum(root, target):
    if not root:
        return False
    target -= root.val
    if not root.left and not root.right:
        return target == 0
    return has_path_sum(root.left, target) or has_path_sum(root.right, target)
```

---

## Part 4 — Graphs

A graph node has a list of neighbors instead of just left/right. The key
challenge: **you can visit the same node multiple times** (cycles), so you
need a `visited` set.

### The Mental Model

```
Graph:
  0 — 1 — 3
  |   |
  2 — 4

Adjacency list:
  0: [1, 2]
  1: [0, 3, 4]
  2: [0, 4]
  3: [1]
  4: [1, 2]
```

### Pattern 1: DFS (Depth First)

Go as deep as possible before backtracking. Uses a stack (or recursion).

```
DFS from 0:

Visit 0. Mark visited. Explore neighbors [1, 2].
  Visit 1. Mark visited. Explore neighbors [0, 3, 4].
    0 already visited → skip.
    Visit 3. Mark visited. Explore neighbors [1].
      1 already visited → skip.
    Backtrack to 1.
    Visit 4. Mark visited. Explore neighbors [1, 2].
      1 already visited → skip.
      Visit 2. Mark visited. Explore neighbors [0, 4].
        0 already visited → skip.
        4 already visited → skip.
      Backtrack to 4.
    Backtrack to 1.
  Backtrack to 0.
  2 already visited → skip.

Order: 0, 1, 3, 4, 2
```

```python
def dfs(graph, start):
    visited = set()
    result = []

    def explore(node):
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor)

    explore(start)
    return result
```

**Iterative DFS (same idea, explicit stack):**

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return result
```

---

### Pattern 2: BFS (Breadth First)

Visit all neighbors before going deeper. Uses a queue. Gives shortest path
in unweighted graphs.

```
BFS from 0:

Queue: [0]. Visited: {0}
Process 0 → add neighbors [1,2]. Queue: [1,2]. Visited: {0,1,2}
Process 1 → add unvisited neighbors [3,4]. Queue: [2,3,4]. Visited: {0,1,2,3,4}
Process 2 → neighbors [0,4] already visited. Queue: [3,4]
Process 3 → neighbor [1] already visited. Queue: [4]
Process 4 → neighbors [1,2] already visited. Queue: []

Order: 0, 1, 2, 3, 4  (level by level)
```

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result
```

**Key difference from DFS:** Add to `visited` when you ENQUEUE (not when you
dequeue). This prevents the same node from being added to the queue multiple
times.

---

### Pattern 3: Grid as Graph

Many problems give you a 2D grid. Each cell is a node; neighbors are the 4
adjacent cells. No explicit adjacency list needed.

```
Grid:
  1 1 0
  1 0 0
  0 0 1

Treat each (row, col) as a node.
Neighbors of (r,c): (r-1,c), (r+1,c), (r,c-1), (r,c+1)
```

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '0'   # mark visited by overwriting (no extra set needed)
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

---

## Part 5 — The Universal Navigation Checklist

Before writing any traversal code, answer these 4 questions:

```
1. WHAT AM I HOLDING?
   - Linked list: curr (one node)
   - Tree: node (one node, two children)
   - Graph: node + visited set

2. WHAT IS MY STOPPING CONDITION?
   - Linked list: curr is None
   - Tree: node is None (base case)
   - Graph: all neighbors visited

3. WHAT DO I DO AT EACH STEP?
   - Process current node (read/write value)
   - Update pointers / recurse into children

4. WHAT DO I NEED TO SAVE BEFORE MOVING?
   - Linked list reversal: save nxt before cutting curr.next
   - DLL insertion: set new node's pointers before updating neighbors
   - Tree: nothing (recursion handles it via call stack)
   - Graph: add to visited before exploring neighbors
```

---

## Part 6 — Side-by-Side Comparison

```
OPERATION        LINKED LIST          TREE                GRAPH
─────────────────────────────────────────────────────────────────
Traverse         curr = curr.next     recurse left/right  BFS/DFS + visited
Visit order      linear               pre/in/post order   BFS=level, DFS=deep
"Go back"        need prev pointer    return value up     backtrack in DFS
Avoid revisit    N/A (no cycles)      N/A (no cycles)     visited set
State passing    variables outside    return values up    visited set + params
                 loop                 or nonlocal var
```

---

## Part 7 — Common Bugs and How to Avoid Them

```
BUG 1: Losing a reference before saving it
  WRONG:  curr.next = prev    ← you just lost curr.next!
          nxt = curr.next     ← nxt is now prev, not the original next
  RIGHT:  nxt = curr.next     ← save first
          curr.next = prev    ← then cut

BUG 2: Off-by-one in slow/fast pointers
  WRONG:  while fast.next:    ← fast might be None, causes AttributeError
  RIGHT:  while fast and fast.next:

BUG 3: Forgetting to mark visited in graph BFS
  WRONG:  queue.append(neighbor)   ← same node added multiple times
  RIGHT:  visited.add(neighbor)
          queue.append(neighbor)   ← mark BEFORE enqueuing

BUG 4: Modifying a node's pointer before using it
  WRONG (DLL insert):
    node.next = new_node          ← lost reference to old node.next!
    new_node.next = node.next     ← this is now new_node, not old next
  RIGHT:
    new_node.next = node.next     ← save old next first
    node.next = new_node

BUG 5: Returning wrong value from tree recursion
  WRONG:  return height(node.left)   ← ignores right subtree
  RIGHT:  return 1 + max(height(node.left), height(node.right))
```
