class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # mark negative numbers to zero
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0
        
        print(nums)

        # mark positive numbers to negative
        for i, num in enumerate(nums):
            val = abs(num)

            if 1 <= val <= n:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (n + 1)

        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                return i

        return n + 1
        

        


        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Iterate through nums
        # return smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements are at the correct index
        # the smallest missing positive number is n + 1
        return n + 1
