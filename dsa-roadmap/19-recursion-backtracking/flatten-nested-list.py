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