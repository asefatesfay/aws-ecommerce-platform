# Next Greater element
# Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
# Output: [-1, 3, -1]

def next_greater_brute(nums1, nums2):
    result = []
    for num in nums1:
        idx = nums2.index(num)
        found = -1
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > num:
                found = nums2[j]
                break
        result.append(found)
    return result

def next_greater(num1, num2):
    nge = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            nge[stack.pop()] = num
        stack.append(num)
    return [nge.get(num, -1) for num in nums1]

if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2, 5]
    print(next_greater_brute(nums1, nums2))

    print(next_greater(nums1, nums2))
    