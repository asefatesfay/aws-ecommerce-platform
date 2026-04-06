# Final Prices With a Special Discount in a Shop

**Difficulty:** Easy
**Pattern:** Monotonic Stack
**LeetCode:** #1475

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of the `i`th item in a shop. There is a special discount for items in the shop. If you buy the `i`th item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all. Return an integer array where the `i`th element is the final price you will pay for the `i`th item of the shop considering the special discount.

## Examples

### Example 1
**Input:** `prices = [8,4,6,2,3]`
**Output:** `[4,2,4,2,3]`
**Explanation:** For item 0 (price 8): next price ≤ 8 is 4 (index 1). Discount = 4. Final = 4.

### Example 2
**Input:** `prices = [1,2,3,4,5]`
**Output:** `[1,2,3,4,5]`
**Explanation:** No item has a smaller or equal price to its right.

## Constraints
- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 10^3`

## Hints

> 💡 **Hint 1:** For each item, you need the next item with price ≤ current price. This is the "next smaller or equal element" pattern.

> 💡 **Hint 2:** Use a monotonic non-decreasing stack of indices. When you find a price ≤ stack top's price, the current item is the discount for the stack top.

> 💡 **Hint 3:** Pop all indices from the stack whose prices are ≥ current price. Apply the discount. Push the current index.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(n)

Monotonic stack: find next smaller-or-equal element for each price. Apply as discount.
