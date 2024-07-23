class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


from collections import deque

# Time Complexity: O(n)
# Space Complexity: O(n)
# Iterative BFS QUEUE
def zigZagLevelOrder(root):
  if not root:
    return []

  res = []
  level = 0

  q = deque([root])

  while q:
    size = len(q)
    sub = []

    for _ in range(size):
      curr = q.popleft()

      sub.append(curr.val)

      if curr.left:
        q.append(curr.left)

      if curr.right:
        q.append(curr.right)

    if level % 2 == 1:
      sub.reverse()

    res.append(sub)
    level += 1
  
  return res

# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursive
def zigZagLevelOrderII(root):

  res = []

  def dfs(root, level):
    if not root:
      return
 
    if len(res) <= level:
      res.append([])

    res[level].append(root.val)

    dfs(root.left, level + 1)
    dfs(root.right, level + 1)

  dfs(root, 0)

  for i in range(len(res)):
    if i % 2 == 1:
      res[i].reverse()
  

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

print("res:", zigZagLevelOrderII(root))

"""


return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



level 0: left to right
level 1: right to left

level 2: left to right
level 3: right to left

level 4: left to right
level 5: right to left

level 6: left to right
level 7: right to left



Even levels left to right
Odd levels right to left
"""
