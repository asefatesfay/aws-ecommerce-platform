# Union-Find — Deep Dive

---

## What Problem Does Union-Find Solve?

Imagine you're a teacher on the first day of school. 30 kids walk in.
You don't know who's friends with whom. Throughout the day, you observe:

```
"Alice and Bob are friends."
"Carol and Dave are friends."
"Bob and Carol are friends."
```

Now a kid asks: "Are Alice and Dave friends?"

You think: Alice is friends with Bob. Bob is friends with Carol.
Carol is friends with Dave. So yes — Alice and Dave are in the same
friend group, even though they never directly interacted.

Union-Find is a data structure that answers exactly this:
  1. "Merge these two people's groups." → union(x, y)
  2. "Are these two people in the same group?" → find(x) == find(y)

And it does both in nearly O(1) time.

---

## The Simplest Possible Version (No Optimizations)

Let's start with 5 people numbered 0-4. Each person starts as their
own group leader (they point to themselves).

```
parent = [0, 1, 2, 3, 4]

What this means:
  Person 0's leader is 0 (themselves)
  Person 1's leader is 1 (themselves)
  Person 2's leader is 2 (themselves)
  Person 3's leader is 3 (themselves)
  Person 4's leader is 4 (themselves)

Groups: {0} {1} {2} {3} {4}   ← 5 separate groups
```

### Operation: find(x) — "Who is x's group leader?"

Follow the parent chain until you find someone who points to themselves.
That person is the group leader (the "root").

```python
def find(x):
    while parent[x] != x:    # keep following the chain
        x = parent[x]
    return x                  # x now points to itself = root
```

Example:
```
parent = [0, 1, 2, 3, 4]

find(3):
  parent[3] = 3. 3 == 3 → return 3.
  Person 3's leader is 3 (themselves).
```

### Operation: union(x, y) — "Merge x's group and y's group."

Find both leaders. Make one leader point to the other.

```python
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:         # different groups
        parent[root_x] = root_y  # x's leader now follows y's leader
```

### Full Trace — Step by Step

```
Start: parent = [0, 1, 2, 3, 4]
       Groups: {0} {1} {2} {3} {4}

─────────────────────────────────────────────────────
union(0, 1):  "Person 0 and Person 1 are friends"

  find(0) = 0  (parent[0]=0, points to self)
  find(1) = 1  (parent[1]=1, points to self)
  0 != 1 → parent[0] = 1

  parent = [1, 1, 2, 3, 4]

  What this means:
    Person 0's parent is now Person 1.
    To find Person 0's leader: parent[0]=1, parent[1]=1 → leader is 1.

  Groups: {0,1} {2} {3} {4}

─────────────────────────────────────────────────────
union(2, 3):  "Person 2 and Person 3 are friends"

  find(2) = 2
  find(3) = 3
  2 != 3 → parent[2] = 3

  parent = [1, 1, 3, 3, 4]

  Groups: {0,1} {2,3} {4}

─────────────────────────────────────────────────────
union(1, 3):  "Person 1 and Person 3 are friends"
              This merges the ENTIRE groups {0,1} and {2,3}!

  find(1) = 1  (parent[1]=1, points to self)
  find(3) = 3  (parent[3]=3, points to self)
  1 != 3 → parent[1] = 3

  parent = [1, 3, 3, 3, 4]

  Now let's trace find(0):
    parent[0] = 1
    parent[1] = 3
    parent[3] = 3 → root is 3

  And find(2):
    parent[2] = 3
    parent[3] = 3 → root is 3

  find(0) == find(2) == 3 → SAME GROUP ✓

  Groups: {0,1,2,3} {4}

─────────────────────────────────────────────────────
Question: "Are Person 0 and Person 4 in the same group?"

  find(0): parent[0]=1 → parent[1]=3 → parent[3]=3 → root is 3
  find(4): parent[4]=4 → root is 4

  3 != 4 → DIFFERENT GROUPS ✓

─────────────────────────────────────────────────────
Question: "Are Person 0 and Person 2 in the same group?"

  find(0): parent[0]=1 → parent[1]=3 → root is 3
  find(2): parent[2]=3 → root is 3

  3 == 3 → SAME GROUP ✓
```

