class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
  def longestZigZag(self, root):

    def dfs(root, curr, fromLeft):
      if not root:
        return curr - 1

      return max(dfs(root.left, 1 if fromLeft else curr + 1, True), dfs(root.right, 1 if not fromLeft else curr + 1, False))

    return max(dfs(root.left, 1, True), dfs(root.right, 1, False))

# Solution from discussion
# Time Complexity: O(n)
# Space Complexity: O(n)
  def longestZigZagII(self, root):

    self.res = 0

    def dfs(node, left, right):
      self.res = max(self.res, left, right)

      if node.left:
        dfs(node.left, right + 1, 0)

      if node.right:
        dfs(node.right, 0, left + 1)
    
    dfs(root, 0, 0)

    return self.res

  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    self.res = 0

    def dfs(node, left, right):
      if not node:
        return max(left, right) - 1

      return max(dfs(node.left, right + 1, 0), dfs(node.right, 0, left + 1))
    
    return dfs(root, 0, 0)


root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node7 = TreeNode(7)


root.left = node2
root.right = node3

node2.right = node4
node4.left = node5
node4.right = node6

node5.right = node7

solution = Solution()

print('res:', solution.longestZigZag(root))
print('res:', solution.longestZigZagII(root))
