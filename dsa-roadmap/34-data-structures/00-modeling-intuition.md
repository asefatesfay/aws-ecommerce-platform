# How to Model Problems to Data Structures

The reason you freeze when you see a problem is not that you don't know the
data structures — it's that you don't have a reliable process for connecting
problem words to data structure choices. This file gives you that process.

---

## The Core Framework: Ask 3 Questions

When you read a problem, don't think about data structures yet. Instead ask:

```
1. WHAT do I need to store?
   → values, pairs, counts, relationships, states

2. WHAT operations do I need to do repeatedly?
   → lookup, insert, delete, get-min, get-max, ordering, grouping

3. WHAT is the performance constraint?
   → O(1) lookup? O(log n) insert? O(n) is fine?
```

The answers to these three questions narrow you down to 1-2 data structures
every time. Let's build the mapping.

---

## The Decision Tree

```
What operation do I need?
│
├── "I need O(1) lookup by key"
│   └── Hash Map (dict)
│
├── "I need to process things in order they arrived"
│   └── Queue (deque)
│
├── "I need to undo / go back / match nested things"
│   └── Stack (list)
│
├── "I need the min or max at all times"
│   └── Heap (heapq)
│
├── "I need sorted order with fast insert/delete"
│   └── BST / SortedList
│
├── "I need to check if a prefix exists"
│   └── Trie
│
├── "I need to model relationships / connections"
│   └── Graph (adjacency list)
│
├── "I need hierarchical parent-child structure"
│   └── Tree
│
└── "I need to group things / check connectivity"
    └── Union-Find
```

---

## Trigger Words → Data Structure

This is the muscle memory part. Train yourself to hear these words in a
problem statement and immediately think of the corresponding structure.

### Hash Map (dict)

```
Trigger words:
  "count", "frequency", "how many times"
  "find pair that sums to"
  "group by", "anagram"
  "have we seen this before"
  "O(1) lookup"
  "two sum", "subarray sum"
  "mapping", "translate"

You need a hash map when:
  → You need to look something up by a key in O(1)
  → You need to count occurrences
  → You need to remember if you've seen something before
```

**Example — the moment you should think "hash map":**

```
"Given an array, find two numbers that add up to target"
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  I need to check: "have I seen target - current_number before?"
  That's a lookup → hash map.

"Group anagrams together"
 ^^^^^
  I need to group strings by some key → hash map where key = sorted(word)

"Count the frequency of each character"
 ^^^^^     ^^^^^^^^^
  Counting = hash map.
```

---

### Stack

```
Trigger words:
  "matching parentheses", "valid brackets"
  "undo", "back"
  "most recent", "last seen"
  "next greater element"
  "nested", "recursive structure"
  "evaluate expression"
  "monotonic" (increasing/decreasing order)

You need a stack when:
  → You process things and need to "go back" to the most recent one
  → You need to match opening/closing pairs
  → You need to maintain a monotonic order
```

**Example — the moment you should think "stack":**

```
"Given a string of brackets, check if they're valid"
                  ^^^^^^^^
  Opening bracket → push. Closing bracket → pop and check match.
  That's LIFO → stack.

"For each element, find the next greater element to its right"
                        ^^^^^^^^^^^^
  I'm looking for "the next thing that breaks the current pattern"
  → monotonic stack.

"Evaluate: 3 + (2 * (4 - 1))"
                ^^^^^^^^^^^^
  Nested expressions → stack to handle inner expressions first.
```

---

### Queue

```
Trigger words:
  "BFS", "level by level", "shortest path" (unweighted)
  "first come first served", "process in order"
  "sliding window" (deque variant)
  "schedule", "task order"
  "spread", "infection", "rotting"

You need a queue when:
  → You process things in the order they arrived (FIFO)
  → You explore a graph/tree level by level
  → You need shortest path in an unweighted graph
```

**Example — the moment you should think "queue":**

```
"Find the shortest path from start to end"
      ^^^^^^^^
  Shortest path in unweighted graph → BFS → queue.

"Rotten oranges spread to adjacent fresh oranges each minute"
                ^^^^^^
  Spreading level by level → multi-source BFS → queue.

"Print the tree level by level"
                 ^^^^^^^^^^^^^
  Level order traversal → BFS → queue.
```

---

### Heap (Priority Queue)

```
Trigger words:
  "kth largest", "kth smallest", "top k"
  "always need the minimum/maximum"
  "merge k sorted"
  "median of a stream"
  "schedule by priority"
  "Dijkstra", "shortest path" (weighted)
  "greedy with priority"

You need a heap when:
  → You repeatedly need the min or max element
  → You need the kth largest/smallest
  → You're merging multiple sorted sequences
```

**Example — the moment you should think "heap":**

```
"Find the kth largest element"
          ^^^^^^^^^^^
  I need to efficiently track the top k elements.
  Min-heap of size k: push everything, pop when size > k.
  heap[0] is always the kth largest.

"Merge k sorted linked lists"
 ^^^^^^^^^^^^^
  I need the minimum across k lists at each step.
  Min-heap of (value, list_index) → always gives me the global minimum.

"Find the median of a stream of numbers"
      ^^^^^^
  Median = middle element. I need quick access to the middle.
  Two heaps: max-heap for lower half, min-heap for upper half.
```

---

### Tree (Binary Tree / BST)

```
Trigger words:
  "hierarchical", "parent-child"
  "sorted order" (BST)
  "lowest common ancestor"
  "depth", "height", "level"
  "serialize", "flatten"
  "subtree", "path from root to leaf"

You need a tree when:
  → The data has a natural parent-child hierarchy
  → You need sorted data with O(log n) operations (BST)
  → The problem gives you a tree and asks about paths/depths/subtrees
```

**Example — the moment you should think "tree":**

```
"Find the lowest common ancestor of two nodes"
      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  This is literally a tree problem. DFS, check if p and q are in
  different subtrees.

"Given a sorted array, build a balanced BST"
       ^^^^^^^^^^^^
  Sorted + balanced → pick middle as root, recurse on halves.
```

---

### Trie (Prefix Tree)

```
Trigger words:
  "prefix", "starts with"
  "autocomplete", "search suggestions"
  "word dictionary", "spell check"
  "longest common prefix"
  "word search in a grid" (trie + DFS)

You need a trie when:
  → You need to check if a prefix exists among many strings
  → You need autocomplete functionality
  → You're searching for multiple words simultaneously
```

**Example — the moment you should think "trie":**

```
"Design a system that returns suggestions as the user types"
                                              ^^^^^^^^^^^^
  Prefix-based lookup → trie. Walk the trie as each character is typed.

"Given a list of words and a board, find all words that can be formed"
                                    ^^^^^^^^^^^^^
  Searching for multiple words at once → build a trie from the word list,
  DFS on the board while walking the trie.
```

---

### Graph

```
Trigger words:
  "connected", "reachable", "path between"
  "network", "friends", "followers"
  "dependencies", "prerequisites"
  "grid" (implicit graph)
  "islands", "regions", "components"
  "topological order", "course schedule"
  "shortest path", "cheapest route"

You need a graph when:
  → Things are connected to other things (relationships)
  → You need to find paths, components, or ordering
  → The problem gives you a grid (each cell = node, neighbors = edges)
```

**Example — the moment you should think "graph":**

```
"There are n courses with prerequisites. Can you finish all courses?"
                       ^^^^^^^^^^^^^
  Dependencies between items → directed graph → cycle detection or
  topological sort.

"Count the number of islands in a grid"
                    ^^^^^^^     ^^^^
  Grid + connected regions → graph → DFS/BFS flood fill.

"Find the cheapest flight with at most k stops"
      ^^^^^^^^^^^^^^^^^^
  Weighted graph + shortest path → Dijkstra or Bellman-Ford.
```

---

### Union-Find (Disjoint Set)

