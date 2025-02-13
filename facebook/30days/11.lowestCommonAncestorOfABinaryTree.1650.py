""""


Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a
tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant
of itself)."



Example 2:

    Input: root = [3,5, 1,6,2,0,8, null, null, 7, 4], p = 5, q=4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of
    itself according to the LCA definition.

Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

Constraints:

• The number of nodes in the tree is in the range [2, 105].
-10^9 <= Node.val <= 10^9
• All Node. val are unique.
• p != q
• p and q exist in the tree.
"""

# Definition for a Node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pParents = set()
        qParents = set()

        while True:
            if p == q:
                return p

            if q in pParents:
                return q
            
            if p in qParents:
                return p

            pParents.add(p)
            qParents.add(q)

            p = p.parent if p.parent else p
            q = q.parent if q.parent else q

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def lowestCommonAncestorII(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = q, p
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1

root = TreeNode(3)

node2 = TreeNode(5)
node3 = TreeNode(1)

node4 = TreeNode(6)
node5 = TreeNode(2)

node6 = TreeNode(0)
node7 = TreeNode(8)

root.left = node2
root.right = node3

node2.parent = root
node3.parent = root

node2.left = node4
node2.right = node5

node4.parent = node2
node5.parent = node2

node3.left = node6
node3.right = node7

node7.parent = node3
node6.parent = node3

solution = Solution()

print("res 1:", solution.lowestCommonAncestor(node3, node7).val)
print("res 2:", solution.lowestCommonAncestorII(root, node3).val)
