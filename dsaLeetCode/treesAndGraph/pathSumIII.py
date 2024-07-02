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



# Time Complexity: O(n)
# Space Complexity: O(n)
# Optimal solution
def pathSumII(root, targetSum):
  self.res = 0

  def dfs(root, currSum, diff):
    if not root:
      return

    currSum += root.val

    if currSum - targetSum in diff:
      self.res += diff.get(currSum - targetSum)

    diff[currSum] = diff.get(currSum, 0) +  1

    dfs(root.left, currSum, diff)
    dfs(root.right, currSum, diff)
    diff[currSum] -= 1


  dfs(root, 0, {0: 1})

  return self.res
      
"""

Return the number of paths


Input: root = [10,5,-3,3,2,null, 11,3,-2,null,1], targetSum = 8
Output: 3


1. Bfs or Dfs and start to calculate targetSum from every node



  

"""
