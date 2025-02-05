"""

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may
or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,31 or [5,2,1,31.

Example 2:
    Input: root = [1,21
    Output: 1


Constraints:
• The number of nodes in the tree is in the range [1, 10^4].
• -100 <= Node.val < 100


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive dfs
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if not root: 
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.ans = max(self.ans, left + right)

            return 1 + max(left, right)

        dfs(root)

        return self.ans
