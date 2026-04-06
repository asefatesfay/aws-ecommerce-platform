# 32. Advanced Topics

## Overview
This section combines advanced string algorithms, range-query data structures, and line-sweep/computational geometry techniques. These problems are usually pattern-combination heavy and require stronger data-structure modeling.

## Key Concepts
- **Advanced string matching**: prefix-function, rolling hash, suffix-style reasoning
- **Fenwick/Segment Trees**: dynamic range query and update support
- **Order statistics**: counting inversions/smaller elements with indexed structures
- **Line sweep**: event sorting and active interval tracking

## Common Patterns
| Pattern | Key Idea |
|---------|----------|
| Prefix-function / KMP | Reuse border information in string matching |
| Rolling hash + binary search | Check duplicate substrings efficiently |
| Segment tree / BIT | Maintain mutable range aggregates |
| Coordinate compression | Make sparse coordinates tractable |
| Sweep line + events | Process geometric overlaps by sorted boundaries |

## When to Use
- Hard string tasks involving repeated patterns or longest duplicate prefixes
- Mutable range sum/count queries
- Dynamic interval/skyline/coverage area problems
- Geometry union/overlap validation in 2D

## Problems
### String Matching
| Problem | Difficulty | LeetCode |
|---------|------------|----------|
| [Repeated Substring Pattern](./repeated-substring-pattern.md) | Easy | #459 |
| [Repeated String Match](./repeated-string-match.md) | Medium | #686 |
| [Number of Distinct Substrings in a String](./number-of-distinct-substrings-in-a-string.md) | Medium | #1698 |
| [Shortest Palindrome](./shortest-palindrome.md) | Hard | #214 |
| [Longest Happy Prefix](./longest-happy-prefix.md) | Hard | #1392 |
| [Longest Duplicate Substring](./longest-duplicate-substring.md) | Hard | #1044 |

### Advanced Data Structures
| Problem | Difficulty | LeetCode |
|---------|------------|----------|
| [Range Sum Query - Mutable](./range-sum-query-mutable.md) | Medium | #307 |
| [Range Sum Query 2D - Mutable](./range-sum-query-2d-mutable.md) | Medium | #308 |
| [Count of Smaller Numbers After Self](./count-of-smaller-numbers-after-self.md) | Hard | #315 |
| [Falling Squares](./falling-squares.md) | Hard | #699 |
| [Block Placement Queries](./block-placement-queries.md) | Hard | #3161 |
| [Longest Balanced Subarray II](./longest-balanced-subarray-ii.md) | Hard | Custom |
| [Number of Pairs Satisfying Inequality](./number-of-pairs-satisfying-inequality.md) | Hard | #2426 |

### Line Sweep
| Problem | Difficulty | LeetCode |
|---------|------------|----------|
| [Minimum Interval to Include Each Query](./minimum-interval-to-include-each-query.md) | Hard | #1851 |
| [The Skyline Problem](./the-skyline-problem.md) | Hard | #218 |
| [Rectangle Area II](./rectangle-area-ii.md) | Hard | #850 |
| [Perfect Rectangle](./perfect-rectangle.md) | Hard | #391 |

## Progress
- Implemented in this section: 17 indexed problems
