# Sparse Table

## What is it?
A data structure for **static range minimum/maximum queries** in O(1) after O(N log N) preprocessing. Unlike Segment Tree, it cannot handle updates — but for read-only data it's faster. Works for any **idempotent** function (f(x,x) = x), like min, max, gcd.

## Visual Example
```
Array: [2, 4, 3, 1, 6, 7, 8, 9]
Index:  0  1  2  3  4  5  6  7

table[i][j] = min of subarray starting at i with length 2^j

j=0 (length 1):  [2, 4, 3, 1, 6, 7, 8, 9]
j=1 (length 2):  [2, 3, 1, 1, 6, 7, 8, _]  (min of pairs)
j=2 (length 4):  [1, 1, 1, 1, 6, _, _, _]  (min of quads)
j=3 (length 8):  [1, _, _, _, _, _, _, _]  (min of all 8)

Query min(2, 6) = min of [3,1,6,7,8]:
  length = 6-2+1 = 5
  k = floor(log2(5)) = 2  (2^2 = 4)
  Two overlapping ranges of length 4:
    table[2][2] = min(arr[2..5]) = 1
    table[3][2] = min(arr[3..6]) = 1
  Answer = min(1, 1) = 1 ✓

The two ranges [2..5] and [3..6] overlap but that's OK for min/max!
(Idempotent: min(x, x) = x, so overlap doesn't matter)
```

## Why O(1) Query Works
```
For any range [l, r] of length len:
  k = floor(log2(len))
  Two ranges of length 2^k cover [l, r]:
    [l, l + 2^k - 1]  and  [r - 2^k + 1, r]
  
  These overlap, but for idempotent functions (min, max, gcd):
  f(f(a,b), f(b,c)) = f(a,b,c)  ← overlap doesn't double-count
```

## Implementation

```python
import math

class SparseTable:
    """
    Static range minimum query in O(1) after O(N log N) build.
    Works for any idempotent function: min, max, gcd, bitwise AND/OR.
    
    Example:
        st = SparseTable([2, 4, 3, 1, 6, 7, 8, 9])
        st.query(0, 3)  # min of [2,4,3,1] = 1
        st.query(2, 6)  # min of [3,1,6,7,8] = 1
        st.query(4, 7)  # min of [6,7,8,9] = 6
    """
    def __init__(self, nums, func=min):
        """
        func: aggregation function (must be idempotent for O(1) queries)
        min, max, gcd, bitwise AND/OR are idempotent.
        sum is NOT idempotent — use Fenwick Tree instead.
        """
        self.n = len(nums)
        self.func = func
        self.LOG = max(1, int(math.log2(self.n)) + 1) if self.n > 0 else 1
        # table[i][j] = func of nums[i .. i + 2^j - 1]
        self.table = [[0] * self.LOG for _ in range(self.n)]
        self._build(nums)

    def _build(self, nums):
        """O(N log N) preprocessing"""
        # Base case: ranges of length 1
        for i in range(self.n):
            self.table[i][0] = nums[i]
        # Fill in larger ranges
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) - 1 < self.n:
                self.table[i][j] = self.func(
                    self.table[i][j-1],
                    self.table[i + (1 << (j-1))][j-1]
                )
                i += 1
            j += 1

    def query(self, l, r):
        """Range query [l, r] — O(1) for idempotent functions"""
        if l > r:
            return None
        length = r - l + 1
        k = int(math.log2(length))
        return self.func(
            self.table[l][k],
            self.table[r - (1 << k) + 1][k]
        )

    def query_range_max(self, l, r):
        """Convenience method for range maximum"""
        if l > r:
            return None
        length = r - l + 1
        k = int(math.log2(length))
        return max(self.table[l][k], self.table[r - (1 << k) + 1][k])


class SparseTableGCD:
    """Sparse table for range GCD queries."""
    def __init__(self, nums):
        from math import gcd
        self.st = SparseTable(nums, func=gcd)

    def query(self, l, r):
        return self.st.query(l, r)


# Precomputed log table for faster queries (avoids math.log2 call)
class SparseTableFast:
    """Sparse table with precomputed log values for maximum speed."""
    def __init__(self, nums):
        self.n = len(nums)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.LOG = self.log[self.n] + 1
        self.table = [[float('inf')] * self.LOG for _ in range(self.n)]
        for i in range(self.n):
            self.table[i][0] = nums[i]
        j = 1
        while (1 << j) <= self.n:
            for i in range(self.n - (1 << j) + 1):
                self.table[i][j] = min(self.table[i][j-1],
                                       self.table[i + (1 << (j-1))][j-1])
            j += 1

    def query(self, l, r):
        k = self.log[r - l + 1]
        return min(self.table[l][k], self.table[r - (1 << k) + 1][k])
```

