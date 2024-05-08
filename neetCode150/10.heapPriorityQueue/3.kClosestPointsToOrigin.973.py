from heapq import heappush, heappop

# Min heap
# Time Complexity: O(k)
# Space Complexity: O(n)
class Solution:
    def kClosest(self, points, k):

        distances = []
        res = []

        for i in range(len(points)):
            [x, y] = points[i]

            distance = (x * x + y * y, i)

            heappush(distances, distance)

        while k > 0:
            res.append(points[heappop(distances)[1]])
            k -= 1

        return res

solution = Solution()


solution.kClosest([[1, 3], [-2, 2], [1, 1], [3, 3]], 1)

"""

 min heap

""" 
