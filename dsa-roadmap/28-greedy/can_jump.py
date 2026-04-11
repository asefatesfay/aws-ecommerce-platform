def can_jump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
    return True

# Example usage:
if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))  # Output: True

    nums = [3, 2, 1, 0, 4]
    print(can_jump(nums))  # Output: False
    
    nums = [1, 1, 1, 1, 1]
    print(can_jump(nums))  # Output: True