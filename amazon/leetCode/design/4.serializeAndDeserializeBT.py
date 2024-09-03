from collections import deque

# Definition for a binary tree node.
class TreeNode():
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

# Add solution using BFS
class Codec:
  def serialize(self, root):
    if not root:
      return ""

    res = ["None", str(root.val)]
    q = deque([root])
        
    # Level Order
    while q:
      node = q.popleft()

      leftVal = None
      rightVal = None

      if node.left:
        q.append(node.left)
        leftVal = node.left.val

      if node.right:
        q.append(node.right)
        rightVal = node.right.val

      res.append(str(leftVal))
      res.append(str(rightVal))

    return ','.join(res)

  def deserialize(self, data):
    data = data.split(",")

    # edge case
    if len(data) <= 1:
      return None

    root = TreeNode(int(data[1]))
    q = deque([root])
    idx = 1

    while q and idx <= len(data) // 2:
      curr = q.popleft()

      left = data[2 * idx]
      right = data[2 * idx + 1]

      if left != 'None':
        curr.left = TreeNode(int(left))
        q.append(curr.left)

      if right != 'None':
        curr.right = TreeNode(int(right))
        q.append(curr.right)

      idx += 1

    return root


# PRE ORDER
class CodecII:
  def serialize(self, root):
    print(root)


  def deserialize(self, data):
    return data




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


"""

                      1
                    /   \
                   2     3
                       /   \
                      4     5


 0 1 2 3 4 5 6 7
"n,1,2,3,n,n,4,5"


LEVEL ORDER TRAVERSAL

q = [1]

popleft() => 1
  ----------------------------------------
  1:
   res = [1, 2, 3, ]
   q = [2, 3]

  q.popleft() => 2
  ----------------------------------------
  2: 
    res = [1, 2, 3, null, null]
    q = [3]

  q.popleft() => 3
  ----------------------------------------

  3:
    res = [1, 2, 3, null, null, 4, 5]
    q = [4, 5]

  q.popleft => 4
  ----------------------------------------
  4:
    res = [1, 2, 3, null, null, 4, 5, null, null]
    q = [5]

  q.popleft => 5
  ----------------------------------------
  5:
    res = [1, 2, 3, null, null, 4, 5, null, null, null, null]
    q = []

  end of loop

           0    1  2  3   4     5    6  7   8     9     10   11
  data = [null, 1, 2, 3, null, null, 4, 5, null, null, null, null]

  return data


  ================================================================================
  root = data[1]
  idx = 1
  curr = root

  while idx < len(data):
    curr.left = data[2*idx]
    curr.right = data[2*idx + 1] 

    idx += 1
    curr = data[idx]

    
    
  

  return root



    



Start root node from the first index.
  
  left child = 2 * x
  right child = 2 * x + 1

x = 1
x.left = 2 * x = 2
x.right = 2 * x + 1 = 3

x = 2
x.left = 2 * x = 4
x.right = 2 * x + 1 = 5





"""


# PRE ORDER
# NEETCODE
class CodecII:
  def serialize(self, root):
    res = []

    # preOrder
    def dfs(root):
      if not root:
        res.append("N")
        return

      res.append(str(root.val))
      dfs(root.left)
      dfs(root.right)

    dfs(root)

    return ",".join(res)

  def deserialize(self, data):
    vals = data.split(",")
    self.i = 0

    # 1 -> 2 -> n -> n -> 3 -> 4 -> n -> n -> 5 -> n -> n

    def dfs():
      if vals[self.i] == "N":
        self.i += 1
        return None

      node = TreeNode(int(vals[self.i]))
      self.i += 1

      node.left = dfs()
      node.right = dfs()

      return node

    return dfs()

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)
        
node4 = TreeNode(4)
node5 = TreeNode(5)


root.left = node2
root.right = node3


node3.left = node4
node3.right = node5

codec = CodecII()

data = codec.serialize(root)

print("data:", data)


print("----------------------------------------------------------------------------------------------------------------------------")

root = codec.deserialize(data)

print("root:", root.val)

print("kkkkkk")

def inOrder(root):
  if not root:
    return

  inOrder(root.left)
  print(root.val)
  inOrder(root.right)

inOrder(root)

"""

                      1
                    /   \
                 2         3
                         /   \
                        4    5


PRE ORDER


root -> left -> right



1 -> 2 -> n -> n -> 3 -> 4 -> n -> 5 -> n -> n





"""
