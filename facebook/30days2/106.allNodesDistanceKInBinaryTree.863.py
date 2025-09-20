# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(root, parent):
            if root and parent:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)
            if root.left:
                build_graph(root.left, root)
            if root.right:
                build_graph(root.right, root)

        build_graph(root, None)

        res = []
        visited = set()
        visited.add(target.val)

        # bfs
        q = deque([[target.val, 0]])

        while q:
            node, distance = q.popleft()

            if distance == k:
                res.append(node)
                continue
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append([neighbor, distance + 1])

        return res

        def dfs(node, distance):
            if distance == k:
                res.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)

        dfs(target.val, 0)

        return res

        
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur)

        add_parent(root, None)

        res = []
        visited = set()

        def dfs(cur, distance):
            if not cur or cur in visited:
                return
            
            visited.add(cur)

            if distance == 0:
                res.append(cur.val)
                return

            dfs(cur.parent, distance - 1)
            dfs(cur.left, distance - 1)
            dfs(cur.right, distance - 1)

        dfs(target, k)

        return res
