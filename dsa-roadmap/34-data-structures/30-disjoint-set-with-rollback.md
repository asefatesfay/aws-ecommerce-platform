# Disjoint Set with Rollback (Union-Find with Undo)

## What is it?
A Union-Find data structure that supports **undoing union operations**. Standard Union-Find with path compression can't be rolled back (path compression permanently changes the structure). This version uses **union by rank only** (no path compression) so operations can be undone by restoring the previous parent and rank.

## Visual Example
```
Initial: {0} {1} {2} {3}

union(0,1): parent[0]=1, rank[1]=1
  {0,1} {2} {3}
  Stack: [(0, old_parent=0, old_rank=1)]

union(2,3): parent[2]=3, rank[3]=1
  {0,1} {2,3}
  Stack: [(0,0,1), (2,2,1)]

union(1,3): parent[1]=3, rank[3]=2
  {0,1,2,3}
  Stack: [(0,0,1), (2,2,1), (1,1,2)]

rollback(): undo union(1,3)
  parent[1]=1, rank[3]=1
  {0,1} {2,3}
  Stack: [(0,0,1), (2,2,1)]

rollback(): undo union(2,3)
  parent[2]=2, rank[3]=0
  {0,1} {2} {3}
```

## Implementation

```python
class RollbackUnionFind:
    """
    Union-Find with rollback support.
    Uses union by rank ONLY (no path compression).
    O(log N) per find/union, O(1) rollback.
    
    Use case: offline dynamic connectivity, LCA queries.
    
    Example:
        uf = RollbackUnionFind(5)
        uf.union(0, 1)
        uf.union(2, 3)
        uf.save()           # save checkpoint
        uf.union(1, 3)      # temporary union
        print(uf.connected(0, 2))  # True
        uf.rollback()       # undo back to checkpoint
        print(uf.connected(0, 2))  # False
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.history = []    # stack of (node, old_parent, old_rank)
        self.checkpoints = []  # stack of history lengths

    def find(self, x):
        """Find root WITHOUT path compression — O(log N)"""
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        """
        Union by rank, record history for rollback.
        Returns True if merged, False if already connected.
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # Union by rank: attach smaller tree under larger
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        # Record state before modification
        self.history.append((py, self.parent[py], px, self.rank[px]))
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

    def rollback(self):
        """Undo the last union operation — O(1)"""
        if not self.history:
            return
        py, old_parent_py, px, old_rank_px = self.history.pop()
        self.parent[py] = old_parent_py
        self.rank[px] = old_rank_px

    def save(self):
        """Save current state as a checkpoint"""
        self.checkpoints.append(len(self.history))

    def restore(self):
        """Rollback to last checkpoint"""
        if not self.checkpoints:
            return
        target = self.checkpoints.pop()
        while len(self.history) > target:
            self.rollback()

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def components(self):
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)


# Application: Offline Dynamic Connectivity
def offline_dynamic_connectivity(n, operations):
    """
    Process queries: add edge, remove edge, check connectivity.
    Uses divide-and-conquer + rollback UF.
    O((N + Q) log^2 N)
    
    operations: list of ('add', u, v), ('remove', u, v), ('query', u, v)
    Returns list of True/False for each query.
    """
    # This is a sketch of the algorithm
    # Full implementation requires segment tree on time intervals
    uf = RollbackUnionFind(n)
    results = []

    for op in operations:
        if op[0] == 'add':
            uf.union(op[1], op[2])
        elif op[0] == 'remove':
            # In full implementation, we'd use time-based rollback
            pass
        elif op[0] == 'query':
            results.append(uf.connected(op[1], op[2]))

    return results
```

## Example Usage
```python
uf = RollbackUnionFind(5)

uf.union(0, 1)
uf.union(2, 3)
print(uf.connected(0, 1))  # True
print(uf.connected(0, 2))  # False

uf.save()                   # checkpoint
uf.union(1, 3)              # temporarily connect {0,1} and {2,3}
print(uf.connected(0, 2))  # True
print(uf.connected(0, 3))  # True

uf.restore()                # rollback to checkpoint
print(uf.connected(0, 2))  # False (restored!)
print(uf.connected(0, 1))  # True (still connected)

# Manual rollback
uf.union(0, 4)
print(uf.connected(0, 4))  # True
uf.rollback()
print(uf.connected(0, 4))  # False
```

