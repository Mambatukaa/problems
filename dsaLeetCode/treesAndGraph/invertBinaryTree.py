# Time Complexity: O(n)
# Space Complexity: O(n)
def invertBinaryTree(root):
    if not root:
      return root

    root.left, root.right = root.right, root.left
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    return root


# Time Complexity: O(n)
# Space Complexity: O(n)
import collections 
def invertBinaryTreeII(root):
  q = collections.deque([root])

  while q:
    curr = q.popleft()

    if not curr:
      continue

    curr.left, curr.right = curr.right = curr.left

    q.append(curr.left)
    q.append(curr.right)

  return root
