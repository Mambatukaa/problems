""""


You are given an integer array nums. The absolute sum of a subarray [nums, [nums,, nums1+1, numsr-1, nums,] is abs (nums +
nums1+1 + ... + numsr-1 + numsr) •
Return the maximum absolute sum of any (possibly empty) subarray of nums .
Note that abs (x) is defined as follows:
• If x is a negative integer, then abs (x) = -x.
• If x is a non-negative integer, then abs (x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs (2+3) = abs (5) = 5.
Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray I-5,1,-4] has absolute sum = abs (-5+1-4) = abs (-8) = 8.

Constraints:
• 1 <= nums. length <= 105
• -104 < nums [i] <= 104

"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Prefix sum find the maxPrefix and minPrefix
    def maxAbsoluteSum(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        minValue = min(nums)
        maxValue = max(nums)

        return max(abs(maxValue - minValue), abs(maxValue), abs(minValue))


    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxAbsoluteSum(self, nums) -> int:
        prefix_sum = 0
        max_prefix_sum = 0
        min_prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(prefix_sum, min_prefix_sum)
            max_prefix_sum = max(prefix_sum, max_prefix_sum)


        return abs(max_prefix_sum - min_prefix_sum)


solution = Solution()

nums = [-3,-5,-3,-2,-6,3,10,-10,-8,-3,0,10,3,-5,8,7,-9,-9,5,-8]

print("res:", solution.maxAbsoluteSum(nums))
