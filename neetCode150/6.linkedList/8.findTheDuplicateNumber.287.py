# Optimal solution (NEETCODE)
# Time Complexity: O(n)
# Space Complexity: O(1)
# FLOYD algorithm
# Gave up
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      slow = 0
      fast = 0

      while(True):
        slow = nums[slow]
        fast = nums[nums[fast]]

        # first intersection
        if slow == fast:
          break
      
      slow1 = 0

      while True:
        # second intersection
        if slow == slow1:
          return slow

        slow1 = nums[slow1]
        slow = nums[slow]

# Modifying the array
# Time Complexity: O(n)
# Space Complexity: O(1)
# Gave up
class Solution1:
    def findDuplicate(self, nums) -> int:

        for i in range(len(nums)):
            idx = nums[i] * -1 if nums[i] < 0 else nums[i]

            if nums[idx] < 0:
                return idx
            else:
                nums[idx] *= -1



solution = Solution()

nums = [1, 3, 4, 2, 2]

print(solution.findDuplicate(nums))
