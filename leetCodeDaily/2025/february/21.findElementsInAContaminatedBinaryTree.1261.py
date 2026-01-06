""""

Given a binary tree with the following rules:
1. root.val == 0
2. For any treeNode:
1. If treeNode. val has a value x and treeNode. left != null, then treeNode. left.val == 2 * x + 1
2. If treeNode.val has a value x and treeNode. right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode. val have been changed to -1.
Implement the FindElements class:
• FindElements (TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
• bool find(int target) Returns true if the target value exists in the recovered binary tree.


Input
["FindElements" ,"find","find". ',"find"]
[LI-1,-1,-1,-1,-1]], [1], [31, [5]]
Output
[null, true, true, false]
Explanation
FindElements findElements = new FindElements ([-1,-1,-1,-1,-1]);
findElements. find (1); // return True
findElements.find (3); // return True
findElements.find(5); // return False



Constraints:
• TreeNode.val == -1
• The height of the binary tree is less than or equal to 20
• The total number of nodes is between [1, 104]
• Total calls of find() is between [1, 104]
• 0 < target <= 106

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    # BFS solution 
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def __init__(self, root: Optional[TreeNode]):
        q = deque([[0, root]])
        self.seen = set()

        while q:
            currVal, node = q.popleft()

            self.seen.add(currVal)

            if node.left:
                q.append([currVal * 2 + 1, node.left])
            if node.right:
                q.append([currVal * 2 + 2, node.right])


    # DFS
    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()

        def dfs(root, value):
            if not root:
                return
            
            self.seen.add(value)

            dfs(root.left, value * 2 + 1)
            dfs(root.right, value * 2 + 2)
        

        dfs(root, 0)


    def find(self, target: int) -> bool:
        if target in self.seen:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
