# in order traversal
# But in order is not work when nodes are equal


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# min, max values
# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursive
def isValidBST(root) -> bool:
  def dfs(node, currMin, currMax):
    if not node:
      return True

    if node.val <= currMin or node.val >= currMax:
      return False

    return dfs(node.left, currMin, node.val) and dfs(node.right, node.val, currMax)
  
  return dfs(root, -float('inf'), float('inf'))

# Time Complexity: O(n)
# Space Complexity: O(n)
# DFS
# Iterative
def isValidBSTII(root) -> bool:
  # DFS
  stack = [[root, -float('inf'), float('inf')]]

  while stack:
    curr, currMin, currMax = stack.pop()

    if curr.val <= currMin or curr.val >= currMax:
      return False

    if curr.left:
      stack.append([curr.left, currMin, curr.val])
    if curr.right:
      stack.append([curr.right, curr.val, currMax])

  return True



root = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)


root.left = node2
root.right = node3


print("res:", isValidBSTII(root))



"""


               5
             /   \
       -inf 3     8
           / \     \
          2   4     9


valid ===>  min < node < max

left ===> min = currMin, max = node.val
right ==> min = node.val, max = currMax


"""
