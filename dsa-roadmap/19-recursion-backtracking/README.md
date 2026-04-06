# Recursion & Backtracking

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") candidates that can't lead to a valid solution.

## Core Template

```
def backtrack(state, choices):
    if is_solution(state):
        record(state)
        return
    
    for choice in choices:
        if is_valid(choice, state):
            make_choice(choice, state)
            backtrack(state, remaining_choices)
            undo_choice(choice, state)  # backtrack
```

## Key Patterns

### Subsets
Generate all subsets. At each element, choose to include or exclude.

### Permutations
Generate all orderings. At each position, try all unused elements.

### Combinations
Generate all k-element subsets. At each step, choose from remaining elements (only forward to avoid duplicates).

### Constraint Satisfaction
N-Queens, Sudoku — place elements satisfying constraints, backtrack when stuck.

## Pruning

The key to efficient backtracking is pruning — cutting off branches early:
- Skip duplicates (sort first, skip same value at same level)
- Check constraints before recursing
- Use bounds to prune (e.g., remaining sum can't reach target)

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Merge Two Sorted Lists](./merge-two-sorted-lists.md) | Easy |
| [Pow(x, n)](./pow-x-n.md) | Medium |
| [Decode String](./decode-string.md) | Medium |
| [Subsets](./subsets.md) | Medium |
| [Combination Sum](./combination-sum.md) | Medium |
| [Combination Sum II](./combination-sum-ii.md) | Medium |
| [Subsets II](./subsets-ii.md) | Medium |
| [Combination Sum III](./combination-sum-iii.md) | Medium |
| [Combinations](./combinations.md) | Medium |
| [Permutations](./permutations.md) | Medium |
| [Letter Combinations of a Phone Number](./letter-combinations-of-a-phone-number.md) | Medium |
| [Permutations II](./permutations-ii.md) | Medium |
| [Generate Parentheses](./generate-parentheses.md) | Medium |
| [Palindrome Partitioning](./palindrome-partitioning.md) | Medium |
| [Restore IP Addresses](./restore-ip-addresses.md) | Medium |
| [N-Queens](./n-queens.md) | Hard |
| [Special Binary String](./special-binary-string.md) | Hard |
| [Integer to English Words](./integer-to-english-words.md) | Hard |
| [Unique Paths III](./unique-paths-iii.md) | Hard |
| [Remove Invalid Parentheses](./remove-invalid-parentheses.md) | Hard |
| [Sudoku Solver](./sudoku-solver.md) | Hard |
