from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None



root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node4 = TreeNode(4)
node5 = TreeNode(5)

node6 = TreeNode(6)
node7 = TreeNode(7)

root.left = node2
root.right = node3


node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7


class Solution:
  def __init__(self):
    self.data = []
