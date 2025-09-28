""""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""

# Time Complexity: O(n log n)
# Space Complexity: O(n log n) N
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        res = 0

        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                res += 1
                l += 1
                r -= 1
            elif s < k:
                l += 1
            else:
                r -= 1

        return res

        
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = defaultdict()
        res = 0

        for num in nums:
            diff = k - num

            if diff in dic and dic[diff] > 0:
                dic[diff] -= 1
                res += 1
            else:
                dic[num] = dic.get(num, 0) + 1
                    
        return res

"""

3, 1, 3, 4, 3 k = 6

{
    3: 1
    1: 1
}


"""
