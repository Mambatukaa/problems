from heapq import heappush, heapify, heappop
from collections import Counter

def topKFrequent(nums, k):
  # count frequency
  count = Counter(nums)

  heap = []
  heapify(heap)

  for k, v in count.items():



  return heap




nums = [1,1,1,2,2,3]
k = 2

print("Res:", topKFrequent(nums, k))

"""

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]



Constraints:
• 1 <= nums.length <= 10^5
• 10^4 <= nums [i] <= 10^4)
• k is in the range [1, the number of unique elements in the array].
• It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n) , where n is the array's size.

"""
