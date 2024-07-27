from collections import defaultdict

def courseSchedule(numCourses, prerequisites):
  graph = defaultdict(list)

  for prerequisite in prerequisites:
    child, parent = prerequisite

    graph[child].append(parent)

  def dfs(course, seen):
    print(course, seen)
    if course in seen:
      return False


    if not graph[course]:
      return True

    seen.add(course)

    for neighbor in graph[course]:
      res = dfs(neighbor, seen)

      return False if not res else True
    

  for course in range(numCourses):
    if not dfs(course, set()):
      return False

  return True

numCourses = 4
prerequisites = [[2, 1], [1, 0]]

prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]


print("Res:", courseSchedule(numCourses, prerequisites))
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
