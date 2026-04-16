# Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers / Prefix-Suffix Max
**LeetCode:** #42
**Asked by:** Google, Microsoft, Adobe, Amazon

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples

### Example 1
**Input:** `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
**Output:** `6`

```
       3
       |
   2   | 2   2
   |   | | ~ |
 1 | 1 | | 1 | 1
 | | | | | | | |
 0 1 0 2 1 0 1 3 2 1 2 1
         ~ = trapped water
```

Water trapped: positions 2(1), 4(1), 5(2), 6(1), 9(1) = 6 units

### Example 2
**Input:** `height = [4, 2, 0, 3, 2, 5]`
**Output:** `9`

## Constraints
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Hints

> 💡 **Hint 1:** Water at position `i` is determined by the minimum of the tallest bar to its left and the tallest bar to its right, minus the height at `i`. `water[i] = max(0, min(max_left[i], max_right[i]) - height[i])`

> 💡 **Hint 2:** Precompute `max_left[i]` (max height from 0 to i) and `max_right[i]` (max height from i to n-1). Then sum up water at each position.

> 💡 **Hint 3:** For O(1) space, use two pointers. The key insight: if `max_left < max_right`, the water at the left pointer is determined by `max_left` (the right side is guaranteed to be at least `max_right`).

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

For each position, scan left and right to find the tallest walls.

```python
def trap_brute(height: list[int]) -> int:
    n = len(height)
    water = 0
    for i in range(1, n - 1):
        max_left = max(height[:i+1])
        max_right = max(height[i:])
        water += max(0, min(max_left, max_right) - height[i])
    return water
```

**Why it's slow:** Recomputes max_left and max_right for every position — O(n) work per position.

---

## Approach 2: Prefix/Suffix Arrays

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Precompute max_left and max_right arrays in two passes, then compute water in a third pass.

```python
def trap_prefix_suffix(height: list[int]) -> int:
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n

    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    water = 0
    for i in range(n):
        water += max(0, min(max_left[i], max_right[i]) - height[i])
    return water
```

### Visual Trace (Prefix/Suffix)

```
height   = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
max_left = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
max_right= [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]

water[i] = max(0, min(max_left[i], max_right[i]) - height[i])
i=2: min(1,3)-0 = 1
i=4: min(2,3)-1 = 1
i=5: min(2,3)-0 = 2
i=6: min(2,3)-1 = 1
i=9: min(3,2)-1 = 1
Total = 6 ✓
```

---

## Approach 3: Two Pointers — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Key insight: if `max_left < max_right`, the water at the left pointer is determined solely by `max_left` (the right wall is guaranteed to be at least `max_right`). Process whichever side has the smaller max.

```python
def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_left = max_right = 0
    water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]      # new max, no water here
            else:
                water += max_left - height[left]  # trapped water
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]
            else:
                water += max_right - height[right]
            right -= 1

    return water
```

### Visual Trace (Two Pointers)

```
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
          0  1  2  3  4  5  6  7  8  9 10 11

left=0, right=11, max_l=0, max_r=0
  h[0]=0 <= h[11]=1 → left side. h[0]=0 >= max_l=0 → max_l=0. left=1

left=1, right=11, max_l=0, max_r=0
  h[1]=1 <= h[11]=1 → left side. h[1]=1 >= max_l=0 → max_l=1. left=2

left=2, right=11, max_l=1, max_r=0
  h[2]=0 <= h[11]=1 → left side. h[2]=0 < max_l=1 → water+=1. left=3

... (continues, total water = 6)
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Recomputes max each time |
| Prefix/suffix arrays | O(n) | O(n) | Three passes, clear logic |
| Two pointers | O(n) | O(1) | Best — one pass, O(1) space |

## Typical Interview Use Cases

- Hard array problem at Google/Microsoft/Adobe — tests multiple approaches
- Interviewers often ask for the O(1) space solution after the O(n) one
- Tests ability to reason about invariants in two-pointer problems
