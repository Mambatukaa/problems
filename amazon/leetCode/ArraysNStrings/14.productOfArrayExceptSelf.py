def productExceptSelf(nums):
  prefixFront = [1] * (len(nums) + 1)
  prefixBack = [1] * (len(nums) + 1)

  
  for i in range(len(nums)):
    prefixFront[i + 1] = prefixFront[i] * nums[i]

  for i in range(len(nums) - 1, -1, -1):
    prefixBack[i] = prefixBack[i + 1] * nums[i]


  for i in range(len(nums)):
    nums[i] = prefixFront[i] * prefixBack[i + 1]

  print(nums)


nums = [1, 2, 3, 4]
productExceptSelf(nums)

"""

Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Write a function that takes O(n) time O(1) space and don't use division operation.


Brute Force 
  Time Complexity: O(n^2)
It's easy to solve with division. Find sum of all nums and divide by current num.


Prefix sum from front and from back

[1, 1, 2, 6, 24]

[24, 24, 12, 4, 1]





"""
