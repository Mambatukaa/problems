# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Time Complexity: O(n)
# Space Complexity: O(1)
# Gave up

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      curr = root

      while curr:
        if curr.val < p.val and curr.val < q.val:
          # go right
          curr = curr.right 
        elif curr.val > p.val and curr.val > q.val:
          # go left
          curr = curr.left
        else:
          # curr is the LCA
          return curr


"""
LOWEST COMMON ANCESTOR

"""
