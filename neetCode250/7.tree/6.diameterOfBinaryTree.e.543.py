""""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0

        def rec(root):
            if not root:
                return 0

            left = rec(root.left)
            right = rec(root.right)

            self.res = max(self.res, left + right)
    
            return 1 + max(left, right)

        rec(root)

        return self.res
        
# res = max(res, left + right)
#
#
#
#
#
#
#
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        diameter = 0
        heights = {None: 0}   # height of null node = 0
        stack = [(root, False)]  # (node, visited)

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left_h = heights[node.left]
                right_h = heights[node.right]

                diameter = max(diameter, left_h + right_h)
                heights[node] = 1 + max(left_h, right_h)
            else:
                # Postorder: left, right, node
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return diameter