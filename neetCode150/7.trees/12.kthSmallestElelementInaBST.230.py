# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 10 minutes
# Iterative in order
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      counter = 1
      stack = []
      curr = root

      while curr or len(stack):
        while curr:
          stack.append(curr)
          curr = curr.left
        
        curr = stack.pop()

        if counter == k:
          return curr.val
        
        counter += 1
        curr = curr.right

# In order traversal and return k th element
