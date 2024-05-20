#initial

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxSum = nums[0]

      curSum = 0

      for n in nums:
        currSum += n

        if currSum < 0:
          currSum = 0

        maxSum = max(maxSum, currSum)

      return maxSum


