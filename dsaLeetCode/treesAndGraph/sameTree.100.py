import collections


class TreeNode: 
  def __init__(self, val):
    self.val = val
    self.right = None
    self.left = None

# Time Complexity: O(n)
# Space Complexity: O(n)
def sameTree(p, q):

  queue = collections.deque([[p, q]])

  while queue:
    first, second = queue.popleft()

    if not first and not second:
      continue

    if not first or not second or first.val != second.val:
      return False

    queue.append([first.left, second.left])
    queue.append([first.right, second.right])

  return True


pRoot = TreeNode(1)
pNode1 = TreeNode(2)
pRoot.right = pNode1

qRoot = TreeNode(1)
qNode1 = TreeNode(2)
qRoot.left = qNode1

print("res:", sameTree(pRoot, qRoot))

"""

p = [1, 2, 3]
q = [1, 2, 3]

output = true


Given two binary tree. Check trees are the same or not.


1. DFS or BFS and check the trees are the same




"""

