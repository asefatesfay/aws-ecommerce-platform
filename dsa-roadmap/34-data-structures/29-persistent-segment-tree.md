# Persistent Segment Tree

## What is it?
A segment tree that **preserves all historical versions** after updates. Instead of modifying nodes in-place, each update creates a new root and shares unchanged nodes with previous versions. Enables queries on any past version in O(log N).

## Visual Example
```
Array: [1, 2, 3, 4, 5]

Version 0 (original):
        [15]           ← sum of all
       /    \
    [6]     [9]
   /   \   /   \
 [3]  [3] [4]  [5]
 / \  / \
[1][2][3][4]

Update index 2 (value 3→7):
Version 1 shares most nodes with Version 0.
Only the PATH from root to index 2 is new:

Version 1 root → [19]  (new)
                /    \
           [10]      [9]  ← SHARED from v0
           /   \
         [3]  [7]  ← [7] is new, [3] is SHARED
         / \
       [1][2]  ← SHARED from v0

Memory: O(N + Q*log N) instead of O(N*Q)
```

## Key Insight
```
Each update touches O(log N) nodes (one path from root to leaf).
All other nodes are shared between versions.
→ Q updates use O(Q * log N) extra space total.

Query version k: use root[k] as starting point.
```

## Implementation

```python
class PSNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PersistentSegmentTree:
    """
    Persistent segment tree for range sum queries with version history.
    O(N) build, O(log N) update and query per version.
    O(N + Q*log N) total space.
    
    Example:
        nums = [1, 2, 3, 4, 5]
        pst = PersistentSegmentTree(nums)
        pst.update(2, 7)          # version 1: index 2 becomes 7
        pst.query(0, 4, version=0) # 15 (original)
        pst.query(0, 4, version=1) # 19 (after update)
        pst.query(0, 2, version=1) # 10 (1+2+7)
    """
    def __init__(self, nums):
        self.n = len(nums)
        self.roots = []
        self.roots.append(self._build(nums, 0, self.n - 1))

    def _build(self, nums, start, end):
        if start == end:
            return PSNode(nums[start])
        mid = (start + end) // 2
        left = self._build(nums, start, mid)
        right = self._build(nums, mid+1, end)
        return PSNode(left.val + right.val, left, right)

    def update(self, idx, val, version=-1):
        """
        Create new version with index idx set to val.
        Returns new version number.
        """
        prev_root = self.roots[version]
        new_root = self._update(prev_root, 0, self.n - 1, idx, val)
        self.roots.append(new_root)
        return len(self.roots) - 1

    def _update(self, node, start, end, idx, val):
        if start == end:
            return PSNode(val)  # new leaf
        mid = (start + end) // 2
        if idx <= mid:
            new_left = self._update(node.left, start, mid, idx, val)
            return PSNode(new_left.val + node.right.val, new_left, node.right)
        else:
            new_right = self._update(node.right, mid+1, end, idx, val)
            return PSNode(node.left.val + new_right.val, node.left, new_right)

    def query(self, l, r, version=-1):
        """Range sum query on given version — O(log N)"""
        return self._query(self.roots[version], 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if not node or r < start or end < l:
            return 0
        if l <= start and end <= r:
            return node.val
        mid = (start + end) // 2
        return (self._query(node.left, start, mid, l, r) +
                self._query(node.right, mid+1, end, l, r))

    def num_versions(self):
        return len(self.roots)


# Application: Count elements in range [l,r] with values in [lo,hi]
# (Merge Sort Tree / Persistent Segment Tree on sorted values)

def count_in_range(nums, queries):
    """
    For each query (l, r, lo, hi): count elements in nums[l..r]
    with values in [lo..hi].
    Uses persistent segment tree on coordinate-compressed values.
    O(N log N) build, O(log N) per query.
    """
    # Coordinate compress
    sorted_vals = sorted(set(nums))
    rank = {v: i for i, v in enumerate(sorted_vals)}
    m = len(sorted_vals)

    # Build persistent segment tree, one version per prefix
    roots = [None]
    tree_nodes = []

    def update(prev_root, pos, start, end):
        node = PSNode(0 if not prev_root else prev_root.val + 1)
        if start == end:
            return node
        mid = (start + end) // 2
        if pos <= mid:
            node.left = update(prev_root.left if prev_root else None, pos, start, mid)
            node.right = prev_root.right if prev_root else None
        else:
            node.left = prev_root.left if prev_root else None
            node.right = update(prev_root.right if prev_root else None, pos, mid+1, end)
        node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
        return node

    root = None
    for num in nums:
        root = update(root, rank[num], 0, m-1)
        roots.append(root)

    def query(v1, v2, lo, hi, start, end):
        if not v2 or hi < start or end < lo:
            return 0
        if lo <= start and end <= hi:
            cnt2 = v2.val if v2 else 0
            cnt1 = v1.val if v1 else 0
            return cnt2 - cnt1
        mid = (start + end) // 2
        return (query(v1.left if v1 else None, v2.left if v2 else None, lo, hi, start, mid) +
                query(v1.right if v1 else None, v2.right if v2 else None, lo, hi, mid+1, end))

    results = []
    for l, r, lo, hi in queries:
        lo_rank = rank.get(lo, 0)
        hi_rank = len(sorted_vals) - 1
        # Find hi_rank as largest rank <= hi
        import bisect
        hi_rank = bisect.bisect_right(sorted_vals, hi) - 1
        lo_rank = bisect.bisect_left(sorted_vals, lo)
        if lo_rank > hi_rank:
            results.append(0)
        else:
            results.append(query(roots[l], roots[r+1], lo_rank, hi_rank, 0, m-1))
    return results
```