---

## Why Is find() Slow Without Optimization?

In the worst case, the parent chain becomes a long line:

```
union(0,1), union(1,2), union(2,3), union(3,4)

parent = [1, 2, 3, 4, 4]

Chain: 0 → 1 → 2 → 3 → 4

find(0) has to follow 4 links. For n elements, find() is O(n).
That's no better than scanning a list.
```

---

## Optimization 1: Path Compression

After you find the root, update every node along the path to point
directly to the root. Next time, find() is O(1) for those nodes.

```
Before path compression:
  0 → 1 → 2 → 3 → 4  (root)

  find(0): follow 0→1→2→3→4. Root is 4.
  Now update: parent[0]=4, parent[1]=4, parent[2]=4, parent[3]=4

After path compression:
  0 → 4
  1 → 4
  2 → 4
  3 → 4

  find(0): parent[0]=4. Done in 1 step!
```

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])   # recursively compress
    return parent[x]
```

Or iteratively:
```python
def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]
    # Now compress: make every node on the path point to root
    while parent[x] != root:
        next_x = parent[x]
        parent[x] = root
        x = next_x
    return root
```

---

## Optimization 2: Union by Rank

When merging two groups, always attach the shorter tree under the
taller tree. This keeps the tree shallow.

```
Without union by rank:
  Always attaching to the same side can create a long chain.

  union(0,1): 0→1
  union(2,1): 2→1→... wait, we attach 2's root to 1's root.
              But if we always pick the same direction, we get:
              0→1, 2→1, 3→1, 4→1  (star shape — good!)
              or: 0→1→2→3→4  (line — bad!)

With union by rank:
  rank[x] = approximate height of x's tree.
  Always attach the shorter tree under the taller one.

  rank = [0, 0, 0, 0, 0]

  union(0,1): rank[0]=0, rank[1]=0 → equal, pick either. parent[0]=1, rank[1]=1
  union(2,3): rank[2]=0, rank[3]=0 → equal. parent[2]=3, rank[3]=1
  union(1,3): rank[1]=1, rank[3]=1 → equal. parent[1]=3, rank[3]=2

  Tree:
       3  (rank 2)
      / \
     1   2
     |
     0

  Height = 2. find(0) takes 2 steps (not 4).
```

```python
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x == root_y:
        return False   # already in same group
    # Attach shorter tree under taller tree
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1
    return True
```

---

## The Complete Implementation

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # everyone is their own leader
        self.rank = [0] * n            # all trees have height 0

    def find(self, x):
        """Find the leader (root) of x's group. Uses path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Merge x's group and y's group. Returns True if they were different."""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False   # already same group
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x   # ensure root_x is taller
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True

    def connected(self, x, y):
        """Are x and y in the same group?"""
        return self.find(x) == self.find(y)
```

With both optimizations, find() and union() are O(α(n)) per operation,
where α is the inverse Ackermann function. For all practical purposes,
α(n) ≤ 4 for any n up to 10^80. So it's effectively O(1).

---

## When Do You Use Union-Find?

Ask yourself: "Am I grouping things and asking if two things are in
the same group?"

```
Trigger phrases in problems:
  "connected components"
  "are these two connected?"
  "merge groups"
  "find redundant connection"
  "minimum spanning tree"
  "number of groups / provinces / islands"
```

---

## Problem 1 — Number of Provinces (Medium) #547

```
There are n cities. isConnected[i][j] = 1 means city i and j are
directly connected. A province is a group of connected cities.
How many provinces?

Input:  [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

  City 0 and City 1 are connected → one province.
  City 2 is alone → second province.
```

