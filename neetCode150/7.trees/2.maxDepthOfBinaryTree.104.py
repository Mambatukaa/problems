# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
# Time Complexity: O(n)
# Space Complexity: O(1)
# Iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0

      queue = collections.deque([root])

      level = 0

      while len(queue):
        size = len(queue)

        while size:
          curr = queue.popleft()

          if curr.left:
            queue.append(curr.left)

          if curr.right:
            queue.append(curr.right)

          size -= 1
        
        level += 1
      

      return level

# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursively
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0 
      
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


"""

LEVEL ORDER

and return max level


"""
        




"""

LEVEL ORDER

and return max level


"""
