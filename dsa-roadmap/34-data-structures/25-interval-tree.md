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

---

### 1. My Calendar I — #729 (Medium)

**Problem**: Implement a calendar where you can book events `[start, end)`. A booking is successful if it doesn't overlap with any existing booking. Return true if successful, false otherwise.

```
Input:
["MyCalendar","book","book","book"]
[[],          [10,20],[15,25],[20,30]]

Output: [null, true, false, true]

Trace:
book(10,20) → no conflicts → true
book(15,25) → overlaps [10,20] (15 < 20 and 25 > 10) → false
book(20,30) → [20,30) starts where [10,20) ends, no overlap → true
```

**Hints**:
1. Two intervals `[a,b)` and `[c,d)` overlap if `a < d AND c < b`
2. Store booked intervals sorted by start; binary search for the insertion point
3. Only check the immediate neighbors for overlap

---

### 2. My Calendar II — #731 (Medium)

**Problem**: Same as My Calendar I, but a booking is only rejected if it would cause a triple booking (3 events overlapping at the same time). Return true if the booking succeeds.

```
Input:
["MyCalendarTwo","book","book","book","book","book","book"]
[[],             [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]

Output: [null, true, true, true, false, true, true]

Trace:
book(10,20) → ok
book(50,60) → ok
book(10,40) → overlaps [10,20] → double booking at [10,20], ok
book(5,15)  → overlaps [10,20] and [10,40] → triple booking at [10,15] → false
book(5,10)  → overlaps [10,20] and [10,40] but only at [10,10) → ok
book(25,55) → overlaps [10,40] and [50,60] → double booking, ok
```

**Hints**:
1. Maintain two lists: `booked` (single bookings) and `overlaps` (double bookings)
2. For a new event, check if it overlaps with anything in `overlaps` → if yes, reject
3. If not rejected, add all overlaps with `booked` to `overlaps`, then add to `booked`

---

### 3. My Calendar III — #732 (Hard)

**Problem**: Same calendar, but after each booking return the maximum number of overlapping events at any point in time.

```
Input:
["MyCalendarThree","book","book","book","book","book","book"]
[[],               [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]

Output: [null, 1, 1, 2, 3, 3, 3]

Trace:
book(10,20) → max overlap = 1
book(50,60) → max overlap = 1
book(10,40) → [10,20] and [10,40] overlap → max = 2
book(5,15)  → [5,15],[10,20],[10,40] all overlap at [10,15] → max = 3
```

**Hints**:
1. Use a difference array / event counting approach
2. For each booking `[start, end)`: increment count at `start`, decrement at `end`
3. Sweep through events sorted by time; track running sum; return maximum

---

### 4. Meeting Rooms II — #253 (Medium)

**Problem**: Given an array of meeting time intervals `[start, end]`, find the minimum number of conference rooms required.

```
Input:  [[0,30],[5,10],[15,20]]
Output: 2
Explanation: Meeting [0,30] needs room 1. [5,10] needs room 2 (overlaps with [0,30]).
             [15,20] can reuse room 2 (after [5,10] ends). Max concurrent = 2.

Input:  [[7,10],[2,4]]
Output: 1  (no overlap)
```

**Hints**:
1. Sort meetings by start time
2. Use a min-heap of end times (one entry per room in use)
3. For each meeting: if the earliest-ending room is free (heap top ≤ start), reuse it; otherwise add a new room
4. Answer = max heap size at any point

---

### 5. Interval List Intersections — #986 (Medium)

**Problem**: Given two lists of closed intervals, each sorted and non-overlapping, return their intersection.

```
Input:
firstList  = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Explanation:
[0,2] ∩ [1,5] = [1,2]
[5,10] ∩ [1,5] = [5,5]
[5,10] ∩ [8,12] = [8,10]
[13,23] ∩ [15,24] = [15,23]
[24,25] ∩ [15,24] = [24,24]
[24,25] ∩ [25,26] = [25,25]
```

**Hints**:
1. Two pointers, one for each list
2. Intersection of `[a,b]` and `[c,d]` = `[max(a,c), min(b,d)]` if `max(a,c) <= min(b,d)`
3. Advance the pointer whose interval ends first
