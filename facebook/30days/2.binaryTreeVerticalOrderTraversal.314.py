""""
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to
bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.





Input: root = [3,9,20, null, null, 15,7]
Output: [[9],[3,15],[20],[7]]


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict, deque
# BFS
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def verticalOrder(self, root):
        columnMap = defaultdict(list)

        leftIdx = 0
        rightIdx = 0

        q = deque([[root, 0]])

        while q:
            curr, column = q.popleft()

            leftIdx = min(leftIdx, column)
            rightIdx = max(rightIdx, column)

            columnMap[column].append(curr.val)

            if curr.left:
                q.append([curr.left, column - 1])
            if curr.right:
                q.append([curr.right, column + 1])

        res = []

        for i in range(leftIdx, rightIdx + 1):
            res.append(columnMap[i])

        return res



root = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)

node4 = TreeNode(15)
node5 = TreeNode(7)

root.left = node2
root.right = node3

node3.left = node4
node3.right = node5

solution = Solution()

print("res:", solution.verticalOrder(root))

