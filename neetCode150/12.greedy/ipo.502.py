import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
      n = len(profits)

      projects = sorted(zip(capital, profits))
      """
      (0, 1)
      (1, 2)
      (1, 3)

      """

      print(projects)

      # create pair by profits and capital
      heap = []
      i = 0

      for _ in range(k):
        while i < n and projects[i][0] <= w:
          heapq.heappush(heap, -projects[i][1])
          i += 1

        if len(heap) == 0:
          return w

        w -= heapq.heappop(heap)

      return w

k, w, profits, capital = 2, 0, [1,2,3], [0,1,1]

solution = Solution()

print('result: ', solution.findMaximizedCapital(k, w, profits, capital))
