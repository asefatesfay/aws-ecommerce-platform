# Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers (Opposite Ends)
**LeetCode:** #11
**Asked by:** Google, Microsoft, Adobe, Amazon

## Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.

## Examples

### Example 1
**Input:** `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
**Output:** `49`
**Explanation:** Lines at index 1 (height=8) and index 8 (height=7). Width=7, min height=7. Area = 7×7 = 49.

```
  8       8
  |       |   7
  |   6   |   |
  |   |   |   |
  |   | 5 | 4 |
  |   | | | | |
  | 2 | | | | | 3
  | | | | | | | |
  1 8 6 2 5 4 8 3 7
  0 1 2 3 4 5 6 7 8
        ←  width=7 →
```

### Example 2
**Input:** `height = [1, 1]`
**Output:** `1`

## Constraints
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Hints

> 💡 **Hint 1:** The area between two lines at indices `i` and `j` is `(j - i) * min(height[i], height[j])`. You want to maximize this.

> 💡 **Hint 2:** Start with the widest possible container (left=0, right=n-1). To potentially increase the area, you must increase the minimum height. Which pointer should you move?

> 💡 **Hint 3:** Always move the pointer pointing to the shorter line. Moving the taller line can only decrease or maintain the width while the height is still bounded by the shorter line — so it can never improve the area.

## Approach 1: Brute Force

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

Try every pair of lines and compute the area.

```python
def max_area_brute(height: list[int]) -> int:
    best = 0
    n = len(height)
    for i in range(n):
        for j in range(i + 1, n):
            area = (j - i) * min(height[i], height[j])
            best = max(best, area)
    return best
```

**Why it's slow:** O(n²) — for n=100,000 this is 5 billion pairs.

---

## Approach 2: Two Pointers — Optimal

**Time Complexity:** O(n)
**Space Complexity:** O(1)

Start with the widest container (left=0, right=n-1). To potentially increase area, move the pointer at the shorter line inward.

### Why Moving the Shorter Side is Correct

```
Current area = (right - left) * min(height[left], height[right])
Suppose height[left] <= height[right].

If we move right inward instead:
  Width decreases by 1.
  New height = min(height[left], height[right-1]) <= height[left]
  → Area can only decrease or stay same. No benefit.

So we MUST move left to have any chance of improvement.
```

### Visual Trace

```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          0  1  2  3  4  5  6  7  8

left=0, right=8: area=(8-0)*min(1,7)=8.  best=8.  h[0]=1<h[8]=7 → move left
left=1, right=8: area=(8-1)*min(8,7)=49. best=49. h[8]=7<h[1]=8 → move right
left=1, right=7: area=(7-1)*min(8,3)=18. best=49. h[7]=3<h[1]=8 → move right
left=1, right=6: area=(6-1)*min(8,8)=40. best=49. equal → move right
left=1, right=5: area=(5-1)*min(8,4)=16. best=49. h[5]=4<h[1]=8 → move right
left=1, right=4: area=(4-1)*min(8,5)=15. best=49. h[4]=5<h[1]=8 → move right
left=1, right=3: area=(3-1)*min(8,2)=4.  best=49. h[3]=2<h[1]=8 → move right
left=1, right=2: area=(2-1)*min(8,6)=6.  best=49. h[2]=6<h[1]=8 → move right
left=1, right=1: left==right → stop

Answer: 49 ✓
```

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

### Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute force | O(n²) | O(1) | Try all pairs |
| Two pointers | O(n) | O(1) | Optimal — greedy proof |

## Typical Interview Use Cases

- Classic two-pointer proof question — interviewers often ask "why move the shorter side?"
- Tests ability to reason about greedy correctness
- Google/Adobe frequently ask this as a warm-up before harder problems
