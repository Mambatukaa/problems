// vertice
class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.visited = false;
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

  getNeighbors(vertice) {
    const neighbors = [];
    const index = vertice.index;

    for(let i = 0; i < this.adjacencyMatrix.length; i++) {
      if(this.adjacencyMatrix[index][i] === 1) {
        neighbors.push(this.nodeList[i]);
      }
    }

    return neighbors;
  };

  bfsVisit(vertice) {
    vertice.visited = true;
  };

  // BFS internal
  bfsVisit(node) {
    const queue = [node];
    //
    // O(V)
    while(queue.length) {
      const currVertice = queue.shift();

      console.log(currVertice.name, '------>');

      currVertice.visited = true;

      const neighbors = this.getNeighbors(currVertice);

      // O(Adj) --> unlisted adjacent
      for(const neighbor of neighbors) {
        if(!neighbor.visited) {
          queue.push(neighbor);
          neighbor.visited = true;
        }
      }

    }

  };

  // Time Complexity: O(V + E)
  // Space Complexity: O(V + E)
  bfs() {
    // O(V)
    for(const node of nodeList) {
      if(!node.visited)
        // O(V) + O(Adj) = O(E) // E is and numbers of edge
        this.bfsVisit(node);
    }
  }

  // DFS internal
  dfsVisit(node) {
    const stack = [node];

    while(stack.length) {
      const current = stack.pop();

      console.log(current.name, '->');
      current.visited = true;

      const neighbors = this.getNeighbors(current);

      for(const neighbor of neighbors) {
        if(!neighbor.visited) {
          stack.push(neighbor);

          neighbor.visited = true;
        };
      };

    };

  };

  // Time Complexity: O(V + E)
  // Space Complexity: O(V + E)
  dfs() {
    for(const node of nodeList) {
      if(!node.visited) {
        this.dfsVisit(node);
      }
    }
  };

};


const vertice1 = new GraphNode('A', 0);
const vertice2 = new GraphNode('B', 1);
const vertice3 = new GraphNode('C', 2);
const vertice4 = new GraphNode('D', 3);

const vertice5 = new GraphNode('E', 4);
const vertice6 = new GraphNode('F', 5);
const vertice7 = new GraphNode('G', 6);

const nodeList = [vertice1, vertice2, vertice3, vertice4, vertice5, vertice6, vertice7];

const graph = new Graph(nodeList);

graph.addUndirectedEdge(0, 1);
graph.addUndirectedEdge(0, 2);

graph.addUndirectedEdge(1, 0);
graph.addUndirectedEdge(1, 3);
graph.addUndirectedEdge(1, 6);

graph.addUndirectedEdge(2, 0);
graph.addUndirectedEdge(2, 3);
graph.addUndirectedEdge(2, 4);

graph.addUndirectedEdge(3, 1);
graph.addUndirectedEdge(3, 5);

graph.addUndirectedEdge(4, 2);
graph.addUndirectedEdge(4, 5);

graph.addUndirectedEdge(5, 3);
graph.addUndirectedEdge(5, 4);
graph.addUndirectedEdge(5, 6);


console.log(graph.toString())
console.log(graph.dfs())
