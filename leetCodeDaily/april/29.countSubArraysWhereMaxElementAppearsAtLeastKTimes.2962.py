""""
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Sliding window
    def countSubarrays(self, nums, k: int) -> int:
        n = len(nums)

        max_el = max(nums)
        max_el_count = 0

        l = 0

        res = 0

        for r in range(n):
            if nums[r] == max_el:
                max_el_count += 1

            while max_el_count >= k:
                # update the res
                res += n - r
                if nums[l] == max_el:
                    max_el_count -= 1

                l += 1

        return res
            
            
solution = Solution()

nums = [1,3,2,3,3]
k = 2

print("res:", solution.countSubarrays(nums, k))