```
Trigger words:
  "connected components", "groups"
  "are these two in the same group?"
  "merge", "union"
  "redundant connection"
  "minimum spanning tree"
  "dynamic connectivity"

You need union-find when:
  → You're grouping elements and need to check/merge groups efficiently
  → You need to count connected components
  → You're building a minimum spanning tree (Kruskal's)
```

**Example — the moment you should think "union-find":**

```
"Given n cities and roads, how many provinces (connected groups) are there?"
                                              ^^^^^^^^^^^^^^^^
  Counting connected components → union-find.
  For each road, union the two cities. Answer = number of distinct roots.

"Find the redundant edge that creates a cycle in a tree"
      ^^^^^^^^^^^^^^^
  Process edges one by one. If two nodes are already connected (same root),
  this edge is redundant.
```

---

## Core Implementations — Build It, Then Use It

For each data structure: a real-world analogy, ASCII visual, the minimal
Python implementation, and a worked problem showing how it's used.

---

### Stack — Implementation

```
Real-world analogy: a stack of plates in a cafeteria.
You can only add or remove from the TOP.
The last plate you put on is the first one you take off.
That's LIFO — Last In, First Out.

Visual:
  push(1), push(2), push(3):

     [3]  ← top (most recently added)
     [2]
     [1]
    -----

  pop() → returns 3, stack becomes:

     [2]  ← new top
     [1]
    -----

  peek() → returns 2 (looks at top without removing)

Operations:
  push(x)  → add to top     O(1)
  pop()    → remove from top O(1)
  peek()   → look at top     O(1)
  is_empty → check if empty  O(1)
```

```python
# Python: just use a list
stack = []
stack.append(1)      # push
stack.append(2)
stack.append(3)
top = stack[-1]      # peek → 3
val = stack.pop()    # pop → 3
is_empty = len(stack) == 0
```

**Worked problem — Valid Parentheses:**

```
Input: "({[]})"

Process each character:
  '(' → push '('     stack: ['(']
  '{' → push '{'     stack: ['(', '{']
  '[' → push '['     stack: ['(', '{', '[']
  ']' → pop '[', matches ']' ✓   stack: ['(', '{']
  '}' → pop '{', matches '}' ✓   stack: ['(']
  ')' → pop '(', matches ')' ✓   stack: []

Stack empty at end → Valid ✓
```

```python
def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
```

---

### Queue — Implementation

```
Real-world analogy: a line at a coffee shop.
First person in line gets served first.
New people join at the BACK, people leave from the FRONT.
That's FIFO — First In, First Out.

Visual:
  enqueue(1), enqueue(2), enqueue(3):

  FRONT → [1] [2] [3] ← BACK

  dequeue() → returns 1 (front leaves):

  FRONT → [2] [3] ← BACK

  enqueue(4):

  FRONT → [2] [3] [4] ← BACK

When to use a queue vs a stack:
  Stack: "I need the most RECENT thing" (undo, brackets, DFS)
  Queue: "I need the OLDEST thing" (BFS, scheduling, fairness)

Operations:
  enqueue(x) → add to back     O(1)
  dequeue()  → remove from front O(1)
  peek()     → look at front    O(1)
```

```python
from collections import deque

q = deque()
q.append(1)        # enqueue
q.append(2)
q.append(3)
front = q[0]       # peek → 1
val = q.popleft()  # dequeue → 1
```

**Worked problem — Rotten Oranges (multi-source BFS):**

```
Grid:
  [[2,1,1],
   [1,1,0],
   [0,1,1]]

Step 1: Find all rotten oranges → queue = [(0,0, t=0)]
Step 2: BFS level by level (each level = 1 minute)

Minute 0: process (0,0) → rot (0,1) and (1,0)
  queue: [(0,1,1), (1,0,1)]

Minute 1: process (0,1) → rot (0,2), (1,1)
           process (1,0) → (1,1) already rotting
  queue: [(0,2,2), (1,1,2)]

Minute 2: process (0,2) → nothing new
           process (1,1) → rot (2,1)
  queue: [(2,1,3)]

Minute 3: process (2,1) → rot (2,2)
  queue: [(2,2,4)]

Minute 4: process (2,2) → nothing new
  queue: []

Answer: 4 minutes ✓
```

```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    if fresh == 0:
        return 0
    time = 0
    while queue:
        r, c, t = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                time = t + 1
                queue.append((nr, nc, t + 1))
    return time if fresh == 0 else -1
```

---

### Hash Map — Implementation

```
Real-world analogy: a phone book.
You look up a person's NAME (the key) and instantly get their
PHONE NUMBER (the value). You don't scan every entry — you jump
directly to the right page.

Visual:
  put("alice", 555-1234)
  put("bob",   555-5678)
  put("carol", 555-9012)

  Internally (simplified):
    bucket[2] → ("alice", 555-1234)
    bucket[5] → ("bob",   555-5678)
    bucket[1] → ("carol", 555-9012)

  get("bob") → hash("bob") = 5 → bucket[5] → 555-5678. Done. O(1).

  The hash function converts the key into a bucket index.
  If two keys hash to the same bucket (collision), they're stored
  in a list at that bucket and you scan the short list.

Why O(1)? Because the hash function jumps directly to the right bucket.
No scanning the entire collection.

Operations:
  put(key, val)   → insert/update  O(1) average
  get(key)        → lookup         O(1) average
  delete(key)     → remove         O(1) average
  key in map      → membership     O(1) average
```

```python
# Python: just use a dict
d = {}
d['apple'] = 3       # put
d['banana'] = 1
val = d['banana']     # get → 1
exists = 'cherry' in d  # membership → False
del d['apple']        # delete

# For counting, use Counter or defaultdict
from collections import Counter, defaultdict
freq = Counter("aabbccc")   # {'c': 3, 'a': 2, 'b': 2}
groups = defaultdict(list)
groups['fruit'].append('apple')
```

**Worked problem — Two Sum:**

```
nums = [2, 7, 11, 15], target = 9

seen = {}

i=0, num=2: complement = 9-2 = 7. 7 in seen? No. seen = {2: 0}
i=1, num=7: complement = 9-7 = 2. 2 in seen? YES at index 0.
  Return [0, 1] ✓
```

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

---

### Heap (Priority Queue) — Implementation

```
Real-world analogy: an emergency room.
Patients don't get treated in arrival order — the most URGENT
patient gets treated first. When a new patient arrives, they're
placed in the right position based on urgency. When the doctor
is free, they always take the most urgent patient next.

That's a heap: it always gives you the min (or max) element in O(1),
and adding/removing elements takes O(log n).

Visual (min-heap — smallest on top):

  After pushing 5, 3, 7, 1, 4:

         1          ← root is always the minimum
        / \
       3   7
      / \
     5   4

  pop() → returns 1 (the minimum), then restructures:

         3
        / \
       4   7
      /
     5

  peek() → 3 (new minimum, without removing)

How it works internally:
  Stored as an array: [1, 3, 7, 5, 4]
  Parent of index i: (i-1) // 2
  Left child of i:   2*i + 1
  Right child of i:  2*i + 2

  push: add to end, "bubble up" (swap with parent while smaller)
  pop:  remove root, move last element to root, "bubble down"
        (swap with smaller child while larger)

Operations:
  push(x)  → add element       O(log n)
  pop()    → remove min/max    O(log n)
  peek()   → look at min/max   O(1)
  heapify  → build from list   O(n)
```

```python
import heapq

# Min-heap (Python default)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
smallest = heap[0]          # peek → 1
val = heapq.heappop(heap)   # pop → 1

# Max-heap: negate values
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
largest = -max_heap[0]      # peek → 5
val = -heapq.heappop(max_heap)  # pop → 5

# Build heap from list
nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)        # O(n), nums is now a min-heap
```

**Worked problem — Kth Largest Element:**

