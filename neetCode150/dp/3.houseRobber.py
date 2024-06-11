# Time Complexity: O(n)
# Space Complexity: O(1)
# BOTTOM TO TOP
# REAL DP
def houseRobber(nums):
  n = len(nums)

  if n == 1:
    return nums[0]

  if n == 2:
    return max(nums[0], nums[1])
  
  nums[2] += nums[0]

  for i in range(3, n):
    nums[i] += max(nums[i - 2], nums[i - 3])

  return max(nums[-1], nums[-2])

# Time Complexity: O(n)
# Space Complexity: O(n)
# Top to bottom
class Solution:
  def houseRobberII(self, nums):
    self.memo = {}

    def helper(nums, n):
      if n < 0:
        return 0

      if n <= 1:
        return nums[n]

      if n in self.memo:
        return self.memo[n]

      self.memo[n] = nums[n] + max(helper(nums, n - 2), helper(nums, n - 3))

      return self.memo[n]

    n = len(nums)

    return max(helper(nums, n - 1), helper(nums, n - 2))

solution = Solution()
nums = [1, 2, 3, 1, 4, 7, 8, 9, 10] 
print(solution.houseRobberII(nums))

print("*****************************")

# Time limit exceeded
# Brute force
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def houseRobberIII(nums):
  def helper(nums, n):
    if n < 0:
      return 0

    if n <= 1:
      return nums[n]

    print(n)

    
    return nums[n] + max(helper(nums, n - 2), helper(nums, n - 3))

  n = len(nums)

  return max(helper(nums, n - 1), helper(nums, n - 2))

print(houseRobberIII(nums))
