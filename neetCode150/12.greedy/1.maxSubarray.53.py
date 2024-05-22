#initial

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums):
      maxSub = nums[0]
      arr = [nums[0]]
      answer = []

      currSum = 0

      for i in range(len(nums)):
        n = nums[i]

        if currSum < 0:
          currSum = 0
          arr = []

        currSum += n
        arr.append(n)

        if currSum > maxSub:
          maxSub = currSum
          answer = arr.copy()

      print(answer)

      return maxSub


nums = [-2,1,-3,4,-1,2,1,-5,4];

solution = Solution()
solution.maxSubArray(nums)
