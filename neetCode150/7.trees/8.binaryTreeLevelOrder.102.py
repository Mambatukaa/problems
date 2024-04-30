# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
# Iterative
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []

      queue = deque([root])
      res = []

      while len(queue):
        subRes = []
        size = len(queue)

        while size:
          curr = queue.popleft()
          subRes.append(curr.val)

          if curr.left:
            queue.append(curr.left)

          if curr.right:
            queue.append(curr.right)

          size -= 1
        
        res.append(subRes)

      return res



  # ***********************8
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
# Recursive
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res = []

      def dfs(root, level):
        if not root:
          return
        
        if len(res) == level:
          res.append([])
        
        res[level].append(root.val)

        if root.left:
          dfs(root.left, level + 1)
        if root.right:
          dfs(root.right, level + 1)

      dfs(root, 0)

      return res



