from heapq import heappop, heappush, heapify
from collections import Counter

# Time Complexity: O(n logn)
# Space Complexity: O(1)
# Greedy
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
      if len(hand) % groupSize != 0:
        return False

      ctr = Counter(hand)

      minHeap = []

      for key in ctr:
        minHeap.append(key)

      print(minHeap[0])

      heapify(minHeap)

      while len(minHeap):
        currSmall = minHeap[0]
        size = 0

        while size < groupSize:
          if currSmall not in ctr:
            return False

          ctr[currSmall] -= 1

          if ctr.get(currSmall) == 0:
            del ctr[currSmall]
            heappop(minHeap)

          currSmall += 1
          size += 1

      return True

solution = Solution()

hand = [1, 2, 2, 3, 3, 4, 6, 7, 8]
groupSize = 3

# {1: 1, 2: 2, 
#  3: 2, 4: 1, 
#  6: 1, 7: 1, 
#  8: 1}

# 1, 2, 3, 4, 6, 7, 8

print(solution.isNStraightHand(hand, groupSize))
        
