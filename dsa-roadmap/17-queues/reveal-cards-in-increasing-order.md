# Reveal Cards In Increasing Order

**Difficulty:** Medium
**Pattern:** Queue Simulation
**LeetCode:** #950

## Problem Statement

You are given an integer array `deck`. There is a deck of cards where every card has a unique integer. The deck is shuffled. One by one, from the top of the deck, you reveal the top card of the deck, then move the next top card of the deck to the bottom of the deck. You stop when all cards are revealed. Return an ordering of the deck that would reveal the cards in increasing order.

## Examples

### Example 1
**Input:** `deck = [17,13,11,2,3,5,7]`
**Output:** `[2,13,3,11,5,17,7]`
**Explanation:** Revealing in order: 2,3,5,7,11,13,17.

### Example 2
**Input:** `deck = [1,1000]`
**Output:** `[1,1000]`

## Constraints
- `1 <= deck.length <= 1000`
- `1 <= deck[i] <= 10^6`
- All values in `deck` are unique

## Hints

> 💡 **Hint 1:** Simulate the reveal process in reverse. Sort the deck. Place cards from largest to smallest.

> 💡 **Hint 2:** Use a queue of indices [0, 1, 2, ..., n-1]. For each card (sorted descending): place it at the front index of the queue, then move the back index to the front.

> 💡 **Hint 3:** Alternatively, simulate forward: use a queue of indices, place sorted cards at the positions revealed by the simulation.

## Approach

**Time Complexity:** O(n log n)
**Space Complexity:** O(n)

Sort deck. Use a queue of indices to simulate the reveal order. Place sorted cards at the simulated positions.
