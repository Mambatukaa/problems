# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Depth first search
# Time Complexity: O(n)
# Space Complexity: O(n)
# 9 minutes
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root:
       return 

      self.invertTree(root.left)
      self.invertTree(root.right)

      root.left, root.right = root.right, root.left

      return root


# Iterative DFS
class Solution1:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      stack = []
      curr = root

      while curr or len(stack):
        while curr:
          stack.append(curr)
          curr = curr.left
        
        curr = stack.pop()

        curr.left, curr.right = curr.right, curr.left

        curr = curr.left
      
      return root


