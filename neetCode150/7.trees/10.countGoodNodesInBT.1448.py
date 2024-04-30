# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      def dfs(root, currMax):
        if not root:
          return 0
        
        adder = 0

        if root.val >= currMax:
          adder = 1
          currMax = root.val

        return adder + dfs(root.left, currMax) + dfs(root.right, currMax)
      
      return dfs(root, root.val)
    

    """
    DFS

    Track max value when go to the child node
      if childNode.val >= max:
        increment the counter
      


    """
