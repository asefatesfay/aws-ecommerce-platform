# Maximum XOR of Two Numbers in an Array

**Difficulty:** Medium
**Pattern:** Trie + Bit Manipulation
**LeetCode:** #421

## Problem Statement
Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]` where `0 <= i <= j < n`.

## Examples

### Example 1
**Input:** `nums = [3,10,5,25,2,8]`
**Output:** `28`
**Explanation:** `5 XOR 25 = 28`

### Example 2
**Input:** `nums = [14,70,53,83,49,91,36,80,92,51,66,70]`
**Output:** `127`

## Constraints
- `1 <= nums.length <= 2×10⁵`
- `0 <= nums[i] <= 2³¹ - 1`

## Hints

> 💡 **Hint 1:** Build a binary Trie where each number is inserted bit by bit from the most significant bit (bit 31) down to bit 0.

> 💡 **Hint 2:** For each number, greedily try to go the opposite direction at each bit level — if the current bit is 0, try to go to the 1-child (to maximize XOR), and vice versa.

> 💡 **Hint 3:** If the opposite child doesn't exist, take the same-direction child. Accumulate the XOR value as you traverse.

## Approach
**Time Complexity:** O(N × 32)
**Space Complexity:** O(N × 32)

Insert all numbers into a binary Trie (32 levels). For each number, greedily traverse the Trie choosing the opposite bit at each level to maximize XOR.