Step-by-step trace:
```
n = 3
uf = UnionFind(3)
parent = [0, 1, 2], rank = [0, 0, 0]

Scan the matrix (upper triangle only):
  isConnected[0][1] = 1 → union(0, 1)
    find(0)=0, find(1)=1. Different → parent[1]=0, rank[0]=1
    parent = [0, 0, 2]

  isConnected[0][2] = 0 → skip
  isConnected[1][2] = 0 → skip

Count distinct roots:
  find(0) = 0
  find(1) = 0  (parent[1]=0)
  find(2) = 2

Distinct roots: {0, 2} → 2 provinces ✓
```

```python
def find_circle_num(isConnected):
    n = len(isConnected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)
    return len(set(uf.find(i) for i in range(n)))
```

---

## Problem 2 — Redundant Connection (Medium) #684

```
A tree of n nodes has one extra edge, creating a cycle. Given the
edges in order, return the edge that creates the cycle.

Input:  [[1,2],[1,3],[2,3]]
Output: [2,3]

  Edge [1,2]: connect 1 and 2. No cycle.
  Edge [1,3]: connect 1 and 3. No cycle.
  Edge [2,3]: 2 and 3 are ALREADY connected (through 1).
              This edge creates a cycle → return [2,3].
```

Step-by-step trace:
```
uf = UnionFind(4)  (nodes 1-3, index 0 unused)
parent = [0, 1, 2, 3]

Edge [1,2]:
  find(1)=1, find(2)=2. Different → union. parent = [0, 1, 1, 3]

Edge [1,3]:
  find(1)=1, find(3)=3. Different → union. parent = [0, 1, 1, 1]

Edge [2,3]:
  find(2): parent[2]=1, parent[1]=1 → root=1
  find(3): parent[3]=1 → root=1
  1 == 1 → ALREADY CONNECTED → this edge is redundant!
  Return [2,3] ✓
```

```python
def find_redundant_connection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)   # nodes are 1-indexed
    for u, v in edges:
        if not uf.union(u, v):   # union returns False if already connected
            return [u, v]
    return []
```

The key insight: process edges one by one. If two nodes are already in
the same group when you try to connect them, that edge creates a cycle.

---

## Problem 3 — Accounts Merge (Medium) #721

```
Given accounts where each is [name, email1, email2, ...], merge
accounts that share at least one email. Two accounts with the same
name but no shared email are different people.

Input:
  [["John","a@mail","b@mail"],
   ["John","a@mail","c@mail"],
   ["Mary","d@mail"],
   ["John","e@mail"]]

Output:
  [["John","a@mail","b@mail","c@mail"],
   ["John","e@mail"],
   ["Mary","d@mail"]]

Account 0 and Account 1 share "a@mail" → merge.
Account 3 has no shared email with 0 or 1 → separate John.
```

Step-by-step trace:
```
Step 1: Assign each unique email an ID.
  "a@mail" → 0
  "b@mail" → 1
  "c@mail" → 2
  "d@mail" → 3
  "e@mail" → 4

Step 2: For each account, union all its emails together.
  Account 0: ["a@mail","b@mail"] → union(0, 1)
  Account 1: ["a@mail","c@mail"] → union(0, 2)
  Account 2: ["d@mail"]          → nothing to union (single email)
  Account 3: ["e@mail"]          → nothing to union

  After unions:
    find(0)=0, find(1)=0, find(2)=0  → {a@mail, b@mail, c@mail}
    find(3)=3                         → {d@mail}
    find(4)=4                         → {e@mail}

Step 3: Group emails by their root.
  Root 0: [a@mail, b@mail, c@mail]
  Root 3: [d@mail]
  Root 4: [e@mail]

Step 4: For each group, look up the account name and sort emails.
  Root 0 → name from account 0 = "John" → ["John","a@mail","b@mail","c@mail"]
  Root 3 → name from account 2 = "Mary" → ["Mary","d@mail"]
  Root 4 → name from account 3 = "John" → ["John","e@mail"]
```

