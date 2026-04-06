def count_subsets(n):
    if n == 0:
        return 1
    
    return count_subsets(n - 1) + count_subsets(n - 1)

def generate_subsets(n, index, current, subsets):
    if index == n:
        subsets.append(current.copy())
        return
    
    # Include this index in the subset.
    current.append(index)
    generate_subsets(n, index + 1, current, subsets)
    
    # Exclude this index from the subset.
    current.pop()
    generate_subsets(n, index + 1, current, subsets)
    
if __name__ == "__main__":
    n = 3
    print(count_subsets(n))  # Output: 8
    
    subsets = []
    generate_subsets(n, 0, [], subsets)
    subsets.reverse()
    print(subsets)  # Output: [[0, 1, 2], [0, 1], [0, 2], [0], [1, 2], [1], [2], []]
    