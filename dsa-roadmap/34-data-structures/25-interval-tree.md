# Interval Tree

## What is it?
A tree data structure that stores intervals and efficiently answers **"which intervals overlap with a given query interval?"** in O(log N + k) where k is the number of results. Built on top of a BST augmented with the maximum endpoint in each subtree.

## Visual Example
```
Intervals: [1,3], [2,6], [5,8], [7,10], [9,12]

Sorted by start point, BST on start:
         [5,8]
        /     \
     [2,6]   [9,12]
     /           \
  [1,3]        [7,10]

Each node stores: interval + max_end in its subtree
         [5,8] max=12
        /          \
   [2,6] max=8   [9,12] max=12
   /                  \
[1,3] max=3         [7,10] max=10

Query: does [6,7] overlap with any interval?
- At [5,8]: 5<=7 and 6<=8 → YES, overlap found!
- Also check left subtree if max_end >= 6
```

## Overlap Condition
```
Two intervals [a,b] and [c,d] overlap if:
  a <= d AND c <= b

Equivalently: NOT (b < c OR d < a)
```

## Implementation

```python
class IntervalNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max_high = high  # max high in subtree
        self.left = None
        self.right = None

class IntervalTree:
    """
    Augmented BST for interval overlap queries.
    O(log N) insert, O(log N + k) overlap search.
    
    Example:
        it = IntervalTree()
        for interval in [(1,3),(2,6),(5,8),(7,10),(9,12)]:
            it.insert(*interval)
        it.find_overlapping(6, 7)   # [(5,8)]
        it.find_all_overlapping(2, 9)  # all overlapping intervals
    """
    def __init__(self):
        self.root = None

    def insert(self, low, high):
        """O(log N)"""
        self.root = self._insert(self.root, low, high)

    def _insert(self, node, low, high):
        if not node:
            return IntervalNode(low, high)
        if low < node.low:
            node.left = self._insert(node.left, low, high)
        else:
            node.right = self._insert(node.right, low, high)
        # Update max_high
        node.max_high = max(node.high,
                           node.left.max_high if node.left else 0,
                           node.right.max_high if node.right else 0)
        return node

    def find_overlapping(self, low, high):
        """Find ONE overlapping interval — O(log N)"""
        return self._find_overlapping(self.root, low, high)

    def _find_overlapping(self, node, low, high):
        if not node:
            return None
        # Check if current interval overlaps
        if node.low <= high and low <= node.high:
            return (node.low, node.high)
        # Go left if left subtree might have overlap
        if node.left and node.left.max_high >= low:
            return self._find_overlapping(node.left, low, high)
        # Otherwise go right
        return self._find_overlapping(node.right, low, high)

    def find_all_overlapping(self, low, high):
        """Find ALL overlapping intervals — O(log N + k)"""
        result = []
        self._find_all(self.root, low, high, result)
        return result

    def _find_all(self, node, low, high, result):
        if not node:
            return
        # Prune: if max_high < low, no overlap possible in this subtree
        if node.max_high < low:
            return
        # Check left subtree
        self._find_all(node.left, low, high, result)
        # Check current node
        if node.low <= high and low <= node.high:
            result.append((node.low, node.high))
        # Check right subtree (only if current start <= high)
        if node.low <= high:
            self._find_all(node.right, low, high, result)

    def delete(self, low, high):
        """O(log N)"""
        self.root = self._delete(self.root, low, high)

    def _delete(self, node, low, high):
        if not node:
            return None
        if low < node.low:
            node.left = self._delete(node.left, low, high)
        elif low > node.low:
            node.right = self._delete(node.right, low, high)
        elif node.high == high:
            # Found the node to delete
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Find inorder successor
            successor = node.right
            while successor.left:
                successor = successor.left
            node.low, node.high = successor.low, successor.high
            node.right = self._delete(node.right, successor.low, successor.high)
        else:
            node.right = self._delete(node.right, low, high)
        if node:
            node.max_high = max(node.high,
                               node.left.max_high if node.left else 0,
                               node.right.max_high if node.right else 0)
        return node
```

## Example Usage
```python
it = IntervalTree()
intervals = [(1,3), (2,6), (5,8), (7,10), (9,12)]
for low, high in intervals:
    it.insert(low, high)

print(it.find_overlapping(6, 7))        # (5, 8)
print(it.find_all_overlapping(2, 9))    # [(1,3),(2,6),(5,8),(7,10),(9,12)] or subset
print(it.find_all_overlapping(10, 11))  # [(9,12),(7,10)]

# Simpler approach using sorted list for interview
def find_overlapping_simple(intervals, low, high):
    """O(N) brute force — fine for small inputs"""
    return [(a, b) for a, b in intervals if a <= high and low <= b]
```

## When to Use
- Calendar/scheduling: "Is this time slot available?"
- Genomics: "Which genes overlap with this region?"
- Network routing: "Which IP ranges match?"
- Graphics: "Which rectangles overlap with this region?"

## LeetCode Problems

| Problem | Difficulty | Connection |
|---------|-----------|------------|
| My Calendar I (#729) | Medium | Interval overlap detection |
| My Calendar II (#731) | Medium | Count overlapping intervals |
| My Calendar III (#732) | Hard | Max overlapping at any point |
| Meeting Rooms II (#253) | Medium | Count concurrent meetings |
| Employee Free Time (#759) | Hard | Find gaps between intervals |
| Interval List Intersections (#986) | Medium | Find all intersections |
| Minimum Interval to Include Each Query (#1851) | Hard | Interval + heap |
