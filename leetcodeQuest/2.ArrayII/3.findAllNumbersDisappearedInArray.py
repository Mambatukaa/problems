""""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
 

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""

# SC: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set(nums)

        res = []

        for num in range(1, n + 1):
            if num not in seen:
                res.append(num)

        return res
        
# SC: O(1)
# in place
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] *= -1
        
        res = []


        for i in range(1, n + 1):
            if nums[i - 1] > 0:
                res.append(i)

        return res

