"""
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

 

Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2000




"""

from collections import defaultdict

class Solution:
    # Brute force
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def countCompleteSubarrays(self, nums) -> int:
        uni_elements = set(nums)

        res = 0

        for i in range(len(nums)):
            seen = set()
            seen.add(nums[i])
            if len(seen) == len(uni_elements):
                res += 1

            for j in range(i + 1, len(nums)):
                seen.add(nums[j])

                if len(seen) == len(uni_elements):
                    res += 1

                if len(seen) > len(uni_elements):
                    break

        return res

    # Sliding window
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def countCompleteSubarraysII(self, nums) -> int:
        n = len(nums)
        k = len(set(nums))

        res = 0

        l = 0

        seen = defaultdict(int)

        for r in range(n):
            seen[nums[r]] += 1

            while len(seen) == k:
                res += n - r
                seen[nums[l]] -= 1

                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1

        return res
        

solution = Solution()
nums = [1,3,1,2,2]

print('res:', solution.countCompleteSubarraysII(nums))

"""
0 1 2 3
5 5 5 5 uni_el = 1

5
5 5 
5 5 5
5 5 5 5

  5
  5 5
  5 5 5
    
    5
    5 5

      5





"""
