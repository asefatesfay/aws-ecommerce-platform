# Distribute Coins in Binary Tree

**Difficulty:** Medium
**Pattern:** DFS / Tree DP
**LeetCode:** #979

## Problem Statement

You are given the root of a binary tree with `n` nodes where each node in the tree has `node.val` coins. There are `n` coins in total throughout the whole tree. In one move, we may choose two adjacent nodes and move one coin from one node to the other. Return the minimum number of moves required to make every node have exactly one coin.

## Examples

### Example 1
**Input:** `root = [3,0,0]`
**Output:** `2`
**Explanation:** Node 3 has 3 coins. Move one to left child (1 move), move one to right child (1 move). Total = 2.

### Example 2
**Input:** `root = [0,3,0]`
**Output:** `3`
**Explanation:** Node with 3 coins must send 2 coins up to the root (2 moves), root sends 1 down to right child (1 move). Total = 3.

## Constraints
- The number of nodes in the tree is `n`
- `1 <= n <= 100`
- `0 <= Node.val <= n`
- The sum of all `Node.val` is `n`

## Hints

> 💡 **Hint 1:** Think about "flow" through each edge. The number of moves equals the total flow across all edges. The flow through an edge is the absolute number of coins that need to cross it.

> 💡 **Hint 2:** For each subtree, compute the "excess" coins: `excess = (number of nodes in subtree) - (coins in subtree)`. If excess > 0, that many coins need to flow out. If excess < 0, that many coins need to flow in. Either way, `|excess|` moves cross the edge to the parent.

> 💡 **Hint 3:** DFS returning excess for each subtree: `excess = node.val + left_excess + right_excess - 1`. Add `|left_excess| + |right_excess|` to the global move count. Return excess to the parent.

## Approach

**Time Complexity:** O(n)
**Space Complexity:** O(h) for the recursion stack

DFS computing excess coins per subtree. The number of moves equals the sum of absolute excesses across all edges. Each node contributes `|left_excess| + |right_excess|` moves.
