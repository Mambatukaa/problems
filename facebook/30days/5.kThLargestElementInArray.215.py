
""""

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
    Input: nums = (3,2,1,5,6,4], k = 2
    Output: 5

Example 2:
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4

Constraints:
• 1 <= k <= nums. length <= 10^5
• -10^4 <= nums [i] <= 10^4


"""


# Solve it without sorting
# Heap
import heapq
import random
# Time Complexity: O(n)
# Space Complexity: O(k log k)
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)
    
    # Quick select
    # Time Complexity: O(n) avg: O(n) worst: O(n^2)
    # Space Complexity: O(n)
    # TIME LIMIT EXCEEDED
    def findKthLargestII(self, nums, k):
        k = len(nums) - k
        
        def quickSelect(l, r):
            # j less num pointer
            pivot, j = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1

            nums[r], nums[j] = nums[j], nums[r]

            if j > k:
                # go left
                return quickSelect(l, j - 1)
            elif j < k:
                # go right
                return quickSelect(j + 1, r)
            else:
                return nums[j]

        return quickSelect(0, len(nums) - 1)
    
    # leetCode quickSelect

    def findKthLargestIII(self, nums, k):

        def quickSelect(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)

            if k <= len(right):
                return quickSelect(right, k)
            elif k > len(right) + len(mid):
                return quickSelect(left, k - len(right) - len(mid))

            return pivot

        return quickSelect(nums, k)

    # Counting sort
    # Time Complexity: O(n + m)
    # Space Complexity: O(m)
    # m count length
    def findKthLargestIV(self, nums, k):
        minValue = min(nums)
        maxValue = max(nums)

        count = [0] * (maxValue - minValue + 1)

        for num in nums:
            count[num - minValue] += 1

        remaining = k

        for num in range(len(count) -1, -1, -1):
            remaining -= count[num]

            if remaining <= 0:
                return num + minValue

        return -1




solution = Solution()

#                       j
#                       i
nums = [3,2,3,1,2,4,5,5,6]
k = 1

nums = [5, 2, 1, 5, 2, 4]
k = 2


print("res:", solution.findKthLargestIV(nums, k))

