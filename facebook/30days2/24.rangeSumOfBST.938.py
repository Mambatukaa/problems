""""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 104
1 <= low <= high <= 105
All Node.val are unique.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        stack = [root]

        res = 0

        while stack:
            node = stack.pop()

            if node.val >= low and node.val <= high:
                res += node.val

            if node.left and node.val > low:
                # go left
                stack.append(node.left)

            if node.right and node.val < high:
                stack.append(node.right)

        return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        self.res = 0


        def dfs(root):
            if not root:
                return

            if low <= root.val and root.val <= high:
                self.res += root.val

            if root.val > low:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)

        dfs(root)
        return self.res




        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0

            if root.val < low:
                return dfs(root.right)
            elif root.val > high:
                return dfs(root.left)
            else:
                return dfs(root.left) + root.val + dfs(root.right)

        return dfs(root)




        
import bisect

#                              m
#                              l   r
#       0  1  2  3  4   5  6   7   8
nums = [1, 3, 5, 7, 9, 10, 10, 10, 11]

def find_right_boundry(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        if nums[mid] <= target:
            # go right
            left = mid + 1
        else:
            # go left
            right = mid - 1

    return right


print("bisect:", bisect.bisect_right(nums, 10) - 1)
print(find_right_boundry(nums, 10))




# t = 3
#          m
#       l  
#       r
#       0  1  2  3  4   5  6   7   8
nums = [1, 3, 5, 7, 9, 10, 10, 10, 11]

def find_left_boundry(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right - left) // 2 + left

        if nums[mid] >= target:
            # go left
            right = mid - 1
        else:
            left = mid + 1

    return left
    


print("bisect:", bisect.bisect_left(nums, 2))
print(find_left_boundry(nums, 2))
