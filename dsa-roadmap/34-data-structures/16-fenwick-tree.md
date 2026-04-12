# Fenwick Tree (Binary Indexed Tree)

## What is it?
A data structure for **prefix sum queries with point updates** in O(log N). Simpler and faster in practice than a Segment Tree when you only need sum queries.

## Visual Example
```
Array (1-indexed): [1, 3, 5, 7, 9, 11]
Indices:            1  2  3  4  5   6

Each BIT node stores sum of a range determined by lowest set bit:

BIT[1] = arr[1]           = 1    (range: 1 element)
BIT[2] = arr[1]+arr[2]    = 4    (range: 2 elements)
BIT[3] = arr[3]           = 5    (range: 1 element)
BIT[4] = arr[1..4]        = 16   (range: 4 elements)
BIT[5] = arr[5]           = 9    (range: 1 element)
BIT[6] = arr[5]+arr[6]    = 20   (range: 2 elements)

Query prefix sum [1..5]:
  i=5: total += BIT[5]=9,  i = 5 - (5&-5) = 5-1 = 4
  i=4: total += BIT[4]=16, i = 4 - (4&-4) = 4-4 = 0
  Result: 9 + 16 = 25 ✓ (1+3+5+7+9=25)

Update index 3 (add 2):
  i=3: BIT[3] += 2, i = 3 + (3&-3) = 3+1 = 4
  i=4: BIT[4] += 2, i = 4 + (4&-4) = 4+4 = 8 > n, stop
```

## The Magic: `i & (-i)`
```python
# i & (-i) gives the lowest set bit of i
# This determines the range each BIT node is responsible for

i=1 (001): 1&-1 = 1  → responsible for 1 element
i=2 (010): 2&-2 = 2  → responsible for 2 elements
i=3 (011): 3&-3 = 1  → responsible for 1 element
i=4 (100): 4&-4 = 4  → responsible for 4 elements
i=6 (110): 6&-6 = 2  → responsible for 2 elements
```

## Implementation

```python
class FenwickTree:
    """
    1-indexed Binary Indexed Tree.
    
    Example:
        bit = FenwickTree(6)
        nums = [1, 3, 5, 7, 9, 11]
        for i, v in enumerate(nums, 1):
            bit.update(i, v)
        
        bit.query(4)          # prefix sum [1..4] = 16
        bit.range_query(2, 5) # sum [2..5] = 3+5+7+9 = 24
        bit.update(3, 2)      # add 2 to index 3
        bit.query(4)          # now 18
    """
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed

    def update(self, i, delta):
        """Add delta to position i — O(log N)"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # move to next responsible node

    def query(self, i):
        """Prefix sum [1..i] — O(log N)"""
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # move to parent
        return total

    def range_query(self, l, r):
        """Sum of range [l..r] — O(log N)"""
        return self.query(r) - self.query(l - 1)

    def build(self, nums):
        """Build from 0-indexed array — O(N log N)"""
        for i, v in enumerate(nums, 1):
            self.update(i, v)

    def point_query(self, i):
        """Get current value at index i — O(log N)"""
        return self.range_query(i, i)
```

## Example Usage
```python
# Range Sum Query - Mutable (LeetCode #307)
class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.bit = FenwickTree(self.n)
        self.nums = [0] * (self.n + 1)
        for i, v in enumerate(nums, 1):
            self.update(i - 1, v)

    def update(self, index, val):
        # index is 0-based
        delta = val - self.nums[index + 1]
        self.nums[index + 1] = val
        self.bit.update(index + 1, delta)

    def sumRange(self, left, right):
        return self.bit.range_query(left + 1, right + 1)

# Count of smaller numbers after self (LeetCode #315)
def count_smaller(nums):
    # Coordinate compress
    sorted_unique = sorted(set(nums))
    rank = {v: i+1 for i, v in enumerate(sorted_unique)}
    bit = FenwickTree(len(sorted_unique))
    result = []
    for num in reversed(nums):
        r = rank[num]
        result.append(bit.query(r - 1))  # count elements < num
        bit.update(r, 1)
    return result[::-1]

print(count_smaller([5, 2, 6, 1]))  # [2, 1, 1, 0]
```

## Fenwick Tree vs Segment Tree

| Feature | Fenwick Tree | Segment Tree |
|---------|-------------|-------------|
| Code complexity | Simple (~15 lines) | More complex |
| Space | O(N) | O(4N) |
| Operations | Sum only | Any associative op |
| Range update | Needs modification | Built-in |
| Constant factor | Smaller | Larger |

## When to Use
- Prefix sum queries with point updates
- Counting inversions
- Coordinate compression + counting
- When Segment Tree is overkill

## LeetCode Problems

| Problem | Difficulty | How BIT Helps |
|---------|-----------|---------------|
| Range Sum Query - Mutable (#307) | Medium | Point update + range sum |
| Count of Smaller Numbers After Self (#315) | Hard | Count elements in range |
| Reverse Pairs (#493) | Hard | Count pairs with condition |
| Count of Range Sum (#327) | Hard | Count sums in range |
| Number of Pairs Satisfying Inequality (#2426) | Hard | Count valid pairs |
| Create Sorted Array through Instructions (#1649) | Hard | Count smaller/larger |
