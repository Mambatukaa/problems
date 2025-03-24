# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:

# BFS Level order traversal
# Get last element from each level
# Time Complexity: O(n)
# Space Complexity: O(n)
    def rightSideView(self, root):

        res = []

        q = deque([root])

        while q:
            size = len(q)

            last = None

            for _ in range(size):
                node = q.popleft()
                last = node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(last.val)


        return res
        
    # DFS
    # Time Complexity: O(n)
    # Space Complexity: O(H) H - tree height
    def rightSideViewII(self, root):
        if not root:
            return []

        res = []

        def dfs(node, level):
            if not root:
                return

            if len(res) == level:
                res.append(node.val)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)


        dfs(root, 0)

        return res
