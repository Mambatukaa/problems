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

  # with min and max value
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def isValidBSTIII(self, root):
    def isValid(minVal, root, maxVal):
      if not root:
        return True

      if minVal >= root.val or maxVal <= root.val:
        return False

      return isValid(minVal, root.left, root.val) and isValid(root.val, root.right, maxVal)
    
    return isValid(float('-inf'), root, float("inf"))

  # BST
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def isValidBSTIV(self, root):
    stack = [[float('-inf'), root, float("inf")]]

    while stack:
      minVal, curr, maxVal = stack.pop()

      if minVal >= curr.val or maxVal <= curr.val:
        return False

      if curr.left:
        stack.append([minVal, curr.left, curr.val])

      if curr.right:
        stack.append([curr.val, curr.right, maxVal])

    return True



root = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(2)


root.left = node2
root.right = node3

solution = Solution()
print("Res:", solution.isValidBSTIV(root))
