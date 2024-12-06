class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class Solution:
  def buildTree(self, preorder, inorder):
    n = len(preorder)
    visited = set()

    preorderMap = {}
    inorderMap = {}

    for idx in range(n):
      preorderMap[preorder[idx]] = idx
      inorderMap[inorder[idx]] = idx

    root = TreeNode(preorder[0])

    # current root node
    curr = root
    currIdx = 0

    while curr and currIdx < n - 1:
      visited.append(curr.val)
      nextNode = None
      # get unvisited next node of current node from preorder
      for i in range(currIdx + 1, n):
        if preorder[i] not in visited:
          # next node
          nextNode = preorder[i]
          break

      # if all node is visited just return the answer
      if not nextNode:
        return root

      # check next node from inorder
      if preorderMap[nextNode] > inorderMap[nextNode]:
        # left node
        curr.left = ListNode(nextNode)
        currIdx = nextNode
        curr = curr.left
      else:
        # some logic
        if visited[inorder[currIdx + 1]]:


      







    return root


preorder = [3, 9, 8, 10, 20, 15, 7]
inorder = [8, 9, 10, 3, 15, 20, 7]

solution = Solution()

res = solution.buildTree(preorder, inorder)


def inorder(root):
  if not root:
    return

  inorder(root.left)
  print(root.val)
  inorder(root.right)

inorder(res)



