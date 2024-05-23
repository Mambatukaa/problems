"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two
whose elements sum up to a multiple of k, or false otherwise.


An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Input: nums = [23,2,4,6, 7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

"""

def find_subArray(nums, k):
  l = 0
  curr = 0

  for r in range(len(nums)):
    left = nums[l]
    right = nums[r]

    curr += right

    print(l, '-------', r)

    if r - l > 0 and curr % k == 0:
      return True

    while curr > k:
      curr -= nums[l]
      l += 1

  return False


nums = [23, 1, 2, 3, 7]
k = 30 

print(find_subArray(nums, k))

