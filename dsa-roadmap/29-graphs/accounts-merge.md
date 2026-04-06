# Accounts Merge

**Difficulty:** Medium
**Pattern:** Union-Find / DFS
**LeetCode:** #721

## Problem Statement
Given a list of accounts where each account is `[name, email1, email2, ...]`, merge accounts that share at least one email. Return merged accounts sorted.

## Examples

### Example 1
**Input:** `accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
**Output:** `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`

## Constraints
- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`

## Hints

> 💡 **Hint 1:** Union-Find approach: union all emails within the same account. Map each email to its account owner.

> 💡 **Hint 2:** After union-find, group emails by their root representative. Each group is a merged account.

> 💡 **Hint 3:** Sort emails within each group and prepend the account name.

## Approach
**Time Complexity:** O(N × K × α(N)) where K = emails per account
**Space Complexity:** O(N × K)

Union-Find on emails. All emails in the same account are unioned. Group by root, sort, and attach name.
