""""




You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (O-indexed), you will apply the following on the ith element of
nums:
    • If nums [i] == nums [i + 1], then multiply nums [i] by 2 and set nums [i + 1] to 0. Otherwise, you skip this operation.
    After performing all the operations, shift all the o's to the end of the array.
    • For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0] •
    Return the resulting array.
    Note that the operations are applied sequentially, not all at once.

Example 1:
    Input: nums = [1,2,2,1,1,0]
    Output: [1,4,2,0,0,0]

After that, we shift the O's to the end, which gives the array [1,4,2,0,0,0].

Example 2:
    Input: nums = [0,1]
    Output: (1,0]
    Explanation: No operation can be applied, we just shift the 0 to the end.










Constraints:
• 2 <= nums.length <= 2000
• 0 <= nums [11 <= 1000

"""


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

        non_zero_index = 0

        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        while non_zero_index < n:
            nums[non_zero_index] = 0
            non_zero_index += 1
        
        return nums
