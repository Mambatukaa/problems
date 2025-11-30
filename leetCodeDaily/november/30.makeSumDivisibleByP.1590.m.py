""""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109


"""

# TLE
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)

        # If the total sum is already divisible by p, no subarray needs to be removed
        if total_sum % p == 0:
            return 0

        n = len(nums)
        min_len = n  # Initialize min_len to the size of the array

        # Try removing every possible subarray
        for start in range(n):
            sub_sum = 0
            for end in range(start, n):
                sub_sum += nums[end]  # Calculate the subarray sum

                # Check if removing this subarray makes the remaining sum divisible by p
                remaining_sum = (total_sum - sub_sum) % p

                if remaining_sum == 0:
                    min_len = min(
                        min_len, end - start + 1
                    )  # Update the smallest subarray length

        # If no valid subarray is found, return -1
        return min_len if min_len != n else -1
