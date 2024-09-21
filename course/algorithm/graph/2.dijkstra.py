import heapq

class WeightedNode:

  def __init__(self, name, index):
    self.name = name
    self.index = index
    self.distance = float('inf')

    self.neighbors = []
    self.weightMap = {}
    self.parent = None

  # Define comparison based on distance for heap operations
  def __lt__(self, other):
    return self.distance < other.distance

  def __repr__(self):
    return f"({self.name}, {self.index}, {self.distance})"

class WeightedGraph:
  def __init__(self, nodeList):
    self.nodeList = nodeList

  def dijkstra(self, node):
    node.distance = 0

    q = []

    for node in self.nodeList:
      heapq.heappush(q, node)


    while q:
      heapq.heapify(q)
      currentNode = heapq.heappop(q)
            
      for neighbor in currentNode.neighbors:
        if neighbor in q:
          newDistance = currentNode.distance + currentNode.weightMap.get(neighbor)

          if neighbor.distance > newDistance:
            neighbor.distance = newDistance
            neighbor.parent = currentNode


    for node in self.nodeList:
      print("Node:", node.name, "distance:", node.distance, "Path:")
      self.pathPrint(node)
      print()


  def pathPrint(self, node):
    if node.parent:
      self.pathPrint(node.parent)

    print("->", node.name)

  def addWeightedEdge(self, i, j, d):
    first = self.nodeList[i]
    second = self.nodeList[j]

    first.neighbors.append(second)
    first.weightMap[second] = d


nodeA = WeightedNode("A", 0)
nodeB = WeightedNode("B", 1)
nodeC = WeightedNode("C", 2)
nodeD = WeightedNode("D", 3)
nodeE = WeightedNode("E", 4)
nodeF = WeightedNode("F", 5)
nodeG = WeightedNode("G", 6)

nodeList = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG]

newGraph = WeightedGraph(nodeList)

newGraph.addWeightedEdge(0, 1, 2)
newGraph.addWeightedEdge(0, 2, 5)
newGraph.addWeightedEdge(1, 2, 6)

newGraph.addWeightedEdge(1, 3, 1)
newGraph.addWeightedEdge(1, 4, 3)

newGraph.addWeightedEdge(2, 5, 8)

newGraph.addWeightedEdge(3, 4, 4)

newGraph.addWeightedEdge(4, 6, 9)

newGraph.addWeightedEdge(5, 6, 7)

newGraph.dijkstra(nodeA)
