import heapq

def dijkstra(edges, n, src):
  # n = nodes count

  adj = {}

  for i in range(1, n + 1):
    adj[i] = []

  for s, d, w in edges:
    adj[s].append((d, w))

  # <cost, vertice>
  minHeap = [(0, src)]
  heapq.heapify(minHeap)

  shortest = {}

  while minHeap:
    w1, n1 = heapq.heappop(minHeap)

    if n1 in shortest:
      continue

    shortest[n1] = w1

    for n2, w2 in adj[n1]:
      if n2 not in shortest:
        heapq.heappush(minHeap, (w1 + w2, n2))


  print(shortest)
  return shortest

edges = [
    [1, 2, 2],
    [1, 3, 5],
    [2, 3, 6],

    [2, 4, 1],
    [2, 5, 3],

    [3, 6, 8],

    [4, 5, 4],

    [5, 7, 9],

    [6, 7, 7],
    ]

dijkstra(edges, 7, 1)
