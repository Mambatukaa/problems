""""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109








"""

# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        def found_bound(is_lower):

            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = (l + r) //2

                if nums[mid] == target:
                    if is_lower:
                        # find lower bound
                        if l == mid or nums[mid - 1] < target:
                            # found
                            return mid

                        # go left
                        r = mid - 1
                    else:
                        # find upper bound
                        if r == mid or nums[mid + 1] > target:
                            # found
                            return mid

                        # go right
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1


        lower = found_bound(True)

        res = [-1, -1]
        if lower == -1:
            return res

        res[0] = lower

        upper = found_bound(False)

        res[1] = upper

        return res


            






# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1

        # Find the lower bound
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        res = [-1, -1]

        if nums[left] != target:
            return res

        res = [left, left]

        right = len(nums) - 1

        # find the upper bound
        while left < right:
            mid = (left + right) // 2 + 1 # stop infinite loop

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res[1] = right

        return res



"""

O(log n)

Binary search

non decreasing order


1. Starting and ending position of the target

 0  1  2  3  4   5
[5, 7, 7, 8, 8, 10] target = 8

[3, 4]

if target is not in nums return [-1, -1]


[5, 7, 7, 8, 10] target = 8

[3, 3]


1. Search target from nums
2. If target found find the first position and second position
3.
   1. Binary search to left most idx
   2. Binary serach to right most idx

   Return answer

                r    
             m
             l
[5, 7, 7, 8, 8, 10]



"""



# Variant Find unique elements count
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        i = 0

        res = 0

        while i < n:
            target = nums[i]
            l = 0
            r = n - 1

            # upper bound
            while l <= r:
                mid = (r - l) // 2 + l

                if nums[mid] <= target:
                    # go right
                    l = mid + 1
                else:
                    # go left
                    r = mid - 1

            res += 1
            i = r + 1


        return res

"""

t = 5

    L
    M
  R
5 5 8

"""