```
nums = [3,2,1,5,6,4], k = 2
Answer: 5 (sorted: [1,2,3,4,5,6], 2nd largest = 5)

Use a min-heap of size k:

Process 3: heap = [3]           (size 1 < k=2, just push)
Process 2: heap = [2, 3]        (size 2 = k, ok)
Process 1: heap = [1, 3, 2]     (size 3 > k, pop min)
           pop 1 → heap = [2, 3]
Process 5: heap = [2, 3, 5]     (size 3 > k, pop min)
           pop 2 → heap = [3, 5]
Process 6: heap = [3, 5, 6]     (size 3 > k, pop min)
           pop 3 → heap = [5, 6]
Process 4: heap = [4, 6, 5]     (size 3 > k, pop min)
           pop 4 → heap = [5, 6]

heap[0] = 5 = kth largest ✓

Why it works: the heap always holds the k largest elements seen so far.
The smallest of those k (heap[0]) is the kth largest overall.
```

```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)   # remove smallest
    return heap[0]                # kth largest
```

---

### Trie (Prefix Tree) — Implementation

```
Real-world analogy: a phone's autocomplete.
When you type "c-a", your phone shows "cat", "car", "card", "care".
It doesn't search every word in the dictionary — it walks down a
tree of characters. After "c" → "a", it only looks at words starting
with "ca". That's a trie.

Visual — storing "cat", "car", "card", "bat":

  root
  ├── 'c'
  │   └── 'a'
  │       ├── 't' ✓ (end of "cat")
  │       └── 'r' ✓ (end of "car")
  │           └── 'd' ✓ (end of "card")
  └── 'b'
      └── 'a'
          └── 't' ✓ (end of "bat")

  search("car"):  root → c → a → r → is_end=True → FOUND ✓
  search("ca"):   root → c → a → is_end=False → NOT a complete word
  startsWith("ca"): root → c → a → node exists → True ✓
  search("dog"):  root → d → not found → False

Each node has:
  - children: a dict mapping character → child node
  - is_end: boolean marking if a complete word ends here

Why not just use a list of words?
  Searching a list for "does any word start with 'ca'?" requires
  scanning every word: O(n × L). A trie does it in O(L) where L
  is the prefix length — regardless of how many words are stored.

Operations:
  insert(word)        → add word          O(L)  L = word length
  search(word)        → exact match       O(L)
  starts_with(prefix) → prefix exists?    O(L)
```

```python
class TrieNode:
    def __init__(self):
        self.children = {}    # char → TrieNode
        self.is_end = False   # marks end of a complete word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

**Worked problem — Replace Words:**

```
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"

Build trie from dictionary: cat, bat, rat

For each word in sentence:
  "the"     → walk trie: t→? 't' not in root → no root found → keep "the"
  "cattle"  → walk trie: c→a→t → is_end=True! → replace with "cat"
  "was"     → walk trie: w→? not found → keep "was"
  "rattled" → walk trie: r→a→t → is_end=True! → replace with "rat"
  "by"      → not found → keep "by"
  "the"     → not found → keep "the"
  "battery" → walk trie: b→a→t → is_end=True! → replace with "bat"

Output: "the cat was rat by the bat" ✓
```

---

### Graph — Implementation

```
Real-world analogy: a social network.
People are NODES. Friendships are EDGES.
"Alice is friends with Bob" = an edge between Alice and Bob.

If friendships are mutual (Alice↔Bob), it's an UNDIRECTED graph.
If Alice follows Bob but Bob doesn't follow Alice, it's DIRECTED.

Visual — 5 people, some friendships:

  Alice --- Bob --- Dave
    |       |
  Carol --- Eve

  Adjacency list (how we store it):
    Alice: [Bob, Carol]
    Bob:   [Alice, Dave, Eve]
    Carol: [Alice, Eve]
    Dave:  [Bob]
    Eve:   [Bob, Carol]

  "Is there a path from Alice to Dave?"
    Alice → Bob → Dave. Yes.

  "How many friend groups are there?"
    Everyone is connected → 1 group.

  If we remove the Bob-Dave edge:
    Group 1: Alice, Bob, Carol, Eve
    Group 2: Dave (alone)
    → 2 groups.

Two ways to explore a graph:
  DFS (Depth First): go as deep as possible, then backtrack.
    Like exploring a maze by always turning left until you hit a dead end.
    Uses a stack (or recursion).

  BFS (Breadth First): visit all neighbors first, then their neighbors.
    Like ripples spreading from a stone dropped in water.
    Uses a queue.
    Gives SHORTEST PATH in unweighted graphs.

CRITICAL: graphs can have CYCLES (Alice→Bob→Eve→Carol→Alice).
You MUST track visited nodes or you'll loop forever.

A GRID is just a graph in disguise:
  Each cell = a node.
  Each cell's 4 neighbors (up/down/left/right) = edges.
  "Number of islands" = "number of connected components in a grid graph."

Operations:
  add_edge(u, v)  → connect two nodes  O(1)
  DFS/BFS         → visit all nodes    O(V + E)
  V = vertices (nodes), E = edges
```

```python
from collections import defaultdict, deque

# Build graph from edge list
graph = defaultdict(list)
edges = [(0,1), (0,2), (1,3), (2,3)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)   # undirected

# DFS (recursive)
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

# BFS
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

**Worked problem — Number of Islands:**

```
Grid:
  [["1","1","0"],
   ["1","0","0"],
   ["0","0","1"]]

Treat each cell as a graph node. Neighbors = 4 adjacent cells.

Scan grid:
  (0,0) = "1" → start DFS, sink entire island
    DFS visits: (0,0)→(0,1)→(1,0) → all become "0"
    count = 1

  (0,1) = "0" → skip (already sunk)
  (0,2) = "0" → skip
  (1,0) = "0" → skip (already sunk)
  (1,1) = "0" → skip
  (1,2) = "0" → skip
  (2,0) = "0" → skip
  (2,1) = "0" → skip

  (2,2) = "1" → start DFS, sink island
    DFS visits: (2,2) → becomes "0"
    count = 2

Answer: 2 ✓
```

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'   # sink (mark visited)
        dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count
```

---

### Union-Find (Disjoint Set) — Implementation

```
Real-world analogy: friend groups at a party.

Imagine 6 people arrive at a party, each alone:
  {Alice} {Bob} {Carol} {Dave} {Eve} {Frank}
  6 separate groups.

Alice meets Bob → they're now in the same group:
  {Alice, Bob} {Carol} {Dave} {Eve} {Frank}
  5 groups.

Carol meets Dave:
  {Alice, Bob} {Carol, Dave} {Eve} {Frank}
  4 groups.

Now Bob meets Carol. But Bob is in {Alice, Bob} and Carol is in
{Carol, Dave}. Their ENTIRE groups merge:
  {Alice, Bob, Carol, Dave} {Eve} {Frank}
  3 groups.

That's Union-Find. It answers two questions:
  1. "Are these two people in the same group?" → find()
  2. "Merge these two people's groups." → union()

