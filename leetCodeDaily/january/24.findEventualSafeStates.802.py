


class Solution:
    def eventualSafeNodes(self, graph):




        












solution = Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
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
