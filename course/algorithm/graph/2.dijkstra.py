import heapq

# Can't deal with negative cycle

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


node1 = WeightedNode("1", 1)
node2 = WeightedNode("2", 2)
node3 = WeightedNode("3", 3)
node4 = WeightedNode("4", 4)


node5 = WeightedNode("5", 5)
node6 = WeightedNode("6", 6)
node7 = WeightedNode("7", 7)
node8 = WeightedNode("8", 8)


node9 = WeightedNode("9", 9)
node10 = WeightedNode("10", 10)
node11 = WeightedNode("11", 11)
node12 = WeightedNode("12", 12)

node13 = WeightedNode("13", 13)
node14 = WeightedNode("14", 14)
node15 = WeightedNode("15", 15)
node16 = WeightedNode("16", 16)
node17 = WeightedNode("17", 17)



nodeList = [node1, node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17]

newGraph = WeightedGraph(nodeList)

newGraph.addWeightedEdge(1, 2, 3)
newGraph.addWeightedEdge(1, 3, 4)
newGraph.addWeightedEdge(1, 4, 2)
newGraph.addWeightedEdge(1, 5, 5)

newGraph.addWeightedEdge(2, 3, 4)
newGraph.addWeightedEdge(2, 6, 2)
newGraph.addWeightedEdge(2, 9, 6)


newGraph.addWeightedEdge(3, 4, 1)
newGraph.addWeightedEdge(3, 6, 3)
newGraph.addWeightedEdge(3, 7, 5)
newGraph.addWeightedEdge(3, 8, 4)


newGraph.addWeightedEdge(4, 5, 2)
newGraph.addWeightedEdge(4, 7, 4)


newGraph.addWeightedEdge(5, 7, 3)
newGraph.addWeightedEdge(5, 14, 6)



newGraph.addWeightedEdge(6, 9, 3)
newGraph.addWeightedEdge(6, 8, 3)


newGraph.addWeightedEdge(7, 8, 3)
newGraph.addWeightedEdge(7, 10, 2)

newGraph.addWeightedEdge(8, 11, 2)
newGraph.addWeightedEdge(8, 12, 4)

newGraph.addWeightedEdge(9, 11, 2)
newGraph.addWeightedEdge(9, 13, 4)

newGraph.addWeightedEdge(10, 12, 2)
newGraph.addWeightedEdge(10, 14, 3)

newGraph.addWeightedEdge(11, 12, 5)
newGraph.addWeightedEdge(11, 13, 1)
newGraph.addWeightedEdge(11, 15, 2)

newGraph.addWeightedEdge(12, 15, 3)
newGraph.addWeightedEdge(12, 16, 1)


newGraph.addWeightedEdge(13, 15, 3)

newGraph.addWeightedEdge(14, 16, 7)

newGraph.addWeightedEdge(15, 17, 5)

newGraph.addWeightedEdge(16, 17, 3)

newGraph.dijkstra(node1)
