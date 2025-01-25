"""

You are given a O-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums (1] and nums (j] if |nums [i] - nums [j] | <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the
corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index
0 and 2 < 10.

Example 1:
    Input: nums = [1,5,3,9,8], limit = 2
    Output: [1,3,5,8,9]

    Explanation: Apply the operation 2 times:
    - Swap nums [1] with nums[2]. The array becomes [1,3,5,9,8]
    - Swap nums [3] with nums[4]. The array becomes [1,3,5,8,9]
    We cannot obtain a lexicographically smaller array by applying any more operations.
    Note that it may be possible to get the same result by doing different operations.





1. Group the elements based on the limit
2. iterate through nums and replace the nums[i] by smallest num of nums[i] group. Use queue for group item.
3. Return the nums

"""

# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Union find
from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        groups = []
        numsGroupIdx = {}

        for num in sorted(nums):
            n = len(groups)

            if num not in numsGroupIdx:
                if len(groups) and num - groups[-1][-1] <= limit:
                    numsGroupIdx[num] = numsGroupIdx[groups[-1][-1]]
                else:
                    # new group
                    numsGroupIdx[num] = n
                    groups.append(deque())

            groups[numsGroupIdx[num]].append(num)

        for i in range(len(nums)):
            num = nums[i]
            idx = numsGroupIdx[num]

            nums[i] = groups[idx].popleft()

        return nums


            






        


nums = [1,5,3,9,8]
limit = 2

nums = [1,7,6,18,2,1]
limit = 3

solution = Solution()

print("res:", solution.lexicographicallySmallestArray(nums, limit))
