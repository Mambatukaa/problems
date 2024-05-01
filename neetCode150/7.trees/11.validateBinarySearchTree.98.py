# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 1 hour
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      def dfs(root, minRange, maxRange):
        if not root:
          return True
        
        if root.val <= minRange or root.val >= maxRange:
          return False

        return dfs(root.left, minRange, root.val) and dfs(root.right, root.val, maxRange)
      
      return dfs(root, -float('inf'), float('inf'))


