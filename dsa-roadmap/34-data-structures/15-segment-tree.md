# Segment Tree

## What is it?
A tree where each node stores an aggregate (sum, min, max) of a range of the array. Supports both **range queries** and **point/range updates** in O(log N).

## Visual Example
```
Array: [1, 3, 5, 7, 9, 11]  (indices 0-5)

Segment tree (sum):
                 [36]          ← sum of [0..5]
               /       \
           [16]          [20]  ← [0..2] and [3..5]
          /    \        /    \
        [4]   [12]   [16]   [11]  ← [0..1],[2..2],[3..4],[5..5]
       /   \         /   \
     [1]  [3]      [7]  [9]

Query sum(1, 4) = 3+5+7+9 = 24:
  - [1..2] fully in range → 8
  - [3..4] fully in range → 16
  Total = 24

Update index 2 (add 2, value 5→7):
  Update path: [2..2]→[0..2]→[0..5]
```

## Implementation

```python
class SegmentTree:
    """
    Segment tree for range sum queries and point updates.
    O(N) build, O(log N) query and update.
    """
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        if nums:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(nums, 2*node+1, start, mid)
            self._build(nums, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, idx, val, node=0, start=0, end=None):
        """Point update: set index idx to val — O(log N)"""
        if end is None: end = self.n - 1
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, 2*node+1, start, mid)
            else:
                self.update(idx, val, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, l, r, node=0, start=0, end=None):
        """Range sum query [l, r] — O(log N)"""
        if end is None: end = self.n - 1
        if r < start or end < l:
            return 0  # out of range
        if l <= start and end <= r:
            return self.tree[node]  # fully in range
        mid = (start + end) // 2
        return (self.query(l, r, 2*node+1, start, mid) +
                self.query(l, r, 2*node+2, mid+1, end))


class SegmentTreeMin:
    """Segment tree for range minimum queries."""
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [float('inf')] * (4 * self.n)
        if nums: self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(nums, 2*node+1, start, mid)
            self._build(nums, 2*node+2, mid+1, end)
            self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])

    def query_min(self, l, r, node=0, start=0, end=None):
        if end is None: end = self.n - 1
        if r < start or end < l: return float('inf')
        if l <= start and end <= r: return self.tree[node]
        mid = (start + end) // 2
        return min(self.query_min(l, r, 2*node+1, start, mid),
                   self.query_min(l, r, 2*node+2, mid+1, end))
```

## Example Usage
```python
nums = [1, 3, 5, 7, 9, 11]
st = SegmentTree(nums)

print(st.query(1, 4))   # 3+5+7+9 = 24
print(st.query(0, 5))   # 1+3+5+7+9+11 = 36

st.update(2, 7)          # change index 2 from 5 to 7
print(st.query(1, 4))   # 3+7+7+9 = 26

st_min = SegmentTreeMin([1, 3, 5, 7, 9, 11])
print(st_min.query_min(1, 4))  # min(3,5,7,9) = 3
```

## Segment Tree vs Fenwick Tree

| Feature | Segment Tree | Fenwick Tree |
|---------|-------------|-------------|
| Operations | Sum, min, max, gcd, any | Sum only (easily) |
| Range update | Yes (with lazy propagation) | Needs modification |
| Code complexity | More complex | Simpler |
| Space | O(4N) | O(N) |

## When to Use
- Range queries with updates (sum, min, max)
- When Fenwick Tree isn't flexible enough
- Range update + range query (with lazy propagation)

## LeetCode Problems

| Problem | Difficulty | Operation |
|---------|-----------|-----------|
| Range Sum Query - Mutable (#307) | Medium | Point update + range sum |
| Count of Smaller Numbers After Self (#315) | Hard | Coordinate compression |
| The Skyline Problem (#218) | Hard | Segment tree on x-coords |
| Falling Squares (#699) | Hard | Range max query |
| My Calendar III (#732) | Hard | Range update + max query |
| Count of Range Sum (#327) | Hard | Merge sort / segment tree |
