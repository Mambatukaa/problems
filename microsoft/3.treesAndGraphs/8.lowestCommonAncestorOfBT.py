from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)

node4 = TreeNode(4)
node5 = TreeNode(5)

node6 = TreeNode(6)
node7 = TreeNode(7)

root.left = node2
root.right = node3

no# de2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

class Solution:
  # Recursive Solution
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def lowestCommonAncestor(self, root, p, q):
    def dfs(curr):
      if not curr:
        return False

      left = dfs(curr.left)
      right = dfs(curr.right)

      mid = curr == p or curr == q

      if left + mid + right == 2:
        self.answer = curr

      return mid or left or right

    
    dfs(root)
    return self.answer


  # Iterative 
  # Use parent pointers
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def lowestCommonAncestorII(self, root, p, q):
    stack = [root]

    parent = {root: None}

    while p not in parent q not in parent:
      curr = stack.pop()

      # While traversing the tree, keep saving the parent pointers.
      if curr.left:
        parent[curr.left] = curr
        stack.append(curr.left)

      if curr.right:
        parent[curr.right] = curr
        stack.append(curr.right)


    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
      ancestors.add(p)
      p = parent[p]


    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
      q = parent[q]

    return q

    
solution = Solution()

print("Res:", solution.lowestCommonAncestor(root, node7, node6).val)


"""

Given a binary tree (BT), find the lowest common ancestor (LCA) node of two given nodes in the BT.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

p != q

All node.val are unique

p and q will exist in BT.


"""
