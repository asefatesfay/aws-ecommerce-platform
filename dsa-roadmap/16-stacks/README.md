# Stacks

A stack is a LIFO (Last In, First Out) data structure. It supports push (add to top), pop (remove from top), and peek (view top) in O(1).

## Key Concepts

- **Monotonic Stack:** A stack that maintains elements in monotonically increasing or decreasing order. Used for "next greater/smaller element" problems.
- **Expression evaluation:** Stacks are natural for parsing and evaluating expressions (infix, postfix).
- **Parenthesis matching:** Classic stack application — push open brackets, pop and match on close brackets.
- **Undo/redo:** Stack of states.

## Monotonic Stack Pattern

For "next greater element to the right":
- Scan left to right. Maintain a decreasing stack.
- When you see a larger element, pop elements from the stack — the current element is their "next greater".
- Push the current element.

For "next smaller element": maintain an increasing stack.

## When to Recognize Stack Problems

- "Valid parentheses" or bracket matching
- "Next greater/smaller element"
- "Evaluate expression"
- "Undo operations"
- "Largest rectangle" or area problems
- Nested structures (HTML tags, function calls)

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Valid Parentheses](./valid-parentheses.md) | Easy |
| [Remove All Adjacent Duplicates In String](./remove-all-adjacent-duplicates-in-string.md) | Easy |
| [Baseball Game](./baseball-game.md) | Easy |
| [Maximum Nesting Depth of the Parentheses](./maximum-nesting-depth-of-the-parentheses.md) | Easy |
| [Min Stack](./min-stack.md) | Medium |
| [Remove Duplicate Letters](./remove-duplicate-letters.md) | Medium |
| [Removing Stars From a String](./removing-stars-from-a-string.md) | Medium |
| [Evaluate Reverse Polish Notation](./evaluate-reverse-polish-notation.md) | Medium |
| [Basic Calculator II](./basic-calculator-ii.md) | Medium |
| [Asteroid Collision](./asteroid-collision.md) | Medium |
| [Car Fleet](./car-fleet.md) | Medium |
| [Valid Parenthesis String](./valid-parenthesis-string.md) | Medium |
| [Validate Stack Sequences](./validate-stack-sequences.md) | Medium |
| [Minimum Remove to Make Valid Parentheses](./minimum-remove-to-make-valid-parentheses.md) | Medium |
| [Simplify Path](./simplify-path.md) | Medium |
| [Exclusive Time of Functions](./exclusive-time-of-functions.md) | Medium |
| [Basic Calculator](./basic-calculator.md) | Medium |
| [Longest Valid Parentheses](./longest-valid-parentheses.md) | Hard |
| [Next Greater Element I](./next-greater-element-i.md) | Easy |
| [Final Prices With a Special Discount in a Shop](./final-prices-with-a-special-discount-in-a-shop.md) | Easy |
| [Daily Temperatures](./daily-temperatures.md) | Medium |
| [Online Stock Span](./online-stock-span.md) | Medium |
| [132 Pattern](./132-pattern.md) | Medium |
| [Next Greater Element II](./next-greater-element-ii.md) | Medium |
| [Buildings With an Ocean View](./buildings-with-an-ocean-view.md) | Medium |
| [Remove K Digits](./remove-k-digits.md) | Medium |
| [Maximum Width Ramp](./maximum-width-ramp.md) | Medium |
| [Max Chunks To Make Sorted](./max-chunks-to-make-sorted.md) | Medium |
| [Sum of Subarray Minimums](./sum-of-subarray-minimums.md) | Medium |
| [Sum of Subarray Ranges](./sum-of-subarray-ranges.md) | Medium |
| [Shortest Unsorted Continuous Subarray](./shortest-unsorted-continuous-subarray.md) | Medium |
| [Next Greater Node In Linked List](./next-greater-node-in-linked-list.md) | Medium |
| [Create Maximum Number](./create-maximum-number.md) | Hard |
| [Number of Visible People in a Queue](./number-of-visible-people-in-a-queue.md) | Hard |
| [Largest Rectangle in Histogram](./largest-rectangle-in-histogram.md) | Hard |
