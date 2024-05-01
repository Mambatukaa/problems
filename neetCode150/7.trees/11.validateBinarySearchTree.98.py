# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 1 hour
# Recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      def dfs(root, minRange, maxRange):
        if not root:
          return True
        
        if root.val <= minRange or root.val >= maxRange:
          return False

        return dfs(root.left, minRange, root.val) and dfs(root.right, root.val, maxRange)
      
      return dfs(root, -float('inf'), float('inf'))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 1 hour
# Iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      queue = deque([[root, -float('inf'), float('inf')]])

      while len(queue):
        [curr, minRange, maxRange] = queue.popleft()

        if curr.val <= minRange or curr.val >= maxRange:
          return False
        
        if curr.left:
          queue.append([curr.left, minRange, curr.val])
        if curr.right:
          queue.append([curr.right, curr.val, maxRange])
      

      return True


