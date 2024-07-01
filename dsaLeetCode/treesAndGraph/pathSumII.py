class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# Time Complexity: O(n)
# Space Complexity: O(n)
def pathSum(root, targetSum):
  res = []

  def dfs(root, currArr, currSum):
    if not root:
      return None

    currSum += root.val
    currArr.append(root.val)

    if (not root.left and not root.right) and currSum == targetSum:
      res.append(currArr.copy())

    dfs(root.left, currArr, currSum)
    dfs(root.right, currArr, currSum)

    currArr.pop()

  dfs(root, [], 0)

  return res


root = TreeNode(-2)
node3 = TreeNode(-3)

root.right = node3

print("res:", pathSum(root, -5))

"""
A root to leaf



Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22




1. Do the DFS with currentArray and currentSum.

if currentSum == targetSum and currNode == leaf:
  add currentArray to the res

# base case
if not root or currentSum > targetSum:
  return

"""
