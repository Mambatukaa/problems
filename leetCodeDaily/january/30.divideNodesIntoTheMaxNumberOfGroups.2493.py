""""



You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.
You are also given a 2D integer array edges, where edges (i) = [ai, bi] indicates that there is a bidirectional edge between nodes aj and
bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:
    • Each node in the graph belongs to exactly one group.
    • For every pair of nodes in the graph that are connected by an edge [as, bil, if as belongs to the group with index x, and bi belongs to
the group with index y, then |y - x| = 1.

Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes
with the given conditions.



Input: n = 6, edges = [[1,2], [1,4], [1,5] , [2,6] , [2,3] , [4,6]]
Output: 4

    Explanation: As shown in the image we:
    - Add node 5 to the first group.
    - Add node 1 to the second group.
    - Add nodes 2 and 4 to the third group.
    - Add nodes 3 and 6 to the fourth group.

We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to
it, at least on of the edges will not be satisfied.




Input: n = 3, edges = [[1,2], [2,3], [3,1]]
Output: -1

Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group
to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.

"""

from collections import defaultdict, deque

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# BFS and bipartite graph
class Solution:
    def magnificentSets(self, n: int, edges):
        adjList = defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def getComponents(i):
            q = deque([i])
            components = set([i])

            while q:
                curr = q.popleft()
                
                for nei in adjList[curr]:
                    if nei not in components:
                        components.add(nei)
                        q.append(nei)

            return components


        def getMaxGroup(i):
            q = deque([[i, 1]])

            groups = {i: 1}

            while q:
                curr, length = q.popleft()

                for nei in adjList[curr]:
                    if nei in groups:
                        if groups[nei] == length:
                            return -1
                        continue

                    visited.add(i)
                    groups[nei] = length + 1
                    q.append([nei, groups[nei]])

            return max(groups.values())

        visited = set()

        res = 0

        for i in range(1, n + 1):
            if i in visited:
                continue

            visited.add(i)

            components = getComponents(i)

            maxCount = 0

            for component in components:
                # do the bfs on each components and find max groups count
                count = getMaxGroup(component)

                if count == -1:
                    return -1
                
                maxCount = max(maxCount, count)
            
            res += maxCount

        return res


n = 6

edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]



solution = Solution()

edges =[[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]
n = 92

print("res:", solution.magnificentSets(n, edges))

