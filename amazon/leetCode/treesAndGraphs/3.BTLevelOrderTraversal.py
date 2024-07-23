
class TreeNode: 
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from collections import deque

# Iterative solution:
# Time Complexity: O(N)
# Space Complexity: O(M)
def levelOrder(root):
  if not root:
    return []

  q = deque([root])
  res = []

  while q:
    size = len(q)
    subArr = []

    # collecting items level by level
    for _ in range(size):
      curr = q.popleft()

      subArr.append(curr.val)

      if curr.left:
        q.append(curr.left)

      if curr.right:
        q.append(curr.right)

    res.append(subArr)

  return res

# Recursive solution:
# Time Complexity: O(N)
# Space Complexity: O(M)
def levelOrderII(root):
  res = []


  def dfs(root, level):
    if not root:
      return

    # NOTE
    if len(res) <= level:
      res.append([])

    res[level].append(root.val)

    dfs(root.left, level + 1)
    dfs(root.right, level + 1)


  dfs(root, 0)


  return res

root = TreeNode(3)

node2 = TreeNode(9)
node3 = TreeNode(20)

node4 = TreeNode(15)
node5 = TreeNode(7)

root.left = node2
root.right = node3

node3.left = node4
node3.right = node5

print("res:", levelOrderII(root))



"""
Input: root = [3,9,20, null, null, 15,7]
Output: [[3],[9, 20], [15,7]]

"""
