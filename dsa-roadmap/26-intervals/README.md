# 26. Intervals

## Overview
Interval problems involve ranges `[start, end]`. The key operations are merging overlapping intervals, inserting new intervals, and finding non-overlapping subsets.

## Key Concepts
- **Overlap condition**: `a.start <= b.end && b.start <= a.end`
- **Merge**: if intervals overlap, merge into `[min(a.start, b.start), max(a.end, b.end)]`
- **Sort first**: almost always sort by start time before processing
- **Sweep line**: process events (start/end) in sorted order

## When to Use
- "Merge overlapping intervals" → sort + linear scan
- "Minimum rooms needed" → sort starts and ends separately
- "Remove minimum intervals to make non-overlapping" → greedy by end time
- "Meeting scheduler" → find gaps between busy intervals

## Problems
| Problem | Difficulty |
|---------|-----------|
| Summary Ranges | Easy |
| Meeting Rooms | Easy |
| Merge Intervals | Medium |
| Insert Interval | Medium |
| Non-overlapping Intervals | Medium |
| Meeting Rooms II | Medium |
| Partition Labels | Medium |
| Employee Free Time | Hard |
