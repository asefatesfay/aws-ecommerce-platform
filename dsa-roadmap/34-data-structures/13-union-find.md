# Union-Find (Disjoint Set Union)

## What is it?
A data structure that tracks a set of elements partitioned into **non-overlapping groups** (components). Supports two operations nearly in O(1): find which group an element belongs to, and merge two groups.

## Visual Example
```
Initial: {0} {1} {2} {3} {4}  (5 separate components)
parent = [0, 1, 2, 3, 4]

union(0, 1): merge groups of 0 and 1
parent = [1, 1, 2, 3, 4]  → 0's parent is now 1
Components: {0,1} {2} {3} {4}

union(2, 3):
parent = [1, 1, 3, 3, 4]
Components: {0,1} {2,3} {4}

union(1, 3): merge {0,1} and {2,3}
parent = [1, 3, 3, 3, 4]
Components: {0,1,2,3} {4}

find(0): 0→1→3, returns 3 (root of component)
find(2): 2→3, returns 3 (same component as 0!)
connected(0, 2): find(0)==find(2) → True
```

## Path Compression
```
Before find(0):          After find(0) with path compression:
    3                        3
   / \                      /|\
  1   2                    0 1 2
  |
  0

All nodes point directly to root — future finds are O(1)
```

## Implementation

```python
class UnionFind:
    """
    Union-Find with path compression + union by rank.
    Nearly O(1) per operation (inverse Ackermann function).
    """
    def __init__(self, n):
        self.parent = list(range(n))  # parent[i] = i initially (self-loop)
        self.rank = [0] * n           # tree height for union by rank
        self.components = n           # number of connected components

    def find(self, x):
        """Find root with path compression — O(α(N))"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        """Merge components of x and y — O(α(N)). Returns True if merged."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already in same component
        # Union by rank: attach smaller tree under larger
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        """Check if x and y are in the same component — O(α(N))"""
        return self.find(x) == self.find(y)

    def __repr__(self):
        return f"UnionFind(n={len(self.parent)}, components={self.components})"
```

## Example Usage
```python
# Number of provinces (connected components)
def find_provinces(is_connected):
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i+1, n):
            if is_connected[i][j]:
                uf.union(i, j)
    return uf.components

# [[1,1,0],[1,1,0],[0,0,1]] → 2 provinces
print(find_provinces([[1,1,0],[1,1,0],[0,0,1]]))  # 2

# Detect cycle in undirected graph
def has_cycle(n, edges):
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):  # already connected → cycle!
            return True
    return False

print(has_cycle(4, [[0,1],[1,2],[2,3],[3,0]]))  # True (cycle 0-1-2-3-0)
print(has_cycle(3, [[0,1],[1,2]]))              # False

# Accounts merge
def accounts_merge(accounts):
    email_to_id = {}
    uf = UnionFind(len(accounts) * 10)  # generous size
    id_counter = [0]

    def get_id(email):
        if email not in email_to_id:
            email_to_id[email] = id_counter[0]
            id_counter[0] += 1
        return email_to_id[email]

    for account in accounts:
        first_email_id = get_id(account[1])
        for email in account[2:]:
            uf.union(first_email_id, get_id(email))

    # Group emails by root
    from collections import defaultdict
    groups = defaultdict(list)
    for email, eid in email_to_id.items():
        groups[uf.find(eid)].append(email)

    return [sorted(emails) for emails in groups.values()]
```

## When to Use
- "Number of connected components"
- "Are these two nodes connected?"
- "Detect cycle in undirected graph"
- "Minimum spanning tree (Kruskal's)"
- "Merge groups dynamically"

## LeetCode Problems

---

### 1. Number of Provinces — #547 (Medium)

**Problem**: There are `n` cities. `isConnected[i][j] = 1` means city i and j are directly connected. A province is a group of directly or indirectly connected cities. Return the number of provinces.

```
Input:  [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation: Cities 0 and 1 are connected → one province. City 2 is alone → second province.

Input:  [[1,0,0],[0,1,0],[0,0,1]]
Output: 3  (all cities are isolated)
```

**Hints**:
1. Initialize Union-Find with n nodes
2. For each pair (i, j) where `isConnected[i][j] == 1`, call `union(i, j)`
3. Return the number of distinct components

---

### 2. Redundant Connection — #684 (Medium)

**Problem**: A tree with n nodes has one extra edge added, creating a cycle. Given the edges, return the redundant edge (the one that creates the cycle). If multiple answers, return the last one in the input.

```
Input:  [[1,2],[1,3],[2,3]]
Output: [2,3]
Explanation: Adding [2,3] creates a cycle 1-2-3-1.

Input:  [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

**Hints**:
1. Process edges one by one; try to union the two endpoints
2. If they're already in the same component (find(u) == find(v)), this edge is redundant
3. Return the first such edge found

---

### 3. Accounts Merge — #721 (Medium)

**Problem**: Given a list of accounts where each account is `[name, email1, email2, ...]`, merge accounts that share at least one email. Return merged accounts sorted.

```
Input:
[["John","johnsmith@mail.com","john_newyork@mail.com"],
 ["John","johnsmith@mail.com","john00@mail.com"],
 ["Mary","mary@mail.com"],
 ["John","johnnybravo@mail.com"]]

Output:
[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
 ["John","johnnybravo@mail.com"],
 ["Mary","mary@mail.com"]]
```

**Hints**:
1. Assign each unique email an ID; union all emails within the same account
2. Group emails by their root ID
3. For each group, sort the emails and prepend the account name

---

### 4. Satisfiability of Equality Equations — #990 (Medium)

**Problem**: Given equations like `"a==b"` and `"a!=b"`, determine if all equations can be satisfied simultaneously.

```
Input:  ["a==b","b!=a"]
Output: false  (a==b and b!=a contradict each other)

Input:  ["b==a","a==b"]
Output: true

Input:  ["a==b","b==c","a==c"]
Output: true

Input:  ["a==b","b!=c","c==a"]
Output: false
```

**Hints**:
1. First pass: process all `==` equations, union the two variables
2. Second pass: for each `!=` equation, check if the two variables are in the same component
3. If they are, it's a contradiction → return false

---

### 5. Min Cost to Connect All Points — #1584 (Medium)

**Problem**: Given an array of points on a 2D plane, return the minimum cost to connect all points. The cost of connecting two points is their Manhattan distance. (This is the Minimum Spanning Tree problem.)

```
Input:  [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input:  [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Hints**:
1. Kruskal's: generate all edges with their Manhattan distances, sort by cost
2. Use Union-Find to add edges greedily — skip edges that would create a cycle
3. Stop when you have n-1 edges (all points connected)
4. Alternative: Prim's algorithm with a min-heap

---

### 6. Most Stones Removed with Same Row or Column — #947 (Medium)

**Problem**: On a 2D plane, stones are placed at integer coordinates. A stone can be removed if it shares a row or column with another stone. Return the maximum number of stones that can be removed.

```
Input:  [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Input:  [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Input:  [[0,0]]
Output: 0
```

**Hints**:
1. Stones in the same row or column are "connected" — they form a component
2. From each component of size k, you can remove k-1 stones (always keep one)
3. Answer = total stones - number of components
4. Union-Find: union stones that share a row or column
