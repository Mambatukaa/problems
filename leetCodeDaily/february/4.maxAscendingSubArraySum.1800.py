
""""

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums .
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [nums, nums +1, ..., nums,-1, nums,1 is ascending if for all i where 1 <= i < r, nums; <
nums i+1. Note that a subarray of size 1 is ascending.

Example 1:
    Input: nums = [10,20,30,5,10,50]
    Output: 65
    Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.



Constraints:
• 1 <= nums.length <= 100
• 1 < nums[1] <= 100

"""



class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def maxAscendingSum(self, nums: List[int]) -> int:

        currSum = nums[0]
        res = currSum

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                currSum = 0
            
            currSum += nums[i + 1]
            res = max(currSum, res)
        
        return res
