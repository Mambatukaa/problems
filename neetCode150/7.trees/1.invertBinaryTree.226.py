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


# BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        queue = collections.deque([root])

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
        """
        if root is None:
            return root

        else:

            #temp = root.left
            #root.left = self.invertTree(root.right)
            #root.right = self.invertTree(temp)
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root 
        """
        """
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root        
        """
