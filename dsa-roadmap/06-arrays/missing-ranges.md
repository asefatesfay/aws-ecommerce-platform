# Missing Ranges

**Difficulty:** Easy
**Pattern:** Array / Linear Scan
**LeetCode:** #163

## Problem Statement

You are given an inclusive range `[lower, upper]` and a sorted unique integer array `nums`, where all elements are within the inclusive range. A number `x` is considered missing if `x` is in `[lower, upper]` and `x` is not in `nums`.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. Each range `[a, b]` in the list should be output as:
- `"a->b"` if `a != b`
- `"a"` if `a == b`

## Examples

### Example 1
**Input:** `nums = [0, 1, 3, 50, 75]`, `lower = 0`, `upper = 99`
**Output:** `["2", "4->49", "51->74", "76->99"]`

### Example 2
**Input:** `nums = [-1]`, `lower = -1`, `upper = -1`
**Output:** `[]`
**Explanation:** No missing numbers.

## Constraints
- `-10^9 <= lower <= upper <= 10^9`
- `0 <= nums.length <= 100`
- `lower <= nums[i] <= upper`
- All values in `nums` are unique

## Hints

> 💡 **Hint 1:** Think of the gaps between consecutive elements (and between the boundaries and the first/last elements). Each gap that is more than 1 wide represents a missing range.

> 💡 **Hint 2:** Add sentinel values: treat `lower - 1` as a virtual element before the array and `upper + 1` as a virtual element after. Then check gaps between consecutive pairs.

> 💡 **Hint 3:** For each consecutive pair (prev, curr), if curr - prev > 1, there's a missing range from prev+1 to curr-1. Format it as a single number or a range accordingly.

## Approach 1: Brute Force

**Time Complexity:** O((upper - lower) × n)
**Space Complexity:** O(1)

Check every number in [lower, upper] against the array.

```python
def find_missing_ranges_brute(nums: list[int], lower: int, upper: int) -> list[str]:
    num_set = set(nums)
    missing = []
    i = lower
    while i <= upper:
        if i not in num_set:
            start = i
            while i <= upper and i not in num_set:
                i += 1
            end = i - 1
            missing.append(str(start) if start == end else f"{start}->{end}")
        else:
            i += 1
    return missing
```

**Downside:** O(upper - lower) which can be up to 2×10⁹ — completely impractical.

---

## Approach 2: Sentinel + Gap Detection — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1) extra

Add virtual sentinels `lower-1` before and `upper+1` after. For each consecutive pair, if the gap is > 1, there's a missing range.

### Visual Trace

```
nums=[0,1,3,50,75], lower=0, upper=99

Add sentinels: prev = lower-1 = -1
Iterate: nums + [upper+1] = [0,1,3,50,75,100]

cur=0:  gap = 0-(-1) = 1 → no missing (0 is in range)
        prev=0
cur=1:  gap = 1-0 = 1 → no missing
        prev=1
cur=3:  gap = 3-1 = 2 → missing: prev+1=2 to cur-1=2 → "2"
        prev=3
cur=50: gap = 50-3 = 47 → missing: 4 to 49 → "4->49"
        prev=50
cur=75: gap = 75-50 = 25 → missing: 51 to 74 → "51->74"
        prev=75
cur=100: gap = 100-75 = 25 → missing: 76 to 99 → "76->99"

Result: ["2","4->49","51->74","76->99"] ✓
```

```python
def find_missing_ranges(nums: list[int], lower: int, upper: int) -> list[str]:
    def fmt(lo: int, hi: int) -> str:
        return str(lo) if lo == hi else f"{lo}->{hi}"

    result = []
    prev = lower - 1

    for cur in nums + [upper + 1]:
        if cur - prev >= 2:
            result.append(fmt(prev + 1, cur - 1))
        prev = cur

    return result
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(upper-lower) | O(1) | Impractical for large ranges |
| Sentinel + gap | O(n) | O(1) | Optimal |

## Typical Interview Use Cases

- Gap detection in sorted arrays
- Inclusive range boundary handling with sentinels
- Formatting logic mixed with algorithmic scanning

