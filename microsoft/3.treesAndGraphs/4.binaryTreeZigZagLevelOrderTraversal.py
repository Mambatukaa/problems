from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None




class Solution: 
  def __init__(self):
    self.res = []


  # Iterative BFS
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def zigzagLevelOrder(self, root):
    if not root:
      return []

    q = deque([root])
    level = 0


    while q:
      size = len(q)
      sub = []

      for _ in range(size):
        curr = q.popleft()
        sub.append(curr.val)

        if curr.left:
          q.append(curr.left)

        if curr.right:
          q.append(curr.right)

      if level % 2 == 1:
        # reverse
        sub.reverse()

      self.res.append(sub)

      level += 1

    return self.res
        

    




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

print("res:", solution.zigzagLevelOrder(root))

"""


Left to right Level % 2 ==0
right to left else



"""
