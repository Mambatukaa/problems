"""

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2, 1, -3, 4,-1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Create a formula
1. Start to create small subarrays
2. Track subarrays sum
3. 

                                   i
nums = [-2, 1, -2, 4, 3, 5, 6, -1, 3]

nums[i] = max(nums[i], (nums[i - 1] if i > 0 else 0) + nums[i])
res = max(res, nums[i])

"""
# Time Complexity: O(n)
# Space Complexity: O(n)
# DP
def maxSubArray(nums):
    res = -float('inf')

    for i in range(len(nums)):
        nums[i] = max(nums[i], (nums[i - 1] if i > 0 else 0) + nums[i])
        res = max(nums[i], res)

    return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# DP
# Set negatives to zero
def maxSubArrayII(nums):
    maxSum = nums[0]
    currSum = 0

    for num in nums:
        if currSum < 0:
            currSum = 0

        currSum += num

        maxSum = max(maxSum, currSum)


    return maxSum

nums = [-2,1, 1, 1, 1, 1]

print('res:', maxSubArray(nums))

