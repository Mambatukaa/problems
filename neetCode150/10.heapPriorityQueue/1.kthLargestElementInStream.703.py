
from heapq import heappush, heappop

# Time Complexity: O(log n)
# Space Complexity: O(n)
# 10 minutes
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

        

    def add(self, val):
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]

        

kthLargest = KthLargest(3, [1,2,3,4,5])

print(kthLargest.add(6))



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
