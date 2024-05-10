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







        


"""
1: 2 -> 4
2: 1 -> 3
3: 2 -> 4
4: 1 -> 3


"""
