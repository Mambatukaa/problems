""""

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive
integers and the number of negative integers.
• In other words, if the number of positive integers in nums is pos and the number of negative integers is
neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.



Example 1:
    Input: nums = [-2,-1,-1,1,2,31
    Output: 3
    Explanation: There are 3 positive integers and 3 negative integers. The maximum
    count among them is 3.

Example 2:
    Input: nums = [-3,-2,-1,0,0,1,2]
    Output: 3
    Explanation: There are 2 positive integers and 3 negative integers. The maximum
    count among them is 3.

Example 3:

    Input: nums = [5,20,66,1314]
    Output: 4
    Explanation: There are 4 positive integers and 0 negative integers. The maximum
    count among them is 4.

"""

class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        first_pos_index = n

        # first positive num
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= 0:
                # go right
                low = mid + 1
            else:
                high = mid - 1
                first_pos_index = mid
        
        low = 0
        high = n - 1
        last_neg_index = n
        # last negative num
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] < 0:
                # go right
                low = mid + 1
            else:
                high = mid - 1
                last_neg_index = mid

        pos_count = n - first_pos_index
        neg_count = last_neg_index

        return max(pos_count, neg_count)
        