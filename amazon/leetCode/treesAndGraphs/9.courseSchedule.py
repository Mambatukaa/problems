from collections import defaultdict, deque

# DFS 
# Time Complexity: O(n)
# Space Complexity: O(n)
def courseSchedule(numCourses, prerequisites):
  graph = defaultdict(list)

  for prerequisite in prerequisites:
    child, parent = prerequisite

    graph[child].append(parent)

  def dfs(course, seen):
    if course in seen:
      return False

    # NOTE add visited node on seen
    seen.add(course)

    # NOTE take the prerequisites of current node
    for neighbor in graph[course]:
      res = dfs(neighbor, seen)

      if not res:
        return False

    # Current courses prerequisites completed and remove the course from visited and remove all prerequisites
    seen.remove(course)
    graph[course] = []

    return True

  for course in range(numCourses):
    if not dfs(course, set()):
      return False

  return True



# Kahn's Algorithm
# Topological Sort
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def courseScheduleII(numCourses, prerequisites):
  indegree = [0] * numCourses
  adj = [[] for i in range(numCourses)]

  for prerequisite in prerequisites:
    adj[prerequisite[1]].append(prerequisite[0])
    indegree[prerequisite[0]] += 1

  queue = deque()

  for i in range(numCourses):
    if indegree[i] == 0:
      queue.append(i)

  visitedNodes = 0

  while queue:
    node = queue.popleft()
    visitedNodes += 1

    # NOTE Reduce the children indegree
    for neighbor in adj[node]:
      indegree[neighbor] -= 1

      if indegree[neighbor] == 0:
        queue.append(neighbor)

  return visitedNodes == numCourses


numCourses = 4
prerequisites = [[2, 1], [1, 0]]

prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]


print("Res:", courseScheduleII(numCourses, prerequisites))
"""
[[1,0],[1,2],[0,1]]


0: [1]
1: [0, 2]
2: []




Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.

To take course 1 you should have finished course 0. So it is possible.







prerequisites[i] = [ai, bi]

to take ai you need to complete bi.





numCourses = 3

0 1 2

[2, 1], [1, 0], [0, 2] ====> FALSE CIRCLE DETECTED Infinit loop

[2, 1], [1, 0] ====> TRUE


0: []
1: [0]
2: [1]

Is it possible to take all courses?

1. Visit to neighbors and complete the prerequisite courses.

Build graph

And iterate through courses and do BFS or DFS

If cycle detected return False

Remove neighbor from the node and visit the removed nodes etc

if visited node has no neighbor return True






"""
