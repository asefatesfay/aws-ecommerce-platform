# Assign Cookies

**Difficulty:** Easy
**Pattern:** Greedy — Sort and Match
**LeetCode:** #455

## Problem Statement
You have `g` children with greed factors and `s` cookie sizes. A child is content if their greed factor ≤ cookie size. Maximize the number of content children.

## Examples

### Example 1
**Input:** `g = [1,2,3]`, `s = [1,1]`
**Output:** `1`

### Example 2
**Input:** `g = [1,2]`, `s = [1,2,3]`
**Output:** `2`

## Constraints
- `1 <= g.length, s.length <= 3×10⁴`
- `1 <= g[i], s[j] <= 2³¹ - 1`

## Hints

> 💡 **Hint 1:** Sort both arrays. Try to satisfy the least greedy child first with the smallest sufficient cookie.

> 💡 **Hint 2:** Use two pointers — one for children, one for cookies. If `s[j] >= g[i]`, assign cookie j to child i and advance both pointers. Otherwise advance only the cookie pointer.

> 💡 **Hint 3:** Count how many children get assigned a cookie.

## Approach
**Time Complexity:** O(N log N + M log M)
**Space Complexity:** O(1)

Sort both, use two pointers to greedily match smallest sufficient cookie to least greedy child.
