""""

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.


"""

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# Topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort

        indegree = [0] * numCourses
        graph = defaultdict(list)

        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1
        
        q = deque([])

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        
        while q:
            node = q.popleft()
            res.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []

        

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# cycle detection dfs 
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for second, first in prerequisites:
            graph[second].append(first)

        stack = set()
        visited = set()

        def dfs(node):
            # circle detected
            if node in stack:
                return True
            if node in visited:
                return False

            stack.add(node)
            visited.add(node)


            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            stack.remove(node)
            res.append(node)

            return False

        
        res = []

        for course in range(numCourses):
            if dfs(course):
                return []
        
        return res
        


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for nxt, pre in prerequisites:
            indegree[nxt] += 1
            adj[pre].append(nxt)

        output = []

        def dfs(node):
            output.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return output if len(output) == numCourses else []