## When to Use
- **Offline dynamic connectivity**: edges added and removed, answer connectivity queries
- **LCA (Lowest Common Ancestor)**: Tarjan's offline LCA algorithm
- **Divide and conquer on graphs**: process edge additions/removals in time segments
- **Backtracking with connectivity**: explore states that require undoing merges

## Comparison with Standard Union-Find

| Feature | Standard UF | Rollback UF |
|---------|------------|-------------|
| Find | O(α(N)) | O(log N) |
| Union | O(α(N)) | O(log N) |
| Rollback | Not supported | O(1) |
| Path compression | Yes | No (breaks rollback) |

## LeetCode Problems

---

### 1. Number of Islands II — #305 (Hard)

**Problem**: Given an `m x n` grid initially all water, process a list of positions where land is added one at a time. After each addition, return the number of islands.

```
Input:  m=3, n=3, positions=[[0,0],[0,1],[1,2],[2,1]]
Output: [1, 1, 2, 3]

Trace:
Add (0,0): grid has 1 island → [1]
Add (0,1): connects to (0,0) → still 1 island → [1]
Add (1,2): isolated → 2 islands → [2]
Add (2,1): isolated → 3 islands → [3]
```

**Rollback UF connection**: This is the online version (no deletions). Standard Union-Find works here. The rollback version would be needed if land could also be removed.

**Hints**:
1. Use Union-Find; each cell is a node
2. When adding land at `(r,c)`: create a new component, then union with any adjacent land cells
3. Track component count: start at 0, +1 on each new land, -1 for each successful union

---

### 2. Checking Existence of Edge Length Limited Paths — #1697 (Hard)

**Problem**: Given an undirected graph with weighted edges and queries `[u, v, limit]`, for each query determine if there's a path from u to v where every edge has weight strictly less than `limit`.

```
Input:
n=3, edgeList=[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries=[[0,1,2],[0,2,5]]

Output: [false, true]

Trace:
Query [0,1,2]: path from 0 to 1 with all edges < 2? Edge (0,1) has weight 2, not < 2 → false
Query [0,2,5]: path from 0 to 2 with all edges < 5? 0→1 (weight 2) → 1→2 (weight 4), both < 5 → true
```

**Rollback UF connection**: Sort both edges and queries by weight/limit. Process queries offline — add edges with weight < limit, check connectivity. Rollback UF allows undoing edge additions between queries.

**Hints**:
1. Sort edges by weight; sort queries by limit
2. For each query (in order of limit), add all edges with weight < limit to Union-Find
3. Check if u and v are connected; this is offline processing (no rollback needed here)

---

### 3. Graph Connectivity With Threshold — #1627 (Hard)

**Problem**: There are n cities. Two cities u and v are connected if there exists a z > threshold such that both u and v are divisible by z. Given queries `[u, v]`, determine if u and v are in the same connected component.

```
Input:  n=6, threshold=2, queries=[[1,4],[2,5],[3,6]]
Output: [false, false, true]

Explanation (threshold=2, so z must be > 2, i.e., z >= 3):
z=3: connects 3 and 6
z=4: connects 4 (only one multiple ≤ 6)
z=5: connects 5 (only one multiple ≤ 6)
z=6: connects 6 (only one multiple ≤ 6)
So: {3,6} are connected, others are isolated.
Query [1,4]: not connected → false
Query [2,5]: not connected → false
Query [3,6]: connected → true
```

**Hints**:
1. For each z from threshold+1 to n, union all multiples of z together
2. Use Union-Find; for each z, union z with 2z, 3z, 4z, ... (up to n)
3. Total work: n/(t+1) + n/(t+2) + ... ≈ O(N log N / threshold)
