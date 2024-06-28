# Definition for a binary tree node.
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

      def dfs(root, res):
        if not root:
          return

        # check the node is leaf or not
        if not root.left and not root.right:
          res.append(root.val)

        dfs(root.left, res)
        dfs(root.right, res)

        return res

      return dfs(root1, []) == dfs(root2, [])

    def leafSimilarII(self, root1, root2) -> bool:
      def dfs(root):
        res = []

        stack = []
        curr = root

        while stack or curr:
          while curr:
            stack.append(curr)
            curr = curr.left

          curr = stack.pop()

          if not curr.left and not curr.right:
            res.append(curr.val)

          curr = curr.right

        return res

      return dfs(root1) == dfs(root2)


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

print("res:", solution.leafSimilarII(root1, root2))





        
