# Monotonic Queue (Deque)

## What is it?
A deque that maintains elements in monotonically increasing or decreasing order. Unlike a monotonic stack (only pops from one end), a monotonic queue can **pop from both ends** — making it ideal for **sliding window** problems where you need the min/max of a window efficiently.

## Visual Example — Sliding Window Maximum
```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Maintain a DECREASING deque of indices.
Front = index of current window maximum.

i=0, val=1:  deque=[]→[0]           window=[1]        (window not full yet)
i=1, val=3:  3>1, pop 0; deque=[1]  window=[1,3]      (window not full yet)
i=2, val=-1: -1<3, push; deque=[1,2] window=[1,3,-1]  max=nums[1]=3
i=3, val=-3: -3<-1, push; deque=[1,2,3] window=[3,-1,-3] max=nums[1]=3
             (front=1 still in window [1..3])
i=4, val=5:  5>-3, pop 3; 5>-1, pop 2; 5>3, pop 1; deque=[4]
             window=[-1,-3,5] max=nums[4]=5
i=5, val=3:  3<5, push; deque=[4,5] window=[-3,5,3]  max=nums[4]=5
i=6, val=6:  6>3, pop 5; 6>5, pop 4; deque=[6]
             window=[5,3,6] max=nums[6]=6
i=7, val=7:  7>6, pop 6; deque=[7]  window=[3,6,7]   max=nums[7]=7

Result: [3, 3, 5, 5, 6, 7]
```

## Key Insight
- **Decreasing deque** → window maximum at front
- **Increasing deque** → window minimum at front
- Pop from **back** when new element violates order
- Pop from **front** when front index is outside window

## Implementation

```python
from collections import deque

class MonotonicQueue:
    """
    Sliding window maximum using a monotonic decreasing deque.
    O(N) total — each element pushed/popped at most once.
    """
    def __init__(self):
        self._dq = deque()  # stores values in decreasing order

    def push(self, val):
        """Add val, maintaining decreasing order — O(1) amortized"""
        while self._dq and self._dq[-1] < val:
            self._dq.pop()
        self._dq.append(val)

    def pop(self, val):
        """Remove val from front if it's the current max — O(1)"""
        if self._dq and self._dq[0] == val:
            self._dq.popleft()

    def max(self):
        """Current window maximum — O(1)"""
        return self._dq[0]


def sliding_window_maximum(nums, k):
    """
    LeetCode #239 — O(N) solution.
    
    Example:
        sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3)
        → [3, 3, 5, 5, 6, 7]
    """
    mq = MonotonicQueue()
    result = []
    for i, num in enumerate(nums):
        mq.push(num)
        if i >= k - 1:
            result.append(mq.max())
            mq.pop(nums[i - k + 1])  # remove element leaving window
    return result


def sliding_window_minimum(nums, k):
    """Sliding window minimum — use increasing deque."""
    dq = deque()  # stores indices, values are increasing
    result = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] >= num:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:  # front is out of window
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


def constrained_subsequence_sum(nums, k):
    """
    LeetCode #1425: Max sum of subsequence where adjacent indices differ by ≤ k.
    dp[i] = max(dp[i-k..i-1]) + nums[i]
    Use monotonic deque to get max of sliding window of dp values.
    """
    n = len(nums)
    dp = nums[:]
    dq = deque([0])  # stores indices of dp in decreasing order of dp values

    for i in range(1, n):
        # Remove indices outside window
        while dq and dq[0] < i - k:
            dq.popleft()
        # dp[i] = max(0, dp[dq[0]]) + nums[i]
        dp[i] = max(dp[dq[0]], 0) + nums[i]
        # Maintain decreasing order
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        dq.append(i)

    return max(dp)
```

## Example Usage
```python
print(sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]

print(sliding_window_minimum([1,3,-1,-3,5,3,6,7], 3))
# [-1, -3, -3, -3, 3, 3]

print(constrained_subsequence_sum([10,2,-10,5,20], 2))
# 37 (10 + 2 + 5 + 20)
```

## Monotonic Queue vs Monotonic Stack

