
def longestIncreasingSubsequence(nums):

  # Bottom UP real dp solution

  # Time Complexity: O(n^2)
  # Space Complexity: O(n)
  # From backward
  def bottomUp(nums):
    dp = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):

      for j in range(i, len(nums)):
        if nums[i] < nums[j]:
          dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

  # Time Complexity: O(n^2)
  # Space Complexity: O(n)
  def bottomUpII(nums):
    dp = [1] * len(nums)

    for i in range(len(nums)):
      for j in range(i):
        if nums[i] > nums[j]:
          dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
    
  bottomUpII(nums)
  return bottomUp(nums)


nums = [10,9,2,5,3,7,101,18 ]
print("res:", longestIncreasingSubsequence(nums))




"""


Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:
  Input: nums = [10,9,2,5,3,7,101,18]
  Output: 4
  Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
  Input: nums = [0,1,0,3,2,3]
  Output: 4

Example 3:
  Input: nums = [7,7,7,7,7,7,7]
  Output: 1

Constraints:
• 1 <= nums.length <= 2500
• -10^4 <= nums[i] <= 10^4

"""
