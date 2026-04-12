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

---

### 1. Range Sum Query - Mutable — #307 (Medium)

**Problem**: Given an integer array, implement `update(index, val)` and `sumRange(left, right)` (returns sum of elements from index left to right inclusive). Both operations must be efficient.

```
Input:
["NumArray","sumRange","update","sumRange"]
[[[1,3,5]], [0,2],     [1,2],   [0,2]]

Output: [null, 9, null, 8]

Trace:
NumArray([1,3,5])
sumRange(0,2) → 1+3+5 = 9
update(1, 2)  → array becomes [1,2,5]
sumRange(0,2) → 1+2+5 = 8
```

**Hints**:
1. Build a segment tree from the array
2. `update`: walk down to the leaf, update it, propagate sums back up
3. `sumRange`: query the tree, combining ranges that fall within [left, right]

---

### 2. Count of Smaller Numbers After Self — #315 (Hard)

**Problem**: Given an integer array, return a count array where `count[i]` is the number of elements to the right of `nums[i]` that are smaller than `nums[i]`.

```
Input:  [5, 2, 6, 1]
Output: [2, 1, 1, 0]

Explanation:
5: elements to right smaller than 5 → [2, 1] → count=2
2: elements to right smaller than 2 → [1] → count=1
6: elements to right smaller than 6 → [1] → count=1
1: no elements to right → count=0
```

**Hints**:
1. Process from right to left; use a segment tree (or BIT) on coordinate-compressed values
2. For each number, query how many values already inserted are smaller
3. Then insert the current number into the tree

---

### 3. The Skyline Problem — #218 (Hard)

**Problem**: Given a list of buildings `[left, right, height]`, return the skyline as a list of key points `[x, height]` where the height changes.

```
Input:  [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Visualization:
         15
      ┌──┐
   10 │  │12
┌────┤  ├──────┐
│    │  │      │  10
│    └──┘      └──────┐  8
│                     └──┐
2  3  5  7  9 12    15 19 20 24
```

**Hints**:
1. Collect all x-coordinates (building starts and ends) as events
2. Use a max-heap (or segment tree) to track active building heights
3. At each x, the current max height determines the skyline; record a point when height changes

---

### 4. My Calendar III — #732 (Hard)

**Problem**: Implement a calendar where you can book events `[start, end)`. After each booking, return the maximum number of overlapping events at any point in time.

```
Input:
["MyCalendarThree","book","book","book","book","book","book"]
[[],               [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]

Output: [null, 1, 1, 2, 3, 3, 3]

Trace:
book(10,20) → max overlap = 1
book(50,60) → max overlap = 1
book(10,40) → [10,20] and [10,40] overlap → max = 2
book(5,15)  → [5,15],[10,20],[10,40] overlap at [10,15] → max = 3
book(5,10)  → max still 3
book(25,55) → max still 3
```

**Hints**:
1. Use a segment tree with lazy propagation on the time axis
2. For each booking, do a range update (+1 on [start, end))
3. Query the maximum value in the entire range after each update
