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

| Problem | Difficulty | How Union-Find Helps |
|---------|-----------|---------------------|
| Number of Provinces (#547) | Medium | Count components |
| Redundant Connection (#684) | Medium | Detect cycle |
| Accounts Merge (#721) | Medium | Merge email groups |
| Number of Connected Components (#323) | Medium | Count components |
| Graph Valid Tree (#261) | Medium | Check if tree (no cycle, connected) |
| Most Stones Removed (#947) | Medium | Group stones by row/col |
| Satisfiability of Equality Equations (#990) | Medium | Group equal variables |
| Number of Islands II (#305) | Hard | Dynamic island merging |
| Min Cost to Connect All Points (#1584) | Medium | Kruskal's MST |
| Swim in Rising Water (#778) | Hard | Binary search + UF |
