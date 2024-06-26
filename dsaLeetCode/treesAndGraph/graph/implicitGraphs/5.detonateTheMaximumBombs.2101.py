from collections import defaultdict, deque
import math

# NOTE
# Time Complexity: O(n ^ 3) Building Graph takes O(n ^ 2) time. 
  # BFS is O(V + E) there are n nodes and n^2 edges in this problem. 
    # Each node is only visited once O(n)
    # For each node we may need to explore up to n - 1 edges to find all neighbors.
    # Since there are n nodes the total number of edges we explore at most n(n - 1) = O(n ^ 2)

# Space Complexity: O(n ^ 2) Graph space QUEUE can store n nodes
  # O(n^2) edges in graph

def detonateMaxBombs(bombs):
  # build graph
  graph = defaultdict(list)
  n = len(bombs)

  for i in range(n):
    x1, y1, r = bombs[i]

    for j in range(n):
      if i == j:
        continue

      # check is second bomb is a neighbor of first bomb
      # use euclidean distance

      x2, y2, _ = bombs[j]

      # NOTE EUCLIDEAN distance
      distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

      # first node can detonate second node
      if distance <= r:
        graph[i].append(j)

   # bfs or dfs

   # BFS
  def bfs(i):
    q = deque([i])
    seen = set([i])

    while q:
     curr = q.popleft()

     for nei in graph[curr]:
       if nei in seen:
         continue

       seen.add(nei)
       q.append(nei)

    return len(seen)

  res = 0

  for i in range(n):
    res = max(bfs(i), res)

  return res


#bombs = [[2, 1, 3], [6, 1, 4]]
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]

print("Res:", detonateMaxBombs(bombs))


"""

bombs that located on the coordinate

[x, y, r]

x = location of the x coordinate.
y = location of the y coordinate.

r = denotes the radius of its range.



Distance between 2 points === EUCLIDEAN DISTANCE

ED = distance^2  = (x1 - x2)^2 + (y1 - y2)^2


"""