## Example Usage
```python
nums = [2, 4, 3, 1, 6, 7, 8, 9]
st = SparseTable(nums)

print(st.query(0, 7))  # 1 (min of entire array)
print(st.query(0, 3))  # 1 (min of [2,4,3,1])
print(st.query(4, 7))  # 6 (min of [6,7,8,9])
print(st.query(2, 5))  # 1 (min of [3,1,6,7])

# Max queries
st_max = SparseTable(nums, func=max)
print(st_max.query(0, 7))  # 9
print(st_max.query(0, 3))  # 4

# GCD queries
from math import gcd
st_gcd = SparseTable([12, 8, 6, 4], func=gcd)
print(st_gcd.query(0, 3))  # gcd(12,8,6,4) = 2
```

## Sparse Table vs Segment Tree vs Fenwick Tree

| Feature | Sparse Table | Segment Tree | Fenwick Tree |
|---------|-------------|-------------|-------------|
| Build | O(N log N) | O(N) | O(N log N) |
| Query | O(1) | O(log N) | O(log N) |
| Update | Not supported | O(log N) | O(log N) |
| Space | O(N log N) | O(4N) | O(N) |
| Functions | Idempotent only | Any | Sum only |
| Best for | Static, read-heavy | Dynamic | Dynamic sum |

## When to Use
- Static array, many range min/max queries
- No updates needed
- Need O(1) query time
- LCA (Lowest Common Ancestor) via Euler tour + RMQ

## LeetCode Problems

Sparse tables are most useful for static range queries. LeetCode problems that benefit from this:

---

### 1. Range Minimum Query (Classic)

**Problem**: Given a static array, answer multiple queries of the form "what is the minimum value in the range [l, r]?"

```
Array:  [2, 4, 3, 1, 6, 7, 8, 9]

Query(0, 3) → min(2,4,3,1) = 1
Query(2, 5) → min(3,1,6,7) = 1
Query(4, 7) → min(6,7,8,9) = 6
Query(1, 1) → 4
```

**Hints**:
1. Build sparse table: `table[i][j] = min(arr[i..i+2^j-1])`
2. Query: `k = floor(log2(r-l+1))`, answer = `min(table[l][k], table[r-2^k+1][k])`
3. The two overlapping ranges are fine because min is idempotent

---

### 2. Sliding Window Maximum — #239 (Hard)

**Problem**: Given an array and window size k, return the maximum in each sliding window.

```
Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]
```

**Sparse table connection**: For static windows, you could precompute a sparse table and answer each window query in O(1). In practice, the monotonic deque solution is preferred since it handles the sliding nature more naturally.

**Hints**:
1. Sparse table approach: build on the array, then for each window [i, i+k-1] query in O(1)
2. Total: O(N log N) build + O(N) queries = O(N log N)
3. Monotonic deque is O(N) total — better for this specific problem

---

### 3. Lowest Common Ancestor of a Binary Tree — #236 (Medium)

**Problem**: Given a binary tree and two nodes p and q, find their lowest common ancestor.

```
Input:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4
p=5, q=1 → Output: 3
p=5, q=4 → Output: 5
```

**Sparse table connection**: The classic O(1) LCA algorithm uses Euler tour + sparse table for range minimum query. This converts the tree LCA problem into an RMQ problem.

**Approach**:
1. Do an Euler tour of the tree, recording each node when first visited and when returning from children
2. LCA(u, v) = the node with minimum depth in the Euler tour between the first occurrences of u and v
3. Use sparse table for O(1) range minimum queries on the depth array

**Hints** (for the simpler O(N) DFS approach):
1. If root is None, p, or q — return root
2. Recurse left and right
3. If both return non-null, root is the LCA; otherwise return whichever is non-null
