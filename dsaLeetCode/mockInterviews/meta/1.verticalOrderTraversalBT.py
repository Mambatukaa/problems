"""
 Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

 For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. 
  The root of the tree is at (0, 0).

 The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from 
  the leftmost column and ending on the rightmost column.


                                       3
                                    /     \
                                  9       20
                                        /    \
                                       15     7


answer: [[9], [3, 15], [20], [7]]

"""

from collections import deque, defaultdict

def vertical_traversal(root):
  # root column = 0
  # BFS
  
  queue = deque([(root, 0)])
  dic = defaultdict(list)

  while queue:
    node, offset = queue.popleft()
    dic[offset].append(node.val)

    if node.left:
      queue.append((node.left, offset - 1))
    if node.right:
      queue.append((node.right, offset + 1))


  ans = []

  for col in sorted(dic.keys()):
    ans.append(dic[col])

  return ans


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None



node1 = TreeNode(3)

node2 = TreeNode(9)
node3 = TreeNode(20)

node4 = TreeNode(15)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3

node3.left = node4
node3.right = node5


print("answer: ", vertical_traversal(node1))