## Example Usage
```python
nums = [1, 2, 3, 4, 5]
pst = PersistentSegmentTree(nums)

print(pst.query(0, 4))           # 15 (version 0, sum all)
v1 = pst.update(2, 7)            # index 2: 3→7
print(pst.query(0, 4, version=0)) # 15 (original unchanged)
print(pst.query(0, 4, version=1)) # 19 (updated)
print(pst.query(0, 2, version=1)) # 10 (1+2+7)

v2 = pst.update(0, 10, version=1) # index 0: 1→10
print(pst.query(0, 4, version=2)) # 28 (10+2+7+4+5)
print(pst.query(0, 4, version=0)) # 15 (still original!)
```

## When to Use
- "Query on historical version of array"
- "Count elements in range [l,r] with values in [lo,hi]" (offline)
- Functional/immutable data structures
- Competitive programming with version queries

## LeetCode Problems

---

### 1. Count of Range Sum — #327 (Hard)

**Problem**: Given an integer array and bounds `[lower, upper]`, return the number of range sums `sum(i, j)` that lie in `[lower, upper]` (inclusive).

```
Input:  nums=[-2,5,-1], lower=-2, upper=2
Output: 3

All range sums:
sum(0,0) = -2  ✓ (in [-2,2])
sum(0,1) = 3   ✗
sum(0,2) = 2   ✓
sum(1,1) = 5   ✗
sum(1,2) = 4   ✗
sum(2,2) = -1  ✓
Count = 3
```

**Persistent segment tree connection**: Build a persistent segment tree on prefix sums. For each prefix sum `P[j]`, count how many previous prefix sums `P[i]` satisfy `P[j] - upper <= P[i] <= P[j] - lower`.

**Hints**:
1. Compute prefix sums; problem becomes: count pairs (i,j) where `lower <= prefix[j] - prefix[i] <= upper`
2. Use merge sort: during merge, count valid pairs across left and right halves
3. Persistent segment tree: for each j, query version j for count of values in `[prefix[j]-upper, prefix[j]-lower]`

---

### 2. Count of Smaller Numbers After Self — #315 (Hard)

**Problem**: Given an integer array, return a count array where `count[i]` is the number of elements to the right of `nums[i]` that are smaller than `nums[i]`.

```
Input:  [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Explanation:
5: [2,1] are smaller to the right → 2
2: [1] is smaller to the right → 1
6: [1] is smaller to the right → 1
1: nothing to the right → 0
```

**Persistent segment tree connection**: Build a persistent segment tree on coordinate-compressed values. For each element (right to left), query the current version for count of values less than current.

**Hints**:
1. Process right to left; coordinate compress values to range [1..n]
2. For each element, query how many values already inserted are smaller (range query [1, rank-1])
3. Insert current element; persistent segment tree preserves all versions

---

### 3. Range Module — #715 (Hard)

**Problem**: Design a data structure to track ranges of numbers. Support `addRange(left, right)`, `queryRange(left, right)` (returns true if every number in [left, right) is tracked), and `removeRange(left, right)`.

```
Input:
["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
[[],           [10,20],   [14,16],      [10,14],     [13,15],     [16,17]]

Output: [null, null, null, true, false, true]

Trace:
addRange(10,20)   → tracking [10,20)
removeRange(14,16)→ tracking [10,14) and [16,20)
queryRange(10,14) → [10,14) fully tracked → true
queryRange(13,15) → [13,15) not fully tracked (14 missing) → false
queryRange(16,17) → [16,17) fully tracked → true
```

**Hints**:
1. Use a sorted list of non-overlapping intervals
2. `addRange`: merge all overlapping intervals with the new one
3. `removeRange`: split/trim intervals that overlap with the removed range
4. `queryRange`: check if a single interval covers [left, right)
