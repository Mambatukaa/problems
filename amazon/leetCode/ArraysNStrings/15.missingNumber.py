
# Easy
# Time Complexity: O(n)
# Space Complexity: O(1)
def missingNumber(nums):
  expectedSum = len(nums) * (len(nums) + 1 ) // 2

  """
  expectedSum = 0

  for i in range(len(nums)):
    expectedSum += i + 1

  """ 
  return expectedSum - sum(nums)

nums = [3, 0, 1]
print("res:", missingNumber(nums))
"""
Solve problem using O(1) space and O(n) time.

nums containing n disting numbers in range [0, n] return the only number in the range that is missing from the array

To find the sum of 0 to n numbers and subtract the sum of nums


"""
