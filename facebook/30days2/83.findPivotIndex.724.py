"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000





"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if left_total == right_total:
                return i

            left_total += nums[i]

        return -1


""""

0. 1. 2. 3. 4. 5
1, 7, 3, 6, 5, 6 ===> total = 28

left_total = 0

right_total = total - left_total - curr

"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix_sum
        n = len(nums)
        left_prefix = [0] * (n + 1)
        right_prefix = [0] * (n + 1)

        for i in range(n):
            left_prefix[i + 1] = left_prefix[i] + nums[i]

        for i in range(n - 1, -1, -1):
            right_prefix[n - i] = right_prefix[n - i - 1] + nums[i]


        for i in range(n):
            if left_prefix[i] == right_prefix[n - i - 1]:
                return i
        

        return -1


"""


 0. 1. 2. 3. 4. 5
[1, 7, 3, 6, 5, 6] n = 6

0. 1. 2.  3.  4.  5. 
1, 8, 11, 17, 22, 28

0   1   2   3   4   5
6, 11, 17, 20, 27, 28

28, 27, 20, 17, 11, 6


0  1   2
2, 1, -1

leftSum =  2, 3, 2

rightSum = 2, 0, -1




"""
        

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix_sum
        n = len(nums)
        left_prefix = [0] * (n)
        right_prefix = [0] * (n)

        left_prefix[0] = nums[0]
        right_prefix[-1] = nums[-1]

        for i in range(1, n):
            left_prefix[i] = left_prefix[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            right_prefix[i] = right_prefix[i + 1] + nums[i]


        for i in range(n):
            if left_prefix[i] == right_prefix[i]:
                return i
        
        return -1
