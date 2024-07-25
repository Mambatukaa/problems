
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursive dfs
def maxPathSum(root):
  res = [root.val]

  def dfs(root):
    if not root:
      return 0

    leftMax = dfs(root.left)
    rightMax = dfs(root.right)

    leftMax = max(leftMax, 0)
    rightMax = max(rightMax, 0)

    # Splitted
    res[0] = max(res[0], root.val + leftMax + rightMax)
    
    # without splitting
    return root.val + max(leftMax, rightMax)

  dfs(root)

  return res[0]

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)

root.left = node2
root.right = node3

print("Sum:", maxPathSum(root))


# With split or without split
