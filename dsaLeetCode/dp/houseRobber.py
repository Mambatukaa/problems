# Bottom UP
# Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)
def houseRobber(nums):
  skipped = 0
  currMax = 0

  for num in nums:
    skipped, currMax = currMax, max(skipped + num, currMax)

  return currMax


nums = [1, 2, 3, 1]
print("Res:", houseRobber(nums))

