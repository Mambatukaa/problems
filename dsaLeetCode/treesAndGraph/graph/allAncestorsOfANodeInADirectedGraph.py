from collections import defaultdict, deque

def getAncestors(n, edges):
  graph = defaultdict(list)

  rootNotes = [1] * n

  for edge in edges:
    graph[edge[0]].append(edge[1])
    rootNotes[edge[1]] = 0

  res = [[]] * n

  def bfs(node):


    """
      Graph: {
        0: [3, 4],
        1: [3],
        2: [4, 7],
        3: [5, 6, 7],
        4: [6],
        5: [],
        6: [],
        7: [],
      }
    """

    q = deque([[node, []]])

    while q:
      curr, ancestor = q.pop()


      ancestor.append(curr)
      neighbors = graph[curr]

      for neighbor in neighbors:
        q.append([neighbor, ancestor.copy()])

  for i in range(n):
    if rootNotes[i] == 1:
      bfs(i)

  return res
  


n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

print("res:", getAncestors(n, edgeList))
"""

Build graph

Do the DFS or BFS and visit to every children's add ancestor node to the each children 



Input: n = 8, edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
          0  1  2   3     4      5         6           7
Output: [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]


0 -> 3 -> 5


"""
