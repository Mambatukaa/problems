
"""


There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array
graph where (graph [1] is an integer array of nodes adjacent to node 1, meaning there is an edge from node i to each node in graph [1] .
A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a
terminal node (or another safe node).
Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""


class Solution:
    # Time Complexity: O(V + E)
    # Space Complexity: O(V + E)
    # Detect cycle
    # DFS
    def eventualSafeNodes(self, graph):

        isSafe = {}

        def dfs(node):
            if node in isSafe:
                return isSafe[node]

            isSafe[node] = False

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
                
            isSafe[node] = True

            return isSafe[node]

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res



        












solution = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print("res:", solution.eventualSafeNodes(graph))
"""


    Building a graph.

    0: [1, 2]
    1: [2, 3]
    2: [5]
    3: [0]
    4: [5]
    5: [] TERMINAL NODE
    6: [] TERMINAL NODE



graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]


0: [1, 2, 3, 4]
1: [1, 2]
2: [3, 4]
3: [0, 4]
4: []




A node is a terminal node if there are no outgoing edges. 
    A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.


[[],[0,2,3,4],[3],[4],[]]


0: []
1: [0, 2, 3, 4]
2: [3]
3: [4]
4: [5]

"""
