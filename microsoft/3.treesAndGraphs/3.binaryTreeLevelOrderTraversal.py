from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None




class Solution:

  def __init__(self):
    self.res = []

  # Iterative level order
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def levelOrderTraversal(self, root):
    q = deque([[root, 0]])

    while q:
      curr, level = q.popleft()

      if len(self.res) <= level:
        self.res.append([])

      self.res[level].append(curr.val)

      if curr.left:
        q.append([curr.left, level + 1])

      if curr.right:
        q.append([curr.right, level + 1])

    return self.res

  # Recursive level order
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def levelOrderTraversalII(self, root):
    res = []

    def dfs(root, level):
      if not root:
        return

      if len(res) <= level:
        res.append([])
      
      res[level].append(root.val)

      dfs(root.left, level + 1)
      dfs(root.right, level + 1)

    dfs(root, 0)


    return res

solution = Solution()


root = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)

node4 = TreeNode(15)
node5 = TreeNode(7)


root.left = node2
root.right = node3

node3.left = node4
node3.right = node5


print("res:", solution.levelOrderTraversalII(root))
