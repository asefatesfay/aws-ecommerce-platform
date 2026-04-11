# Input: intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    # sort intervals based on their end time
    intervals.sort(key=lambda x: x[1])
    removed = 0
    
    prev_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            removed += 1
        else:
            prev_end = intervals[i][1]
    
    return removed

if __name__ == "__main__":
    intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
    print(erase_overlap_intervals(intervals))  # Output: 1
    
    intervals1= [(1, 2), (1, 2), (1, 2)]
    print(erase_overlap_intervals(intervals1))  # Output: 2