class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  # In order
  # Recursive
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def isValidBST(self, root):
    self.prev = float('-inf')
    def inOrder(root):
      if not root:
        return True

      
      leftRes = inOrder(root.left)

      if root.val <= self.prev:
        return False

      self.prev = root.val

      rightRes = inOrder(root.right)

      return leftRes and rightRes

    return inOrder(root)


root = TreeNode(8)
node2 = TreeNode(1)
node3 = TreeNode(3)


root.left = node2
root.right = node3

solution = Solution()
print("Res:", solution.isValidBST(root))
