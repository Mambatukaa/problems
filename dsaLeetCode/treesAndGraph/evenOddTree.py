class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    

from collections import deque

# Time Complexity: O(n)
# Space Complexity: O(n)
def evenOddTree(root):
  def isEven(num):
    return num % 2 == 0

  q = deque([root])
  level = 0

  while q:
    size = len(q)
    prev = None

    for _ in range(size):
      curr = q.popleft()

      if isEven(level):
        # check curr is odd and items are increasing
        if isEven(curr.val) or prev and prev.val >= curr.val:
          return False
      else:
        # check curr is even and items are decreasing
        if not isEven(curr.val) or prev and prev.val <= curr.val:

          return False

      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)

      prev = curr

    level += 1

  return True


root = TreeNode(1)

node2 = TreeNode(10)
node3 = TreeNode(1)

node4 = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(7)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6

print("res:", evenOddTree(root))




"""
Do bfs that is level order traversal.

And check the tree is even or odd and compare values on each level

If the level is not in the right order return False







"""
