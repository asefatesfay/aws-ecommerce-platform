# Koko Eating Bananas

**Difficulty:** Medium
**Pattern:** Binary Search on Answer
**LeetCode:** #875

## Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours. Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour. Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## Examples

### Example 1
**Input:** `piles = [3,6,7,11]`, `h = 8`
**Output:** `4`

### Example 2
**Input:** `piles = [30,11,23,4,20]`, `h = 5`
**Output:** `30`

## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Hints

> 💡 **Hint 1:** The answer is between 1 and max(piles). The condition "can finish in h hours at speed k" is monotonic: if k works, k+1 also works.

> 💡 **Hint 2:** Binary search on k. For a given k, compute total hours = sum(ceil(pile/k) for pile in piles).

> 💡 **Hint 3:** If total hours ≤ h, k is feasible — try smaller (right = mid). Otherwise, try larger (left = mid + 1). Return left.

## Approach

**Time Complexity:** O(n log(max_pile))
**Space Complexity:** O(1)

Binary search on the answer space [1, max(piles)]. Check feasibility by computing total hours needed at speed k.
