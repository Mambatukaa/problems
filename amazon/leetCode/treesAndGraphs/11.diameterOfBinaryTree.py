class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def diameterOfBinaryTree(root):
  res = [0]

  def dfs(root):
    if not root:
      return 0

    left = dfs(root.left)
    right = dfs(root.right)

    res[0] = max(res[0], left + right)

    return 1 + max(left, right)
  
  dfs(root)

  return res[0]

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)

node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

print("res:", diameterOfBinaryTree(root))

"""

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
  This path may or may not pass through the root.

"""
