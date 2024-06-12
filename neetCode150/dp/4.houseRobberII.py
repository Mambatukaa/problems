# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def rob(self, nums) -> int:


      def helper(nums):
        rob1, rob2 = 0, 0

        for num in nums:
          temp = rob2
          rob2 = max(rob1 + num, rob2)
          rob1 = temp

        return rob2

      # edge case nums[0]
      return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
      


solution = Solution()

print(solution.rob([1, 2, 3, 4, 5]))
