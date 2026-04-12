# B-Tree

## What is it?
A self-balancing search tree designed for **disk-based storage** where each node can have many children (order `t` means 2t-1 keys per node). All leaves are at the same depth. Used in databases and file systems because it minimizes disk I/O by keeping many keys per node (matching disk block size).

## Visual Example
```
B-Tree of order 3 (each node has 2-5 keys, 3-6 children):

                    [30, 70]
                   /    |    \
          [10,20]  [40,50,60]  [80,90]
         /  |  \   / | | \    /  |  \
       [5] [15] [25] ... ...  [75] [85] [95]

Properties:
- All leaves at same depth
- Each internal node has between t-1 and 2t-1 keys
- Root has at least 1 key (or is a leaf)
- Keys in each node are sorted
- Children between keys contain values in that range
```

## Why B-Trees for Databases
```
Hard disk read: ~10ms
RAM access: ~100ns
→ 100,000x slower!

B-Tree minimizes disk reads by:
1. Storing many keys per node (matches disk block ~4KB)
2. All leaves at same depth → predictable O(log_t N) reads
3. t=1000 → tree of height 3 holds 10^9 records!

MySQL InnoDB: B+ Tree (all data in leaves, leaves linked)
PostgreSQL: B-Tree indexes
```

## Implementation

```python
class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t          # minimum degree
        self.keys = []      # sorted keys
        self.children = []  # child pointers
        self.leaf = leaf    # is this a leaf?
        self.n = 0          # current number of keys

class BTree:
    """
    B-Tree of minimum degree t.
    Each node has between t-1 and 2t-1 keys.
    O(log N) search, insert, delete.
    
    Example:
        bt = BTree(t=3)  # min degree 3, max 5 keys per node
        for v in [10, 20, 5, 6, 12, 30, 7, 17]:
            bt.insert(v)
        bt.search(6)   # True
        bt.search(15)  # False
    """
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    def search(self, key, node=None):
        """O(log N) — t * log_t(N) comparisons"""
        if node is None:
            node = self.root
        i = 0
        while i < node.n and key > node.keys[i]:
            i += 1
        if i < node.n and key == node.keys[i]:
            return True
        if node.leaf:
            return False
        return self.search(key, node.children[i])

    def insert(self, key):
        """O(log N)"""
        root = self.root
        if root.n == 2 * self.t - 1:  # root is full
            new_root = BTreeNode(self.t, leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        i = node.n - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
            node.n += 1
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if node.children[i].n == 2 * self.t - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def _split_child(self, parent, i):
        """Split full child at index i"""
        t = self.t
        full_child = parent.children[i]
        new_child = BTreeNode(t, leaf=full_child.leaf)

        # Move median key up to parent
        parent.keys.insert(i, full_child.keys[t-1])
        parent.n += 1
        parent.children.insert(i+1, new_child)

        # Split keys
        new_child.keys = full_child.keys[t:]
        new_child.n = t - 1
        full_child.keys = full_child.keys[:t-1]
        full_child.n = t - 1

        # Split children if not leaf
        if not full_child.leaf:
            new_child.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

    def inorder(self, node=None):
        """Return all keys in sorted order"""
        if node is None:
            node = self.root
        result = []
        for i in range(node.n):
            if not node.leaf:
                result.extend(self.inorder(node.children[i]))
            result.append(node.keys[i])
        if not node.leaf:
            result.extend(self.inorder(node.children[node.n]))
        return result
```

## B-Tree vs B+ Tree
```
B-Tree:
- Data stored in ALL nodes (internal + leaf)
- Shorter paths to some data

B+ Tree (used in databases):
- Data stored ONLY in leaf nodes
- Internal nodes only store keys for routing
- Leaf nodes linked together → efficient range scans
- Better cache performance

MySQL InnoDB, PostgreSQL use B+ Trees for indexes.
```

## Real-World Uses
- **MySQL InnoDB**: B+ Tree for primary and secondary indexes
- **PostgreSQL**: B-Tree indexes (default index type)
- **SQLite**: B-Tree for tables and indexes
- **NTFS/ext4**: File system directory structure
- **MongoDB**: WiredTiger storage engine

## When to Use
- Database index implementation
- File system directory structures
- Any disk-based sorted data structure
- When you need O(log N) with minimal disk I/O

## Interview Notes
You won't implement a B-Tree from scratch in interviews, but you should know:
- Why databases use B-Trees (disk I/O optimization)
- Difference between B-Tree and B+ Tree
- Why B+ Trees are preferred for range queries
- How indexes work in SQL databases

## LeetCode Problems

B-Trees are a systems/database concept — you won't implement one in a LeetCode interview. However, the underlying concepts appear in these problems:

---

### 1. Search in a Sorted Array of Unknown Size — #702 (Medium)

**Problem**: You have access to a sorted array of unknown size via an API `ArrayReader.get(index)` (returns 2^31-1 for out-of-bounds). Find the index of a target value, or -1 if not found.

```
Input:  array=[-1,0,3,5,9,12], target=9
Output: 4

Input:  array=[-1,0,3,5,9,12], target=2
Output: -1
```

**B-Tree connection**: B-Trees use binary search within each node to find the right child pointer — same idea as searching within a sorted range.

**Hints**:
1. First find the search bounds: start with `[0, 1]`, double the right bound until `reader.get(right) >= target`
2. Then binary search within those bounds

---

### 2. Range Sum Query - Immutable — #303 (Easy)

**Problem**: Given an integer array, handle multiple `sumRange(left, right)` queries efficiently.

```
Input:
["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

Output: [null, 1, -1, -3]

Trace:
sumRange(0,2) → -2+0+3 = 1
sumRange(2,5) → 3+(-5)+2+(-1) = -1
sumRange(0,5) → -2+0+3+(-5)+2+(-1) = -3
```

**B-Tree connection**: Database indexes (B-Trees) are used to answer range queries efficiently — this problem is the simplest form of a range query.

**Hints**:
1. Precompute prefix sums: `prefix[i] = sum(nums[0..i-1])`
2. `sumRange(l, r) = prefix[r+1] - prefix[l]`

---

### 3. Design a Key-Value Store (Conceptual)

B-Trees are the foundation of key-value stores. Understanding them helps with:

- **LevelDB/RocksDB internals**: LSM-tree (Log-Structured Merge-tree) vs B-Tree tradeoffs
- **SQL index design**: When to use a B-Tree index vs hash index
- **Range queries**: B-Tree indexes support `WHERE x BETWEEN a AND b`; hash indexes don't

**Key interview talking points**:
```
Q: Why does MySQL use B+ Trees instead of hash tables for indexes?
A: B+ Trees support range queries (BETWEEN, >, <) and ORDER BY.
   Hash tables only support exact lookups.

Q: Why are B-Trees better than BSTs for disk storage?
A: B-Trees have high branching factor (many keys per node),
   so tree height is O(log_t N) with large t.
   Fewer disk reads needed to find a record.

Q: What's the difference between clustered and non-clustered indexes?
A: Clustered: leaf nodes contain actual row data (InnoDB primary key).
   Non-clustered: leaf nodes contain primary key → extra lookup needed.
```
