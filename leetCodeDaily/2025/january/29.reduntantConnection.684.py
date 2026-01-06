""""

In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.

The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The
graph is represented as an array edges of length n where edges [i] = [aj, bil indicates that there is an edge
between nodes aj and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple
answers, return the answer that occurs last in the input.




Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:
    • n == edges. length
    • 3 < n <= 1000
    • edges [i].length == 2
    • 1 < ai < bi < edges. length
    • ai != bi
    • There are no repeated edges.
    • The given graph is connected.

"""


from collections import defaultdict
# Time Complexity: O(N)
# Space Complexity: O(N)
# DFS 
class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges)

        parent = [-1] * (N + 1)
        visited = [False] * (N + 1)

        self.cycleStart = -1


        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        def dfs(src):
            visited[src] = True

            for nei in graph[src]:
                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = src
                    dfs(nei)
                elif self.cycleStart == -1 and nei != parent[src]:
                    parent[nei] = src
                    self.cycleStart = src


        dfs(1)

        cycleNodes = set()
        node = self.cycleStart

        while True:
            cycleNodes.add(node)
            node = parent[node]

            if node in cycleNodes:
                break

        
        for i in range(N - 1, -1, -1):
            if edges[i][0] in cycleNodes and edges[i][1] in cycleNodes:
                return edges[i]


solution = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

print("res:", solution.findRedundantConnection(edges))

class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0


    def find(self, n):
        p = self.parent[n]

        # find the root parent
        while p != self.parent[p]:
            # optimization connect with grandparent
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        # cycle detected 
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Union find solution
class Solution:
    def findRedundantConnection(self, edges):
        unionFind = UnionFind(len(edges))

        for n1, n2 in edges:
            if not unionFind.union(n1, n2):
                return [n1, n2]
        
