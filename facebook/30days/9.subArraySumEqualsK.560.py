""""

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

    Input: nums = [1,1,1], k = 2
    Output: 2

Example 2:
    Input: nums = [1,2,3], k = 3
    Output: 2



Constraints:
• 1 < nums.length <= 2 * 10*
•-1000 ＜= numsi ≤= 1000
•-10^7 <= k <= 107


"""
class Solution:
    # Brute force
    # Time limit exceeded
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def subarraySum(self, nums, k: int) -> int:
        n = len(nums)

        res = 0

        for i in range(n):
            curr = nums[i]

            if curr == k:
                res += 1

            for j in range(i + 1, n):
                curr += nums[j]

                if curr == k:
                    res += 1

        return res

    # Prefix sum - allows us to find the sum of any subarray
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def subarraySumII(self, nums, k: int) -> int:
        prefix_sums = { 0: 1}
        res = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            if diff in prefix_sums:
                res += prefix_sums[diff]

            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

        return res

solution = Solution()

nums = [1, -1, 1, 1, 1, 1]
k = 3
print("res:", solution.subarraySumII(nums, k))



