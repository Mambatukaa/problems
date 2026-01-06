""""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#         TC: O(n)
#         SC: O(n)
#         BFS
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')
        res = 1
        curr_level = 1

        q = deque([root])
        
        while q:
            size = len(q)
            curr_sum = 0

            for _ in range(size):
                node = q.popleft()
                curr_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < curr_sum:
                res = curr_level
                max_sum = curr_sum

            curr_level += 1

        return res


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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = []


        def dfs(root, level):
            if not root:
                return

            if len(level_sum) == level:
                level_sum.append(root.val)
            else:
                level_sum[level] += root.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        res = 0
        max_sum = -float('inf')

        for i in range(len(level_sum)):
            if max_sum < level_sum[i]:
                res = i + 1
                max_sum = level_sum[i]
        return res


        # calculate sum on each level

