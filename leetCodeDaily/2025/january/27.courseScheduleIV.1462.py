
""""

There are a total of numCourses courses you have to take, labeled from @ to numCourses - 1. You are given an array prerequisites where
prerequisites [1] = [ai, bil indicates that you must take course a first if you want to take course bi.

    • For example, the pair [0, 1] indicates that you have to take course @ before you can take course 1.
    Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a
    prerequisite of course c.

You are also given an array queries where queries [j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite
of course vj or not.

Return a boolean array answer, where answer [jl is the answer to the jt query.



Input: numCourses = 3, prerequisites = [[1,2], [1,0], [2,0]], queries = [[1,0], [1,2]]
Output: [true, truel



Constraints:

• 2 < numCourses < 100
• 0 < prerequisites. length < (numCourses * (numCourses - 1) / 2)
• prerequisites [i]. length == 2
• 0 < ai, bi <= numCourses - 1
• as |= bs
• All the pairs [as, bi] are unique.
• The prerequisites graph has no cycles.
• 1 <= queries. length <= 104
• 0 <= ui, Vi <= numCourses - 1
• ui != vi

"""



from collections import defaultdict
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites, queries):
        # build graph
        graph = defaultdict(list)

        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()

                for prereq in graph[crs]:
                    prereqMap[crs].update(dfs(prereq))
                prereqMap[crs].add(crs)

            return prereqMap[crs]

        prereqMap = {}
        # collect prerequisites
        for crs in range(numCourses):
            dfs(crs)

        res = []

        for u, v in queries:
            res.append(u in prereqMap[v])

        return res





# 0 --> 1 --> 2

numCourses = 2
prerequisites = [[1,0],[2,1]]
queries = [[1,0],[2,0]]

solution = Solution()

print("res:", solution.checkIfPrerequisite(numCourses, prerequisites, queries))
