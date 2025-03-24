""""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = defaultdict(list)

        for first, second in prerequisites:
            graph[first].append(second)

        visited = set()
        stack = set()
        # topological sort
        def dfs(node):
            if node in stack:
                return False

            if node in visited:
                return True

            visited.add(node)
            stack.add(node)

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            stack.remove(node)
            return True

        for node in range(numCourses):
            if node not in visited:
                print(node, stack)
                if not dfs(node):
                    return False

        return True

    def canFinishII(self, numCourses: int, prerequisites) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for first, second in prerequisites:
            # add the next courses to the prerequisites
            graph[second].append(first)
            
            # increase the prerequisites count 
            indegree[first] += 1

        q = deque([])

        for i in range(numCourses):
            # add the course which has no prerequisites to the queue
            if indegree[i] == 0:
                q.append(i)


        nodeVisited = 0

        while q:
            node = q.popleft()
            nodeVisited += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return nodeVisited == numCourses


solution = Solution()

numCourses = 2
prerequisites = [[1,0]]


print("res:", solution.canFinishII(numCourses, prerequisites))

