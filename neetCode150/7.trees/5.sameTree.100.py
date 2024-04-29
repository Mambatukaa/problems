# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
# Recursive DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      def dfs(p, q):
        if not p and not q:
          return True

        if not p or not q or q.val != p.val:
          return False

        return dfs(p.left, q.left) and dfs(p.right, q.right)

      return dfs(p, q)

# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
# Iterative BFS

 class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      queue = deque([[p, q]])

      while len(queue):
        [currP, currQ] = queue.popleft()

        if not currP and not currQ:
          continue
        
        if not currP or not currQ or currP.val != currQ.val:
          return False

        queue.append([currP.left, currQ.left])
        queue.append([currP.right, currQ.right])
      
      return True
               
