// Adjacency matrix
// 2D array
//
class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.visited = false;
  };
};

class Graph {
  constructor(nodeList) {
    this.nodeList = nodeList;

    this.adjacencyMatrix = Array.from(Array(nodeList.length), () => new Array(nodeList.length).fill(0));
  };

  addUndirectedEdge(i, j) {
    this.adjacencyMatrix[i][j] = 1;
    this.adjacencyMatrix[j][i] = 1;
  };

  toString() {
    let string = "   ";

    for(const { name } of nodeList) {
      string += `${name} `; 
    };

    string += "\n";

    for(let i = 0; i < nodeList.length; i++) {
      string += `${nodeList[i].name}: `;

      for(const item of this.adjacencyMatrix[i]) {
        string += `${item} `;
      };

      string += '\n';

    };

    return string;
  };

  getNeighbors(vertice) {
    const { index } = vertice;

    const neighbors = [];

    for(let i = 0; i < this.adjacencyMatrix.length; i++) {
      if(this.adjacencyMatrix[index][i] === 1) {
        neighbors.push(this.nodeList[i]);
      };
    };

    return neighbors;
  };

  bfsHelper(vertice) {
    const queue = [vertice];

      // O(E) ===> O(E) = O(V) + O(adj)
    while(queue.length) { // O(V)
      const curr = queue.shift();
      curr.visited = true;

      console.log(curr.name);

      const neighbors = this.getNeighbors(curr);

      for(const neighbor of neighbors) { // O(adj)
        // if neighbor is not visited add to the queue
        if(!neighbor.visited) {
          queue.push(neighbor);
          neighbor.visited = true;
        };

      };

    };

  };

  // TC: O(V) + O(E) ===> O(E) = O(V) + O(adj)
  // SC: O(V) + O(E) ===> O(E) = O(V) + O(adj) QUEUE
  bfs() {
    for(const vertice of this.nodeList) {
      // O(E) ===> O(E) = O(V) + O(adj)
      if(!vertice.visited) {
        this.bfsHelper(vertice);
      };
    }
  };
  

  dfsHelper(vertice) {
    // 1. use stack
    // 2. push any vertice to the stack
    // 3. pop the first element + print curr
    // 4. set element to unvisited
    // 5. add unvisited popped elements neighbors to the stack
    // 6. set visited to the neighbor
    // 7. repeat
    
    const stack = [vertice];

    while(stack.length) {
      const curr = stack.pop();
      curr.visited = true;
      console.log(curr.name, '-----------');
      const neighbors = this.getNeighbors(curr);

      for(const neighbor of neighbors) {
        if(!neighbor.visited) stack.push(neighbor);
        neighbor.visited = true;
      };
    }


  };

  // TC: O(V) + O(E) ===> O(E) = O(V) + O(adj)
  // SC: O(V) + O(E) ===> O(E) = O(V) + O(adj) QUEUE
  dfs() {
    for(const vertice of this.nodeList) {
      // O(E) ===> O(E) = O(V) + O(adj)
      if(!vertice.visited) {
        this.dfsHelper(vertice);
      };
    }
  };

  resetNodes() {
    for(const vertice of this.nodeList) {
      vertice.visited = false;
    };
  };
};

const A = new GraphNode("A", 0);
const B = new GraphNode("B", 1);
const C = new GraphNode("C", 2);
const D = new GraphNode("D", 3);
const E = new GraphNode("E", 4);

const nodeList = [A, B, C, D, E];

const graph = new Graph(nodeList);

graph.addUndirectedEdge(0, 1);
graph.addUndirectedEdge(0, 2);
graph.addUndirectedEdge(0, 3);

graph.addUndirectedEdge(1, 4);

graph.addUndirectedEdge(2, 3);

graph.addUndirectedEdge(3, 4);

console.log(graph.toString())
graph.bfs();
graph.resetNodes();
console.log('===================');
graph.dfs();


/*


  A -------- B
  | \         \
  |   \        \
  |     \       E
  |       \    /
  |         \ /
  C -------- D

  // Adjacency Matrix - 2D Array
  // If a graph is complete or almost complete we should use ADJACENCY MATRIX
    01234
    ABCDE 
  A 01110 
  B 10001
  C 10010
  D 10101
  E 01010

  // Adjacency List - Linked List
  // If a graph is complete or almost complete we should use ADJACENCY MATRIX
  // If the number of edges are few then we should use ADJACENCY LIST
  
  A: -> B -> C -> D
  B: -> A -> E
  C: -> A -> D
  D: -> A -> C -> E
  E: -> B -> D


 */