| Feature | Monotonic Stack | Monotonic Queue |
|---------|----------------|-----------------|
| Pop from | Back only | Both ends |
| Use case | Next greater/smaller | Sliding window max/min |
| Window support | No | Yes (pop expired front) |

## When to Use
- Sliding window maximum or minimum
- DP optimization where you need max/min of a range of previous states
- Any problem with "maximum/minimum in a window of size k"

## LeetCode Problems

---

### 1. Sliding Window Maximum — #239 (Hard)

**Problem**: Given an integer array and a window size k, return the maximum value in each sliding window of size k.

```
Input:  nums=[1,3,-1,-3,5,3,6,7], k=3
Output: [3,3,5,5,6,7]

Window positions:
[1,3,-1]  → max 3
[3,-1,-3] → max 3
[-1,-3,5] → max 5
[-3,5,3]  → max 5
[5,3,6]   → max 6
[3,6,7]   → max 7
```

**Hints**:
1. Monotonic decreasing deque of indices
2. Remove front when `dq[0] <= i - k` (outside window)
3. Remove back when `nums[dq[-1]] <= nums[i]` (can never be max while current exists)
4. `dq[0]` is always the index of the current window's maximum

---

### 2. Jump Game VI — #1696 (Medium)

**Problem**: Given an integer array and integer k, start at index 0. At each step, jump forward 1 to k indices. The score is the sum of values at visited indices. Return the maximum score to reach the last index.

```
Input:  nums=[1,-1,-2,4,-7,3], k=2
Output: 7
Path:   index 0 (1) → index 3 (4) → index 5 (3) = 1+4+3 = 8? 
        Wait: 0→1→3→5: 1+(-1)+4+3=7. Or 0→2→3→5: 1+(-2)+4+3=6.
        Best: 0→1→3→5 = 7

Input:  nums=[10,-5,-2,4,0,3], k=3
Output: 17
Path:   0→3→5: 10+4+3=17
```

**Hints**:
1. DP: `dp[i] = nums[i] + max(dp[i-k..i-1])`
2. Use a monotonic decreasing deque to get `max(dp[i-k..i-1])` in O(1)
3. Remove front when it's outside the window of size k

---

### 3. Constrained Subsequence Sum — #1425 (Hard)

**Problem**: Given an integer array and integer k, return the maximum sum of a non-empty subsequence where for every two consecutive elements in the subsequence, their indices differ by at most k.

```
Input:  nums=[10,2,-10,5,20], k=2
Output: 37
Subsequence: [10,2,5,20] (indices 0,1,3,4 — each gap ≤ 2)

Input:  nums=[-1,-2,-3], k=1
Output: -1  (must pick at least one element)

Input:  nums=[10,-2,-10,-5,20], k=2
Output: 23
Subsequence: [10,-2,-5,20] → 23? Or [10,20]? Indices 0 and 4, gap=4 > k=2.
Best: [10,-2,20] indices 0,1,4? Gap 1→4 = 3 > 2. 
Best valid: [10,-2,-5,20] indices 0,1,3,4 → 23.
```

**Hints**:
1. `dp[i] = nums[i] + max(0, max(dp[i-k..i-1]))`
2. Use a monotonic decreasing deque of dp indices to get the max in the window
3. If the best previous dp is negative, don't extend (take 0 instead)

---

### 4. Shortest Subarray with Sum at Least K — #862 (Hard)

**Problem**: Given an integer array (may contain negatives) and integer k, return the length of the shortest subarray with sum at least k. Return -1 if no such subarray exists.

```
Input:  nums=[1], k=1
Output: 1

Input:  nums=[1,2], k=4
Output: -1

Input:  nums=[2,-1,2], k=3
Output: 3  (entire array sums to 3)

Input:  nums=[84,-37,32,40,95], k=167
Output: 3  (subarray [32,40,95] = 167)
```

**Hints**:
1. Compute prefix sums; problem becomes: find shortest `[j, i]` where `prefix[i] - prefix[j] >= k`
2. Use a monotonic increasing deque of prefix sum indices
3. For each i, pop from front while `prefix[i] - prefix[dq[0]] >= k` (valid subarray found)
4. Then pop from back while `prefix[dq[-1]] >= prefix[i]` (maintain increasing order)
