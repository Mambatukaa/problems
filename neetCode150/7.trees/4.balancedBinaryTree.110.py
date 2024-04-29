# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# Gave up
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      if not root:
        return True

      def dfs(root):
        if not root:
          return [True, 0] 
  
        left = dfs(root.left)
        right = dfs(root.right)

        balanced = left[0] and right[0] and  abs(left[1] - right[1]) < 2
        
        return [balanced, 1 + max(left[1], right[1])]; 

      return dfs(root)[0] 

class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True


# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 84 ms
