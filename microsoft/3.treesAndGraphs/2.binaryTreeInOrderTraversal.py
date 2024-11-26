class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def __init__(self):
    self.answer = []

  # Recursive
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def inOrder(self, root):
    if not root:
      return

    self.inOrder(root.left)
    self.answer.append(root.val)
    self.inOrder(root.right)

    return self.answer

  # Iterative
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def inOrderII(self, root):
    stack = []
    curr = root

    while curr or stack:
      while curr:
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      self.answer.append(curr.val)
      curr = curr.right

    return self.answer


root = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)

root.left = node2
root.right = node3

solution = Solution()

print("res:", solution.inOrderII(root))
