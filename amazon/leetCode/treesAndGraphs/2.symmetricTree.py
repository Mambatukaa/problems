
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Recursive
# Time Complexity: O(n)
# Space Complexity: O(log n)
def isSymmetric(root):
  def dfs(node1, node2):
    if not node1 and not node2:
      return True

    if (not node1 or not node2):
      return False

    return node1.val == node2.val and dfs(node1.left, node2.right) and dfs(node1.right, node2.left)

  
  return dfs(root.left, root.right)

# Iterative
# Time Complexity: O(n)
# Space Complexity: O(log n)
def isSymmetricII(root):

  stack = [[root.left, root.right]]

  while stack:
    node1, node2 = stack.pop()

    if not node1 and not node2:
      continue

    if not node1 or not node2 or node1.val != node2.val:
      return False

    stack.append([node1.left, node2.right])
    stack.append([node1.right, node2.left])
  
  return True

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(2)

node4 = TreeNode(3)
node5 = TreeNode(4)

node6 = TreeNode(4)
node7 = TreeNode(3)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7


print(isSymmetricII(root))
