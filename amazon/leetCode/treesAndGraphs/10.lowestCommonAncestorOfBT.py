# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    self.ans = TreeNode(0)

    def dfs(root):
      if not root:
        return False

      left = dfs(root.left)
      right = dfs(root.right)

      mid = root == p or root == q

      if left + right + mid >= 2:
        self.ans = root

      return left or right or mid


    dfs(root)
    return self.ans
        
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def lowestCommonAncestorII(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    res = None

    stack = []
    curr = root

    while curr or stack:
      while curr:
        # PRE ORDER print(curr.val)
        stack.append(curr)
        curr = curr.left

      curr = stack.pop()
      # IN ORDER print(curr.val)
      curr = curr.right

    return res

  # Minimized solution
  def lowestCommonAncestorIII(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root in [p, q]:
      return root

    left = self.lowestCommonAncestorIII(root.left, p, q)
    right = self.lowestCommonAncestorIII(root.right, p, q)

    if (left and right):
      return root

    return left or right
      

  
  # Iterative solution
  def lowestCommonAncestorIV(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    stack = [root]
    parent = {root: None}

    while (p not in parent) or (q not in parent):
      curr = stack.pop()

      if curr.left:
        parent[curr.left] = curr
        stack.append(curr.left)
      if curr.right:
        parent[curr.right] = curr
        stack.append(curr.right)

    ancestors = set()

    while p:
      ancestors.add(p)
      p = parent[p]

    # Find the q from ancestors
    while q not in ancestors:
      q = parent[q]

    return q

    

root = TreeNode(3)

node2 = TreeNode(5)
node3 = TreeNode(1)

node4 = TreeNode(6)
node5 = TreeNode(2)

node6 = TreeNode(0)
node7 = TreeNode(8)

node8 = TreeNode(7)
node9 = TreeNode(4)


root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node5.left = node8
node5.right = node9

solution = Solution()

p = node2
q = node9

print("res:", solution.lowestCommonAncestor(root, p, q).val)
print("-------------------------------------------------------------------------------------------------------------------")
print("res:", solution.lowestCommonAncestorIV(root, p, q).val)
