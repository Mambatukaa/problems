""""
Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000





"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # right and not: False

        q = deque([root])
        noneNodeFound = False

        while q:
            curr = q.popleft()

            if curr:
                q.append(curr.left)
                q.append(curr.right)
            else:
                while q:
                    if q.popleft():
                        return False

        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # right and not: False

        q = deque([root])
        noneNodeFound = False

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()

                if not curr:
                    noneNodeFound = True
                else:
                    if noneNodeFound:
                        return False

                    q.append(curr.left)
                    q.append(curr.right)

        return True


# DFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def countNodes(root):

            if not root:
                return 0

            return 1 + countNodes(root.left) + countNodes(root.right)


        def dfs(node, index, n):
            print(index)
            if not node:
                return True


            if index >= n:
                return False

            return dfs(node.left, 2 * index + 1, n) and dfs(node.right, 2 * index + 2, n)
        
        return dfs(root, 0, countNodes(root))

