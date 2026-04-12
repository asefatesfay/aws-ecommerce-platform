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

| Problem | Difficulty | Pattern |
|---------|-----------|---------|
| Sliding Window Maximum (#239) | Hard | Decreasing deque |
| Jump Game VI (#1696) | Medium | DP + deque optimization |
| Constrained Subsequence Sum (#1425) | Hard | DP + deque |
| Shortest Subarray with Sum ≥ K (#862) | Hard | Increasing deque |
| Max Value of Equation (#1499) | Hard | Decreasing deque |
| Longest Continuous Subarray Abs Diff ≤ Limit (#1438) | Medium | Two deques (min+max) |
| Count Partitions with Max-Min Diff ≤ K (#2779) | Medium | Two deques |
| Find the Most Competitive Subsequence (#1673) | Medium | Increasing deque |
