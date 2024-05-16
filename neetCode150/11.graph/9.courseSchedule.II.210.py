class Solution:
    def findOrder(self, numCourses, prerequisites):
        # build graph
        graph = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)

        output = []

        visited, cycle = set()

        def dfs(crs):
            print('1111')

        for crs in range(numCourses):
            if not dfs(crs): return []

        return output

solution = Solution()

numCourses = 2
prerequisites = [
        [0, 1]
]

print(solution.findOrder(numCourses, prerequisites))





