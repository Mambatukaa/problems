class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first = 0
        second = 0

        for i in range(len(nums)):
            tmp = second
            second = max(first + nums[i], second)
            first = tmp

        return max(first, second)

        