How it works internally:
  Each person points to a "parent." The root of the chain is the
  group leader. Two people are in the same group if they have the
  same root.

  Initially everyone is their own parent:
    parent = [0, 1, 2, 3, 4, 5]
    (person 0's parent is 0, person 1's parent is 1, etc.)

  union(0, 1):  (Alice meets Bob)
    parent[1] = 0   →  parent = [0, 0, 2, 3, 4, 5]
    Now find(1) → parent[1]=0 → parent[0]=0 → root is 0.
    find(0) → root is 0. Same root → same group.

  union(2, 3):  (Carol meets Dave)
    parent[3] = 2   →  parent = [0, 0, 2, 2, 4, 5]

  union(1, 2):  (Bob meets Carol → merge their groups)
    find(1) = 0 (Alice's group leader)
    find(2) = 2 (Carol's group leader)
    parent[2] = 0   →  parent = [0, 0, 0, 2, 4, 5]
    Now find(3) → parent[3]=2 → parent[2]=0 → root is 0.
    Alice, Bob, Carol, Dave all have root 0. Same group. ✓

  Two optimizations make it nearly O(1) per operation:
    Path compression: when you call find(3), update parent[3]
      directly to the root (skip intermediate nodes).
    Union by rank: always attach the shorter tree under the taller one.

Why not just use a set?
  Sets can check membership, but merging two sets is O(n).
  Union-Find merges in nearly O(1).

When to use Union-Find:
  "How many connected groups?"
  "Are these two in the same group?"
  "Merge these groups."
  "Find the redundant edge that creates a cycle."

Operations:
  find(x)       → find root of x's group   O(α(n)) ≈ O(1)
  union(x, y)   → merge groups of x and y  O(α(n)) ≈ O(1)
  connected(x,y)→ same group?              O(α(n)) ≈ O(1)
```

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False   # already connected
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

**Worked problem — Number of Provinces:**

```
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

City 0 connected to city 1 (isConnected[0][1] = 1)
City 2 is isolated.

uf = UnionFind(3)   # parent = [0, 1, 2]

Process connections:
  (0,1): union(0,1) → parent = [0, 0, 2]  (1's root is now 0)
  (0,2): isConnected[0][2] = 0 → skip
  (1,2): isConnected[1][2] = 0 → skip

Count distinct roots:
  find(0) = 0
  find(1) = 0  (same as 0)
  find(2) = 2

Distinct roots: {0, 2} → 2 provinces ✓
```

```python
def find_provinces(isConnected):
    n = len(isConnected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)
    # Count distinct roots
    return len(set(uf.find(i) for i in range(n)))
```

---

### Binary Tree — Implementation

```
Real-world analogy: a family tree (but upside down).
One person at the top (the root). Each person has at most two
children (left and right). People at the bottom with no children
are called leaves.

Visual:
        1          ← root
       / \
      2   3        ← 2 is left child of 1, 3 is right child
     / \   \
    4   5   6      ← 4 and 5 are children of 2, 6 is child of 3
   /
  7                ← 7 is left child of 4

  Height = 4 (longest path: 1→2→4→7)
  Leaves = 7, 5, 6 (no children)

A Binary Search Tree (BST) adds one rule:
  For every node: left child < node < right child.

  BST example:
        5
       / \
      3   8
     / \   \
    1   4   9

  Inorder traversal (left→root→right) gives sorted order: 1,3,4,5,8,9

Three ways to visit every node (DFS):
  Preorder  (Root→Left→Right): 1,2,4,7,5,3,6  — used to copy/serialize
  Inorder   (Left→Root→Right): 7,4,2,5,1,3,6  — gives sorted order in BST
  Postorder (Left→Right→Root): 7,4,5,2,6,3,1  — used to delete/compute subtrees

One way to visit level by level (BFS):
  Level order: [1], [2,3], [4,5,6], [7]

The key mental model for tree problems:
  Most tree problems are solved by recursion.
  At each node, you either:
    - Return something UP to the parent (height, count, boolean)
    - Pass something DOWN to children (remaining sum, depth, range)

Operations:
  DFS traversals → O(n)
  BFS level order → O(n)
  Height → O(n)
  Search in BST → O(log n) average, O(n) worst
```

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder traversal (gives sorted order for BST)
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Height
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

# Level order (BFS)
from collections import deque
def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

**Worked problem — Maximum Depth:**

```
Tree:
    3
   / \
  9  20
     / \
    15   7

depth(3):
  left  = depth(9)  = 1 + max(depth(None), depth(None)) = 1 + max(0,0) = 1
  right = depth(20) = 1 + max(depth(15), depth(7))
                     = 1 + max(1, 1) = 2
  return 1 + max(1, 2) = 3 ✓
```

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

---

### Linked List — Implementation

```
Real-world analogy: a scavenger hunt.
Each clue tells you where the NEXT clue is. You can only go forward
by following the clue. You can't jump to clue #5 directly — you
have to go through clues 1, 2, 3, 4 first.

Visual:
  head → [1 | next:→] → [2 | next:→] → [3 | next:→] → None

  Each box (node) contains:
    - A value (1, 2, 3)
    - A pointer to the next box (or None if it's the last)

  To reach node 3, you MUST start at head and follow the chain:
    head → node1 → node2 → node3

  You can't do list[2] like an array. There's no random access.

Why use a linked list instead of an array?
  Array:  insert at front = O(n) (shift everything right)
  List:   insert at front = O(1) (just update one pointer)

  Array:  delete from middle = O(n) (shift everything left)
  List:   delete from middle = O(1) IF you have the node reference

  Array:  access by index = O(1)
  List:   access by index = O(n) (must traverse)

  Use a linked list when you need fast insert/delete and don't need
  random access. Classic use: LRU cache, undo history, merge operations.

Doubly linked list: each node also has a PREV pointer.
  None ← [1] ⇄ [2] ⇄ [3] → None
  You can go both forward AND backward.
  Deletion is O(1) because you can reach the previous node directly.

Operations:
  prepend(val)  → add to front    O(1)
  append(val)   → add to end      O(n)  (O(1) with tail pointer)
  delete(node)  → remove node     O(1) if you have the node reference
  search(val)   → find node       O(n)
  reverse()     → reverse list    O(n)
```

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Build a list from array
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Traverse and print
def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" → ".join(vals) + " → None")

# Reverse
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Worked problem — Merge Two Sorted Lists:**

```
l1: [1] → [2] → [4]
l2: [1] → [3] → [4]

Use a dummy node to build the result:

dummy → ?
curr = dummy

Compare l1=1 vs l2=1 → take l1. curr.next = l1. l1 advances to [2].
  dummy → [1]

Compare l1=2 vs l2=1 → take l2. curr.next = l2. l2 advances to [3].
  dummy → [1] → [1]

Compare l1=2 vs l2=3 → take l1. curr.next = l1. l1 advances to [4].
  dummy → [1] → [1] → [2]

Compare l1=4 vs l2=3 → take l2. curr.next = l2. l2 advances to [4].
  dummy → [1] → [1] → [2] → [3]

Compare l1=4 vs l2=4 → take l1. l1 = None.
  dummy → [1] → [1] → [2] → [3] → [4]

l1 exhausted → attach remaining l2.
  dummy → [1] → [1] → [2] → [3] → [4] → [4] ✓
```

```python
def merge_two_lists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

---

### Monotonic Stack — Implementation

```
A stack that maintains elements in increasing or decreasing order.
When a new element violates the order, pop until order is restored.

Decreasing stack for "next greater element":

nums = [2, 1, 5, 3, 6]

Process 2: stack empty → push 2.          stack: [2]
Process 1: 1 < 2 → push 1.               stack: [2, 1]
Process 5: 5 > 1 → pop 1, NGE[1]=5
           5 > 2 → pop 2, NGE[0]=5
           push 5.                        stack: [5]
Process 3: 3 < 5 → push 3.               stack: [5, 3]
Process 6: 6 > 3 → pop 3, NGE[3]=6
           6 > 5 → pop 5, NGE[2]=6
           push 6.                        stack: [6]

Remaining: NGE[4] = -1 (no greater element)
Result: [5, 5, 6, 6, -1]
```

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []   # stores indices, values are decreasing
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    return result
```

**Worked problem — Daily Temperatures:**

```
temps = [73, 74, 75, 71, 69, 72, 76, 73]

Same as next greater element, but return DISTANCE instead of value.

i=0 (73): stack=[] → push 0.                stack: [0]
i=1 (74): 74>73 → pop 0, ans[0]=1-0=1.     stack: [1]
i=2 (75): 75>74 → pop 1, ans[1]=2-1=1.     stack: [2]
i=3 (71): 71<75 → push 3.                  stack: [2,3]
i=4 (69): 69<71 → push 4.                  stack: [2,3,4]
i=5 (72): 72>69 → pop 4, ans[4]=5-4=1.
          72>71 → pop 3, ans[3]=5-3=2.
          72<75 → push 5.                   stack: [2,5]
i=6 (76): 76>72 → pop 5, ans[5]=6-5=1.
          76>75 → pop 2, ans[2]=6-2=4.
          push 6.                           stack: [6]
i=7 (73): 73<76 → push 7.                  stack: [6,7]

Remaining: ans[6]=0, ans[7]=0

Result: [1, 1, 4, 2, 1, 1, 0, 0] ✓
```

```python
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
```

---

## Practice: Read the Problem, Name the Structure

Try to name the data structure BEFORE reading the solution.

```
Problem: "Given an array of meeting intervals, find the minimum
          number of conference rooms required."

Step 1 — What do I store?
  Meeting start/end times.

Step 2 — What operation do I need?
  For each new meeting, I need to know: "is any room free?"
  A room is free when its earliest ending meeting has ended.
  I need the MINIMUM end time across all active rooms.

Step 3 — What gives me the minimum efficiently?
  → Heap (min-heap of end times).

Answer: Sort by start time + min-heap of end times. ✓
```

```
Problem: "Given a string, find the length of the longest substring
          without repeating characters."

Step 1 — What do I store?
  Characters in the current window.

Step 2 — What operation do I need?
  Check if a character is already in the window → O(1) lookup.
  Add/remove characters as the window slides.

Step 3 — What gives me O(1) lookup + add/remove?
  → Hash Map (or Hash Set).

Answer: Sliding window + hash map tracking last seen index. ✓
```

```
Problem: "Design a browser back/forward button."

Step 1 — What do I store?
  URLs visited.

Step 2 — What operation do I need?
  "Back" = go to the most recently visited page.
  "Forward" = go to the page you just went back from.
  LIFO for back, LIFO for forward.

Step 3 — What gives me LIFO?
  → Two stacks (one for back history, one for forward history).

Answer: Two stacks. ✓
```

```
Problem: "Given a stream of numbers, find the median at any point."

Step 1 — What do I store?
  All numbers seen so far, in a way that gives me the middle.

Step 2 — What operation do I need?
  Insert a number.
  Get the median (middle element of sorted order).

Step 3 — What gives me efficient insert + access to the middle?
  → Two heaps (max-heap for lower half, min-heap for upper half).

Answer: Two heaps. ✓
```

```
Problem: "Implement autocomplete: given a prefix, return all matching words."

Step 1 — What do I store?
  A dictionary of words.

Step 2 — What operation do I need?
  Given a prefix, find all words that start with it.

Step 3 — What's optimized for prefix lookup?
  → Trie.

Answer: Trie with DFS from the prefix node. ✓
```

---

## The Combination Patterns

Many hard problems use TWO data structures together. Here are the most
common combos:

```
COMBO                          USED FOR
──────────────────────────────────────────────────────────────
Hash Map + Stack               Next greater element with lookup
Hash Map + Heap                Top K frequent elements
Hash Map + DLL                 LRU Cache (O(1) get + O(1) evict)
Hash Map + Queue               BFS with visited tracking
Two Heaps                      Median of stream, sliding window median
Trie + DFS                     Word search II, autocomplete
Graph + Heap                   Dijkstra's shortest path
Graph + Queue                  BFS shortest path (unweighted)
Graph + Stack                  DFS, topological sort
Sorted Array + Binary Search   Search in rotated array, find bounds
```

When a single data structure doesn't give you everything you need,
ask: "what's missing?" and add a second structure to fill the gap.

```
LRU Cache needs:
  O(1) lookup by key → hash map ✓
  O(1) eviction of least recent → ??? hash map can't do this
  O(1) move-to-front on access → ??? hash map can't do this either

What gives O(1) insert/delete at both ends with node references?
  → Doubly linked list.

Combo: hash map (key → node) + DLL (recency order). ✓
```

---

## The 30-Second Problem Reading Ritual

Do this every time you read a new problem:

```
1. Read the problem once. Don't code.

2. Underline the KEY OPERATION words:
   "find", "count", "check if exists", "shortest", "maximum",
   "next greater", "all paths", "group", "prefix"

3. Ask: "What data structure gives me this operation efficiently?"
   Use the trigger word table above.

4. Ask: "Is one structure enough, or do I need a combo?"

5. THEN start thinking about the algorithm.
```

The data structure choice should take 30 seconds. If you're spending
5 minutes deciding between a stack and a queue, you haven't internalized
the trigger words yet. Practice the examples above until the mapping
is automatic.

---

## Drill: 30 Problems — Read, Think, Then Check

For each problem below, read the description and I/O, then try to name the
primary data structure BEFORE looking at the answer. Cover the answer column.

---

### 1. Valid Parentheses

```
Given a string containing only '(', ')', '{', '}', '[', ']',
determine if the input string is valid.

Input:  "({[]})"
Output: True

Input:  "({[})"
Output: False  (the ] is missing before })
```

**Think:** I need to match each closing bracket with the most recent
unmatched opening bracket. "Most recent" = LIFO.

**Answer:** Stack. Push openers, pop on closers, check match.

---

### 2. Two Sum

```
Given an array of integers and a target, return the indices of
two numbers that add up to the target.

Input:  nums=[2,7,11,15], target=9
Output: [0,1]  (2+7=9)
```

**Think:** For each number, I need to check if `target - num` exists.
That's a lookup.

**Answer:** Hash Map. Store {value: index}, check for complement.

---

### 3. Kth Largest Element in an Array

```
Given an unsorted array, return the kth largest element.

Input:  nums=[3,2,1,5,6,4], k=2
Output: 5  (sorted: [1,2,3,4,5,6], 2nd largest = 5)
```

**Think:** I need to efficiently track the top k elements. I need
the minimum of those k elements (to know if a new element qualifies).

**Answer:** Min-Heap of size k. Push each element, pop when size > k.
`heap[0]` is always the kth largest.

---

### 4. Number of Islands

```
Given a 2D grid of '1' (land) and '0' (water), count the number
of islands. An island is a group of connected '1's (horizontally
or vertically).

Input:
  [["1","1","0"],
   ["1","0","0"],
   ["0","0","1"]]
Output: 2  (top-left group + bottom-right single cell)
```

**Think:** I need to find connected groups in a grid. Each cell connects
to its 4 neighbors. That's a graph where cells are nodes.

**Answer:** Graph (implicit) + DFS/BFS. For each unvisited '1', flood-fill
the entire island, count += 1.

---

### 5. LRU Cache

```
Design a cache with capacity k. When full, evict the least recently
used item. get(key) and put(key, value) must both be O(1).

LRUCache(2)
put(1,1)  → cache: {1:1}
put(2,2)  → cache: {1:1, 2:2}
get(1)    → 1  (1 is now most recently used)
put(3,3)  → evict 2 (least recently used), cache: {1:1, 3:3}
get(2)    → -1  (evicted)
```

**Think:** I need O(1) lookup by key AND O(1) eviction of the oldest
unused item AND O(1) move-to-front on access. No single structure does all three.

**Answer:** Hash Map + Doubly Linked List. Map gives O(1) lookup.
DLL gives O(1) move-to-front and O(1) eviction from tail.

---

### 6. Course Schedule

```
There are n courses (0 to n-1). Some have prerequisites:
[1,0] means "take course 0 before course 1".
Can you finish all courses?

Input:  n=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]
Output: True  (take 0, then 1 and 2, then 3)

Input:  n=2, prerequisites=[[1,0],[0,1]]
Output: False  (circular dependency: 0 needs 1, 1 needs 0)
```

**Think:** Courses depend on other courses. That's a directed graph.
"Can you finish all?" = "Is there a valid ordering?" = "Is there a cycle?"

**Answer:** Graph + DFS (cycle detection) or BFS (topological sort).

---

### 7. Implement Trie (Prefix Tree)

```
Build a data structure that supports:
  insert("apple")
  search("apple")  → True
  search("app")    → False  (not a complete word)
  startsWith("app") → True  (prefix exists)
```

**Think:** I need to check if a prefix exists among stored words.
Character-by-character prefix matching.

**Answer:** Trie. Each node = one character, path from root = prefix.

---

### 8. Sliding Window Maximum

```
Given an array and window size k, return the max in each window.

Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]

