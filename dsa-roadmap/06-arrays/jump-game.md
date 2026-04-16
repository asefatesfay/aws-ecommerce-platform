# Jump Game

**Difficulty:** Medium
**Pattern:** Greedy
**LeetCode:** #55
**Asked by:** Microsoft, Google, Adobe

## Problem Statement

You are given an integer array `nums`. You are initially positioned at the first index. Each element `nums[i]` represents your maximum jump length from that position. Return `true` if you can reach the last index, or `false` otherwise.

## Examples

### Example 1
**Input:** `nums = [2, 3, 1, 1, 4]`
**Output:** `true`
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.

### Example 2
**Input:** `nums = [3, 2, 1, 0, 4]`
**Output:** `false`
**Explanation:** You will always arrive at index 3 with value 0. You can never reach index 4.

### Example 3
**Input:** `nums = [0]`
**Output:** `true`
**Explanation:** Already at the last index.

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Track the farthest index you can reach at any point. If you ever reach a position beyond the farthest reachable index, you're stuck.

> 💡 **Hint 2:** At each index `i`, update `farthest = max(farthest, i + nums[i])`. If `i > farthest` at any point, return False.

> 💡 **Hint 3:** If you make it through the entire loop without getting stuck, return True.

## Approach 1: Brute Force (BFS/DFS)

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

Try every possible jump sequence using BFS.

```python
from collections import deque

def can_jump_brute(nums: list[int]) -> bool:
    n = len(nums)
    visited = set()
    queue = deque([0])
    while queue:
        i = queue.popleft()
        if i == n - 1:
            return True
        if i in visited:
            continue
        visited.add(i)
        for jump in range(1, nums[i] + 1):
            if i + jump < n:
                queue.append(i + jump)
    return False
```

**Why it's slow:** Explores many redundant paths.

---

## Approach 2: DP (Bottom-Up)

**Time Complexity:** O(n²)
**Space Complexity:** O(n)

`dp[i] = True` if index i is reachable. For each reachable position, mark all positions it can reach.

```python
def can_jump_dp(nums: list[int]) -> bool:
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i in range(n):
        if not dp[i]:
            continue
        for jump in range(1, nums[i] + 1):
            if i + jump < n:
                dp[i + jump] = True

    return dp[n - 1]
```

---

## Approach 3: Greedy — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Track the farthest index reachable so far. If you ever reach a position beyond the farthest, you're stuck.

### Visual Trace

```
nums = [2, 3, 1, 1, 4]
        0  1  2  3  4

farthest=0
i=0: farthest=max(0, 0+2)=2. 0<=2 ✓
i=1: farthest=max(2, 1+3)=4. 1<=4 ✓
i=2: farthest=max(4, 2+1)=4. 2<=4 ✓
i=3: farthest=max(4, 3+1)=4. 3<=4 ✓
i=4: farthest=max(4, 4+4)=8. 4<=8 ✓ → True

nums = [3, 2, 1, 0, 4]
        0  1  2  3  4

farthest=0
i=0: farthest=max(0, 0+3)=3
i=1: farthest=max(3, 1+2)=3
i=2: farthest=max(3, 2+1)=3
i=3: farthest=max(3, 3+0)=3
i=4: 4 > farthest=3 → STUCK → False
```

```python
def can_jump(nums: list[int]) -> bool:
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| BFS | O(n²) | O(n) | Explores all paths |
| DP | O(n²) | O(n) | Marks reachable positions |
| Greedy | O(n) | O(1) | Optimal — single pass |

## Follow-up: Jump Game II — #45 (Minimum Jumps, Google/Microsoft)

Return the minimum number of jumps to reach the last index.

```python
def jump(nums: list[int]) -> int:
    """
    nums=[2,3,1,1,4] → 2 (0→1→4)
    nums=[2,3,0,1,4] → 2 (0→1→4)
    
    Greedy: at each "level" (current jump range), find the farthest
    you can reach in the next jump.
    """
    jumps = 0
    current_end = 0   # end of current jump range
    farthest = 0      # farthest reachable from current range

    for i in range(len(nums) - 1):  # don't need to jump from last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break

    return jumps

# Trace: nums=[2,3,1,1,4]
# i=0: farthest=2, i==current_end(0) → jumps=1, current_end=2
# i=1: farthest=4, i<current_end(2)
# i=2: farthest=4, i==current_end(2) → jumps=2, current_end=4 >= 4 → break
# Answer: 2
```

## Follow-up: Jump Game III — #1306 (Adobe)

Given array and start index, can you reach any index with value 0? From index i, you can jump to `i + arr[i]` or `i - arr[i]`.

```python
def can_reach(arr: list[int], start: int) -> bool:
    """
    arr=[4,2,3,0,3,1,2], start=5 → True (5→4→1→3, arr[3]=0)
    arr=[3,0,2,1,2], start=2 → False
    """
    n = len(arr)
    visited = set()
    stack = [start]
    while stack:
        i = stack.pop()
        if i < 0 or i >= n or i in visited:
            continue
        if arr[i] == 0:
            return True
        visited.add(i)
        stack.append(i + arr[i])
        stack.append(i - arr[i])
    return False
```

## Typical Interview Use Cases

- Classic greedy problem at Microsoft/Google
- Tests ability to identify greedy invariant (farthest reachable)
- Jump Game II (minimum jumps) is a common follow-up in the same session
