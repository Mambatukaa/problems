from heapq import heappush, heappop, heapify

# Min heap
# Time Complexity: O(k)
# Space Complexity: O(n)
class Solution:
    def kClosest(self, points, k):
        minHeap = []

        for [x, y] in points:
            dist = x ** 2  + y ** 2
            minHeap.append([dist, x, y])

        heapify(minHeap)

        res = []

        while k > 0:
            dist, x, y = heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

solution = Solution()


print(solution.kClosest([[1, 3], [-2, 2], [1, 1], [3, 3]], 2))

"""

 min heap

""" 
