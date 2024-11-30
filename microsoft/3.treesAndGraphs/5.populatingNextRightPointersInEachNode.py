from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None



root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node4 = TreeNode(4)
node5 = TreeNode(5)

node6 = TreeNode(6)
node7 = TreeNode(7)

root.left = node2
root.right = node3


node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7


class Solution:
  # Iterative BFS
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def connect(self, root):
    # BFS

    q = deque([root])

    while q:
      size = len(q)
      prev = None

      for _ in range(size):
        curr = q.popleft()

        if curr.left:
          q.append(curr.left)
        if curr.right:
          q.append(curr.right)

        if prev:
          prev.next = curr
        
        prev = curr


    return root


solution = Solution()

res = solution.connect(root)
