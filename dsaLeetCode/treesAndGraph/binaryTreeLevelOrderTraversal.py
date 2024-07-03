import collections

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Iterative BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
def levelOrder(root):
  res = []
  queue = collections.deque([root])

  while queue:
   size = len(queue)
   subArr = [] 

   for _ in range(size):
     curr = queue.popleft()

     subArr.append(curr.val)

     if curr.left:
       queue.append(curr.left)

     if curr.right:
       queue.append(curr.right)
   
   res.append(subArr)

  return res

# Recursive BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
# Always neighbors pass first
def levelOrderII(root):
  res = []

  def dfs(root, depth):
    if not root:
      return
 
    if len(res) <= depth:
      res.append([])

    res[depth].append(root.val)

    dfs(root.left, depth + 1)
    dfs(root.right, depth + 1)

  dfs(root, 0)

  return res



"""
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


"""


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

