# initial
#


""""
The next permutation of an array of integers is the next lexicographically 
    greater permutation of its integer. 
 Next permutation is the next possible bigger 

1. Find the best digit to swap
2. Find the best number to swap
3. Swap it
4. Reverse pivot + 1 to n - 1

"""



# Time Complexity: O(n)
# Space Complexity: O(1)
# LeetCode
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        if n == 1:
            return

        pivot = n - 2

        # find the best digit to swap
        for i in range(n - 1, -1, -1):
            if nums[pivot] < nums[i]:
                break

            pivot -= 1


        # find the best num to swap with digit
        if pivot != -1:
            for i in range(n - 1, -1, -1):
                if nums[pivot] < nums[i]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break;
        
        # reverse pivot + 1 to n - 1
        # swap
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        """
        Do not return anything, modify nums in-place instead.
        """




nums = [1,3,2]
solution = Solution()

solution.nextPermutation(nums)

print("res:", nums)
