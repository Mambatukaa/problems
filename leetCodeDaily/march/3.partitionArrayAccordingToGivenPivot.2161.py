""""


You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
• Every element less than pivot appears before every element greater than pivot .
• Every element equal to pivot appears in between the elements less than and greater than pivot.
• The relative order of the elements less than pivot and the elements greater than pivot is maintained.
• More formally, consider every pi, Pj where pi is the new position of the ith element and pj is the new position of the jth element.
If i < j and both elements are smaller (or larger) than pivot, then pi < Pj •
Return nums after the rearrangement.

Example 1:
    Input: nums = [9,12,5,10,14,3,10], pivot = 10
    Output: (9,5,3,10,10,12,14]|

    Explanation:

        The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
        The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
        The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and
        [12, 14] are the respective orderings.

Example 2:
    Input: nums = [-3,4,3,2], pivot = 2
    Output: [-3,2,4,3]|
Explanation:
    The element -3 is less than the pivot so it is on the left side of the array.
    The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
    The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3]|
    are the respective orderings.


Constraints:
• 1 <= nums. length <= 105
• -106 <= nums [i] <= 106
• pivot equals to an element of nums.

"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                mid.append(num)
        return left + mid + right

    # Fixed array
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = 0
        equal = 0

        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1
            
        lessIdx = 0
        equalIdx = less
        greaterIdx = less + equal

        res = [0] * len(nums)

        for num in nums:
            if num < pivot:
                res[lessIdx] = num
                lessIdx += 1
            elif num == pivot:
                res[equalIdx] = num
                equalIdx += 1
            else:
                res[greaterIdx] = num
                greaterIdx += 1

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def pivotArrayIII(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1
                
            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1

        while l <= r:
            res[l] = pivot
            res[r] = pivot
            l += 1
            r -= 1

        return res

