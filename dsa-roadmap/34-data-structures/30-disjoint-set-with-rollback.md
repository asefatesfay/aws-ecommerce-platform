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

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| Offline dynamic connectivity | Classic | Direct application |
| Tarjan's LCA | Classic | Uses rollback UF |
| Number of Islands II (#305) | Hard | Online version (no rollback needed) |
