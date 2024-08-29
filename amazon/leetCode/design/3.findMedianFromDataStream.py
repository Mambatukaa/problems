from heapq import heappop, heappush, heapify 

class MedianFinder:

  def __init__(self):
    # max heap
    self.small = []

    # min heap
    self.large = []

  def addNum(self, num):
    if not self.small and not self.large:
      heappush(self.small, -num)
      return
    
    if num <= -self.small[0]:
      heappush(self.small, -num)
    else:
      heappush(self.large, num)

    #
    if len(self.small) - len(self.large) > 1:
      heappush(self.large, -heappop(self.small))
    elif len(self.large) - len(self.small) > 1:
      heappush(self.small, -heappop(self.large))

  def findMedian(self):

    if not self.large or len(self.small) > len(self.large):
      return -self.small[0]
    elif len(self.small) < len(self.large):
      return self.large[0]

    return (-self.small[0] + self.large[0]) / 2

medianFinder = MedianFinder()

medianFinder.addNum(1)
print("small:", medianFinder.small, "large:", medianFinder.large)
print(medianFinder.findMedian())

medianFinder.addNum(2)
print("small:", medianFinder.small, "large:", medianFinder.large)
print(medianFinder.findMedian())

medianFinder.addNum(3)
print("small:", medianFinder.small, "large:", medianFinder.large)
print(medianFinder.findMedian())
