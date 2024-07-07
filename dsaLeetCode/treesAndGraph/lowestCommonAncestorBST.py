class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val



# Time Complexity: O(n)
# Space Complexity: O(n)
# DFS
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      if not root:
        return

      if p.val == root.val or q.val == root.val or (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
        return root

      if p.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
      else:
        return self.lowestCommonAncestor(root.left, p, q)

    # iterative
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lowestCommonAncestorII(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      while root:
        if p.val > root.val and q.val > root.val:
          root = root.right
        elif p.val < root.val and q.val < root.val:
          root = root.left
        else:
          return root

    # clean code
    def lowestCommonAncestorIII(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
      elif p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
      else:
        return root


root = TreeNode(6)

node2 = TreeNode(2)
node3 = TreeNode(8)

node4 = TreeNode(0)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(9)

node8 = TreeNode(3)
node9 = TreeNode(5)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node5.left = node8
node5.right = node9

p = node2
q = node5


solution = Solution()

print("Res:", solution.lowestCommonAncestorII(root, p, q).val)
