# Time Complexity: O(n^2)
# Space Complexity: O(1)
def threeSumClosest(nums, target):
  nums.sort()

  closest = nums[0] + nums[1] + nums[2]

  for i, num in enumerate(nums):
    l = i + 1
    r = len(nums) - 1

    while l < r:
      threeSum = num + nums[l] + nums[r]

      if threeSum == target:
        return target

      if abs(threeSum - target) < abs(closest - target):
        closest = threeSum

      if threeSum < target:
        l += 1
      else:
        r -= 1

  return closest

nums = [-4, -1, 1, 2]
target = 1

print("res:", threeSumClosest(nums, target))

"""

nums = [ -4, -1, 1, 2 ]
target = 1

Output: -1 + 2 + 1 = 2

return the closest sum


the sum that is closest to the target


"""
