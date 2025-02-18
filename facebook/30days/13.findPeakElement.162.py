""""

A peak element is an element that is strictly greater than its neighbors.
Given a O-indexed integer array nums, find a peak element, and return its index. If the array contains multiple
peaks, return the index to any of the peaks.
You may imagine that nums [-1] = nums [n] = -∞. In other words, an element is always considered to be
strictly greater than a neighbor that is outside the array.
You must write an algorithm that runs in 0(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number
    2.
Example 2:
    Input: nums = [1,2, 1,3,5,6,41
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element
    is 2, or index number 5 where the peak element is 6.


Constraints:
• 1 < nums.length <= 1000
• -2^31 <= nums [i] <= 2^31 - 1
• nums[i] != nums[i + 1] for all valid i.

"""


class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def findPeakElement(self, nums):
        l = 0
        r = len(nums) - 1

        n = len(nums)

        while True:
            mid = l + (r - l) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            elif mid < n - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid


solution = Solution()


#       0  1  2  3  4  5
nums = [4, 5, 4, 3, 2]
nums = [1, 2, 3, 4]
nums = [1, 2, 1, 3, 5, 6, 4]
print("res:", solution.findPeakElement(nums))
