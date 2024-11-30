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

  # Iterative BFS
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def connect(self, root):
    # BFS

    q = deque([root])

    while q:
      size = len(q)
      prev = None

      for _ in range(size):
        curr = q.popleft()

        if curr.left:
          q.append(curr.left)
        if curr.right:
          q.append(curr.right)

        if prev:
          prev.next = curr
        
        prev = curr


    return root

  # Iterative BFS
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  # Let's do the level order traversal and start to collect nodes in the array. When appending the next node of the level to the array update the current last node's next node by current node.
  def connectII(self, root):
    def dfs(root, level):
      if not root:
        return None

      if len(self.data) <= level:
        self.data.append([])

      # if current level has nodes update the last nodes next by current node
      if self.data[level]:
        self.data[level][-1].next = root

      self.data[level].append(root)

      dfs(root.left, level + 1)
      dfs(root.right, level + 1)
    
    dfs(root, 0)

    return root

solution = Solution()

res = solution.connectII(root)

print(res.val)
