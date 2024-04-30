# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
# 5 minutes
# Level order traversal
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      if not root:
        return []

      queue = deque([root])
      res = []

      while len(queue):
        size = len(queue)

        for i in range(size):
          curr = queue.popleft()

          if i + 1 == size:
            res.append(curr.val)
          
          if curr.left:
            queue.append(curr.left)
          if curr.right:
            queue.append(curr.right)
      

      return res


        



# Level order and add the last element of each level to the res 
