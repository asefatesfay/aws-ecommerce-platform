def flatten(nestedList):
    result = []
    for item in nestedList:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    
    return result

if __name__ == "__main__":
    nestedList = [1, [2, [3, 4], 5], 6,[7, 8, [9, 10]]]
    print(flatten(nestedList))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    pairs = [("apple", 2), ("banana", 3), ("orange", 1)]
    pairs.sort(key=lambda x: -x[1])
    print(pairs)  # Output: [('banana', 3), ('apple', 2), ('orange', 1)]