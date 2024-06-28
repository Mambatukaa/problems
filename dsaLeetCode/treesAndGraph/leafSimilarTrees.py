# Definition for a binary tree node.
import collections
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
# Naive solution
# DFS
class Solution:
    def leafSimilar(self, root1, root2) -> bool:
      q = collections.deque()

      def dfs(root, isStoring):
        if not root:
          return True

        # check the node is leaf or not
        if not root.left and not root.right:
          if isStoring:
            q.append(root.val)
          else:
            if not q or q.popleft() != root.val:
              return False
          return True

        return dfs(root.left, isStoring) and dfs(root.right, isStoring)

      return dfs(root1, True) and dfs(root2, False) and not 


"""

1. Do dfs or bfs traversal on first node and store all leafs 
2. Do dfs or bfs traverl on second node and check leaf node in first notes set
    If True continue
    else return False





"""


root1 = TreeNode(1)
root2 = TreeNode(1)

root1.left = TreeNode(2)
root2.right = TreeNode(2)

root1.right = TreeNode(2)
root2.left = TreeNode(3)

solution = Solution()

print("res:", solution.leafSimilar(root1, root2))





        
