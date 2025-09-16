""""
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109







"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = 0
        closest = float('inf')

        q = deque([root])

        while q:
            curr = q.popleft()
            diff = abs(target - curr.val)

            # update the answer
            if diff < closest or (diff == closest and curr.val < res):
                res = curr.val
                closest = diff
            
            if curr.val > target and curr.left:
                q.append(curr.left)
            elif curr.right:
                q.append(curr.right)

        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = 0
        closest = float('inf')

        while root:
            diff = abs(target - root.val)

            # update the answer
            if diff < closest or (diff == closest and root.val < res):
                res = root.val
                closest = diff
            
            if root.val > target:
                root = root.left
            else:
                root = root.right

        return res


        
