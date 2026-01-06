"""

1. Brute force TIMIT LIMIT EXCEEDED

2. Optimal approach
    a. Reduce the repeated work
        xor nums2 for n times
        xor nums1 for m times

            xor the above results

        if n or m is even the answer will be 0

"""

def xorSum(nums):
    res = 0

    for num in nums:
        res ^= num

    return res

# Time Complexity: O(n + m)
# Space Complexity: O(1)
# math
def xorAllNums(nums1, nums2):
    isNums1Even = len(nums1) % 2 == 0
    isNums2Even = len(nums2) % 2 == 0

    if isNums1Even and isNums2Even:
        return 0
    elif isNums1Even:
        return xorSum(nums1)
    elif isNums2Even:
        return xorSum(nums2)
    else:
        return xorSum(nums1) ^ xorSum(nums2)


nums1 = [2,1,3] # n = 3
nums2 = [10,2,5,0] # m = 4

print("Res:", xorAllNums(nums1, nums2))
