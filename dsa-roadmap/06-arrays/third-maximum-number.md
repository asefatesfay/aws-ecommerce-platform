# Third Maximum Number

**Difficulty:** Easy
**Pattern:** Array / Tracking Top-K
**LeetCode:** #414

## Problem Statement

Given an integer array `nums`, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

## Examples

### Example 1
**Input:** `nums = [3, 2, 1]`
**Output:** `1`
**Explanation:** The third maximum is 1.

### Example 2
**Input:** `nums = [1, 2]`
**Output:** `2`
**Explanation:** The third maximum does not exist, so return the maximum (2).

### Example 3
**Input:** `nums = [2, 2, 3, 1]`
**Output:** `1`
**Explanation:** The third distinct maximum is 1. Note that 2 appears twice but counts as one distinct value.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Hints

> 💡 **Hint 1:** You need to track the top 3 distinct values. Use three variables: first, second, third maximum.

> 💡 **Hint 2:** Initialize all three to negative infinity. For each number, update the three variables carefully — skip duplicates, and cascade updates (if a number beats first, the old first becomes second, old second becomes third).

> 💡 **Hint 3:** Be careful with the initial values — since nums can contain `Integer.MIN_VALUE`, use a sentinel like `None` or a separate boolean to track whether each slot has been filled.

## Approach 1: Brute Force (Sort)

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

Sort, deduplicate, return the third element from the end (or first if fewer than 3 distinct).

```python
def third_max_sort(nums: list[int]) -> int:
    unique = sorted(set(nums), reverse=True)
    return unique[2] if len(unique) >= 3 else unique[0]
```

**Downside:** O(n log n) and O(n) extra space. Can we do O(n) time, O(1) space?

---

## Approach 2: Track Top-3 — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Maintain three variables for the top 3 distinct values. Cascade updates downward when a new maximum is found.

### Visual Trace

```
nums = [2, 2, 3, 1]

first=None, second=None, third=None

x=2: 2>None → third=None, second=None, first=2
x=2: x==first → skip
x=3: 3>first=2 → third=None, second=2, first=3
x=1: 1<first=3, 1<second=2, 1>third=None → third=1

third=1 is not None → return 1 ✓
```

```python
def third_max(nums: list[int]) -> int:
    first = second = third = None

    for x in nums:
        if x == first or x == second or x == third:
            continue  # skip duplicates
        if first is None or x > first:
            third = second
            second = first
            first = x
        elif second is None or x > second:
            third = second
            second = x
        elif third is None or x > third:
            third = x

    return third if third is not None else first
```

### Edge Case: `None` vs `-inf`

```
Why use None instead of float('-inf')?
nums can contain -2^31 (Python's int min equivalent).
If we initialize to float('-inf'), we can't distinguish
"third slot not yet filled" from "third slot filled with -inf".
Using None as a sentinel avoids this.
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Sort + deduplicate | O(n log n) | O(n) | Simple |
| Track top-3 | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Distinct top-k tracking in one pass
- Sentinel handling and duplicate filtering
- Alternative to sorting when only small-order statistics are needed

