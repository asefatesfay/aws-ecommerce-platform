# Majority Element II

**Difficulty:** Medium
**Pattern:** Boyer-Moore Voting (Extended)
**LeetCode:** #229

## Problem Statement

Given an integer array of size `n`, find all elements that appear more than `⌊n / 3⌋` times. Return all such elements in any order.

## Examples

### Example 1
**Input:** `nums = [3, 2, 3]`
**Output:** `[3]`

### Example 2
**Input:** `nums = [1, 2]`
**Output:** `[1, 2]`

### Example 3
**Input:** `nums = [1, 1, 1, 3, 3, 2, 2, 2]`
**Output:** `[1, 2]`

## Constraints
- `1 <= nums.length <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Hints

> 💡 **Hint 1:** How many elements can appear more than n/3 times? At most 2 (since 3 × (n/3 + 1) > n). So you're looking for at most 2 candidates.

> 💡 **Hint 2:** Extend Boyer-Moore Voting to track 2 candidates and 2 counts. When both counts are 0, assign the current element to an empty candidate slot. If it matches a candidate, increment that count; otherwise decrement both counts.

> 💡 **Hint 3:** After the first pass, you have at most 2 candidates. Do a second pass to verify each candidate actually appears more than n/3 times (the voting algorithm finds candidates, not guarantees).

## Approach 1: Brute Force (Hash Map)

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Count all frequencies, return those with count > n/3.

```python
from collections import Counter

def majority_element_brute(nums: list[int]) -> list[int]:
    n = len(nums)
    return [num for num, cnt in Counter(nums).items() if cnt > n // 3]
```

**Downside:** O(n) extra space.

---

## Approach 2: Boyer-Moore Voting (2 Candidates) — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

At most 2 elements can appear more than n/3 times. Track 2 candidates with 2 vote counts. First pass finds candidates, second pass verifies them.

### Why at Most 2 Candidates?

```
If 3 elements each appeared > n/3 times:
  total count > 3 × (n/3) = n → impossible.
So at most 2 elements can exceed the n/3 threshold.
```

### Visual Trace

```
nums = [1, 1, 1, 3, 3, 2, 2, 2]

Pass 1 (find candidates):
x=1: cand1=None → cand1=1, cnt1=1
x=1: x==cand1 → cnt1=2
x=1: x==cand1 → cnt1=3
x=3: cand2=None → cand2=3, cnt2=1
x=3: x==cand2 → cnt2=2
x=2: x≠cand1, x≠cand2 → cnt1=2, cnt2=1
x=2: x≠cand1, x≠cand2 → cnt1=1, cnt2=0
x=2: cnt2=0 → cand2=2, cnt2=1

Candidates: cand1=1, cand2=2

Pass 2 (verify):
nums.count(1)=3 > 8//3=2 ✓
nums.count(2)=3 > 8//3=2 ✓

Result: [1, 2] ✓
```

```python
def majority_element(nums: list[int]) -> list[int]:
    cand1 = cand2 = None
    cnt1 = cnt2 = 0

    for x in nums:
        if x == cand1:
            cnt1 += 1
        elif x == cand2:
            cnt2 += 1
        elif cnt1 == 0:
            cand1, cnt1 = x, 1
        elif cnt2 == 0:
            cand2, cnt2 = x, 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    return [c for c in (cand1, cand2)
            if c is not None and nums.count(c) > len(nums) // 3]
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Hash map | O(n) | O(n) | Simple, extra space |
| Boyer-Moore (2 candidates) | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Frequency threshold problems with strict O(1) extra space
- Understanding why at most 2 candidates can exceed n/3
- Follow-up to classic Boyer-Moore majority element

