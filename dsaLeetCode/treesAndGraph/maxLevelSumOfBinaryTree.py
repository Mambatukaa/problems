# Definition for a binary tree node.
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

import collections

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxLevelSum(self, root) -> int:
      resSum = -float('inf')
      resLevel = 0
      level = 1

      q = collections.deque([root])

      while q:
        size = len(q)
        levelSum = 0

        for _ in range(size):
          node = q.popleft()

          levelSum += node.val

          if node.left:
            q.append(node.left)
          if node.right:
            q.append(node.right)

        if levelSum > resSum:
          resSum = levelSum
          resLevel = level

        level += 1

      return resLevel

    # Recursive BFS
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def maxLevelSumII(self, root) -> int:
      res = []

      def bfs(root, depth):
        if not root:
          return

        if len(res) <= depth:
          res.append(0)

        res[depth] += root.val


        bfs(root.left, depth + 1)
        bfs(root.right, depth + 1)

      bfs(root, 0)

      level = -1
      maxVal = -float('inf')

      for i, num in enumerate(res):
        if num > maxVal:
          level = i + 1
          maxVal = num

      return level


solution = Solution()

root = TreeNode(1)

node2 = TreeNode(7)
node3 = TreeNode(0)

node4 = TreeNode(7)
node5 = TreeNode(-8)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5


# Return the level that has max sum
print("res:", solution.maxLevelSumII(root))
