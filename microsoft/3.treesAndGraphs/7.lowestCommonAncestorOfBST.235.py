from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = TreeNode(6)

node2 = TreeNode(2)
node3 = TreeNode(8)

node4 = TreeNode(0)
node5 = TreeNode(4)

node6 = TreeNode(7)
node7 = TreeNode(9)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

class Solution:
  # Recursive Solution
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def lowestCommonAncestor(self, root, p, q):
    if root.val < p.val and root.val < q.val:
      # go right
      return self.lowestCommonAncestor(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
      # go left
      return self.lowestCommonAncestor(root.left, p, q)
    else:
      return root

    
  # Iterative solution
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  def lowestCommonAncestorII(self, root, p, q):
    while root:
    if root.val < p.val and root.val < q.val:
      # go right
      root = root.right
    elif root.val > p.val and root.val > q.val:
      # go left
      root = root.left
    else:
      return root

    return None
    


solution = Solution()

print("Res:", solution.lowestCommonAncestorII(root, node5, node7).val)


"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

p != q

All node.val are unique

p and q will exist in BST.



*****************

BST:
  1. if (root.val >= p.val and root.val <= q.val) or 
        (root.val <= p.val and root.val >= q.val):
          return root
  2. if root.val < q.val:
        # go right
     else:
        # go left



"""