Window [1,3,-1]  → 3
Window [3,-1,-3] → 3
Window [-1,-3,5] → 5
...
```

**Think:** I need the maximum in a sliding window. Elements enter from
the right and leave from the left. I need to discard elements that can
never be the max (smaller elements behind a larger one).

**Answer:** Monotonic Queue (Deque). Maintain decreasing order.
Front = current max. Pop from back when new element is larger.
Pop from front when it leaves the window.

---

### 9. Find Median from Data Stream

```
Numbers arrive one at a time. After each number, return the median.

addNum(1)  → median = 1.0
addNum(2)  → sorted: [1,2], median = 1.5
addNum(3)  → sorted: [1,2,3], median = 2.0
```

**Think:** I need the middle element of a growing sorted collection.
Sorting after each insert is O(n log n). I need something faster.
If I split the data into a lower half and upper half, the median is
at the boundary.

**Answer:** Two Heaps. Max-heap for lower half, min-heap for upper half.
Median = top of max-heap (or average of both tops).

---

### 10. Merge K Sorted Lists

```
Given k sorted linked lists, merge them into one sorted list.

Input:  [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Think:** At each step, I need the minimum value across k list heads.
Then advance that list's pointer.

**Answer:** Min-Heap. Push (value, list_index) for each list head.
Pop minimum, push the next element from that list.

---

### 11. Word Search II

```
Given a grid of letters and a list of words, find all words that
can be formed by connecting adjacent cells (no reuse per word).

Input:
  board = [["o","a","a","n"],
           ["e","t","a","e"],
           ["i","h","k","r"],
           ["i","f","l","v"]]
  words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

**Think:** I need to search for multiple words simultaneously on a grid.
Checking each word independently is slow. If I organize all words by
their prefixes, I can prune early during grid DFS.

**Answer:** Trie + DFS. Build trie from words. DFS on grid while walking
the trie. If current path isn't a trie prefix, stop early.

---

### 12. Number of Provinces

```
There are n cities. isConnected[i][j] = 1 means city i and j are
directly connected. A province is a group of directly or indirectly
connected cities. How many provinces are there?

Input:  [[1,1,0],[1,1,0],[0,0,1]]
Output: 2  (cities 0,1 are connected = 1 province; city 2 alone = 1 province)

Input:  [[1,0,0],[0,1,0],[0,0,1]]
Output: 3  (all cities isolated)
```

**Think:** I need to count groups of connected things. "Are these two
in the same group?" is the core question.

**Answer:** Union-Find. For each connection, union the two cities.
Count distinct roots at the end. (Or: Graph + DFS, count components.)

---

### 13. Daily Temperatures

```
Given daily temperatures, for each day find how many days until a
warmer temperature. If no warmer day exists, put 0.

Input:  [73,74,75,71,69,72,76,73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]

Day 0 (73°): next warmer = day 1 (74°) → 1 day
Day 2 (75°): next warmer = day 6 (76°) → 4 days
```

**Think:** For each element, I need the "next greater element to the right."
I'm looking for the first thing that breaks the current decreasing trend.

**Answer:** Monotonic Stack (decreasing). Push indices. When current temp
is greater than stack top, pop and record the distance.

---

### 14. Top K Frequent Elements

```
Given an array and integer k, return the k most frequent elements.

Input:  nums=[1,1,1,2,2,3], k=2
Output: [1,2]  (1 appears 3 times, 2 appears 2 times)
```

**Think:** Step 1: count frequencies → hash map.
Step 2: find the top k by frequency → I need the k largest frequencies.

**Answer:** Hash Map (count) + Min-Heap of size k (top k).
Or: Hash Map + Bucket Sort (bucket[freq] = list of nums).

---

### 15. Longest Substring Without Repeating Characters

```
Given a string, find the length of the longest substring with all
unique characters.

Input:  "abcabcbb"
Output: 3  (substring "abc")

Input:  "bbbbb"
Output: 1  (substring "b")
```

**Think:** I'm looking at a window of characters. I need to know if a
character is already in the window → O(1) lookup. I need to shrink the
window when a duplicate is found.

**Answer:** Hash Map (char → last index) + Sliding Window.

---

### 16. Binary Tree Level Order Traversal

```
Given a binary tree, return values level by level.

Input:
    3
   / \
  9  20
     / \
    15   7
Output: [[3],[9,20],[15,7]]
```

**Think:** I need to visit nodes level by level, left to right.
"Level by level" = breadth-first.

**Answer:** Queue (BFS). Process all nodes at current level before
moving to the next.

---

### 17. Network Delay Time

```
There are n nodes and weighted directed edges. A signal is sent from
node k. How long until all nodes receive it? Return -1 if impossible.

Input:  times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
Output: 2  (signal reaches node 1 in 1, node 3 in 1, node 4 in 2)
```

**Think:** Shortest path from one source to all nodes in a weighted graph.

**Answer:** Graph + Heap (Dijkstra's algorithm). Min-heap of (distance, node).

---

### 18. Evaluate Reverse Polish Notation

```
Evaluate a math expression in postfix notation.

Input:  ["2","1","+","3","*"]
Output: 9  ((2+1)*3 = 9)

Input:  ["4","13","5","/","+"]
Output: 6  (4+(13/5) = 4+2 = 6)
```

**Think:** Numbers get pushed. When I see an operator, I need the two
most recent numbers. "Most recent" = LIFO.

**Answer:** Stack. Push numbers. On operator: pop two, compute, push result.

---

### 19. Accounts Merge

```
Given accounts where each is [name, email1, email2, ...], merge
accounts that share at least one email.

Input:
  [["John","john@mail.com","john_ny@mail.com"],
   ["John","john@mail.com","john00@mail.com"],
   ["Mary","mary@mail.com"],
   ["John","johnny@mail.com"]]

Output:
  [["John","john00@mail.com","john@mail.com","john_ny@mail.com"],
   ["John","johnny@mail.com"],
   ["Mary","mary@mail.com"]]
```

**Think:** Emails that appear in the same account are "connected."
I need to merge groups that share any element. That's grouping with
dynamic merging.

**Answer:** Union-Find. Assign each email an ID. Union all emails within
the same account. Group by root at the end.

---

### 20. Design Search Autocomplete System

```
Given a list of past sentences and their frequencies, design a system:
  input('i') → top 3 sentences starting with "i"
  input('i ') → top 3 sentences starting with "i "
  input('i l') → top 3 sentences starting with "i l"
  input('#') → save the current sentence, reset
```

**Think:** I need to find all sentences matching a prefix, ranked by
frequency. Prefix lookup across many strings.

**Answer:** Trie. Each node stores a list of (sentence, frequency) pairs.
Walk the trie as characters are typed.

---

### 21. Min Stack

```
Design a stack that supports push, pop, top, and getMin — all in O(1).

push(-2), push(0), push(-3)
getMin() → -3
pop()    → removes -3
getMin() → -2
```

**Think:** Regular stack gives push/pop/top in O(1). But getMin normally
requires scanning all elements. I need to track the minimum at each state.

**Answer:** Two Stacks. Main stack + parallel min stack where min_stack[i]
= minimum of all elements from bottom to position i.

---

### 22. Task Scheduler

```
Given tasks ['A','A','A','B','B','B'] and cooldown n=2, find the
minimum intervals to execute all tasks. Same task must be separated
by at least n intervals.

Input:  tasks=["A","A","A","B","B","B"], n=2
Output: 8  (A → B → idle → A → B → idle → A → B)
```

**Think:** I should always execute the most frequent remaining task first
(greedy). I need to quickly find "which task has the highest remaining count?"

**Answer:** Max-Heap. Pop the most frequent task each round. After cooldown,
re-add tasks with remaining count > 0.

---

### 23. Rotten Oranges

```
A grid has 0 (empty), 1 (fresh orange), 2 (rotten orange). Each minute,
rotten oranges rot adjacent fresh ones. How many minutes until no fresh
oranges remain? Return -1 if impossible.

Input:
  [[2,1,1],
   [1,1,0],
   [0,1,1]]
Output: 4
```

**Think:** Rot spreads from multiple sources simultaneously, one step at
a time. "Simultaneously" + "step by step" = level-by-level BFS.

**Answer:** Queue (multi-source BFS). Start with all rotten oranges in
the queue. Each BFS level = 1 minute.

---

### 24. Decode String

```
Given an encoded string, decode it.

Input:  "3[a]2[bc]"
Output: "aaabcbc"

Input:  "3[a2[c]]"
Output: "accaccacc"  (inner first: 2[c]=cc, then 3[acc]=accaccacc)
```

**Think:** Nested brackets — I need to process the innermost bracket first,
then work outward. "Most recent unmatched bracket" = LIFO.

**Answer:** Stack. On `[`: push current string and number. On `]`: pop
and repeat.

---

### 25. Meeting Rooms II

```
Given meeting intervals, find the minimum number of rooms needed.

Input:  [[0,30],[5,10],[15,20]]
Output: 2  ([0,30] and [5,10] overlap → need 2 rooms)

Input:  [[7,10],[2,4]]
Output: 1  (no overlap)
```

**Think:** For each new meeting, I need to know: "has any room's meeting
ended?" I need the earliest ending time across all active rooms.

**Answer:** Min-Heap of end times. For each meeting (sorted by start):
if heap top ≤ start, reuse that room (pop). Push new end time.

---

### 26. Longest Consecutive Sequence

```
Given an unsorted array, find the length of the longest consecutive
sequence. Must run in O(n).

Input:  [100,4,200,1,3,2]
Output: 4  (sequence: 1,2,3,4)
```

**Think:** I need to check "does n+1 exist? does n+2 exist?" — that's
repeated lookups. O(1) lookup per check.

**Answer:** Hash Set. Put all numbers in a set. For each number n where
n-1 is NOT in the set (start of a sequence), count forward.

---

### 27. Clone Graph

```
Given a node in a connected undirected graph, return a deep copy.
Each node has a value and a list of neighbors.

Input:  node 1 connected to [2,4], node 2 connected to [1,3], etc.
Output: new graph with same structure but all new node objects
```

**Think:** I need to visit every node (DFS/BFS) and create a copy.
But nodes can point to already-copied nodes (cycles). I need to track
"have I already copied this node?" → O(1) lookup.

**Answer:** Graph DFS + Hash Map (original → clone). Before recursing
into a neighbor, check if it's already in the map.

---

### 28. Implement LFU Cache

```
Like LRU, but evict the LEAST FREQUENTLY USED item. Ties broken by
least recently used. get and put must be O(1).

LFUCache(2)
put(1,1)  → freq[1]=1
put(2,2)  → freq[2]=1
get(1)    → 1, freq[1]=2
put(3,3)  → evict key 2 (lowest freq=1, LRU among freq=1)
```

**Think:** I need O(1) lookup by key, O(1) frequency tracking, AND O(1)
eviction of the item with minimum frequency (with LRU tiebreaking).

**Answer:** Three Hash Maps. key→value, key→freq, freq→OrderedDict(keys).
Plus a min_freq variable.

---

### 29. Shortest Path in Binary Matrix

```
Given an n×n grid of 0s and 1s, find the shortest path from top-left
to bottom-right. You can move in 8 directions. Path goes through 0s only.

Input:
  [[0,0,0],
   [1,1,0],
   [1,1,0]]
Output: 4  (path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2))

