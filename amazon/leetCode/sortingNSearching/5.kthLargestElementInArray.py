from heapq import heapify, heappop, heappush

# Time Complexity: O(n log k)
# Space Complexity: O(k)
def kthLargestElementInArray(nums, k):
  heap = []

  heapify(heap)

  for num in nums:
    heappush(heap, num)

    if len(heap) > k:
      heap.heappop()


  return heap[0]
  


nums = [1]
k = 2

print("Res:", kthLargestElementInArray(nums, 1))

"""


Input: nums = [3,2,1,5,6,4], k = 2
Output: 5



Solve the problem without sorting.

"""
