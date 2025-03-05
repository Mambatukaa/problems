""""
You are given the root of a binary tree containing digits from 0 to 9 only.
Each root-to-leaf path in the tree represents a number.
• For example, the root-to-leaf path 1 → 2 - 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit
integer.
A leaf node is a node with no children.



Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
    The root-to-leaf path 4->9->5 represents the number 495.
    The root-to-leaf path 4->9->1 represents the number 491.
    The root-to-leaf path 4->0 represents the number 40.
    Therefore, sum = 495 + 491 + 40 = 1026.

Constraints:
• The number of nodes in the tree is in the range [1, 1000].
• 0 <= Node.val <= 9
• The depth of the tree will not exceed 10 .




"""









from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root) -> int:
        self.res = 0
        def dfs(root, currSum):
            if not root:
                return 0

            currSum += str(root.val)

            # leaf
            if not root.left and not root.right:
                self.res += int(currSum)
                return

            
            dfs(root.left, currSum)
            dfs(root.right, currSum)

        dfs(root, "")

        return self.res


    # DFS
    def sumNumbersII(self, root) -> int:
        def dfs(root, currSum):
            if not root:
                return 0

            currSum += str(root.val)

            # leaf
            if not root.left and not root.right:
                return int(currSum)

            
            left = dfs(root.left, currSum)
            right = dfs(root.right, currSum)

            return left + right

        return dfs(root, "")

    # BFS
    def sumNumbersII(self, root) -> int:
        q = deque([[root, 0]])
        res = 0

        while q:
            node, currSum = q.popleft()

            currSum = currSum * 10 + node.val

            if not node.left and not node.right:
                res += currSum

            if node.left:
                q.append([node.left, currSum])

            if node.right:
                q.append([node.right, currSum])


        return res





solution = Solution()

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)

root.left = node2
root.right = node3

print("res:", solution.sumNumbers(root))
print("res:", solution.sumNumbersII(root))
