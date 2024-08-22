from heapq import heappush, heappop, heapify

# Sort 
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def closestOrigin(points, k):

  distances = [] 

  for i in range(len(points)):
    point = points[i]
    distance = (point[0] * point[0]) + (point[1] * point[1])

    distances.append([i, distance])

  distances.sort(key = lambda distance: distance[1])

  res = []

  for i in range(k):
    res.append(points[distances[i][0]])

  return res

# Min Heap 
# Time Complexity: O(k)
# Space Complexity: O(n)
def closestOriginII(points, k):
  minHeap = []

  for [x, y] in points:
    dist = x ** 2 + y ** 2

    minHeap.append([dist, x, y])

  heapify(minHeap)

  res = []

  while k > 0:
    _, x, y = heappop(minHeap)

    res.append([x, y])

    k -= 1

  return res

points = [[3,3],[5,-1],[-2,4]]
k = 2

print("res:", closestOriginII(points, k))

"""

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


"""
