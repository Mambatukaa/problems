""""

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
 

Example 1:

Input: nums = [3,1,2,2,2,1,3], k = 2
Output: 4
Explanation:
There are 4 pairs that meet all the requirements:
- nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
- nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
- nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
- nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.
Example 2:

Input: nums = [1,2,3,4], k = 1
Output: 0
Explanation: Since no value in nums is repeated, there are no pairs (i,j) that meet all the requirements.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], k <= 100
"""


class Solution:
    # Brute force
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def countPairs(self, nums, k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        
        return res


from collections import defaultdict
class Solution:
    def countPairs(self, nums, k: int) -> int:
        pairs = defaultdict(list)

        for i, v in enumerate(nums):
            pairs[v].append(i)


        res = 0

        for value in pairs.values():
            n = len(value)
            if n >= 2:
                for i in range(n):
                    for j in range(i + 1, n):
                        if value[i] * value[j] % k == 0:
                            res += 1
        return res



nums = [3,1,2,2,2,1,3]
k = 2

solution = Solution()

print("res:", solution.countPairs(nums, k))

# count pairs
"""
        0 1 2 3 4 5 6
nums = [3,1,2,2,2,1,3], k = 2

pair = {
    1: [1, 5]
    2: [2, 3, 4]
    3: [0, 6]
}            

"""
