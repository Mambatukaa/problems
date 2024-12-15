from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Clone graph

class Solution:
    # BFS
    # Time Complexity: O(N + M) N = number of nodes, M = number of vertices
    # Space Complexity: O(N)
    def cloneGraph(self, node):
        queue = deque([node])

        visited = defaultdict()
        visited[node] = Node(node.val)


        while queue:
            currNode = queue.popleft()

            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[currNode].neighbors.append(visited[neighbor])
        
        return visited[node]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node1.neighbors.append(node4)

node2.neighbors.append(node1)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(node1)
node4.neighbors.append(node3)

# adjList = [[2,4],[1,3],[2,4],[1,3]]


solution = Solution()

newRoot = solution.cloneGraph(node1)

stack = [newRoot]
visited = set()


while stack:
    newRoot = stack.pop()
    print("root:", newRoot.val)
    visited.add(newRoot)
    neighbors = newRoot.neighbors

    for neighbor in neighbors:
        if neighbor in visited:
            continue
        print("neighbor:", neighbor.val)
        stack.append(neighbor)



        
# Create deep copy of each node and start dfs to create deep copy graph
