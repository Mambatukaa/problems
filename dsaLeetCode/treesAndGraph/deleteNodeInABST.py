class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def getSmallestNode(root):
  curr = root

  while curr.left:
    curr = curr.left

  return curr

# Time Complexity: O(height)
# Space Complexity: O(height)
def deleteNode(root, key):
  if not root:
    return root

  if key > root.val:
    root.right = deleteNode(root.right, key)
  elif key < root.val:
    root.left = deleteNode(root.left, key)
  else:
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    
    smallest = getSmallestNode(root.right)

    root.val = smallest.val
    root.right = deleteNode(root.right, root.val)

  return root

# in order
def traversal(root):
  if not root:
    return

  traversal(root.left)
  print(root.val)
  traversal(root.right)



root = TreeNode(5)

node2 = TreeNode(3)
node3 = TreeNode(6)

node4 = TreeNode(2)
node5 = TreeNode(4)
node6 = TreeNode(7)

node7 = TreeNode(1)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.right = node6

node4.left = node7


print("Traversal starting......")
traversal(root)
print("Traversal end")

print("res:", deleteNode(root, 1))
print("========================================")
print("Traversal starting......")
traversal(root)
print("Traversal end")



"""

To delete node from BST

If node has 2 children:
  Delete the node and replace to the right node's small node

else
  if not root.left:
    return root.right
  if not root.right:
    return root.left


1. To make new connection just replace the node's value







"""
