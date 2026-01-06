""""



You are given a 0-indexed integer array nums, and an integer k.
You are allowed to perform some operations on nums, where in a single operation, you can:
• Select the two smallest integers x and y from nums .
• Remove x and y from nums .
• Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
Note that you can only apply the described operation if nums contains at least two elements.
Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.

Example 1:
    Input: nums = [2,11,10,1,3], k = 10
    Output: 21

    Explanation:
    1. In the first operation, we remove elements 1 and 2, then add 1 * 2 + 2 to nums. nums becomes equal to [4, 11, 10, 3) .
    2. In the second operation, we remove elements 3 and 4, then add 3 * 2 + 4 to nums. nums becomes equal to [10, 11, 10] .
    At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
    It can be shown that 2 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.



Constraints:
• 2 < nums.length <= 2 * 10^5)
• 1 ^ numsi］<= 10^9
• 1 <= k <= 10^9
• The input is generated such that an answer always exists. That is, there exists some sequence of operations after which all elements of the array are
greater than or equal to k.
"""



import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0

        while len(nums) >= 2 and nums[0] < k:
            res += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, x * 2 + y)

        return res
