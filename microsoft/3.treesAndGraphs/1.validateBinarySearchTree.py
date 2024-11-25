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

  # Iterative in order
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def isValidBSTII(self, root):
    stack = []
    curr = root
    self.prev = float('-inf')

    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      if self.prev >= curr.val:
        return False
      self.prev = curr.val
      curr = curr.right

    return True


root = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)


root.left = node2
root.right = node3

solution = Solution()
print("Res:", solution.isValidBSTII(root))
