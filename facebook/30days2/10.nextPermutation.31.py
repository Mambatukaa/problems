from typing import List

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n == 1:
            return
        
        decreasing_idx = n - 2

        for i in range(n - 1, -1, -1):
            if nums[decreasing_idx] <  nums[i]:
                break
            decreasing_idx -= 1

        # swap the decreasing element with the just greater element
        if decreasing_idx != -1:
            for i in range(n - 1, -1, -1):
                if nums[i] > nums[decreasing_idx]:
                    # swap
                    nums[i], nums[decreasing_idx] = nums[decreasing_idx], nums[i]
                    break


        # reverse the subarray 
        self.reverse(nums, decreasing_idx + 1, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

"""


1. Find the first decreasing element
2. Swap with the just larger element than decreasing element 
3. Reverse the array after decreasing element
"""



# PrevPermutation
class Solution:
    def prevPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        if n == 1:
            return
        
        increasing_idx = n - 2

        for i in range(n - 1, -1, -1):
            if nums[increasing_idx] >  nums[i]:
                break
            increasing_idx -= 1

        # swap the increasing element with the just less element
        if increasing_idx != -1:
            for i in range(n - 1, -1, -1):
                if nums[i] < nums[increasing_idx]:
                    # swap
                    nums[i], nums[increasing_idx] = nums[increasing_idx], nums[i]
                    break

        # reverse the subarray 
        self.reverse(nums, increasing_idx + 1, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

"""


  8 9 1 1 4 5
- 8 5 9 4 1 1
  8 5 4 9 1 1


  8 5 4 1 1 3 
        
  8 5 3 4 1 1




"""

