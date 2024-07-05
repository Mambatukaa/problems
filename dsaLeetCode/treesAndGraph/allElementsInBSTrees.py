class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def getAllElements(root1, root2):

  def inOrder(root, array):
    if not root:
      return 

    inOrder(root.left, array)
    array.append(root.val)
    inOrder(root.right, array)

  array1 = []
  array2 = []

  inOrder(root1, array1)
  inOrder(root2, array2)

  res = []
  l = 0
  r = 0

  # merge arrays
  while l < len(array1) and r < len(array2):
    if array1[l] < array2[r]:
      res.append(array1[l])
      l += 1
    else:
      res.append(array2[r])
      r += 1

  return res + array1[l:] + array2[r:]

root1 = TreeNode(2)

node2 = TreeNode(1)
node3 = TreeNode(3)

root1.left = node2
root1.right = node3

root2 = TreeNode(5)

node4 = TreeNode(4)

root2.left = node4

print("res:",getAllElements(root1, root2))



"""

Given two binary search trees.

Merge trees values in array by ascending order.


Naive approach

Do the inOrderTraversal on two binary Search trees and collect values on arrays.

Merge two arrays by sorted by order.

return mergedArray

Time Complexity: O(n + m)
Space Complexity: O(n + m)



"""
