""""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.

"""

# Iterative DFS
# Time Complexity: O(N + E) --> O(N)
# Space Complexity: O(N)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = {0}
        stack = [0]

        while stack:
            node = stack.pop()

            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)
        
        return len(seen) == n

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]

        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)

        seen = {0}
        queue = deque([0])

        while queue:
            node = queue.popleft()

            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
        
        return len(seen) == n

# DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        seen = set()
        
        def dfs(node, parent):
            if node in seen: return;
            seen.add(node)
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in seen:
                    return False
                result = dfs(neighbour, node)
                if not result: return False

    return True
        

# BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1: return False
        
        adj_list = [[] for _ in range(n)]
        for A, B in edges:
            adj_list[A].append(B)
            adj_list[B].append(A)
        
        parent = {0: -1}
        queue = collections.deque([0])
        
        while queue:
            node = queue.popleft()
            for neighbour in adj_list[node]:
                if neighbour == parent[node]:
                    continue
                if neighbour in parent:
                    return False
                parent[neighbour] = node
                queue.append(neighbour)
        
        return len(parent) == n
