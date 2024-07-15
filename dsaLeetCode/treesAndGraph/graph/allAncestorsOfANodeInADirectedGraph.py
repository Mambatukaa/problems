from collections import deque

# Build reversed graph
# Visit to the ancestors from node using DFS
# Track visited ancestor nodes on each node
# Collect nodes
# Time Complexity: O(n^2 + n * m)
# Space Complexity: O(n + m)
# Visit through parent nodes
def getAncestors(n, edges):
  # Initialize adjacency list for the graph
  reversedGraph = [[] for _ in range(n)]

  # Populate the adjacency list with reversed edges
  for fromNode, toNode in edges:
    reversedGraph[toNode].append(fromNode)

  # dfs
  def findAncestors(currentNode, reversedGraph, visited):
    visited.add(currentNode)

    for neighbour in reversedGraph[currentNode]:
      if not neighbour in visited:
        findAncestors(neighbour, reversedGraph, visited)

  res = []

  for i in range(n):
    ancestors = []
    visitedAncestors = set()

    findAncestors(i, reversedGraph, visitedAncestors)

    for node in range(n):
      if node == i:
        continue

      if node in visitedAncestors:
        ancestors.append(node)

    res.append(ancestors.copy())

  return res

# Visit through child nodes
# Time Complexity: O(n^2 n * m)
# Space Complexity: O(n + m)
# Only visit once to the visited nodes (OPTIMIZED)
def getAncestorsII(n, edges):
  graph = [[] for _ in range(n)]
  ancestors = [[] for _ in range(n)]

  # building a graph
  # collect children nodes in parent
  for fromNode, toNode in edges:
    graph[fromNode].append(toNode)


  def findAncestorsDfs(ancestor, currentNode):
    for childNode in graph[currentNode]:
      # avoid duplicates
      if not ancestors[childNode] or ancestors[childNode][-1] != ancestor:
        ancestors[childNode].append(ancestor)
        findAncestorsDfs(ancestor, childNode)

  # traverse to childrens and add parent 
  for i in range(n):
    findAncestorsDfs(i, i)

  return ancestors


n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

print("res:", getAncestorsII(n, edgeList))
"""

Build graph

Do the DFS or BFS and visit to every children's add ancestor node to the each children 



Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
          0  1  2   3     4      5         6           7
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]


0 -> 3 -> 5


"""
