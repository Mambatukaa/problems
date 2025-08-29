""""
All the values of nums are unique.You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

 

 

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
Example 2:

Input: nums= [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
 

Constraints

-109 <= lower <= upper <= 109
0 <= nums.length <= 100
lower <= nums[i] <= upper

"""
class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        if len(nums) == 0:
            return [[lower, upper]]
            
        res = []

        if lower < nums[0]:
            res.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):
            if nums[i] + 1 < nums[i + 1]:
                res.append([nums[i] + 1, nums[i + 1] - 1])
        
        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])
        
        return res

class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        res = []

        for num in nums + [upper + 1]:
            if num > lower:
                res.append([lower, num - 1])
            lower = num + 1

        
        return res

solution = Solution()

nums = [0,1,3,50,75]

lower = 0
upper = 99

print("Res 1:", solution.findMissingRanges(nums, lower, upper))

nums = [0,13,50,75]

nums = [-1]
lower = -1
upper = -1


print("Res 2:", solution.findMissingRanges(nums, lower, upper))
