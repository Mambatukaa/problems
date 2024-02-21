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

  addDirectedEdge(i, j) {
    this.adjacencyMatrix[i][j] = 1;
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

  // Time Complexity: O(E)
  // Space Complexity: O(E)
  topologicalSortHelper(vertice, stack) {
    // if vertex depends on the currentVertex
      // Go to that vertex
      // then come back to currentVertex
    // else
      // Push currentVertex to Stack

    const neighbors = this.getNeighbors(vertice);

    if(neighbors.length) {
      for(const neighbor of neighbors) {
        if(neighbor.visited) continue;
        this.topologicalSortHelper(neighbor, stack);
        neighbor.visited = true;
      };
    } 

    stack.push(vertice);

    vertice.visited = true;
  };

  // Time Complexity: O(V + E)
  // Space Complexity: O(V + E)
  topologicalSort() {
    const stack = [];

    // Time Complexity: O(V)
    // Space Complexity: O(V)
    for(const vertice of this.nodeList) {
      if(!vertice.visited)
      // Time Complexity: O(E)
      // Space Complexity: O(E)
        this.topologicalSortHelper(vertice, stack);
    };

    while(stack.length) {
      const curr = stack.pop();

      console.log(curr.name);
    }
  };


};

const A = new GraphNode("A", 0);
const B = new GraphNode("B", 1);
const C = new GraphNode("C", 2);
const D = new GraphNode("D", 3);
const E = new GraphNode("E", 4);
const F = new GraphNode("F", 5);
const G = new GraphNode("G", 6);
const H = new GraphNode("H", 7);

const nodeList = [A, B, C, D, E, F, G, H];

const graph = new Graph(nodeList);
console.log(graph.toString())

// A: C
graph.addDirectedEdge(0, 2);

// B: C
graph.addDirectedEdge(1, 2);
// B: D
graph.addDirectedEdge(1, 3);

// C: E
graph.addDirectedEdge(2, 4);

// D: F
graph.addDirectedEdge(3, 5);

// E: F
graph.addDirectedEdge(4, 5)

// E: H
graph.addDirectedEdge(4, 7)


// F: G
graph.addDirectedEdge(5, 6)

console.log('===================');

console.log(graph.toString())
graph.topologicalSort()





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
