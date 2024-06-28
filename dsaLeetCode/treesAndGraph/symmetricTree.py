


# recursive
# Time Complexity: O(n)
# Space Complexity: O(n)
def symmetricTree(root):
  def dfs(root1, root2):
    if not root1 and not root2:
      return True

    if not root1 or not root2:
      return False

    if root1.val != root2.val:
      return False

    return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

  return dfs(root.left, root.right)


# iterative
# Time Complexity: O(n)
# Space Complexity: O(n)
#BFS
import collections
def symmetricTreeII(root):
  q = collections.deque([[root.left, root.right]])


  while q:
    root1, root2 = q.popleft()

    if not root1 and not root2:
      continue

    if not root1 or not root2 or root1.val != root2.val:
      return False

    q.append([root1.left, root2.right])
    q.append([root1.right, root2.left])
  

  return True