Input:
  [[1,0,0],
   [1,1,0],
   [1,1,0]]
Output: -1  (start cell is blocked)
```

**Think:** Shortest path in an unweighted graph (grid). Each cell = node,
8 neighbors = edges. "Shortest" + "unweighted" = BFS.

**Answer:** Queue (BFS). Start from (0,0), explore all 8 neighbors,
first time you reach (n-1,n-1) = shortest path.

---

### 30. Maximum Frequency Stack

```
Design a stack where pop() removes the most frequent element.
Ties broken by most recently pushed.

push(5), push(7), push(5), push(7), push(4), push(5)
pop() → 5  (freq 3, most frequent)
pop() → 7  (freq 2, tied with 5 at freq 2, but 7 was pushed more recently)
pop() → 5
pop() → 4
```

**Think:** I need to track frequency of each element AND maintain push
order within each frequency level. Pop from the highest frequency group,
LIFO within that group.

**Answer:** Hash Map (val→freq) + Hash Map (freq→stack). Track max_freq.
Pop from group[max_freq]. If that group empties, decrement max_freq.

---

### 31. Subarray Sum Equals K

```
Given an array of integers and integer k, count the number of
subarrays whose sum equals k.

Input:  nums=[1,1,1], k=2
Output: 2  (subarrays [1,1] at positions 0-1 and 1-2)

