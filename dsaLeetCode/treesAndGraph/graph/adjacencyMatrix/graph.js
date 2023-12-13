// vertice
class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
  };
}


class Graph {
  constructor(nodeList = []) {
    this.nodeList = nodeList;
    this.adjacencyMatrix = new Array(nodeList.length).fill().map(() => new Array(nodeList.length).fill(0));
  }

  addUndirectedEdge(i, j) {
    this.adjacencyMatrix[i][j] = 1;
    this.adjacencyMatrix[j][i] = 1;
  }

  toString() {
    let stringBuilder = "  ";

    // rows
    for(let i = 0; i < nodeList.length; i++) {
      stringBuilder += ` ${nodeList[i].name}`;
    };

    for(let i = 0; i < nodeList.length; i++) {
      stringBuilder += `\n${nodeList[i].name}:`;

      for(const j of this.adjacencyMatrix[i]) {
        stringBuilder += ` ${j}`;
      }

    };

    return stringBuilder;
  }

};


const node1 = new GraphNode('A', 0);
const node2 = new GraphNode('B', 1);
const node3 = new GraphNode('C', 2);
const node4 = new GraphNode('D', 3);
const node5 = new GraphNode('E', 4);

const nodeList = [node1, node2, node3, node4, node5];

const graph = new Graph(nodeList);

graph.addUndirectedEdge(0,1);
graph.addUndirectedEdge(0,2);
graph.addUndirectedEdge(0,3);

graph.addUndirectedEdge(1,0);
graph.addUndirectedEdge(1,4);


graph.addUndirectedEdge(2,0);
graph.addUndirectedEdge(2,3);

graph.addUndirectedEdge(3,2);
graph.addUndirectedEdge(3,0);
graph.addUndirectedEdge(3,4);


graph.addUndirectedEdge(4,1);
graph.addUndirectedEdge(4,3);
