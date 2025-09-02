""""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.







"""

from typing import Optional

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
  # Time Complexity: O(h) where h is the height of the tree
  # Space Complexity: O(1)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        p2 = q

        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p


class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
  # Time Complexity: O(h) where h is the height of the tree
  # Space Complexity: O(1)
  def lowestCommonAncestor(self, nodes, p: Optional[Node], q: Optional[Node]) -> Optional[Node]:
    # adjacency list
    child_to_parent = defaultdict()

    for node in nodes:
            if node.left:
                child_to_parent[node.left] = node
            if node.right:
                child_to_parent[node.right] = node

    p1 = p
    p2 = q

    while p1 and p2:
        if p1 == p2:
            return p1

        p1 = child_to_parent[p1] if p1 in child_to_parent else q
        p2 = child_to_parent[p2] if p2 in child_to_parent else p

    return None


solution = Solution()

root = Node(1)
node2 = Node(2)
p = Node(3)
q = Node(4)

root.left = node2
node2.left = p
root.right = q

nodes = [root, node2, p, q]


print("res:", solution.lowestCommonAncestor(nodes, p, q).val)
