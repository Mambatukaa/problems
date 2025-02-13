""""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
cording to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
according to the LCA definition.


Constraints:
• The number of nodes in the tree is in the range [2, 105].
• -109 <= Node.val <= 10º
• All Node.val are unique.
• p!= q
• p and q will exist in the tree.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            right = dfs(root.right)

            res = (root == p or root == q) + left + right

            if not self.res and res == 2:
                self.res = root

            return res

        dfs(root)
        
        return self.res

    def lowestCommonAncestorII(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root in (None, p, q):
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            return left or right

        return dfs(root)




root = TreeNode(3)

node2 = TreeNode(5)
node3 = TreeNode(1)

node4 = TreeNode(6)
node5 = TreeNode(2)

node6 = TreeNode(0)
node7 = TreeNode(8)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

solution = Solution()

print("res:", solution.lowestCommonAncestorII(root, node6, node7).val)
