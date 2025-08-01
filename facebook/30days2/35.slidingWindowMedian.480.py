""""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6



Example 2:
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
 

Constraints:

1 <= k <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap = [] # right side
        max_heap = [] # left side
        n = len(nums)

        res = []

        for i in range(k):
            heappush(max_heap, -nums[i]) # add to the left
            heappush(min_heap, -heappop(max_heap)) # add to the right

            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))
        
        if k % 2 == 1:
            median = -max_heap[0]
            res.append(median)
        else:
            median = (-max_heap[0] + min_heap[0]) / 2
            res.append(median)

        heap_dict = defaultdict(int)

        # slide the window
        for i in range(k, n):
            prev = nums[i - k]
            heap_dict[prev] += 1
            curr = nums[i]

            balance = -1 if prev <= median else 1

            if curr <= median:
                balance += 1
                heappush(max_heap, -curr)
            else:
                balance -= 1
                heappush(min_heap, curr)

            if balance < 0:
                heappush(max_heap, -heappop(min_heap))
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))

            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-heappop(max_heap)] -= 1

            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[heappop(min_heap)] -= 1

            if k % 2 == 1:
                median = -max_heap[0]
                res.append(median)
            else:
                median = (-max_heap[0] + min_heap[0]) / 2
                res.append(median)
        
        return res







from collections import defaultdict
from heapq import heappush, heappop
from typing import List

# Time Complexity: O(n log k)
# Space Complexity: O(k)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median() -> float:
            if k % 2 == 1:
                return -max_heap[0]
            return (-max_heap[0] + min_heap[0]) / 2

        def prune(heap, is_max_heap):
            while heap and invalid_count[(val := (-heap[0] if is_max_heap else heap[0]))] > 0:
                heappop(heap)
                invalid_count[val] -= 1

        min_heap, max_heap = [], []
        res = []
        invalid_count = defaultdict(int)

        # Initial window
        for i in range(k):
            heappush(max_heap, -nums[i])
        for _ in range(k // 2):
            heappush(min_heap, -heappop(max_heap))

        res.append(get_median())

        for i in range(k, len(nums)):
            out_num, in_num = nums[i - k], nums[i]
            median = get_median()
            balance = 0

            invalid_count[out_num] += 1

            if out_num <= median:
                balance -= 1
            else:
                balance += 1

            if in_num <= median:
                heappush(max_heap, -in_num)
                balance += 1
            else:
                heappush(min_heap, in_num)
                balance -= 1

            # Rebalance
            if balance > 0:
                heappush(min_heap, -heappop(max_heap))
            elif balance < 0:
                heappush(max_heap, -heappop(min_heap))

            # Lazy deletion
            prune(max_heap, True)
            prune(min_heap, False)

            res.append(get_median())

        return res

from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median() -> float:
            if k % 2 == 1:
                return -max_heap[0]
            return (-max_heap[0] + min_heap[0]) / 2

        def prune(heap, is_max_heap):
            while heap and invalid_count[(val := (-heap[0] if is_max_heap else heap[0]))] > 0:
                heappop(heap)
                invalid_count[val] -= 1

        min_heap, max_heap = [], []
        res = []
        invalid_count = defaultdict(int)

        # Initial window
        for i in range(k):
            heappush(max_heap, -nums[i])
        for _ in range(k // 2):
            heappush(min_heap, -heappop(max_heap))

        res.append(get_median())

        for i in range(k, len(nums)):
            out_num, in_num = nums[i - k], nums[i]
            median = get_median()
            balance = 0

            invalid_count[out_num] += 1
            if out_num <= median:
                balance -= 1
            else:
                balance += 1

            if in_num <= median:
                heappush(max_heap, -in_num)
                balance += 1
            else:
                heappush(min_heap, in_num)
                balance -= 1

            # Rebalance
            if balance > 0:
                heappush(min_heap, -heappop(max_heap))
            elif balance < 0:
                heappush(max_heap, -heappop(min_heap))

            # Lazy deletion
            prune(max_heap, True)
            prune(min_heap, False)

            res.append(get_median())

        return res
