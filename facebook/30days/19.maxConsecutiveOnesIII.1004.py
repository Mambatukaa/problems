""""



Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k o's.

Example 1:
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]|
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
• 1 <= nums. length <= 105
• nums [i] is either 0 or 1.
• 0 <= k <= nums.length


"""

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0

        res = 0

        for r in range(len(nums)):
            while k == 0 and nums[r] == 0:
                if nums[l] == 0:
                    k += 1

                l += 1

            if nums[r] == 0:
                k -= 1
                
            res = max(res, r - l + 1)

        return res
