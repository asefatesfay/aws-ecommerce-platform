# Search Suggestions System

**Difficulty:** Medium
**Pattern:** Trie / Binary Search
**LeetCode:** #1268

## Problem Statement
Given an array of `products` and a `searchWord`, design a system that suggests at most 3 product names from `products` after each character of `searchWord` is typed. Suggested products should have a common prefix with `searchWord`. Return the suggestions sorted lexicographically.

## Examples

### Example 1
**Input:** `products = ["mobile","mouse","moneypot","monitor","mousepad"]`, `searchWord = "mouse"`
**Output:** `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`

### Example 2
**Input:** `products = ["havana"]`, `searchWord = "havana"`
**Output:** `[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]`

## Constraints
- `1 <= products.length <= 1000`
- `1 <= products[i].length <= 3000`
- All products are unique

## Hints

> 💡 **Hint 1:** Sort the products array first. Then for each prefix of `searchWord`, find matching products.

> 💡 **Hint 2:** Binary search approach: after sorting, use `bisect_left` to find where the current prefix would be inserted, then take up to 3 products starting from that position that still match the prefix.

> 💡 **Hint 3:** Trie approach: insert all products into a Trie. At each node, store up to 3 lexicographically smallest words. Traverse the Trie following the search prefix.

## Approach
**Time Complexity:** O(N log N + M × log N) where M = searchWord length
**Space Complexity:** O(N × L) for Trie

Sort products, then for each prefix use binary search to find the first matching product and collect up to 3 consecutive matches.
