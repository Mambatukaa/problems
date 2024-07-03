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