Input:  nums=[1,2,3], k=3
Output: 2  (subarrays [1,2] and [3])
```

**Think:** I need to count subarrays with a specific sum. A subarray sum
= prefix[j] - prefix[i]. So I need: "how many previous prefix sums equal
current_prefix - k?" That's a lookup.

**Answer:** Hash Map (prefix_sum → count of times seen).

---

### 32. Asteroid Collision

```
Asteroids in a row. Positive = moving right, negative = moving left.
When two meet, smaller one explodes. Equal = both explode.
Return the state after all collisions.

Input:  [5, 10, -5]
Output: [5, 10]  (-5 hits 10, 10 wins)

Input:  [8, -8]
Output: []  (both explode)

Input:  [10, 2, -5]
Output: [10]  (-5 destroys 2, then 10 destroys -5)
```

**Think:** I process asteroids left to right. A negative asteroid collides
with the most recently seen positive asteroid. "Most recently seen" = LIFO.

**Answer:** Stack. Push positive asteroids. For negative ones, pop from
stack while top is smaller. If equal, both pop.

---

### 33. K Closest Points to Origin

```
Given points on a 2D plane, return the k closest to origin (0,0).

Input:  points=[[1,3],[-2,2]], k=1
Output: [[-2,2]]  (distance √8 < √10)

Input:  points=[[3,3],[5,-1],[-2,4]], k=2
Output: [[3,3],[-2,4]]
```

**Think:** I need the k smallest distances. I need to efficiently track
"what are the k closest so far?"

**Answer:** Max-Heap of size k (negate distances for max behavior in Python).
Push each point, pop when size > k. Remaining k = closest.

---

### 34. Word Ladder

```
Transform beginWord to endWord, changing one letter at a time.
Each intermediate word must be in the wordList.
Return the length of the shortest transformation sequence.

Input:  beginWord="hit", endWord="cog"
        wordList=["hot","dot","dog","lot","log","cog"]
Output: 5  (hit → hot → dot → dog → cog)

Input:  beginWord="hit", endWord="cog"
        wordList=["hot","dot","dog","lot","log"]
Output: 0  ("cog" not in wordList)
```

**Think:** Each word is a "state." Changing one letter = moving to an
adjacent state. "Shortest path" between states in an unweighted graph.

**Answer:** Queue (BFS). Each word = node. Edges = words differing by
one letter. BFS gives shortest path.

---

### 35. Simplify Path

```
Given a Unix-style file path, simplify it.

Input:  "/home/"
Output: "/home"

Input:  "/home//foo/"
Output: "/home/foo"

Input:  "/a/./b/../../c/"
Output: "/c"  (. = current dir, .. = parent dir)
```

**Think:** I process path components left to right. ".." means "go back
to the most recent directory." "Most recent" = LIFO.

**Answer:** Stack. Push directory names. On "..", pop. On "." or empty, skip.
Join remaining stack with "/".

---

### 36. Redundant Connection

```
A tree of n nodes has one extra edge added, creating a cycle.
Given the edges, return the extra edge.

