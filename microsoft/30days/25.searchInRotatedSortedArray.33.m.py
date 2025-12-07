"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        """
               m
        [3, 4, 5, 1, 2] t = 4

               m
        [4, 5, 8, 2, 3] t = 5
        [11, 5, 8, 9, 10] t = 5

               m
        [5, 1, 2, 3, 4] t = 3

               m
        [1, 1, 2, 5, 0] t = 5
        

                 l m r
        [4,5,6,7,0,1,2] t = 0

        """        

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if target >= nums[l] or nums[l] > nums[mid]:
                    # left side
                    r = mid - 1
                else:
                    # right side
                    l = mid + 1
            else:
                if target <= nums[r] or nums[mid] > nums[r]:
                    # right
                    l = mid + 1
                else:
                    # left
                    r = mid - 1
                

        return -1



