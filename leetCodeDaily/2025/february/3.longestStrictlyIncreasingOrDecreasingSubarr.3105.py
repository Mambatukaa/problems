""""


You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or
strictly decreasing.

Example 1:
    Input: nums = [1,4,3,3,2]
    Output: 2

    Explanation:
    The strictly increasing subarrays of nums are (11, (21, 131, (31, (4), and [1,4).
    The strictly decreasing subarrays of nums are [1]. [2]. [3]. [3]. [4]. [3,2], and [4,3] •
    Hence, we return 2.


Example 2:

    Input: nums = [3,3,3,3]
    Output: 1
    Explanation:
    The strictly increasing subarrays of nums are [3]. [3], [3], and [3] .
    The strictly decreasing subarrays of nums are [3]. [3]. [3], and [3] •
    Hence, we return 1.

"""



class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # find the max increasing sub array
        res = 1
        incCtr = 1
        decCtr = 1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                incCtr = 1
                decCtr += 1
            elif nums[i] < nums[i + 1]:
                incCtr += 1
                decCtr = 1
            else:
                incCtr = 1
                decCtr = 1
            res = max(res, incCtr, decCtr)

        
        return res