Input:  [[1,2],[1,3],[2,3]]
Output: [2,3]  (removing this edge makes it a tree again)

Input:  [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Think:** I'm adding edges one by one. If two nodes are already connected
when I try to add an edge between them, that edge is redundant.
"Are these two already in the same group?" = connectivity check.

**Answer:** Union-Find. Process edges in order. If find(u) == find(v)
before union, this edge creates a cycle → return it.

---

### 37. Maximum Depth of Binary Tree

```
Given a binary tree, return its maximum depth (number of nodes on
the longest path from root to a leaf).

Input:
    3
   / \
  9  20
     / \
    15   7
Output: 3

Input: [1, null, 2]
Output: 2
```

**Think:** Depth of a tree = 1 + max(depth of left subtree, depth of right
subtree). That's a recursive definition → tree DFS.

**Answer:** Tree (DFS recursion). `depth(node) = 1 + max(depth(left), depth(right))`.

---

### 38. Trapping Rain Water

```
Given bar heights, compute how much water is trapped after rain.

Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input:  [4,2,0,3,2,5]
Output: 9
```

**Think:** Water at position i = min(max_left, max_right) - height[i].
I need the max to the left and max to the right of each position.
Two pointers from both ends can track this.

**Answer:** Two Pointers (or prefix/suffix arrays). Process from both
ends, tracking max_left and max_right.

---

### 39. Group Anagrams

```
Given an array of strings, group anagrams together.

Input:  ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Think:** Two strings are anagrams if they have the same characters.
I need to group strings by some key. sorted("eat") = "aet" = sorted("tea").
Grouping by key = hash map.

**Answer:** Hash Map where key = sorted(word), value = list of words.

---

### 40. Palindrome Linked List

```
Given a singly linked list, check if it's a palindrome.

Input:  [1] → [2] → [2] → [1]
Output: True

Input:  [1] → [2]
Output: False
```

**Think:** I need to compare the first half with the reversed second half.
To find the middle → slow/fast pointers. To reverse → three-pointer reversal.

**Answer:** Linked List (slow/fast to find middle + reverse second half).

---

### 41. Minimum Window Substring

```
Given strings s and t, find the smallest substring of s that contains
all characters of t (including duplicates).

Input:  s="ADOBECODEBANC", t="ABC"
Output: "BANC"

Input:  s="a", t="a"
Output: "a"

Input:  s="a", t="aa"
Output: ""  (s doesn't have two 'a's)
```

**Think:** I need a sliding window that contains all characters of t.
I need to track character counts in the window → hash map.
Expand right to include characters, shrink left to minimize.

**Answer:** Hash Map + Sliding Window. Map tracks character counts needed
vs. character counts in current window.

---

### 42. Invert Binary Tree

```
Mirror a binary tree — swap left and right children at every node.

Input:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

**Think:** At every node, swap left and right, then recurse.
That's a tree traversal with modification.

**Answer:** Tree (DFS). `node.left, node.right = invert(right), invert(left)`.

---

### 43. Cheapest Flights Within K Stops

```
There are n cities and flights with prices. Find the cheapest price
from src to dst with at most k stops.

Input:  n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
        src=0, dst=3, k=1
Output: 700  (0→1→3 costs 100+600=700, only 1 stop)
```

**Think:** Shortest path in a weighted graph, but with a constraint on
number of edges (stops). Standard Dijkstra doesn't handle edge count limits.

**Answer:** Graph + BFS (Bellman-Ford variant). Relax edges k+1 times.
Or: modified Dijkstra with state = (cost, node, stops_remaining).

---

### 44. Valid Sudoku

```
Determine if a 9×9 Sudoku board is valid. Only filled cells need to
be validated — no duplicates in any row, column, or 3×3 box.

Input:  (a partially filled 9×9 board)
Output: True or False
```

**Think:** For each number, I need to check: "have I seen this number
in this row / column / box before?" That's a membership check.

**Answer:** Hash Set (three sets: one per row, one per column, one per box).
For each filled cell, check all three sets.

---

### 45. Serialize and Deserialize Binary Tree

```
Convert a binary tree to a string and back.

Input:
    1
   / \
  2   3
     / \
    4   5
Serialized: "1,2,null,null,3,4,null,null,5,null,null"
```

**Think:** I need to traverse the tree and record every node (including
nulls for structure). Preorder DFS gives a natural serialization.
Deserialization consumes tokens in the same order.

**Answer:** Tree (DFS preorder). Serialize: visit node, recurse left, right.
Deserialize: consume tokens in same order.

---

### 46. Implement Stack using Queues

```
Implement a LIFO stack using only two FIFO queues.

push(1), push(2), top() → 2, pop() → 2, empty() → False
```

**Think:** A queue is FIFO but I need LIFO. On push, I can rotate all
existing elements behind the new one so the new one is always at the front.

**Answer:** Queue. On push(x): add x to queue, then rotate all previous
elements to the back (dequeue and re-enqueue n-1 times).

---

### 47. Find All Anagrams in a String

```
Given strings s and p, find all start indices of p's anagrams in s.

Input:  s="cbaebabacd", p="abc"
Output: [0, 6]  (s[0:3]="cba" is anagram, s[6:9]="bac" is anagram)

Input:  s="abab", p="ab"
Output: [0, 1, 2]
```

**Think:** I need a sliding window of size len(p) over s. At each position,
check if the window's character counts match p's counts. Tracking counts
= hash map. Sliding = add right char, remove left char.

**Answer:** Hash Map + Sliding Window of fixed size.

---

### 48. Lowest Common Ancestor of a BST

```
Given a BST and two nodes p and q, find their lowest common ancestor.

Input:
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
p=2, q=8 → Output: 6
p=2, q=4 → Output: 2
```

**Think:** In a BST, if both p and q are less than root, LCA is in the
left subtree. If both are greater, LCA is in the right subtree.
If they split (one left, one right), root is the LCA.

**Answer:** Tree (BST property). Walk down: go left if both < root,
right if both > root, otherwise current node is LCA.

---

### 49. Design Twitter

```
Design a simplified Twitter:
  postTweet(userId, tweetId)
  getNewsFeed(userId) → 10 most recent tweets from user + followees
  follow(followerId, followeeId)
  unfollow(followerId, followeeId)
```

**Think:** getNewsFeed needs the 10 most recent tweets across multiple
users. That's merging k sorted lists (each user's tweets sorted by time)
and taking the top 10.

**Answer:** Hash Map (userId → tweets, userId → followees) + Heap
(merge k sorted tweet lists, take top 10).

---

### 50. Surrounded Regions

```
Given an m×n board of 'X' and 'O', capture all 'O' regions that are
completely surrounded by 'X'. An 'O' on the border (or connected to
a border 'O') is NOT captured.

Input:
  [["X","X","X","X"],
   ["X","O","O","X"],
   ["X","X","O","X"],
   ["X","O","X","X"]]

Output:
  [["X","X","X","X"],
   ["X","X","X","X"],
   ["X","X","X","X"],
   ["X","O","X","X"]]
(The O at [3][1] is on the border, so it's not captured.
 The O's at [1][1],[1][2],[2][2] are surrounded → captured.)
```

**Think:** Instead of finding surrounded regions (hard), find UNsurrounded
regions (easy — they touch the border). Mark all O's connected to border
O's as safe. Everything else gets captured.

**Answer:** Graph (DFS/BFS from border O's). Mark safe O's, then flip
all remaining O's to X.

---

## Scoring

```
40-50 correct: The mapping is second nature. You're ready for interviews.
30-39 correct: Strong foundation. Review the ones you missed.
20-29 correct: Good progress. Focus on the data structures you missed most.
10-19 correct: Re-read the trigger words section. Try again in 2 days.
 0-9  correct: Focus on one data structure at a time. Pick the 3 you
               missed most and study their trigger words for a week.
```
