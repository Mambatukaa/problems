class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.neighbors = [];
    this.isVisited = false;
    this.parent = null;
  };
};


class Graph {
  constructor(nodeList) {
    this.nodeList = nodeList;
  };

  addUndirectedEdge(i, j) {
    const first = this.nodeList[i]; 
    const second = this.nodeList[j]; 

    first.neighbors.push(second);
    second.neighbors.push(first);
  };

  addDirectedEdge(i, j) {
    const first = this.nodeList[i];
    const second = this.nodeList[j];

    first.neighbors.push(second)
  };

  toString() {
    let string = "";

    for(const { name, neighbors} of nodeList) {
      string += `${name}: `;

      for(let i = 0; i < neighbors.length; i++) {
        string += `${neighbors[i].name}`;

        if(i !== neighbors.length - 1) {
          string += " -> ";
        }
      };

      string += '\n';

    };

    return string;

  };

  bfsHelper(vertice) {
    const queue = [vertice];

    // O(E) ===> O(E) = O(V) + O(adj)
    while(queue.length) { // O(V)
      const curr = queue.shift();
      curr.isVisited = true;
      const neighbors = curr.neighbors;

      console.log(curr.name, '==========');

      for(const neighbor of neighbors) { // O(adj)
        if(!neighbor.isVisited) {
          queue.push(neighbor);
          neighbor.isVisited = true;
        };
      };
    };
  };

  // TC: O(V) + O(E) ===> O(E) = O(V) + O(adj)
  // SC: O(V) + O(E) ===> O(E) = O(V) + O(adj) QUEUE
  bfs() {
    for(const vertice of this.nodeList) {
      // O(E) ===> O(E) = O(V) + O(adj)
      if(!vertice.isVisited) {
        this.bfsHelper(vertice);
      }
    };

  };

  dfsHelper(vertice) {
    const stack = [vertice];

    while(stack.length) {
      const curr = stack.pop();
      console.log(curr.name, '-------------');
      curr.isVisited = true;
      const neighbors = curr.neighbors;

      for(const neighbor of neighbors) {

        if(!neighbor.isVisited) {
          stack.push(neighbor);
          neighbor.isVisited = true;
        };

      };

    };

  };

  // TC: O(V) + O(E) ===> O(E) = O(V) + O(adj)
  // SC: O(V) + O(E) ===> O(E) = O(V) + O(adj) STACK
  dfs() {
    for(const vertice of this.nodeList) {
      if(!vertice.isVisited)
        this.dfsHelper(vertice);
    };
  };

  resetNodes() {
    for(const vertice of this.nodeList) {
      vertice.isVisited = false;
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

    const neighbors = vertice.neighbors;

    if(neighbors.length) {
      // TC: O(m), m = neighbors
      for(const neighbor of neighbors) {
        if(neighbor.visited) continue;
        // TC: O(m)
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

  parentPrint(vertice) {
    if(vertice.parent) {
      this.parentPrint(vertice.parent);
    };

    console.log(vertice.name)
  };

  // SSSPP
  // Source and destination
  // Time Complexity: O(V * ADJ) 
  // Space Complexity: O(V) 
  /*
    create queue ------------------------------------------------> O(1)
    enqueue any starting index ----------------------------------> O(1)
    while(queue is not empty) -----------------------------------> O(V)
      p = dequeue(); --------------------------------------------> O(1)
      if p is univisited ----------------------------------------> O(1)
        mark is univisited --------------------------------------> O(1)
        enqueue all adjacent unvisited vertices to curVertex ----> O(adj)
        update parent of adjacent vertices to curVertex ---------> O(1)
    TC: O(V * adj) === O(E) edges
    SC: O(V) // add all nodes to the queue
    // !!!!! BFS won't work with weighted GRAPH
   */
  BFSForSSSPP(vertice) {
    const queue = [vertice];

    while(queue.length) {
      const curr = queue.shift();
      curr.isVisited = true;

      console.log(`Printing for path: ${curr.name}:`)

      this.parentPrint(curr);

      for(const neighbor of curr.neighbors) {
        if(!neighbor.isVisited) {
          queue.push(neighbor);
          neighbor.parent = curr;
          neighbor.isVisited = true;
        };
      };
    }
  };
  
};

// P = null
const A = new GraphNode("A", 0);
// P = A
const B = new GraphNode("B", 1);
// P = A
const C = new GraphNode("C", 2);
// P = B
const D = new GraphNode("D", 3);
// P = C
const E = new GraphNode("E", 4);
// P = D
const F = new GraphNode("F", 5);
// P = B
const G = new GraphNode("G", 6);

const nodeList = [A, B, C, D, E, F, G];

const graph = new Graph(nodeList);

// A <-> B
graph.addUndirectedEdge(0, 1);
// A <-> C
graph.addUndirectedEdge(0, 2);

// B <-> D
graph.addUndirectedEdge(1, 3);
// B <-> D
graph.addUndirectedEdge(1, 6);

// C <-> D
graph.addUndirectedEdge(2, 3);
// C <-> E
graph.addUndirectedEdge(2, 4);

// D <-> F
graph.addUndirectedEdge(3, 5);

// E <-> F
graph.addUndirectedEdge(4, 5);

// F <-> G
graph.addUndirectedEdge(5, 6);

console.log(graph.toString())
graph.bfs()
graph.resetNodes();

console.log('=========');
graph.BFSForSSSPP(nodeList[0])

/*

 A: -> B -> C
 B: -> A -> E
 C: -> A -> D
 D: -> A -> C -> E
 E: -> B -> D



      A       B
        \   /  \
          C     D
         /     /
        E     /
      /  \   /
     H     F ---> G


A: -> C
B: -> C -> D
C: -> E
D: -> F
E: -> F -> H
F: -> G
G:
H:

A->B->C->D->E->H->F->G


  A B C D E F G H
A 0 0 1 0 0 0 0 0
B 0 0 1 1 0 0 0 0
C 0 0 0 0 1 0 0 0
D 0 0 0 0 0 1 0 0
E 0 0 0 0 0 1 0 1
F 0 0 0 0 0 0 1 0
G 0 0 0 0 0 0 0 0
H 0 0 0 0 0 0 0 0


 */
