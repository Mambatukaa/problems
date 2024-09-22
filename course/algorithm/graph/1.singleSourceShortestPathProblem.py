"""
SSSPP

  Time Complexity: O(E) edges
  Time Complexity: O(V) vertices
- BFS not work with weighted graph


  enqueue any starting vertex
  while queue is not empty
    p = dequeue()

    if p is unvisited:
      mark it visited
      enqueue all adjacent unvisited vertices of p
      update parent of adjacent vertices to curVertex

  QUEUE DS

- Dijkstra's Algorithm

- Bellman Ford



"""
