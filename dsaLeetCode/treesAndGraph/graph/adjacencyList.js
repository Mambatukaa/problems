class GraphNode {
  constructor(name, index) {
    this.name = name;
    this.index = index;
    this.neighbors = [];
    this.isVisited = false;
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
graph.bfs()
graph.resetNodes();
console.log('===================');
graph.dfs()

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
