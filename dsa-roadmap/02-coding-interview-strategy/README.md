# Coding Interview Strategy

Before writing a single line of code, you need a repeatable process. Interviewers evaluate *how* you think, not just whether you get the right answer.

## The UMPIRE Method

A structured framework for tackling any coding problem:

### U — Understand
- Read the problem twice
- Identify: input type, output type, what "success" looks like
- Ask clarifying questions: edge cases, constraints, expected input range
- Example questions: "Can the array be empty?", "Are there negative numbers?", "Is the input sorted?"

### M — Match
- What pattern does this look like? (sorted array → binary search, subarray sum → prefix sum, etc.)
- Have you seen a similar problem before?
- What data structures are relevant?

### P — Plan
- Outline your approach in plain English before coding
- Identify the time and space complexity of your plan
- Consider edge cases upfront

### I — Implement
- Code your plan — don't jump straight to clever tricks
- Write clean, readable code with meaningful variable names
- Talk through what you're doing as you write

### R — Review
- Trace through your code with the given examples
- Check edge cases: empty input, single element, all same values, negative numbers
- Look for off-by-one errors

### E — Evaluate
- State the time and space complexity
- Discuss trade-offs
- Mention potential optimizations if time allows

---

## Complexity Targets by Constraint

| Input size (n) | Expected complexity |
|----------------|---------------------|
| n ≤ 20 | O(2^n) or O(n!) — backtracking/brute force OK |
| n ≤ 1,000 | O(n²) acceptable |
| n ≤ 100,000 | O(n log n) or O(n) required |
| n ≤ 10,000,000 | O(n) or O(log n) required |

---

## Common Mistakes to Avoid

- Jumping to code before understanding the problem
- Not considering edge cases (empty array, single element, overflow)
- Confusing 0-indexed vs 1-indexed
- Forgetting to handle null/None inputs
- Not communicating your thought process

---

## When You're Stuck

1. Work through a small example by hand
2. Think about the brute force first — then optimize
3. Ask yourself: "What information do I have? What do I need?"
4. Consider: can I sort the input? Can I use extra space?
5. Think about what data structure would make the key operation O(1)

---

## After the Interview

- Write down what you learned regardless of outcome
- If you got stuck, solve the problem fully afterward
- Track patterns you keep missing — those are your weak spots
