from collections import deque, defaultdict

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
  def numOfMinutes(self, n, headID, manager, informTime):
    graph = defaultdict(list)

    for i in range(n):
      lead = manager[i]

      if not lead == -1:
        graph[lead].append(i)

    res = informTime[headID]

      # Do bfs starting from headID
    q = deque([headID])

    print(graph)

    while q:
      size = len(q)

      maxInformMinute = 0

      for _ in range(size):
        curr = q.popleft()
        neighbors = graph[curr]

        for neighbor in neighbors:
          maxInformMinute = max(maxInformMinute, informTime[neighbor])
          print(maxInformMinute)
          q.append(neighbor)

      res += maxInformMinute

    return res

n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]

n= 10
headID = 3
manager = [8,9,8,-1,7,1,2,0,3,0]
informTime = [224,943, 160,909,0,0,0,643, 867, 722]


n = 11
headID = 4

manager = [5,9,6,10,-1,8,9,1,9,3,4]
informTime = [0,213,0,253,686,170,975,0,261,309,337]


solution = Solution()
print("res:", solution.numOfMinutes(n, headID, manager, informTime))



"""
BFS (GRAPH)

result's initial value is informTime to HeadID

1. Start to add neighbors starting from HEADID

2. Add maxInform time from each level to the result

3. collectNeighbors using manager




"""


