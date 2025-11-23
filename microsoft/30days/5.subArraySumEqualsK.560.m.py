"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


"""
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {
            0: 1
        }

        prefix = 0
        res = 0

        for num in nums:
            prefix += num

            diff = prefix- k 

            if diff in dic:
                res += dic[diff]

            dic[prefix] = dic.get(prefix, 0) + 1

        return res

        
"""

k = 3

-------------  
    ----------
                -----
1, -1, 1, 1, 1, 4, -1
0.  1. 2. 3. 4. 5,  6

1, 0, 1, 2, 3, 5, 4
-2 -3 -2 -1 0  2  1

diff = curr_sum - k

[1, -1, 1, 1, 1]
[4, -1]

res = 2


t = 2

1, 1, -1, 3
1. 2.  1  4


2       
--    2
     ----
1 1  -1 3


k = 2
diff = curr_sum - k = 2

1 2 1 4

if diff in dic:
    # answer found
    res += dic[diff]

dic[curr_sum] = 



"""       
