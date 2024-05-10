"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
# Time Complexity: O(n) V+E
# Space Complexity: O(n) V+E
# Gave up (neetcode)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      oldToNew = {}

      def dfs(node):
        if node in oldToNew:
          return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy

        for nei in node.neighbors:
          copy.neighbors.append(dfs(nei))

        return copy
      
      return dfs(node) if node else None

# Using queue
# BFS
# Time Complexity: O(n) n = V + E
# Space Complexity: O(n)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
      if not node:
        return None

      oldToNew = {node: Node(node.val)}

      def bfs(node):
          if not node:
            return None
            
          queue = deque([node])

          while len(queue):
              curr = queue.popleft()

              for nei in curr.neighbors:
                if nei not in oldToNew:
                  oldToNew[nei] = Node(nei.val)
                  queue.append(nei)
                
                oldToNew[curr].neighbors.append(oldToNew[nei])

      bfs(node)

      return oldToNew[node]


"""
1: 2 -> 4
2: 1 -> 3
3: 2 -> 4
4: 1 -> 3 




queue = [4, 3, 3]

    map = 1:1,

    for nei in neighbors:
        if map[nei]:

        
        queue.append(nei)
    




      


"""
