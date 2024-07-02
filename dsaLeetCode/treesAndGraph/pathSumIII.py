class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Time Complexity: O(n)
# Space Complexity: O(n)
def pathSum(root, targetSum):
  self.counter = 0

  def helper(root, currSum):
    if not root:
      return

    currSum += root.val
    
    if currSum == targetSum:
      self.counter += 1

    helper(root.left, currSum)
    helper(root.right, currSum)

  def dfs(root):
    if not root:
      return 0
    
    helper(root, 0)
    dfs(root.left)
    dfs(root.right)
  
  dfs(root)

  return self.counter  return 1






"""

Return the number of paths


Input: root = [10,5,-3,3,2,null, 11,3,-2,null,1], targetSum = 8
Output: 3


1. Bfs or Dfs and start to calculate targetSum from every node



  

"""
