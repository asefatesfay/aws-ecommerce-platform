# Fruit Into Baskets

**Difficulty:** Medium
**Pattern:** Sliding Window (Variable) — At Most K Distinct
**LeetCode:** #904

## Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i`th tree produces. You want to collect as much fruit as possible. However, the owner has some strict rules:
- You only have two baskets, and each basket can only hold a single type of fruit.
- Starting from any tree, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Return the maximum number of fruits you can pick.

## Examples

### Example 1
**Input:** `fruits = [1, 2, 1]`
**Output:** `3`

### Example 2
**Input:** `fruits = [0, 1, 2, 2]`
**Output:** `3`
**Explanation:** Pick [1,2,2] — two types, fits in two baskets.

### Example 3
**Input:** `fruits = [1, 2, 3, 2, 2]`
**Output:** `4`
**Explanation:** Pick [2,3,2,2].

## Constraints
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Hints

> 💡 **Hint 1:** Rephrase: find the longest subarray with at most 2 distinct values.

> 💡 **Hint 2:** Variable sliding window with a HashMap tracking the count of each fruit type in the window. Expand right; when distinct types > 2, shrink from the left.

> 💡 **Hint 3:** When a fruit type's count reaches 0, remove it from the map. Track the maximum window size.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(1) (at most 2 entries in the map)

Variable window with a frequency map. Shrink when more than 2 distinct types are in the window. Track maximum window size.
