""""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


# Heap Solution
# TC: O(n * log k)
# SC: O(k)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = []

        for num in nums:
            heappush(min_heap, num)

            if len(min_heap) > k:
                heappop(min_heap)

        return min_heap[0]


# TC: O(N + M) m - maxValue
# SC: O(M)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)

        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1

        remain = k

        for num in range(len(count) - 1, -1 , -1):
            remain -= count[num]

            if remain <= 0:
                return num + min_value
        
        return -1
