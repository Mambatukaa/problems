# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Iterative solution
    def averageOfLevels(self, root):
      res = []

      q = deque([root])
      

      while q:
        size = len(q)
        currSum = 0

        for _ in range(size):
          node = q.popleft()

          currSum += node.val

          if node.left:
            q.append(node.left)

          if node.right:
            q.append(node.right)

        res.append(currSum / size)


      return res

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Recursive solution
    def averageOfLevelsII(self, root):
      levels = {} 

      # key: [sum, countOfItems]

      def bfs(root, depth):
        if not root:
          return
         
        if not depth in levels:
          levels[depth] = [0, 0]

        levels[depth][0] += root.val
        levels[depth][1] += 1

        bfs(root.left, depth + 1)
        bfs(root.right, depth + 1)

      bfs(root, 0)

      res = []

      for v in levels.values():
        res.append(v[0] / v[1])

      return res



root = TreeNode(3)

node2 = TreeNode(9)
node3 = TreeNode(20)

node4 = TreeNode(15)
node5 = TreeNode(7)

root.left = node2
root.right = node3

node3.left = node4
node3.right = node5


solution = Solution()

print("res:", solution.averageOfLevelsII(root))
