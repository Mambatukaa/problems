""""
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#         TC: O(n)
#         SC: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
    
            l_height = dfs(root.left)

            if l_height == -1:
                return -1

            r_height = dfs(root.right)

            if r_height == -1 or abs(r_height - l_height) > 1:
                return -1
            
            return max(l_height, r_height) + 1
        
        return dfs(root) != -1
