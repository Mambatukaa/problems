class Solution:
    def sumOfGoodNumbers(self, nums, k: int) -> int:

        ans = 0

        for i in range(len(nums)):
            res = 0
            num = nums[i]

            idx1 = i - k
            idx2 = i + k


            if idx1 >= 0 and nums[idx1] >= num:
                continue
                
            if idx2 < len(nums) and nums[idx2] >= num:
                continue

            ans += num

        return ans



solution = Solution()

nums = [1,3,2,1,5,4]

nums = [47, 47]
k = 1

print("res:", solution.sumOfGoodNumbers(nums, k))
