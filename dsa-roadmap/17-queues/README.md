# Queues

A queue is a FIFO (First In, First Out) data structure. It supports enqueue (add to back), dequeue (remove from front), and peek in O(1). A deque (double-ended queue) supports O(1) operations at both ends.

## Key Concepts

- **Monotonic Deque:** A deque that maintains elements in monotonically increasing or decreasing order. Used for sliding window maximum/minimum problems.
- **BFS:** Queues are the natural data structure for breadth-first search.
- **Circular Queue:** Fixed-size queue using an array with wrap-around indices.

## Monotonic Deque Pattern

For sliding window maximum:
- Maintain a decreasing deque of indices.
- When adding a new element, remove all smaller elements from the back.
- Remove elements from the front when they're outside the window.
- The front always holds the maximum.

## Problems in This Section

| Problem | Difficulty |
|---------|-----------|
| [Number of Recent Calls](./number-of-recent-calls.md) | Easy |
| [Time Needed to Buy Tickets](./time-needed-to-buy-tickets.md) | Easy |
| [Moving Average from Data Stream](./moving-average-from-data-stream.md) | Easy |
| [Reveal Cards In Increasing Order](./reveal-cards-in-increasing-order.md) | Medium |
| [First Unique Number](./first-unique-number.md) | Medium |
| [Number of People Aware of a Secret](./number-of-people-aware-of-a-secret.md) | Medium |
| [Find the Winner of the Circular Game](./find-the-winner-of-the-circular-game.md) | Medium |
| [Continuous Subarrays](./continuous-subarrays.md) | Medium |
| [Jump Game VI](./jump-game-vi.md) | Medium |
| [Find the Most Competitive Subsequence](./find-the-most-competitive-subsequence.md) | Medium |
| [Count Partitions With Max-Min Difference at Most K](./count-partitions-with-max-min-difference-at-most-k.md) | Medium |
| [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](./longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.md) | Medium |
| [Sliding Window Maximum](./sliding-window-maximum.md) | Hard |
| [Max Value of Equation](./max-value-of-equation.md) | Hard |
| [Constrained Subsequence Sum](./constrained-subsequence-sum.md) | Hard |
| [Shortest Subarray with Sum at Least K](./shortest-subarray-with-sum-at-least-k.md) | Hard |
