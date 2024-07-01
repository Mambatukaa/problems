class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Time Complexity: O(n)
# Space Complexity: O(n)
# Post order traversal
# Recursive
def removeLeafNodes(root, target):
  if not root:
    return

  removeLeafNodes(root.left, target)
  removeLeafNodes(root.right, target)

  leftNode = root.left

  if leftNode and (not leftNode.left and not leftNode.right):
    if leftNode.val == target:
      root.left = None

  rightNode = root.right

  if rightNode and (not rightNode.left and not rightNode.right):
    if rightNode.val == target:
      root.right = None

  if not root.left and not root.right and root.val == target:
    root = None

  return root


root = TreeNode(2)

node2 = TreeNode(2)
node3 = TreeNode(2)

root.left = node2
root.right = node3

root = removeLeafNodes(root, 2)
print(root.val)

print(root.left, '==', root.right)


"""

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]

Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Post order traversal:

  1. If node is a leaf and equal to target:
      Remove the node



  DELETING A LEAF NODE
    root.left is a leaf and root.left == target:
      root.left = None
    root.right is a leaf and root.right == target:
      root.right = None

    


"""
