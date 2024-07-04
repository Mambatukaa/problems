# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(log n) # if tree is balanced
# Space Complexity: O(1)
class Solution:
    def searchBST(self, root, val):
      # left or right

      while root:
        if root.val == val:
          return root

        if root.val < val:
          # go right
          root = root.right
        else:
          # go left
          root = root.left

      return None

    # recursive
    def searchBST(self, root, val):
      if not root:
        return None
      
      if root.val == val:
        return root

      if root.val < val:
        return self.searchBST(root.right, val)
      else:
        return self.searchBST(root.left, val)
      

