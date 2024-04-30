# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(s * t)
# Space Complexity: O(s * t)
# Gave up
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
      if not t: return True
      if not s: return False

      if(self.isSameTree(s, t)):
        return True
      
      return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, s, t):
      if not s and not t:
        return True
      
      if not s or not t or s.val != t.val:
        return False
      
      return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
      queue = deque([root])
      sameRoot = []

      while len(queue):
        curr = queue.popleft()

        if curr.val == subRoot.val:
          # same root found
          sameRoot.append(curr)
        
        if curr.left:
          queue.append(curr.left)
        
        if curr.right:
          queue.append(curr.right)

      
      if not len(sameRoot):
        return False


      def dfs(root, subRoot):
        if root is None and subRoot is None:
          return True
        
        if not root or not subRoot or root.val != subRoot.val:
          return False
        
        return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)


      for i in range(len(sameRoot)):
        if dfs(sameRoot[i], subRoot) != False:
          return True
      
      return False

        



"""

Search subRoot's root from root node
  if found compare two nodes as a sameTree

to search SubRoot's root from root node use BFS

"""
