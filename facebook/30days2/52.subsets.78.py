
"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.



"""


class Solution:
    # Time Complexity: O(n * 2^n)
    # Space Complexity: O(n) n - len of curr
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(idx, curr):
            if idx > len(nums):
                return

            res.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtracking(i + 1, curr)
                curr.pop()

        backtracking(0, [])

        return res

        


