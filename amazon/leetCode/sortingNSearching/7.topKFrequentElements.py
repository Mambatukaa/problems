from heapq import heappush, heapify, heappop
from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(n)
# HEAP
# TODO
def topKFrequent(nums, k):
  # count frequency
  count = Counter(nums)

  heap = []
  heapify(heap)



  return heap


# Time Complexity: O(n)
# Space Complexity: O(n)
# Bucket sort
# NEETCODE
def topKFrequentII(nums, k):
  count = Counter(nums)

  freq = [[] for i in range(len(nums) + 1)]

  for n, c in count.items():
    freq[c].append(n)

  res = []

  for i in range(len(freq) -1, 0, -1):
    for n in freq[i]:
      res.append(n)

      if len(res) == k:
        return res

nums = [1,1,1,2,2,3]
k = 2

print("Res:", topKFrequentII(nums, k))

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
