from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.next = None

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

root.left = node2
root.right = node3

node2.left = node4


# Time Complexity: O(n)
# Space Complexity: O(n)
# Use prev node like prev node's Linked list
class Solution:
  def processChild(self, childNode, prev, leftmost):
    if childNode:
      if prev:
        prev.next = childNode
      else:
        # first child of the next level
        leftmost = childNode

      # update the prev pointer
      prev = childNode

    return prev, leftmost


  def connect(self, root):
    leftmost = root

    while leftmost:
      prev, curr = None, leftmost

      leftmost = None

      while curr:
        prev, leftmost = self.processChild(curr.left, prev, leftmost)
        prev, leftmost = self.processChild(curr.right, prev, leftmost)

        curr = curr.next

    return root


solution = Solution()

res = solution.connect(root)

print("Res:", res.val)




# With clear comments
class Solution111:

    def processChild(self, childNode, prev, leftmost):
        if childNode:

            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode
        return prev, leftmost

    def connect(self, root: Optional["Node"]) -> Optional["Node"]:

        if not root:
            return root

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:

            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost

            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:

                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                # Move onto the next node.
                curr = curr.next

        return root
