#initial

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxSub = nums[0]

      currSum = 0

      for n in nums:
        if currSum < 0:
          currSum = 0

        currSum += n

        maxSub = max(maxSub, currSum)

      return maxSub