```python
from collections import defaultdict

def accounts_merge(accounts):
    email_to_id = {}
    email_to_name = {}
    id_counter = 0

    # Assign IDs to emails
    for name, *emails in accounts:
        for email in emails:
            if email not in email_to_id:
                email_to_id[email] = id_counter
                id_counter += 1
            email_to_name[email] = name

    # Union all emails within each account
    uf = UnionFind(id_counter)
    for name, *emails in accounts:
        first_id = email_to_id[emails[0]]
        for email in emails[1:]:
            uf.union(first_id, email_to_id[email])

    # Group emails by root
    groups = defaultdict(list)
    for email, eid in email_to_id.items():
        groups[uf.find(eid)].append(email)

    # Build result
    return [[email_to_name[emails[0]]] + sorted(emails)
            for emails in groups.values()]
```

---

## Problem 4 — Satisfiability of Equality Equations (Medium) #990

```
Given equations like "a==b" and "a!=b", determine if all equations
can be satisfied simultaneously.

Input:  ["a==b","b!=a"]
Output: false  (a==b and b!=a contradict)

Input:  ["a==b","b==c","a==c"]
Output: true

Input:  ["a==b","b!=c","c==a"]
Output: false  (a==b, c==a → a,b,c same group, but b!=c contradicts)
```

Step-by-step trace for `["a==b","b!=c","c==a"]`:
```
Step 1: Process all "==" equations first (union equal variables).
  "a==b" → union(a, b)
  "c==a" → union(c, a)

  After unions: a, b, c are all in the same group.

Step 2: Process all "!=" equations (check for contradictions).
  "b!=c" → find(b) == find(c)?
           Yes! They're in the same group.
           But the equation says they must be different.
           CONTRADICTION → return false ✓
```

```python
def equations_possible(equations):
    uf = UnionFind(26)   # 26 lowercase letters

    # First pass: process all "==" (union)
    for eq in equations:
        if eq[1] == '=':
            uf.union(ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a'))

    # Second pass: check all "!=" (verify)
    for eq in equations:
        if eq[1] == '!':
            a = ord(eq[0]) - ord('a')
            b = ord(eq[3]) - ord('a')
            if uf.find(a) == uf.find(b):
                return False   # contradiction!

    return True
```

Why two passes? You must process all equalities first to build the
complete groups. Then check inequalities against those groups.

---

## Union-Find vs DFS/BFS — When to Use Which?

```
USE UNION-FIND WHEN:
  - Edges arrive one at a time (streaming)
  - You need to merge groups dynamically
  - You need to detect cycles as edges are added
  - You're building a minimum spanning tree (Kruskal's)
  - The problem says "connected components" and edges come in a list

USE DFS/BFS WHEN:
  - You have the full graph upfront
  - You need shortest path (BFS)
  - You need to explore all paths (DFS)
  - The graph is a grid (DFS flood fill is simpler)
  - You need topological ordering

BOTH WORK FOR:
  - Counting connected components
  - Checking if two nodes are connected
  - Number of islands (DFS is simpler, UF works too)
```

---

## Common Mistakes

```
MISTAKE 1: Forgetting to use find() before comparing
  WRONG:  if parent[x] == parent[y]   ← parent might not be the root!
  RIGHT:  if find(x) == find(y)

MISTAKE 2: Union without finding roots first
  WRONG:  parent[x] = y              ← x might not be a root
  RIGHT:  parent[find(x)] = find(y)

MISTAKE 3: Not handling 1-indexed nodes
  Problem says nodes are 1 to n, but your array is 0-indexed.
  Solution: create UnionFind(n + 1) and ignore index 0.

MISTAKE 4: Counting components wrong
  WRONG:  count unique values in parent[]
  RIGHT:  count unique values of find(i) for all i
          (parent[i] might not be the root due to path compression)
```
