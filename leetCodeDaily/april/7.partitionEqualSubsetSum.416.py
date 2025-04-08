""""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""

class Solution:
    # Time Complexity: O(n * sum(nums) / 2)
    # Space Complexity: O(n * sum(nums) / 2)
    def canPartition(self, nums) -> bool:

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        half = total_sum // 2

        cache = {}
        
        def dfs(i, curr_sum):
            if i == len(nums) or curr_sum > half:
                return False
            if curr_sum == half:
                return True
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            res = dfs(i + 1, curr_sum) or dfs(i + 1, curr_sum + nums[i])

            cache[(i, curr_sum)] = res

            return res
            
        return dfs(0, 0)


    # Time Complexity: O(sum(nums) / 2)
    # Space Complexity: O(sum(nums) / 2)
    def canPartitionII(self, nums) -> bool:
        total_sum = sum(nums)

        if total_sum % 2:
            return False
        
        dp = set()
        dp.add(0)

        target = total_sum / 2

        for i in range(len(nums) -1, -1, -1):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False

    def canPartitionIII(self, nums):
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        dp = [False] * (targetSum + 1)
        dp[0] = True

        for num in nums:
            for currSum in range(targetSum, num - 1, -1):
                dp[currSum] = dp[currSum] or dp[currSum - num]
        return dp[targetSum]



solution = Solution()

nums = [1,5,11,5]

print("Res:", solution.canPartitionIII(nums))
